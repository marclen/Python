# Determining the maximum number of sequential numbers in a list
# Using a loop in a loop, as we need to iterate through a list while keeping track of all the sequential numbers
# Outer loop keeps track of where we currently are in the loop and instantiates sequence details
# Inner loop keeps track of sequence details and records them
# I wanted to record the details of each sequence, so I created an object and recorded them in a list

class Sequence:
    def __init__(self, minimum_value, maximum_value, length):
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.length = length


provided_list = [5, 2, 99, 3, 4, 1, 100, 11, 9, 14, 12, 10, 13, 15]

# code works whether your sort it or not of course
provided_list.sort()

sequence_list = []

loop_count = 0

while loop_count < len(provided_list):
    current_minimum_value = provided_list[loop_count]
    current_maximum_value = provided_list[loop_count]
    sequence_bool = False
    current_sequence_length = 0

    if loop_count == len(provided_list) - 1:
        # you're at the last value, don't think anything needs to be done here
        break

    # code to determine if the next item in list is a sequential number, and iterates until  it no longer is
    elif provided_list[loop_count + 1] - provided_list[loop_count] == 1:
        sequence_bool = True

        # Keeps iterating until the next number is not sequential OR you're at the end of the list
        while sequence_bool and loop_count < len(provided_list):

            current_sequence_length += 1

            if current_minimum_value > provided_list[loop_count]:
                current_minimum_value = provided_list[loop_count]

            if current_maximum_value < provided_list[loop_count]:
                current_maximum_value = provided_list[loop_count]

            if loop_count == len(provided_list) - 1:
                # We want to be in here when we're at the last digit to record sequence information
                # but we need to break before the next if statement, because it will throw out of range exception
                break

            if provided_list[loop_count + 1] - provided_list[loop_count] != 1:
                sequence_bool = False

            loop_count += 1
        
        # recording sequence details
        sequence_list.append(Sequence(current_minimum_value, current_maximum_value, current_sequence_length))
    
    else:
        loop_count += 1

sequence_list.sort(key=lambda x: x.length, reverse=True)

for i in sequence_list:
    print(f'Sequence: Run: {i.length}, Min: {i.minimum_value}, Max: {i.maximum_value}')

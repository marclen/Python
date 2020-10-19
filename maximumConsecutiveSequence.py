class Sequence:
    def __init__(self, minval, maxval, length):
        self.minVal = minval
        self.maxVal = maxval
        self.length = length


providedList = [5, 2, 99, 3, 4, 1, 100, 9, 10, 11, 12, 13, 14, 15]
providedList.sort()

sequencelist = []

outerLoopCount = 0
sequenceBool = False
while outerLoopCount < len(providedList):
    currentMinSeq = providedList[outerLoopCount]
    currentMaxSeq = providedList[outerLoopCount]
    currentSequenceCount = 0

    # code to determine if the next is sequential, and then to iterate until  it no longer is
    if outerLoopCount == len(providedList) - 1:
        # you're at the last value, don't think anything needs to be done here
        break
    elif providedList[outerLoopCount + 1] - providedList[outerLoopCount] == 1:
        sequenceBool = True
        while sequenceBool and outerLoopCount < len(providedList):

            currentSequenceCount += 1

            if currentMinSeq > providedList[outerLoopCount]:
                currentMinSeq = providedList[outerLoopCount]

            if currentMaxSeq < providedList[outerLoopCount]:
                currentMaxSeq = providedList[outerLoopCount]

            if outerLoopCount == len(providedList) - 1:
                break
            if providedList[outerLoopCount + 1] - providedList[outerLoopCount] != 1:
                sequenceBool = False

            outerLoopCount += 1
        sequencelist.append(Sequence(currentMinSeq, currentMaxSeq, currentSequenceCount))
    else:
        outerLoopCount += 1

sequencelist.sort(key=lambda x: x.length, reverse=True)

i = sequencelist[0]
print(f'Sequence: Run: {i.length}, Min: {i.minVal}, Max: {i.maxVal}')

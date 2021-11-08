class AttendGraduationCeremony:
    def __init__(self):
        self.consecutiveAbsent = 4

    def calculateTotalNumWays(self, num):
        if (num - self.consecutiveAbsent + 1)>0:
            notPossibleWays = (((num - self.consecutiveAbsent + 1)*(num - self.consecutiveAbsent + 2))//2)
            totalWay = 2**num - (0 if notPossibleWays<= 0 else notPossibleWays)
        else:
            totalWay = 2**num
        return totalWay
    
    def probabilityOfNotMissingGraduationCeremony(self, num):
        numOfWaysMissing = 1
        if num-1>0:
            numOfWaysMissing = self.calculateTotalNumWays(num-1)
        totalNumWays = self.calculateTotalNumWays(num)
        return str(totalNumWays - numOfWaysMissing)+"/"+str(totalNumWays)

obj = AttendGraduationCeremony()
print(obj.calculateTotalNumWays(6))
print(obj.probabilityOfNotMissingGraduationCeremony(6))





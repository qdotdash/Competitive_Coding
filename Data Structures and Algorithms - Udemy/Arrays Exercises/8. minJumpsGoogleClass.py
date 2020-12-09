A = [ 33, 21, 50, 0, 0, 46, 34, 3, 0, 12, 33, 0, 31, 37, 15, 17, 34, 18, 0, 4, 12, 41, 18, 35, 37, 34, 0, 47, 0, 39, 32, 49, 5, 41, 46, 26, 0, 2, 49, 35, 4, 19, 2, 27, 23, 49, 19, 38, 0, 33, 47, 1, 21, 36, 18, 33, 0, 1, 0, 39, 0, 22, 0, 9, 36, 45, 31, 4, 14, 48, 2, 33, 0, 39, 0, 37, 48, 44, 0, 11, 24, 16, 10, 23, 22, 41, 32, 14, 22, 16, 23, 38, 42, 16, 15, 0, 39, 23, 0, 42, 15, 25, 0, 41, 2, 48, 28 ]

class Solution:

    # @param A : list of integers
    # @return an integer

    def returnMaxInRange(self, limitIndex, A):  # function that returns the next index within limitIndex with max value that can reach upto or beyond limitIndex
        minIndex = 1000000
        j = limitIndex - 1
        while j >= 0:
            if j + A[j] >= limitIndex:
                if j < minIndex:
                    minIndex = j
            j -= 1

        if minIndex == 1000000:
            return -2
        else:
            return minIndex

    def jump(self, A):
        length1 = len(A)
        jumps = 0
        i = length1 - 1
        limitIndex = i

        while limitIndex != 0:
            limitIndex = self.returnMaxInRange(limitIndex, A)
            if limitIndex == -2:
                return -1
            else:
                jumps += 1
        return jumps


obj = Solution()
print(obj.jump(A),end='')

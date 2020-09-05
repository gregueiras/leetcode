def helper(maxValue, options, target, targetIdx):
    for des in reversed(range(maxValue + 1)):
        if (des in options):
            target[targetIdx] = des
            options.remove(des)
            return

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        hour = [0, 0]
        minute = [0, 0]


        if (not 0 in A and not 1 in A and not 2 in A):
            return ""

        if (min(A) == 2 and (not 3 in A and A.count(2) == 1)):
            return ""

        cpy = A.copy()
        cpy.remove(min(A))

        if (min(cpy) > 5):
            return ""


        cpy.remove(min(cpy))
        if (min(cpy) <= 5):
            helper(2, A, hour, 0)
        else:
            helper(1, A, hour, 0)

        if (hour[0] != 2):
            helper(9, A, hour, 1)
        else:
            helper(3, A, hour, 1)

        helper(5, A, minute, 0)
        helper(9, A, minute, 1)    

        print((hour, minute)) 
        
        if len(A) > 0:
            return ""

        return f"{hour[0]}{hour[1]}:{minute[0]}{minute[1]}"
        
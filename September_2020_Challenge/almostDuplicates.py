from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        ss = SortedSet()
    
        for s in range(min(k + 1, len(nums))):
            num = nums[s]
            print(num)
            print(s, num)
            if num in ss:
                print("INIT")
                return True
            else:
                ss.add(num)

        print(ss)

        for i in range(len(ss) - 1):
            j = i + 1
            print(f"A {(ss[i], ss[j])}")

            if (abs(ss[i] - ss[j]) <= t):
                print((i, j))
                print((ss[i], ss[j]))
                return True

        print(f"B {(k, nums)}")
        if (k >= len(nums)):
            print("INIT B")
            return False

        ss.remove(nums[0])

        for s in range(len(nums) - k - 1):
            idx = s + k + 1
            if (nums[idx] in ss):
                return True

            ss.add(nums[idx])         

            for i in range(len(ss) - 1):
                j = i + 1

                if (abs(ss[i] - ss[j]) <= t):
                    print((i, j))
                    print((ss[i], ss[j]))
                    return True

            ss.remove(nums[s + 1])


        return False
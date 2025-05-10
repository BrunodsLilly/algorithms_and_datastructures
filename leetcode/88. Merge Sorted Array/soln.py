from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer_sorted = m + n - 1
        pointer1 = m - 1
        pointer2 = n - 1

        while 0 <= pointer_sorted and pointer1 >= 0 and pointer2 >= 0:
            print("Comparing", nums1[pointer1], "and", nums2[pointer2])
            if nums1[pointer1] < nums2[pointer2]:
                nums1[pointer_sorted] = nums2[pointer2]
                pointer2 -= 1
            else:
                nums1[pointer_sorted] = nums1[pointer1]
                pointer1 -= 1
            pointer_sorted -= 1
            print(nums1)
            print("pointer_sorted", pointer_sorted)
            print("pointer1", pointer1)
            print("pointer2", pointer2)

        while 0 <= pointer_sorted and pointer2 >=0:
            if nums1[pointer1] < nums2[pointer2]:
                nums1[pointer_sorted] = nums2[pointer2]
                pointer2 -= 1
            pointer_sorted -= 1

nums1 = [1, 2, 3, 4, 0, 0, 0, 0, 0]
nums2 = [3, 5, 67, 100, 140]
m = 4
n = 5
Solution().merge(nums1, m, nums2, n) 
assert nums1 == [1, 2, 3, 3, 4, 5, 67, 100, 140]

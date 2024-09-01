# Two-Pointers-2

## Problem1 (https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        cnt = 1
        slow = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cnt = cnt + 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[slow] = nums[i]
                slow = slow + 1
        return slow
# TC = O(n), SC = O(1)

## Problem2 (https://leetcode.com/problems/merge-sorted-array/)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums1 == None or len(nums1) == 0:
            return 
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 = p1 - 1
            else:
                nums1[p3] = nums2[p2]
                p2 = p2 - 1
            p3 = p3 - 1
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 = p2 - 1
            p3 = p3 - 1
# TC = O(m + n) , SC= O(1)

## Problem3 (https://leetcode.com/problems/search-a-2d-matrix-ii/)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0:
            return Fasle
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                row = row + 1
            else:
                col = col - 1
        return False
# TC = O(m + n), SC= O(1)
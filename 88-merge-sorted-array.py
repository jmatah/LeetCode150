class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[:] = nums1[:(m+n)] + [0] * ( (m+n) - len( nums1 ) )
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if ( i >= 0 and nums1[i] > nums2[j] ):
                nums1[k] = nums1[i]
                i -= 1
            else:
                print( 'inside: ', k, i, j, nums1[i], nums2[j] )
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        return nums1

"""
Most of the Solutions online fail simple tests:
1. len(nums1) = 7
nums1 = [1,2,3,0,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

and:
2. len(nums1) = 5
nums1 = [1,2,3,0,0]
m = 3
nums2 = [2,5,6]
n = 3

https://leetcode.com/problems/merge-sorted-array/solutions/228730/python-solution-w-explanation/
Because everything in Python is an object, when doing nums1 = sorted(nums1[:m] + nums2[:n]) two things happen:

    a new object is created which is the result of sorted(nums1[:m] + nums2[:n]), while the original nums1 that was passed in to the function remains untouched
    So the line nums1 = sorted(nums1[:m] + nums2[:n]) is actually equivalent to nums1 = new object, i.e. the address of new object is now assigned to nums1

But since the problem requires modifying the original object nums1, you get an error.
However, when using nums1[:], you fill up the indices of the original nums1 with new values, so the original nums1 is indeed sorted by the end.
"""
sol = Solution()

nums1 = [1,2,3,4,0,0]
m = 3
nums2 = [6,7,8]
n = 3
ret = sol.merge( nums1, m, nums2, n )
print('out: ', nums1)

"""
nums1 = [1,2,3,0,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
ret = sol.merge( nums1, m, nums2, n )
print('out: ', nums1)


nums1 = [1,2,3,0]
m = 3
nums2 = [2,5,6]
n = 3
ret = sol.merge( nums1, m, nums2, n )
print('out: ', nums1)
"""

nums1 = [1]
m = 1
nums2 = []
n = 0
ret = sol.merge( nums1, m, nums2, n )
print('out: ', nums1)


nums1 = [0]
m = 0
nums2 = [1]
n = 1
ret = sol.merge( nums1, m, nums2, n )
print('out: ', nums1)


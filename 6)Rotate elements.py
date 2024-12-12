class Solution(object):
    def rotate(self, nums, k):
        # Get the actual number of rotations
        k = k % len(nums) 
        # Perform the rotation using slicing
        nums[:] = nums[-k:] + nums[:-k]

        """
        Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

solution:

 k = k % len(nums) --- uncessary rotations are avoided
 nums[:] = nums[-k:] + nums[:-k] --- the list is rotated to the right


        nums[-k:]: Gets the last k elements of the array (the elements to move to the front).
        nums[:-k]: Gets the remaining elements of the array (the elements to stay at the back).
        nums[:] = ...: Updates the original array nums in place with the rotated result.

        
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = 3 % 7 = 3
nums[:] = nums[-3:] + nums[:-3]
        = [5, 6, 7] + [1, 2, 3, 4]
        = [5, 6, 7, 1, 2, 3, 4]
[5, 6, 7, 1, 2, 3, 4]


        """
        
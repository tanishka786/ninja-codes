class Solution(object):
    def majorityElement(self, nums):
        count = 0 # Initialize count of potential majority element as 0
        temp = None  # Initialize a temporary variable to hold the candidate for majority element

        for n in nums: # Loop through each element in the nums array
            
            if count == 0: # If count is 0, we pick the current element as the new candidate
                temp = n  # Set temp to current element
            if n == temp: # Adjust the count based on whether the current element matches the candidate
                count += 1  # Increment count if the element matches temp
            else:
                count -= 1  # Decrement count if the element does not match temp

        return temp  # After looping through all elements, temp should be the majority element

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

"""
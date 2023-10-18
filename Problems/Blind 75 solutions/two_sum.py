"""
Problem: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Solution 1:
One solution can involve testing each pair from the list using two for loops, 
such as (2,7) , (2,11) , (2,15). But this going to result in O(n**2) time complexity.

Let's think about a better approach.

Solution 2:
So we need to find two numbers that add up to the target number:
x + y = target, from example:
x + y = 9
y = 9 - x

Now what we can do we can pick each number from the give list/array.
y = 9 - 2 = 7, and check if 7 is in the array/List or not
if yes we have found our pair (answer).

To look up fast for a number we can use Hashmap as a data Structures,
as in hashmap look up speed is O(1) constant.
"""

def twoSum(self, nums, target):
        num_index = {nums[i] : i for i in range(len(nums))}
        """
        num_index = {nums[i] : i for i in range(len(nums))} This can b written as:
        num_index = {}
        for i in range(len(nums)):
            num_index[nums[i]] = i

        I just used one liner.
        """
        ans = []
        # Iterate through the array
        for i in range(len(nums)):
            # check if after subtraction y = 9-2 = 7 exists in dictionary 
            # Also check  for the case y = 6 - 3 = 3, we have 3 in array but it is already used
            # So we need to find a number other than 3 for the pair, so index should not match.
            if(num_index.get(target-nums[i], 0) and i != num_index.get(target-nums[i])):
                ans.append(i)
                ans.append(num_index.get(target-nums[i]))
                return ans
        return -1
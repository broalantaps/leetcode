#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# from copy import deepcopy
# @lc code=start
class Solution:
    def __init__(self):
        self.nums_ = []
        self.vis = []
        
    def find(self,target: int) -> int:
        for i in range(len(self.nums_)):
            if self.nums_[i] == target and not self.vis[i]:
                self.vis[i] = True
                return i
        return -1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort the list first
        self.nums_ = nums.copy()
        self.vis = [False for i in range(len(nums))]
        nums.sort()
        # use stack to handle the problem
        stack = []
        for i in range(len(nums)):
            if len(stack) == 0:
                stack.append(nums[i])
            else:
                if stack[-1] == target - nums[i]:
                    return [self.find(stack[-1]), self.find(nums[i])]
                elif stack[-1] < target - nums[i]:
                    stack.append(nums[i])
                else:
                    while len(stack) > 0 and stack[-1] > target - nums[i]:
                        stack.pop()
                    if len(stack) > 0 and stack[-1] == target - nums[i]:
                        return [self.find(stack[-1]), self.find(nums[i])]  
        
        
# @lc code=end


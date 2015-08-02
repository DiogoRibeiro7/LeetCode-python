# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        q, res = [], []
        for i in range(len(nums)):
            if q and q[0] == i-k:
                del q[0]
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if(i >= k-1):
                res.append(nums[q[0]])
        return res

if __name__ == '__main__':
    s = Solution()
    print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)

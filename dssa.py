class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        flag = 0
        for k in range(1,n-2):#k is the pointer
            former = 0
            later = 0
            for i in range(0,k-1):
                former = former + nums[i]
            for j in range(k-1,n-1):
                later = later + nums[j]
            if former == later:
                print(k)
                flag = 1
                break

        if flag== 0:
            print(-1)
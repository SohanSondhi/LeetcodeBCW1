class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr = [0,0,0]
        for i in nums:
            if i == 0:
                arr[0] += 1
            if i == 1:
                arr[1] += 1
            if i == 2:
                arr[2] += 1
        for i in range(arr[0]):
            nums[i] = 0
        j = arr[0]
        for i in range(arr[1]):
            nums[j + i] = 1 
        g = arr[1] + j
        for i in range(arr[2]):
            nums[g + i] = 2
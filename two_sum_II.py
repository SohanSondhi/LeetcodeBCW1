class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers)-1
        arr = []
        while low < high:
            if numbers[low] + numbers[high] == target:
                arr.append(low+1)
                arr.append(high+1)
                return arr
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                high -= 1
        
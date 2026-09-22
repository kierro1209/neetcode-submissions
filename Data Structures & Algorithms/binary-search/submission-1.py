class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1
        i = int((low + high)/2)
        print(i)
        while low <= high:
            if nums[i] == target:
                return i
            if nums[i] < target:
                low = i+1
            else:
                high = i-1
            print("low: " + str(low)+" high: "+ str(high))
            i = int((low + high)/2)

        return -1 
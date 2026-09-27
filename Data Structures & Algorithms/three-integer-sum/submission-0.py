class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = set()
        nums.sort()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] > 0:
                break
            k = i+1
            j = len(nums)-1
            target = 0 - nums[i]
            print("i: " +str(nums[i]) +" k: "+str(nums[k]) + " j: "+str(nums[j]) + " target: " +str(target))
            while k < j:
                if (nums[k] + nums[j]) == target:
                    triples.add(tuple([nums[i], nums[j], nums[k]]))
                    k += 1
                    j -= 1
                elif (nums[k] + nums[j]) > target:
                    j -= 1
                else:
                    k += 1
                    
        
        return list(triples)
                

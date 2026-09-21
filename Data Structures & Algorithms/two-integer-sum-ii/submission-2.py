class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1
        summed = numbers[index1] + numbers[index2]

        while summed != target:
            if summed < target:
                index1 += 1
                summed = numbers[index1] + numbers[index2]
                
            elif summed > target:
                index2 -= 1
                summed = numbers[index1] + numbers[index2]
                
            
            if(index1 == index2):
                return []
        
        return [index1+1, index2+1]

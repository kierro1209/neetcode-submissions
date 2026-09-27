class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                nums.append(int(token))
            else:
                if len(nums) > 1:
                    nums1 = nums.pop()
                    nums2 = nums.pop()
                    
                    if token == "+":
                        nums.append(nums1+nums2)
                    elif token == "-":
                        nums.append(nums2 - nums1)
                    elif token == "*":
                        nums.append(nums1*nums2)
                    else:
                        nums.append(int(float(nums2)/nums1))
        
        return nums[0]
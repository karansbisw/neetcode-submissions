class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            left_product = 1
            right_product = 1
            
            # Loop through indexes before i
            for j in range(0, i):
                left_product *= nums[j]
            
            # Loop through indexes after i
            for j in range(i + 1, len(nums)):
                right_product *= nums[j]
                
            # FIXED: This must be indented inside the 'i' loop
            output.append(left_product * right_product)
            
        return output
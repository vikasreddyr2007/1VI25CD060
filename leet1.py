class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the number and its corresponding index
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # Calculate the required complement
            complement = target - num
            
            # If the complement exists in our dictionary, we found the pair
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Otherwise, save the current number and its index to the dictionary
            num_to_index[num] = index
       

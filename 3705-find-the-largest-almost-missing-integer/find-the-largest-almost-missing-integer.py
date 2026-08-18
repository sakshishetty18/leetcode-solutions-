class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarray_counts = {}
        
        # Iterate through all subarrays of size k
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i+k]
            # Use a set to only count an element once per subarray
            for num in set(subarray):
                subarray_counts[num] = subarray_counts.get(num, 0) + 1
                
        # Find the maximum integer that appears in exactly one subarray
        largest_missing = -1
        for num, count in subarray_counts.items():
            if count == 1:
                largest_missing = max(largest_missing, num)
                
        return largest_missing
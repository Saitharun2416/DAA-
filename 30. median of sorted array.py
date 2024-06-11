def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1 
    
    m, n = len(nums1), len(nums2)
    total_length = m + n
    half_length = (total_length + 1) // 2  

    left, right = 0, m
    while left <= right:
        partition_nums1 = (left + right) // 2
        partition_nums2 = half_length - partition_nums1
        
        nums1_left_max = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
        nums1_right_min = float('inf') if partition_nums1 == m else nums1[partition_nums1]
        
        nums2_left_max = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
        nums2_right_min = float('inf') if partition_nums2 == n else nums2[partition_nums2]

        if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
           
            if total_length % 2 == 0:
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            else:
                return max(nums1_left_max, nums2_left_max)
        elif nums1_left_max > nums2_right_min:
            right = partition_nums1 - 1
        else:
            left = partition_nums1 + 1
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

#Time complexity: O(log(min(m, n)))
#Space complexity: O(log(min(m, n)))

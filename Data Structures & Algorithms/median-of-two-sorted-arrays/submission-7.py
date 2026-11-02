class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m= len(nums1) 
        n= len(nums2)

        left_half= (m+n+1)//2

        left = max(0,left_half-n)
        right = min(m, left_half)

        while left<=right: 
            mid=(left+right)//2
            #i gets recomputed every iteration
            i=mid
            j= left_half-i 

            #if/else bound check
            left1= nums1[i-1] if i >0 else float('-inf')
            right1= nums1[i] if i<m else float('inf')
            left2= nums2[j-1] if j>0 else float('-inf')
            right2= nums2[j] if j<n else float('inf')

            if left1<=right2 and left2<=right1: 
                if (m+n)%2!=0: 
                    return float(max(left1,left2))
                else: 
                    return (max(left1,left2)+min(right1,right2))/2
            elif left2>right1: 
                left= mid+1 
            elif left1>right2:
                right= mid-1 





        
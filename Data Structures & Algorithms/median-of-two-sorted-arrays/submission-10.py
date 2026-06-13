class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2

        if len(a) > len(b):
            a, b = b, a 

        size = len(a) + len(b)
        mid = size // 2

        # iterate the biggest list
        l, r = 0, len(a) - 1
        n, m = len(a), len(b)

        while True:
            ai = (l + r) // 2
            bi = mid - ai - 2

            print("ai, bi", ai, bi)

            # update the in array pointers
            # fix out of bound
            a_left = a[ai] if ai >= 0 else float('-inf')
            b_left = b[bi] if bi >= 0 else float('-inf')
            a_right = a[ai + 1] if ai + 1 < n else float('inf')
            b_right = b[bi + 1] if bi + 1 < m else float('inf')

            print(".   left ", a_left, b_left)
            print(".   right ", a_right, b_right)
            if a_left <= b_right and b_left <= a_right:
                # at a median 
                if size % 2 == 1:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right: 
                r = ai - 1
            else:
                l = ai + 1

        


        
            
                

                

                

        




        



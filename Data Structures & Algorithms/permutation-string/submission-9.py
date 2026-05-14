class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        expected_alpha_counts = [0] * 26 

        # fill the expected alpha count 
        for i in range(len(s1)):
            expected_alpha_counts[ord(s1[i]) - ord("a")] += 1

        l = r = 0
        current_count = [0] * 26 
        expected_len = len(s1)

        while l <= r <= len(s2):
            # print("while starts")
            while l < len(s2) and expected_alpha_counts[ord(s2[l]) - ord("a")] == 0:
                l += 1
                # print(" - l ", l)

            r = l
            while r < len(s2) and r - l + 1 <= expected_len and expected_alpha_counts[ord(s2[r]) - ord("a")] != 0:
                current_count[ord(s2[r]) - ord("a")] += 1
                r += 1
                # print(" - r ", r)


            # print(expected_alpha_counts, current_count)
            if expected_alpha_counts == current_count: 
                return True 

            current_count = [0] * 26 
            r += 1 
            l += 1
                
        return False
        
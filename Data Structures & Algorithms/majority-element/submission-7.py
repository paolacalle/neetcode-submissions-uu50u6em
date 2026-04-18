from random import choice
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # proablistic way, though not always the best way
        # success with probability of p, where p > 0.5
        # failure with 1 - p 

        # this is a geometric dist.
        # E[tries] = 1 / p

        # K-th try and success P(X = k) = (1 - p)^(k - 1) * p

        # E[X] = sumation_inf_1(k * P(X = k))

        # E[X] = p * sumation_inf_1((1 - p)^(k - 1))

        # series trick tells us 
        # E[X] = p * (1 / p^2) = 1 / p 

        # Here, p > 0.5, so E[tries] = 1 / (1 / 2) = 2
        # Meaning, that on average youll hit hit the majority 
        # element in under 2 guesses

        n = len(nums)

        while True: 
            candiate = choice(nums)

            if nums.count(candiate) > n // 2:
                return candiate

        


        

    


        


        
        
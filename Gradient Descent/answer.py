class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        val=init
        for i in range(iterations):
            val=val-learning_rate*(2*val)
        ans=round(val,5)
        
        return ans

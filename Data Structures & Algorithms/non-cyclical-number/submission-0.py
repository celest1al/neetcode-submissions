class Solution:
    def isHappy(self, n: int) -> bool:
        def step(x: int):
            return sum(int(d) ** 2 for d in str(x))
        
        slow, fast = n, step(n)

        while fast != 1 and slow != fast:
            slow, fast = step(slow), step(step(fast))
        
        return fast == 1
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_indicies = sorted(range(len(position)), key=lambda i: position[i])

        prev_time = 0
        fleet = 0
        for i in sorted_indicies[::-1]:
            target_time = (target - position[i]) / speed[i]

            if target_time > prev_time:
                fleet += 1
                prev_time = target_time
        return fleet
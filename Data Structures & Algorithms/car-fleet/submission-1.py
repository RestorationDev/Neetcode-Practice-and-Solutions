class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        paired = list(zip(position, speed))

        sorted_pairs = sorted(paired, reverse=True)

        print(sorted_pairs)

        fleet_ct = 1
        
        fleet_time = (target - sorted_pairs[0][0])/sorted_pairs[0][1]

        for pos, spd in sorted_pairs:

            time = (target - pos)/spd

            if time > fleet_time:
                fleet_ct += 1
                fleet_time = time
        
        return fleet_ct






        
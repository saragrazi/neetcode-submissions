class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleet = 0
        fleet_speed = 0
        for pos, spe in cars:
            if (target-pos) / spe > fleet_speed:
                fleet+=1
                fleet_speed = (target-pos) / spe
        return fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Pair position and speed
        cars = list(zip(position, speed))
        
        # Sort cars from closest to target to farthest
        cars.sort(reverse=True)
        
        stack = []
        
        for pos, spd in cars:
            # Time needed to reach target
            time = (target - pos) / spd
            
            # If this car takes longer, it cannot catch
            # the fleet ahead, so it creates a new fleet.
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
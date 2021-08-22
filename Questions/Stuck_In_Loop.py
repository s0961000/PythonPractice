"""

Robot starting at (0,0)
Robot facing north
Robot can only go L,R,G
Robot doesn't move on L or R, just G

Example Robot:

LLG
        ^
        X (0,0)

      < X (0,0)

        X (0,0)
        V

        X (1,0)
        V


Robot in circle (true)

Return if Robot is in circle (true/false)

"""


class Robot:
    coordinates = [0, 0]
    direction = 0

    def get_friendly_direction(self):
        current_direction = {0: "N", 1: "E", 2: "S", 3: "W"}
        return current_direction[self.direction]

    def check_loop(self, directions):
        current_direction = {0: "N", 1: "E", 2: "S", 3: "W"}
        # Return True if in loop
        if len(directions) == 0:
            return True
        for i in directions:
            if i == "G":
                # Check current direction
                if current_direction[self.direction] == "E":
                    self.coordinates[0] += 1
                elif current_direction[self.direction] == "W":
                    self.coordinates[0] -= 1
                elif current_direction[self.direction] == "N":
                    self.coordinates[1] += 1
                elif current_direction[self.direction] == "S":
                    self.coordinates[1] -= 1
            elif i == "R":
                # Move to the right
                self.direction += 1
                if self.direction == 4:
                    self.direction = 0
            elif i == "L":
                # Move to the left
                self.direction -= 1
                if self.direction == -1:
                    self.direction = 3

        # Check if in loop. Coordinates = 0,0 OR direction != North
        if current_direction[self.direction] != "N" or self.coordinates == [0, 0]:
            return True

        return False


if __name__ == "__main__":
    robot = Robot()
    print(robot.check_loop("LRG"))
    print(
        f"Direction Number: {robot.direction}, Facing Direction: {robot.get_friendly_direction()}, Coordinates: {robot.coordinates}")

"""

Leetcode Solution for the Robot

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        coordinates = [0, 0]
        direction = 0
        current_direction = {0: "N", 1: "E", 2: "S", 3: "W"}
        # Return True if in loop
        if len(instructions) == 0:
            return True
        for i in instructions:
            if i == "G":
                # Check current direction
                if current_direction[direction] == "E":
                    coordinates[0] += 1
                elif current_direction[direction] == "W":
                    coordinates[0] -= 1
                elif current_direction[direction] == "N":
                    coordinates[1] += 1
                elif current_direction[direction] == "S":
                    coordinates[1] -= 1
            elif i == "R":
                # Move to the right
                direction += 1
                if direction == 4:
                    direction = 0
            elif i == "L":
                # Move to the left
                direction -= 1
                if direction == -1:
                    direction = 3

        # Check if in loop. Coordinates = 0,0 OR direction != North
        if current_direction[direction] != "N" or coordinates == [0, 0]:
            return True

        return False

"""
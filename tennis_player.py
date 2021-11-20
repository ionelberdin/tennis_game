from typing import AsyncContextManager
from geometry import Array

class TennisPlayer:
    def __init__(self, id, host=True) -> None:
        self.id = id
        self.is_host = host
        self.position = Array()
        self.speed = Array()
        self.acceleration = Array()
        self.max_speed = 10  # m/s
        self.max_acceleration = 10  # m/s^2
        self.width = 0.6  # m
        self.depth = 0.3  # m
        self.colour = 'white'
        self.aim = Array(1)
        self.aim_ang_speed = 0  # rad/s
    
    def next_position(self, dt:float) -> None:
        self.speed /= (2 + dt)
        self.speed += self.acceleration * dt
        abs_speed = abs(self.speed)
        if abs_speed > self.max_speed:
            self.speed *= self.max_speed / abs_speed
        self.position += self.speed * dt + self.acceleration * ((dt ** 2) / 2)

        self.aim = self.aim.rotate_z(self.aim_ang_speed * dt)

    def set_acceleration(self, direction:str, on:bool=True) -> None:
        factor = -on if '-' in direction else on
        if 'x' in direction:
            self.acceleration.x = factor * self.max_acceleration
        else:
            self.acceleration.y = factor * self.max_acceleration


if __name__ == '__main__':
    tp = TennisPlayer(1)
    tp.acceleration = Array(8)
    print(tp.position, tp.speed, tp.acceleration)
    for _ in range(10):
        tp.next_position(dt=1)
        print(tp.position, tp.speed, tp.acceleration)
        
    tp.acceleration.x = 0
    for _ in range(10):
        tp.next_position(dt=0.1)
        print(tp.position, tp.speed, tp.acceleration)
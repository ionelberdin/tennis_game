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
        self.max_acceleration = 4  # m/s^2
        self.width = 0.6  # m
        self.depth = 0.3  # m
        self.colour = 'white'
    
    def next_position(self, dt:float) -> None:
        self.speed += self.acceleration * dt
        abs_speed = abs(self.speed)
        if abs_speed > self.max_speed:
            self.speed *= self.max_speed / abs_speed
        self.position += self.speed * dt + self.acceleration * (dt ** 2) / 2


if __name__ == '__main__':
    tp = TennisPlayer(1)
    tp.acceleration = Array(1, 2)
    print(tp.position, tp.speed, tp.acceleration)
    for _ in range(10):
        tp.next_position(dt=1)
        print(tp.position, tp.speed, tp.acceleration)
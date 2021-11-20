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
    
    def next_position(self, dt):
        self.speed += self.acceleration * dt
        self.position += self.speed * dt + self.acceleration * (dt ** 2) / 2
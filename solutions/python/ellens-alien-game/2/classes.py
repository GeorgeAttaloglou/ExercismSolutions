"""Solution to Ellen's Alien Game exercise."""


class Alien:
    total_aliens_created = 0
    
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created += 1


    def hit(self):
        self.health = max(0, self.health - 1)

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coord, y_coord):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord

    def collision_detection(self, other):
        pass


def new_aliens_collection(positions):
    return [Alien(x,y) for x,y in positions]

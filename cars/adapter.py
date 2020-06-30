
class SpeedAdapter:
    """Speed Adapter class to limit speed of other cars to 50"""
    def __init__(self, name):
        self.name = name
        self.city_speed = 50

    def speed(self):
        return self.city_speed

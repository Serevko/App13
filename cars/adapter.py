
class SpeedAdapter:
    """
    A class to limit speed of the car.

    ...

    Attributes
    ----------
    name : str
        name of the car

    Methods
    -------
    speed():
        Limits speed of the car to 50.
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the SpeedAdapter object.

        Parameters
        ----------
            name : str
                name of the car
            city_speed : int
                      city limit(50)
        """

        self.name = name
        self.city_speed = 50

    def speed(self):
        """
        Returns the SpeedAdapter object with city_speed

        Returns
        -------
        city_speed : int
            limits speed to 50
        """

        return self.city_speed

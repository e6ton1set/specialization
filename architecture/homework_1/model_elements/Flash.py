from . import Point3D, Angle3D


class Flash:
    # region init
    def __init__(self, location: Point3D, angle: Angle3D, color: str, power: float):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    # endregion

    # region methods
    def rotate(self, data: Angle3D) -> None:
        pass

    def move(self, data: Angle3D) -> None:
        pass
    # endregion
from . import Point3D, Angle3D


class Camera:
    # region init
    def __init__(self, location: Point3D, angle: Angle3D) -> None:
        self.location = location
        self.angle = angle

    # endregion

    # region methods
    def rotate(self, data: Angle3D) -> None:
        pass

    def move(self, data: Point3D) -> None:
        pass
    # endregion
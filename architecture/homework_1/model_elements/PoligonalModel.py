from . import Poligon
from . import Texture


class PoligonalModel:
    # region init
    def __init__(self, poligons: Poligon, texture: Texture):
        self.poligons = poligons
        self.texture = texture

    # endregion

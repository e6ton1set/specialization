import PoligonalModel
from Flash import Flash


class Scene:
    # region init
    def __init__(self, id: int, models: PoligonalModel, flashes: Flash):
        self.id = id
        self.models = models
        self.flashes = flashes

    # endregion

    # region methods
    def remove(self, data: None) -> None:
        pass

    @staticmethod
    def update(self, data: None) -> None:
        new_models = PoligonalModel.PoligonalModel()
        ...
        return new_models

    # endregion
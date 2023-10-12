from ..model_elements.PoligonalModel import PoligonalModel
from ..model_elements.Scene import Scene
from ..model_elements.Flash import Flash
from ..model_elements.Camera import Camera
from . import IModelChangeObserver, IModelChanger


class ModelStore(IModelChanger):
    """Class modelstore

    Args:
        IModelChanger : наследует метод NotifyChange абстрактного класса IModelChanger

    Attributes:
        models - (public) поле типа Model
        scenes - (public) поле типа Scene
        flashes - (public) поле типа Flash
        cameras - (public) поле типа Camera
        __changeObservers - (private) поле типа IModelChangeObserver

    Methods:
        get_scena(int) -
        notify_change(IModelChanger) -
    """

    # region init
    def __init__(self,
                 models: PoligonalModel,
                 scenes: Scene,
                 flashes: Flash,
                 cameras: Camera,
                 changeObservers: IModelChangeObserver) -> None:
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self.__changeObservers = changeObservers

    # endregion

    # region methods
    def get_scene(data: int) -> Scene:
        return data

    def notify_change(data: IModelChanger) -> None:
        pass

    # endregion
from abc import ABC, abstractmethod


class PhysicsEngineAdapter(ABC):
    @abstractmethod
    def add_object(self, cfg: ObjectConfig) -> int:
        pass

    @abstractmethod
    def remove_object(self, obj_id: int) -> None:
        pass

    @abstractmethod
    def step(self, dt: float) -> None:
        pass

    @abstractmethod
    def get_state(self, obj_id: int) -> dict:
        pass

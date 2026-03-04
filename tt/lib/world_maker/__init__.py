from __future__ import annotations
from typing import Optional, Tuple, Literal


class World:
    def __init__(self) -> None:
        pass


class Environment:
    def __init__(
        self,
        physics_engine: Literal["mujoco", "newton", "genesis"],
        prebuilt_env_uri: Optional[str] = None,
        seed: Optional[int] = None,
        tick: Optional[int] = 5,  # 5ms
    ) -> None: ...

    def add_object(self, object: Object): ...

    def clone(self) -> Environment: ...


class Object:
    def __init__(
        self,
        obj_uri_or_prebuilt_name: str,
        pos: Tuple[float, float, float] = (0, 0, 0),
        quat: Tuple[float, float, float, float] = (0, 0, 0, 1),
    ) -> None:
        pass


class BIV:
    def __init__(self) -> None:
        pass

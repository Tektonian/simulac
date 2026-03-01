from dataclasses import dataclass
from typing import Any, Dict

from urllib.parse import urlencode
from websockets.sync.client import connect, ClientConnection

from tt.sdk.runner_service.common.runner import IRunner


@dataclass
class RemoteRunner(IRunner):
    """It is more like BenchmarkRunner for now. Not RemoteRunner
    TODO: Should change logic and add BenchmarkRunner class instead

    Args:
        IRunner (_type_): _description_
    """

    id: str
    env_id: str
    state: object

    def __init__(
        self,
        id: str,
        env_id: str,
        state: object,
        owner: str,
        remote_env_id: str,
        kwargs: dict[str, Any],
    ):

        self.id = id
        self.env_id = env_id
        self.state = state

        params = urlencode(kwargs)

        self._socket = connect(
            f"ws://localhost:3000/api/container/{owner}/{remote_env_id}?{params}"
        )

    def step(self, action: object) -> object: ...

    def set_state(self) -> None:
        pass

    def get_state(self) -> None:
        pass

    def clone_state(self) -> None: ...

    def render(self) -> None:
        pass

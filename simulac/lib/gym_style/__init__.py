from __future__ import annotations

from typing import Any, Optional, overload

from .gym_style_environment import BenchmarkEnvironment, BenchmarkVecEnvironment


@overload
def init_bench(
    benchmark_id: str,
    env_id: str,
    seed: int = 0,
    /,
    benchmark_specific: dict[str, Any] = {},
) -> BenchmarkEnvironment: ...
@overload
def init_bench(
    benchmark_id: str,
    env_id: None,
    seed: int = 0,
    /,
    benchmark_specific: dict[str, Any] = {},
) -> BenchmarkVecEnvironment: ...
def init_bench(
    benchmark_id: str,
    env_id: Optional[str],
    seed: int = 0,
    /,
    benchmark_specific: dict[str, Any] = {},
):
    """Initalize benchmark service

    Args:
        benchmark_id (str): Full benchmark id.\n
            Example: benchmark_id="Tektonian/Libero"
        env_id (Optional[str]): Environment id of the benchmark.\n
            `env_id=None` means run all benchmark list\n
            `env_id="libero_10"` means run all `"libero_10"` benchmark list\n
            `env_id="libero_10/TASK_EXAMPLE"` means run one specific test\n
            If you want to see the full list of the `env_id` visit https://tektonian.com/benchmark
        seed (int, optional): Seed for inital state. Defaults to 0.
        benchmark_specific (dict[str, Any], optional): Benchmark specific option field.\n
            Also, if you want to know the full field and meaning please visit https://tektonian.com/benchmark\n
            Defaults to {}.

    Returns:
        ret (BenchmarkEnvironment|BenchmarkVecEnvironment):
    """

    if env_id is None:
        vec_env = BenchmarkVecEnvironment([])
        return vec_env

    env = BenchmarkEnvironment(
        "id",
        benchmark_id,
        env_id,
        seed,
        benchmark_specific,
    )

    return env


def make_vec(envs: list[BenchmarkEnvironment]):
    vec_env = BenchmarkVecEnvironment(envs)
    return vec_env


__all__ = ["init_bench", "make_vec"]

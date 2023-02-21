__doc__ = """
"""
__all__ = ["_Cachable", "DataclassCacher"]

from typing import Generator, Literal, Protocol, Union

import collections
import dataclasses
import functools
import glob
import itertools
import json
import os
import pathlib
import pickle as pkl

from miv.core.datatype import DataTypes

CACHE_POLICY = Literal["AUTO", "ON", "OFF"]


class _CacherProtocol(Protocol):
    @property
    def config_filename(self) -> Union[str, pathlib.Path]:
        ...

    def load_cache(self) -> bool:
        ...

    def save_cache(self) -> bool:
        ...

    def _compile_configuration_as_dict(self) -> dict:
        ...

    def _load_configuration_from_cache(self) -> dict:
        ...

    def check_cached_configuration(self) -> bool:
        ...


class _Cachable(Protocol):
    @property
    def cacher(self) -> _CacherProtocol:
        ...


class DataclassCacher:
    def __init__(self, parent, cache_dir: Union[str, pathlib.Path]):
        super().__init__()
        self.cache_policy: CACHE_POLICY = "AUTO"  # TODO: make this a property
        self.parent = parent
        self.cache_dir = cache_dir

    @property
    def config_filename(self) -> str:
        return os.path.join(self.cache_dir, "config.json")

    def cache_filename(self, idx) -> str:
        index = idx if isinstance(idx, str) else f"{idx:04}"
        return os.path.join(self.cache_dir, f"cache_{index}.pkl")

    def check_cached(self) -> bool:
        current_config = self._compile_configuration_as_dict()
        cached_config = self._load_configuration_from_cache()
        if cached_config is None:
            return False
        return current_config == cached_config  # TODO: fix this

    def _load_configuration_from_cache(self) -> dict:
        if os.path.exists(self.config_filename):
            with open(self.config_filename) as f:
                return json.load(f)
        return None

    def _compile_configuration_as_dict(self) -> dict:
        return dataclasses.asdict(self.parent, dict_factory=collections.OrderedDict)

    def save_config(self):
        config = self._compile_configuration_as_dict()
        os.makedirs(self.cache_dir, exist_ok=True)
        with open(self.config_filename, "w") as f:
            json.dump(config, f, indent=4)

    def load_cached(self) -> Generator[DataTypes, None, None]:
        paths = glob.glob(self.cache_filename("*"))
        for path in paths:
            with open(path, "rb") as f:
                yield pkl.load(f)

    def save_cache(self, values, idx) -> bool:
        os.makedirs(self.cache_dir, exist_ok=True)
        with open(self.cache_filename(idx), "wb") as f:
            pkl.dump(values, f)
        return True

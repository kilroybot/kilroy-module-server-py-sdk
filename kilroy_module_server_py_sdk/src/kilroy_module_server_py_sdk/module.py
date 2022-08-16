from abc import ABC, abstractmethod
from typing import Any, AsyncIterable, Dict, Generic, List, Set, Tuple, TypeVar
from uuid import UUID

from kilroy_module_py_shared import Metadata
from kilroy_server_py_utils import Configurable, classproperty
from kilroy_server_py_utils.schema import JSONSchema

from kilroy_module_server_py_sdk.metrics import Metric

StateType = TypeVar("StateType")


class Module(Configurable[StateType], Generic[StateType], ABC):
    @classproperty
    @abstractmethod
    def metadata(cls) -> Metadata:
        pass

    @classproperty
    @abstractmethod
    def post_schema(cls) -> JSONSchema:
        pass

    @classproperty
    @abstractmethod
    def metrics(cls) -> Set[Metric]:
        pass

    @abstractmethod
    def generate(self, n: int) -> AsyncIterable[Tuple[UUID, Dict[str, Any]]]:
        pass

    @abstractmethod
    async def fit_posts(self, posts: AsyncIterable[Dict[str, Any]]) -> None:
        pass

    @abstractmethod
    async def fit_scores(self, scores: List[Tuple[UUID, float]]) -> None:
        pass

    @abstractmethod
    async def step(self) -> None:
        pass

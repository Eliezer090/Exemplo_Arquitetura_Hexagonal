from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.pedido.pedido import Pedido


class DatabaseInterface(ABC):
    @abstractmethod
    def get_pedidos(self) -> List[Pedido]:
        pass

    @abstractmethod
    def post_pedido(self, pedido: Pedido) -> List[Pedido]:
        pass

    @abstractmethod
    def get_next_id(self) -> int:
        pass

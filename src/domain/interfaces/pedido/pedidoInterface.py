import inject
from abc import ABC, abstractmethod
from typing import List

from src.domain.interfaces.pedido.pedido import Pedido


class PedidoInterface(ABC):
    @abstractmethod
    def getPedidosList(self) -> List[Pedido]:
        pass

    @abstractmethod
    def post_pedido(self, pedido: Pedido) -> List[Pedido]:
        pass

from typing import List
import inject
from src.domain.interfaces.database.database import DatabaseInterface
from src.domain.interfaces.pedido.pedido import Pedido
from src.domain.interfaces.pedido.pedidoInterface import PedidoInterface


class GetPedido:
    @inject.autoparams()
    def __init__(self, pedidointerface: PedidoInterface):
        self.__pedinterface = pedidointerface

    def execute(self) -> List[Pedido]:
        return self.__pedinterface.getPedidosList()

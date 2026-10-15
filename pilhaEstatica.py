from dataclasses import dataclass
from copy import deepcopy

_TERRA = -1

@dataclass
class tipoItem:
    valor: str | int | float | None = None

class pilhaEstDin:
    def __init__(self, maxTam: int) -> None:
        self._topo: int = _TERRA
        self._maxTam: int = maxTam
        self.pilha: list = [None for i in range(maxTam)]
        self.item: tipoItem | None = None

    def vazia(self) -> bool:
        return self._topo == _TERRA

    def cheia(self) -> bool:
        return self._topo == self._maxTam - 1

    def empilha(self, item: tipoItem) -> bool:
        if self.cheia():
            return False
        else:
            self._topo += 1
            self.pilha[self._topo] = deepcopy(item)

            return True

    def desempilha(self) -> bool:
        if self.vazia():
            self.item = None
            return False
        else:
            self.item = deepcopy(self.pilha[self._topo])
            self._topo -= 1

            return True

    def mostra(self, texto: str) -> None:
        if self.vazia():
            print('Situação da Pilha: VAZIA!')
        else:
            print('Situação da Pilha: ', texto)
            for i in range(self._topo, -1, -1):
                print(self.pilha[i].valor, end= ' ')
            print()

    def esvazia(self) -> None:
        self._topo = _TERRA
        self.item = None

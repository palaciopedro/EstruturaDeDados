from dataclasses import dataclass
from copy import deepcopy

@dataclass
class tipoItem:
    valor: str | int | float | None = None

class filaEstDin:
    def __init__(self, maxTam: int) -> None:
        self.fila: list = [None for i in range(maxTam)]
        self._maxTam: int = maxTam
        self._numItens: int = 0
        self._primeiro: int = 0
        self._ultimo: int = -1
        self.item: tipoItem | None = None

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return self._numItens == self._maxTam

    def enfileira(self, item: tipoItem) -> bool:
        if self.cheia():
            return False
        else:
            self._ultimo = (self._ultimo + 1) % self._maxTam
            self.fila[self._ultimo] = deepcopy(item)
            self._numItens += 1

            return True

    def desenfileira(self) -> bool:
        if self.vazia():
            self.item = None
            return False
        else:
            self.item = deepcopy(self.fila[self._primeiro])
            self._primeiro = (self._primeiro + 1) % self._maxTam
            self._numItens -= 1

            return True

    def mostra(self) -> None:
        if self.vazia():
            print('Situação da Fila: VAZIA!')
        else:
            print('Situação da Fila: ')
            pos = self._primeiro
            for i in range(self._numItens):
                print(self.fila[pos].valor, end=' ')
                pos = (pos + 1) % self._maxTam
            print()

    def esvazia(self) -> None:
        self._primeiro = 0
        self._ultimo = -1
        self._numItens = 0
        self.item = None

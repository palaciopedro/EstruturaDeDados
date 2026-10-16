from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class tipoItem:
    valor: str | int | float | None = None

@dataclass
class _tipoNo:
    item: tipoItem | None = None
    _prox: _tipoNo | None = None

class filaEstDin:
    def __init__(self, maxTam: int | None = None) -> None:
        self._primeiro: _tipoNo | None = None
        self._ultimo: _tipoNo | None = None
        self.item: tipoItem | None = None

    def vazia(self) -> bool:
        return self._primeiro == None

    def cheia(self) -> bool:
        return False

    def enfileira(self, item: tipoItem) -> bool:
        if self.cheia():
            return False
        else:
            novoNo: _tipoNo = _tipoNo()
            novoNo.item = deepcopy(item)

            if self.vazia():
                self._primeiro = novoNo
                self._ultimo = novoNo
            else:
                self._ultimo._prox = novoNo
                self._ultimo = novoNo

            return True

    def desenfileira(self) -> bool:
        if self.vazia():
            self.item = None
            return False
        else:
            self.item = deepcopy(self._primeiro.item)
            self._primeiro = self._primeiro._prox

            if self._primeiro is None:
                self._ultimo = None

            return True

    def mostra(self) -> None:
        if self.vazia():
            print('Situação da Fila: VAZIA!')
        else:
            print('Situação da Fila: ', end=' ')
            pos = self._primeiro
            while pos is not None:
                print(pos.item.valor, end=' ')
                pos = pos._prox
            print()

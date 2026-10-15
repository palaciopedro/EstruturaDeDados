from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class tipoItem:
    valor: str | int | float | None = None

class _tipoNo:
    item: tipoItem | None = None
    _prox: _tipoNo | None = None

class pilhaEstDin:
    def __init__(self, maxTam: int | None = None) -> None:
        self._topo: _tipoNo | None = None
        self.item: tipoItem | None = None

    def vazia(self):
        return self._topo == None

    def cheia(self):
        return False

    def empilha(self, item: tipoItem) -> bool:
        if self.cheia():
            return False
        else:
            novoNo: _tipoNo = _tipoNo()
            novoNo.item = deepcopy(item)
            novoNo._prox = self._topo
            self._topo = novoNo

            return True

    def desempilha(self) -> bool:
        if self.vazia():
            self.item = None
            return False
        else:
            self.item = deepcopy(self._topo.item)
            self._topo = self._topo._prox

            return True

    def mostra(self, texto: str) -> None:
        if self.vazia():
            print('Situação da Pilha: VAZIA!')
        else:
            print('Situação da Pilha: ', texto)
            pos = self._topo
            while pos is not None:
                print(pos.item.valor, end=' ')
                pos = pos._prox
            print()

    def esvazia(self) -> None:
        self._topo = None
        self.item = None

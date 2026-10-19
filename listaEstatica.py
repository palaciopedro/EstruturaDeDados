from dataclasses import dataclass
from copy import deepcopy

_TERRA = -1

LISTAVAZIA = 1
LISTACHEIA = 2
ITEMEXISTENTE = 3
ITEMINEXISTENTE = 4

@dataclass
class tipoItem:
    valor: int | None = None

@dataclass
class _tipoNo:
    _item: tipoItem | None = None
    _prox: int | None = None

class listaEstDin:
    def __init__(self, maxTam: int) -> None:
        self._maxTam: int = maxTam
        self._lista: list = [_tipoNo() for i in range(maxTam)]
        self._inicio: int = _TERRA
        self._livre: int = 0
        self._numItens: int = 0
        self._opSt: int = LISTAVAZIA
        for c in range(maxTam - 1):
            self._lista[c]._prox = c + 1
        self._lista[maxTam - 1]._prox = _TERRA
        self.item: tipoItem | None = None

    def vazia(self) -> bool:
        return self._numItens == 0

    def cheia(self) -> bool:
        return self._numItens == self._maxTam

    def _busca(self, valor: int) -> int:
        if self.vazia():
            self._opSt = ITEMINEXISTENTE
            return _TERRA
        else:
            posAnt: int = _TERRA
            posAtual: int = self._inicio
            achou: bool = False
            fimLista: bool = False

            while not achou and not fimLista:
                achou = valor <= self._lista[posAtual]._item.valor

                if not achou:
                    posAnt = posAtual
                    posAtual = self._lista[posAtual]._prox
                    fimLista = posAtual == _TERRA

            if not achou:
                self._opSt = ITEMINEXISTENTE
            elif valor == self._lista[posAtual]._item.valor:
                self._opSt = ITEMEXISTENTE
            else:
                self._opSt = ITEMINEXISTENTE

            return posAnt

    def insere(self, item: tipoItem) -> bool:
        if self.cheia():
            self._opSt = LISTACHEIA
            return False
        else:
            pos: int = self._busca(item.valor)
            if self._opSt == ITEMEXISTENTE:
                return False
            else:
                posLivre: int = self._livre
                self._livre = self._lista[posLivre]._prox
                self._lista[posLivre]._item = deepcopy(item)

                if pos != _TERRA:
                    self._lista[posLivre]._prox = self._lista[pos]._prox
                    self._lista[pos]._prox = posLivre
                else:
                    self._lista[posLivre]._prox = self._inicio
                    self._inicio = posLivre
                    
                self._numItens += 1
                return True

    def remove(self, valor: int) -> bool:
        if self.vazia():
            self._opSt = ITEMINEXISTENTE
            self.item = None
            return False
        else:
            pos: int = self._busca(valor)
            if self._opSt == ITEMINEXISTENTE:
                self.item = False
                return False
            else:
                if pos != _TERRA:
                    aux: int = self._lista[pos]._prox
                    self._lista[pos]._prox = self._lista[aux]._prox
                else:
                    aux: int = self._inicio
                    self._inicio = self._lista[aux]._prox

            self._lista[aux]._prox = self._livre
            self._livre = aux
            self._numItens -= 1
            self.item = deepcopy(self._lista[aux]._item)

            return True

    def mostra(self) -> None:
        print('\nSituação da Lista: ')
        if self.vazia():
            print('VAZIA!')
        else:
            pos = self._inicio
            while pos != _TERRA:
                print(self._lista[pos]._item.valor, end=' ')
                pos = self._lista[pos]._prox
            print()
                    

"""
Módulo Lista Doblemente Ligada
"""

from typing import TypeVar, Iterator, Optional, Generic
from lista import Lista

T = TypeVar("T")

class _Nodo(Generic[T]):
    """
    """
    __slots__ = ("elemento", "siguiente", "anterior")

    def __init__(self, elemento : T) -> None:
        self.elemento : T = elemento
        self.siguiente : Optional[_Nodo[T]] = None
        self.anterior : Optional[_Nodo[T]] = None

class ListaDoblementeLigada(Lista[T]):
    """
    """
    def __init__(self) -> None:
        self.__cabeza : Optional[_Nodo[T]] = None
        self.__rabo : Optional[_Nodo[T]] = None
        self.__longitud = 0

    def __iter__(self) -> Iterator[T]:
        pass

    def agregar(self, elemento: T) -> None:
        pass


    def buscar(self, elemento: T) -> bool:
        pass

    def eliminar(self, elemento: T) -> None:
        pass


    def eliminar_indice(self, indice: int) -> None:
        pass

    def acceder(self, indice: int) -> T:
       pass


    def devolver_indice_elemento(self, elemento: T) -> int:
        pass

    def devolver_longitud(self) -> int:
        pass

    def agregar_final(self, elemento : T) -> None:
        pass
            

    def reversa(self) -> ListaDoblementeLigada[T]:
        pass


    def acceder_nodo(self, indice : int) -> _Nodo:
        pass

    def __str__(self) -> str:
        pass

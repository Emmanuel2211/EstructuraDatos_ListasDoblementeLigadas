from lista_doblemente_ligada import ListaDoblementeLigada

class MainListaDoble():

    def main(self) -> None:
        lista = ListaDoblementeLigada[int]()
        lista.agregar(10)
        lista.agregar(20)
        lista.agregar(30)
        print(lista)               # esperado: [10, 20, 30]
        print(len(lista))          # esperado: 3
        print(20 in lista)         # esperado: True
        print(lista[1])            # esperado: 20
        l = lista.reversa()
        print(l)
        l.agregar_final(34)
        l.agregar_final(45)
        print(l)
        print(l.acceder(3))
        print(l.devolver_indice_elemento(30))

if __name__ == "__main__":
    ld = MainListaDoble()
    ld.main()

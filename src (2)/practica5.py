"""
Resolución del problema del historial del navegador "El Chido".
"""

from lista_doblemente_ligada import ListaDoblementeLigada


class Pagina:
    """Representa una página web individual visitada en el historial."""

    def __init__(self, nombre: str, fecha: str):
        self.nombre = nombre
        self.fecha = fecha

    def __eq__(self, otro: object) -> bool:
        """
        Sobrescribe la igualdad para que dos objetos Pagina sean considerados iguales
        si tienen el mismo nombre, permitiendo a la Lista encontrar y eliminar duplicados.
        """
        if not isinstance(otro, Pagina):
            return False
        return self.nombre == otro.nombre

    def __str__(self) -> str:
        return f"{self.nombre} (Visitado: {self.fecha})"


class Historial:
    """Maneja el historial de navegación utilizando una Lista Doblemente Ligada."""

    def __init__(self):
        self.paginas = ListaDoblementeLigada[Pagina]()

    def cargar_archivo(self, ruta_archivo: str) -> None:
        """
        Lee el archivo txt donde los registros están ordenados cronológicamente
        desde el más antiguo hasta el más reciente[cite: 3].
        """
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                partes = linea.split(":")
                if len(partes) == 2:
                    nombre = partes[0].strip()
                    fecha = partes[1].strip()
                    nueva_pagina = Pagina(nombre, fecha)

                    if self.paginas.buscar(nueva_pagina):
                        self.paginas.eliminar(nueva_pagina)

                    self.paginas.agregar(nueva_pagina)

    def imprimir_historial(self) -> None:
        """Muestra el historial completo en pantalla."""
        print("=== HISTORIAL DE NAVEGACIÓN 'EL CHIDO' ===")
        for pagina in self.paginas:
            print(pagina)
        print("==========================================")


def main() -> None:
    navegador = Historial()
    navegador.cargar_archivo("paginas.txt")
    navegador.imprimir_historial()


if __name__ == "__main__":
    main()

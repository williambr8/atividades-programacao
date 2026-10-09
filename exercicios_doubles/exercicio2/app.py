from abc import ABC, abstractmethod
from typing import Optional


class IRepositorioUsuarios(ABC):

    @abstractmethod
    def adicionar_usuario(self, nome: str):
        pass

    @abstractmethod
    def buscar_usuario(self, nome: str) -> Optional[str]:
        pass


class RepositorioUsuariosFake(IRepositorioUsuarios):

    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome: str):
        self.usuarios.append(nome)

    def buscar_usuario(self, nome: str) -> Optional[str]:
        if nome in self.usuarios:
            return nome

        return None


class GerenciadorUsuarios:

    def __init__(self, repositorio: IRepositorioUsuarios):
        self.repositorio = repositorio

    def registrar_usuario(self, nome: str):
        self.repositorio.adicionar_usuario(nome)

    def encontrar_usuario(self, nome: str) -> Optional[str]:
        return self.repositorio.buscar_usuario(nome)
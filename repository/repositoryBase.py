from abc import ABC, abstractmethod

from clases.clases import (
    AsistentePcyt,
    Beca,
    Credencial,
    Estudiante,
    Posgrado,
    Rol,
    SistemasEscolares,
)


class PosgradoRepositoryBase(ABC):
    @abstractmethod
    def nuevoPosgrado(self, posgrado: Posgrado):
        raise NotADirectoryError()

    @abstractmethod
    def cambiarCoordinador(self, id: Posgrado, coordinador):
        raise NotADirectoryError()

    @abstractmethod
    def eliminarPosgrado(self, id: Posgrado):
        raise NotADirectoryError()


class RolRepositoryBase(ABC):
    @abstractmethod
    def crearRol(self, rol: Rol):
        raise NotImplementedError()


class EstudianteRepositoryBase(ABC):
    @abstractmethod
    def nuevoEstudiante(self, estudiante: Estudiante):
        raise NotImplementedError()

    @abstractmethod
    def crearUsuario(self, estudiante: Estudiante, usuario, password):
        raise NotImplementedError()

    @abstractmethod
    def cambiarUsuario(self, estudiante: Estudiante, usuario):
        raise NotImplementedError()

    @abstractmethod
    def cambiarPassword(self, estudiante: Estudiante, password):
        raise NotImplementedError()

    @abstractmethod
    def actualizarPosgrado(self, estudiante: Estudiante, posgrado):
        raise NotImplementedError()


class SistemasEscolaresRepositoryBase(ABC):
    @abstractmethod
    def nuevoAsistenteSis(self, asistente: SistemasEscolares):
        raise NotImplementedError()

    @abstractmethod
    def crearUsuario(self, asistente: SistemasEscolares, usuario, password):
        raise NotImplementedError()

    @abstractmethod
    def cambiarUsuario(self, asistente: SistemasEscolares, usuario):
        raise NotImplementedError()

    @abstractmethod
    def cambiarPassword(self, asistente: SistemasEscolares, password):
        raise NotImplementedError()


class CredencialRepositoryBase(ABC):
    @abstractmethod
    def solicitudCredencial(self, estudiante: Estudiante, credencial: Credencial):
        raise NotImplementedError()

    @abstractmethod
    def actualizarFirma(self, solicitud: Credencial, firma):
        raise NotImplementedError()

    @abstractmethod
    def actualizarFotografia(self, solicitidud: Credencial, fotografia):
        raise NotImplementedError()

    @abstractmethod
    def insertarObservacion(self, solicitud: Credencial, observacion):
        raise NotADirectoryError()

    @abstractmethod
    def consultarSolicitudes(self):
        raise NotImplementedError()


class AsistentePcytRepositoryBase(ABC):
    @abstractmethod
    def nuevoAsistentePcyt(self, asistente: AsistentePcyt):
        raise NotImplementedError()

    @abstractmethod
    def crearUsuario(self, asistente: AsistentePcyt, usuario, password):
        raise NotImplementedError()

    @abstractmethod
    def cambiarUsuario(self, asistente: AsistentePcyt, usuario):
        raise NotImplementedError()

    @abstractmethod
    def cambiarPassword(self, asistente: AsistentePcyt, password):
        raise NotImplementedError()

    @abstractmethod
    def consultarSolicitudes(self):
        raise NotImplementedError()


class BecaRepositoryBase(ABC):
    @abstractmethod
    def solicitudBeca(self, estudiante: Estudiante, beca: Beca):
        raise NotImplementedError()

    @abstractmethod
    def actualizarSolicitudBeca(self, beca: Beca, solicitud):
        raise NotImplementedError()

    @abstractmethod
    def actualizarArchivosAdjuntos(self, beca: Beca, adjuntos):
        raise NotImplementedError()

    @abstractmethod
    def actualizarCartaApoyo(self, solicitidud: Credencial, carta):
        raise NotImplementedError()

    @abstractmethod
    def insertarObservacion(self, solicitud: Credencial, observacion):
        raise NotADirectoryError()

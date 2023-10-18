class Rol:
    def __init__(self, id, rol):
        self.id = id
        self.rol = rol


class Beca:
    def __init__(
        self,
        idSolicitud,
        estudiante,
        solicitud,
        archivosAdjuntos,
        cartaApoyo,
        observacion,
    ):
        self.idSolicitud = idSolicitud
        self.estudiante = estudiante
        self.solicitud = solicitud
        self.archivosAdjuntos = archivosAdjuntos
        self.cartaApoyo = cartaApoyo
        self.observacion = observacion


class Credencial:
    def __init__(self, id, estudiante, firma, fotografia, observacion):
        self.id = id
        self.estudiante = estudiante
        self.firma = firma
        self.fotografia = fotografia
        self.obserservacion = observacion


class Estudiante:
    def __init__(self, matricula, nombre, posgrado, rol, usuario, password):
        self.matricula = matricula
        self.nombre = nombre
        self.posgrado = posgrado
        self.rol = rol
        self.usuario = usuario
        self.password = password


class SistemasEscolares:
    def __init__(self, idAsistente, nombre, rol, usuario, password):
        self.idAsistente = idAsistente
        self.nombre = nombre
        self.usuario = usuario
        self.rol = rol
        self.usuario = usuario
        self.password = password


class Posgrado:
    def __init__(self, idPosgrado, posgrado, coordinador):
        self.idPosgrado = idPosgrado
        self.posgrado = posgrado
        self.coordinador = coordinador


class AsistentePcyt:
    def __init__(self, idAsistente, nombre, rol, usuario, password):
        self.idAsistente = idAsistente
        self.nombre = nombre
        self.rol = rol
        self.usuario = usuario
        self.password = password

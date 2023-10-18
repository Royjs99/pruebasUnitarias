from BD.BaseDeDatos import BaseDeDatos
from clases.clases import (
    AsistentePcyt,
    Credencial,
    Estudiante,
    Beca,
    SistemasEscolares,
    Rol,
    Posgrado,
)


class PosgradoRepository(BaseDeDatos, Posgrado):
    def nuevoPosgrado(self, posgrado: Posgrado):
        cursor = self.conn.cursor()
        sql = "INSERT INTO `posgrado` (`idposgrado`, `posgrado`, `coordinador`) VALUES (NULL, %s, %s)"
        valores = (posgrado.posgrado, posgrado.coordinador)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def cambiarCoordinador(self, id: Posgrado, coordinador):
        cursor = self.conn.cursor()
        sql = "UPDATE `posgrado` SET `coordinador` = %s WHERE `posgrado`.`idposgrado` = %s"
        valor = [coordinador, id.idPosgrado]
        cursor.execute(sql, valor)
        self.conn.commit()
        cursor.close()

    def eliminarPosgrado(self, id: Posgrado):
        cursor = self.conn.cursor()
        sql = "DELETE FROM posgrado WHERE `posgrado`.`idposgrado` = %s"
        valor = [id.idPosgrado]
        cursor.execute(sql, valor)
        self.conn.commit()
        cursor.close()

    def consultarPosgrado(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM posgrado")
        datos = cursor.fetchall()
        return datos

    def consultarPosgradoEliminado(self, id: Posgrado):
        cursor = self.conn.cursor()
        sql = "SELECT idposgrado FROM posgrado WHERE idposgrado = %s"
        valor = [id.idPosgrado]
        cursor.execute(sql, valor)
        datos = cursor.fetchone()
        return datos


class RolRepository(BaseDeDatos):
    def crearRol(self, rol: Rol):
        cursor = self.conn.cursor()
        sql = "INSERT INTO `rol` (`idrol`, `rol`) VALUES (NULL, %s);"
        valores = rol.rol
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def consultaRol(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM rol")
        datos = cursor.fetchall()
        return datos


class EstudianteRepository(BaseDeDatos):
    def nuevoEstudiante(self, estudiante: Estudiante):
        cursor = self.conn.cursor()
        sql = "INSERT INTO `estudiante` (`matricula`, `nombre`, `posgrado_idposgrado`, `rol_idrol`, `usuario`, `password`) VALUES (%s, %s, %s, %s, NULL, NULL) "
        valores = [
            estudiante.matricula,
            estudiante.nombre,
            estudiante.posgrado,
            estudiante.rol,
        ]

        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def crearUsuario(self, estudiante: Estudiante, usuario, password):
        cursor = self.conn.cursor()
        sql = "UPDATE `estudiante` SET `usuario` = %s, `password` = %s WHERE `estudiante`.`matricula` = %s "
        valores = [usuario, password, estudiante.matricula]
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def cambiarUsuario(self, estudiante: Estudiante, usuario):
        cursor = self.conn.cursor()
        sql = "UPDATE `estudiante` SET `usuario` = %s WHERE `estudiante`.`matricula` = %s "
        valores = (usuario, estudiante.matricula)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def cambiarPassword(self, estudiante: Estudiante, password):
        cursor = self.conn.cursor()
        sql = "UPDATE `estudiante` SET `password` = %s WHERE `estudiante`.`matricula` = %s "
        valores = (password, estudiante.matricula)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def actualizarPosgrado(self, estudiante: Estudiante, posgrado):
        cursor = self.conn.cursor()
        sql = "UPDATE `estudiante` SET `posgrado_idposgrado` = %s WHERE `estudiante`.`matricula` = %s "
        valores = (posgrado, estudiante.matricula)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def consultarAlumnos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM estudiante")
        datos = cursor.fetchall()
        return datos


class SistemasEscolaresRepository(BaseDeDatos):
    def nuevoAsistenteSis(self, asistente: SistemasEscolares):
        cursor = self.conn.cursor()
        sql = "INSERT INTO `sistemasescolares` (`idAsistente`, `nombre`, `rol_idrol`, `usuario`, `password`) VALUES (NULL, %s, %s, NULL, NULL) "
        valores = (asistente.nombre, asistente.rol)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def crearUsuario(self, asistente: SistemasEscolares, usuario, password):
        cursor = self.conn.cursor()
        sql = "UPDATE `sistemasescolares` SET `usuario` = %s, `password` = %s WHERE `sistemasescolares`.`idasistente` = %s "
        valores = (usuario, password, asistente.idAsistente)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def cambiarUsuario(self, asistente: SistemasEscolares, usuario):
        cursor = self.conn.cursor()
        sql = "UPDATE `sistemasescolares` SET `usuario` = %s WHERE `sistemasescolares`.`idAsistente` = %s AND `sistemasescolares`.`nombre` = %s"
        valores = (usuario, asistente.idAsistente, asistente.nombre)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def cambiarPassword(self, asistente: SistemasEscolares, password):
        cursor = self.conn.cursor()
        sql = "UPDATE `sistemasescolares` SET `password` = %s WHERE `sistemasescolares`.`idasistente` = %s "
        valores = (password, asistente.idAsistente)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def consultarAsistentes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM sistemasescolares")
        datos = cursor.fetchall()
        return datos


class AsistentePcytRepository(BaseDeDatos):
    def nuevoAsistentePcyt(self, asistente: AsistentePcyt):
        cursor = self.conn.cursor()
        sql = "INSERT INTO `asistentepcyt` (`idAsistente`, `nombre`, `rol_idrol`, `usuario`, `password`) VALUES (NULL, %s, %s, NULL, NULL) "
        valores = (asistente.nombre, asistente.rol)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def crearUsuario(self, asistente: AsistentePcyt, usuario, password):
        cursor = self.conn.cursor()
        sql = "UPDATE `asistentepcyt` SET `usuario` = %s, `password` = %s WHERE `asistentepcyt`.`idasistente` = %s "
        valores = (usuario, password, asistente.idAsistente)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def cambiarUsuario(self, asistente: AsistentePcyt, usuario):
        cursor = self.conn.cursor()
        sql = "UPDATE `asistentepcyt` SET `usuario` = %s WHERE `asistentepcyt`.`idasistente` = %s "
        valores = (usuario, asistente.idAsistente)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def cambiarPassword(self, asistente: AsistentePcyt, password):
        cursor = self.conn.cursor()
        sql = "UPDATE `asistentepcyt` SET `password` = %s WHERE `asistentepcyt`.`idasistente` = %s "
        valores = (password, asistente.idAsistente)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def consultarSolicitudes(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """SELECT estudiante_matricula AS 'Matricula', estudiante.nombre, posgrado.posgrado,cartaApoyo, archivosAdjuntos, cartaApoyo FROM beca JOIN estudiante JOIN posgrado ON estudiante.posgrado_idposgrado = posgrado.idposgrado AND estudiante_matricula = estudiante.matricula;"""
        )
        solicitudes = cursor.fetchone()
        cursor.close()
        return solicitudes

    def consultarAsistentes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM asistentepcyt")
        datos = cursor.fetchall()
        return datos


class CredencialRepository(BaseDeDatos):
    def solicitudCredencial(self, estudiante: Estudiante, credencial: Credencial):
        cursor = self.conn.cursor()
        sql = "INSERT INTO `credencial` (`idDocumentos`, `estudiante_matricula`, `firma`,`fotografia`, `observacion`) VALUES (NULL, %s, %s, %s, NULL)"
        valores = (estudiante.matricula, credencial.firma, credencial.fotografia)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def actualizarFirma(self, solicitud: Credencial, firma):
        cursor = self.conn.cursor()
        sql = """UPDATE `credencial` SET `firma` = %s WHERE `credencial`.`idDocumentos` = %s"""
        valores = (firma, solicitud.id)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def actualizarFotografia(self, solicitidud: Credencial, fotografia):
        cursor = self.conn.cursor()
        sql = """UPDATE `credencial` SET `fotografia` = %s WHERE `credencial`.`idDocumentos` = %s """
        valores = (fotografia, solicitidud.id)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def insertarObservacion(self, credencial: Credencial, observacion):
        cursor = self.conn.cursor()
        sql = """UPDATE `credencial` SET `observacion` = %s WHERE `credencial`.`iddocumentos` = %s"""
        valores = (observacion, credencial.id)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def consultarSolicitudes(self):
        cursor = self.conn.cursor()
        cursor.execute(
                """SELECT estudiante_matricula AS 'Matricula', estudiante.nombre, posgrado.posgrado,firma,
                fotografia FROM credencial JOIN estudiante JOIN posgrado ON estudiante.posgrado_idposgrado = posgrado.idposgrado
                AND credencial.estudiante_matricula = estudiante.matricula;"""
        )
        solicitudes = cursor.fetchall()
        cursor.close()
        return solicitudes


class BecaRepository(BaseDeDatos):
    def solicitudBeca(self, estudiante: Estudiante, beca: Beca):
        cursor = self.conn.cursor()
        sql = "INSERT INTO `beca` (`idSolicitud`, `estudiante_matricula`, `solicitudBeca`, `archivosAdjuntos`, `cartaApoyo`, `observacion`) VALUES (NULL, %s, %s, %s, %s, NULL)"
        valores = (
            estudiante.matricula,
            beca.solicitud,
            beca.archivosAdjuntos,
            beca.cartaApoyo,
        )
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def actualizarSolicitudBeca(self, beca: Beca, solicitud):
        cursor = self.conn.cursor()
        sql = (
            """UPDATE `beca` SET `solicitudbeca` = %s WHERE `beca`.`idsolicitud` = %s"""
        )
        valores = (solicitud, beca.idSolicitud)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def actualizarArchivosAdjuntos(self, beca: Beca, adjuntos):
        cursor = self.conn.cursor()
        sql = """UPDATE `beca` SET `archivosadjuntos` = %s WHERE `beca`.`idsolicitud` = %s"""
        valores = (adjuntos, beca.idSolicitud)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def actualizarCartaApoyo(self, beca: Beca, carta):
        cursor = self.conn.cursor()
        sql = """UPDATE `beca` SET `cartaapoyo` = %s WHERE `beca`.`idsolicitud` = %s"""
        valores = (carta, beca.idSolicitud)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def insertarObservacion(self, beca: Beca, observacion):
        cursor = self.conn.cursor()
        sql = """UPDATE `beca` SET `observacion` = %s WHERE `beca`.`idsolicitud` = %s"""
        valores = (observacion, beca.idSolicitud)
        cursor.execute(sql, valores)
        self.conn.commit()
        cursor.close()

    def consultaBeca(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM beca")
        datos = cursor.fetchall()
        return datos

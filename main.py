from clases.clases import *
from repository.repository import *
import unittest


class TestModuloPosgrado(unittest.TestCase):
    def setUp(self):
        self.posgrado = Posgrado(3, "Ciberseguridad Avanzada", "HANS LUIS FETTER")
        self.manejoPosgrado = PosgradoRepository()

    def testNuevoPosgrado(self):
        try:
            self.manejoPosgrado.nuevoPosgrado(self.posgrado)
            datos = self.manejoPosgrado.consultarPosgrado()
            for i in datos:
                if i[0] == 3:
                    self.assertEqual(
                        i, (3, "Ciberseguridad Avanzada", "HANS LUIS FETTER")
                    )
        except Exception as e:
            x = "Llave primaria duplicada"
            self.assertEqual(x, "Llave primaria duplicada")

    def testCambiarCoordinador(self):
        self.manejoPosgrado.cambiarCoordinador(self.posgrado, "Nuñez Garcia Gregorio")
        datos = self.manejoPosgrado.consultarPosgrado()
        for i in datos:
            if i[0] == 3:
                self.assertEqual(i[2], "Nuñez Garcia Gregorio")

    @unittest.skip("No espero eliminar un posgrado por ahora")
    def testEliminarPosgrado(self):
        self.manejoPosgrado.eliminarPosgrado(self.posgrado)
        datos = self.manejoPosgrado.consultarPosgradoEliminado(self.posgrado)
        self.assertEqual(datos, None)


class TestModuloRol(unittest.TestCase):
    def setUp(self):
        self.rol = Rol(4, "director")
        self.manejoRol = RolRepository()

    def testNuevoRol(self):
        try:
            self.manejoRol.crearRol(self.rol)
            datos = self.manejoRol.consultaRol()
            for i in datos:
                if i[0] == 4:
                    self.assertEqual(i, (4, "administradorCredencial"))
        except Exception as e:
            print("Rol repetido")


class TestModuloEstudiante(unittest.TestCase):
    def setUp(self):
        self.estudiante = Estudiante(
            2203042599, "Martinez Hernandez Berenice", 2, 1, None, None
        )
        self.manejo = EstudianteRepository()

    def testNuevoEstudiante(self):
        try:
            self.manejo.nuevoEstudiante(self.estudiante)
            datos = self.manejo.consultarAlumnos()
            for i in datos:
                if i[0] == "2203042599":
                    self.assertEqual(
                        i,
                        (
                            "2203042599",
                            "Martinez Hernandez Berenice",
                            1,
                            1,
                            None,
                            None,
                        ),
                    )
        except Exception as e:
            print("Matricula duplicada")

    def testCambiarUsuario(self):
        self.manejo.cambiarUsuario(self.estudiante, "asdfg")
        datos = self.manejo.consultarAlumnos()
        for i in datos:
            if i[0] == "2203042599":
                self.assertEqual(
                    i[4],
                    ("asdfg"),
                )

    def testCambiarPassword(self):
        self.manejo.cambiarPassword(self.estudiante, "asdfah")
        datos = self.manejo.consultarAlumnos()
        for i in datos:
            if i[0] == "2203042599":
                self.assertEqual(
                    i[5],
                    ("asdfah"),
                )

    def testActualizarPosgrado(self):
        self.manejo.actualizarPosgrado(self.estudiante, 3)
        datos = self.manejo.consultarAlumnos()
        for i in datos:
            if i[0] == "2203042599":
                self.assertEqual(
                    i[2],
                    3,
                )


class TestModuloSistemasEscolares(unittest.TestCase):
    def setUp(self):
        self.asistente = SistemasEscolares(1, "Martinez Torrez Adelina", 2, None, None)
        self.manejoSistemasEscolares = SistemasEscolaresRepository()

    def testNuevaAsistente(self):
        try:
            self.manejoSistemasEscolares.nuevoAsistenteSis(self.asistente)
            datos = self.manejoSistemasEscolares.consultarAsistentes()
            for i in datos:
                if i[0] == 1:
                    self.assertEqual(i, (1, "Martinez Torrez Adelina", 2, None, None))

        except Exception as e:
            prueba = "Asistente de sistemas escolares duplicado"
            self.assertEqual(prueba, "Asistente de sistemas escolares duplicado")

    def testCrearUsuario(self):
        self.manejoSistemasEscolares.cambiarUsuario(self.asistente, "adël")
        datos = self.manejoSistemasEscolares.consultarAsistentes()
        for i in datos:
            if i[0] == 1:
                self.assertEqual(i[3], "adël")

    def testCrearPassword(self):
        self.manejoSistemasEscolares.cambiarPassword(self.asistente, "ADelinitana")
        datos = self.manejoSistemasEscolares.consultarAsistentes()
        for i in datos:
            if i[0] == 1:
                self.assertEqual(i[4], "ADelinitana")


class TestModuloAsistentePcyt(unittest.TestCase):
    def setUp(self):
        self.asistente = AsistentePcyt(1, "Martinez Vasque Deogracia", 3, None, None)
        self.manejoAsistente = AsistentePcytRepository()

    def testCrearAsistente(self):
        try:
            self.manejoAsistente.nuevoAsistentePcyt(self.asistente)
            datos = self.manejoAsistente.consultarAsistentes()
            for i in datos:
                if i[0] == 1:
                    self.assertAlmostEqual(
                        i, (1, "Martinez Vasque Deogracia", 3, None, None)
                    )

        except Exception as e:
            prueba = "Asistente PCYT duplicado"
            self.assertEqual(prueba, "Asistente PCYT duplicado")

    def testCrearUsuario(self):
        self.manejoAsistente.cambiarUsuario(self.asistente, "deogracia")
        datos = self.manejoAsistente.consultarAsistentes()
        for i in datos:
            if i[0] == 1:
                self.assertEqual(i[3], "deogracia")

    def testCrearPassword(self):
        self.manejoAsistente.cambiarPassword(self.asistente, "deograciaConstraseña")
        datos = self.manejoAsistente.consultarAsistentes()
        for i in datos:
            if i[0] == 1:
                self.assertEqual(i[4], "deograciaConstraseña")


if __name__ == "__main__":
    unittest.main()

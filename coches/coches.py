from conexionBD import conexion, cursor

class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        self._velocidad -= 1

    @property
    def velocidad(self):
        return self._velocidad

    @property
    def marca(self):
        return self._marca

    @property
    def color(self):
        return self._color

    @property
    def modelo(self):
        return self._modelo

    @property
    def potencia(self):
        return self._potencia

    @property
    def asientos(self):
        return self._asientos



    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @color.setter
    def color(self, color):
        self._color = color

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia

    @asientos.setter
    def asientos(self, asientos):
        self._asientos = asientos


    def insertar(self):
        try:
            cursor.execute("insert into coches values (null, %s, %s, %s, %s, %s, %s)", (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from coches")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from coches where id=%s",(id,))
            conexion.commit()
            return True
        except:
            return False

    def actualizar(self, id):
        try:
            cursor.execute("update coches set marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, asientos=%s where id=%s",(self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos, id))
            conexion.commit()
            return True
        except: 
            return False
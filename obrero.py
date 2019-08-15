class Obrero(Persona):

    def __init__(self, cedula, nombre, apellido, sexo, area):
        Persona.__init__(self, cedula, nombre, apellido,sexo)

        self.area = area

        def __str__(self):
            return "%s: %s, area: '%s'." % ( self.__doc__[24:37], self.nombre, self.apellido, self.area)

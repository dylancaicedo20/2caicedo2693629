class Empleado:
    counter = 0

    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
        Empleado.counter += 1

    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setCargo(self, cargo):
        self.__cargo = cargo
    
    def setSalario(self, salario):
        self.__salario = salario
    
    def getNombre(self):
        return self.__nombre
    
    def getCargo(self):
        return self.__cargo
    
    def getSalario(self):
        return self.__salario
    
    def salHora(self):
        x = self.__salario / 30
        y = x / 7
        z = y / 24
        return z
    
    def aumIPC(self):
        aumento = self.__salario * 0.1312
        nuevo_salario = self.__salario + aumento
        return nuevo_salario
    
    def calcular_salario(self, horas_extras):
        horas_extras_diarias = self.limitar_horas_extras(horas_extras, 2)  
        horas_trabajadas = 8 + horas_extras_diarias  
        salario_hora = self.__salario / 40  
        salario_total = salario_hora * horas_trabajadas * 5  
        return salario_total

    def limitar_horas_extras(self, horas_extras, max_horas_diarias):
        if horas_extras <= max_horas_diarias:
            return horas_extras
        else:
            return max_horas_diarias


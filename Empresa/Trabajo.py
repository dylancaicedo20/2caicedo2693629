from empleado import Empleado

em1 = Empleado("Juan", "Técnico", 1800000)
em2 = Empleado("Andrea", "Ingeniera", 3500000)
em3 = Empleado("Sebastián", "Arquitecto", 4000000)

print("Información del Empleado 1:")
print("Nombre:", em1.getNombre())
print("Cargo:", em1.getCargo())
print("Salario:", em1.getSalario())
print("Salario por hora:", em1.salHora())
print("Aumento del salario:", em1.aumIPC())

print("\nInformación del Empleado 2:")
print("Nombre:", em2.getNombre())
print("Cargo:", em2.getCargo())
print("Salario:", em2.getSalario())
print("Salario por hora:", em2.salHora())
print("Aumento del salario:", em2.aumIPC())

print("\nInformación del Empleado 3:")
print("Nombre:", em3.getNombre())
print("Cargo:", em3.getCargo())
print("Salario:", em3.getSalario())
print("Salario por hora:", em3.salHora())
print("Aumento del salario:", em3.aumIPC())
print("\nEl numero total de veces que se creo un objeto de la clase fue de:",Empleado.counter)
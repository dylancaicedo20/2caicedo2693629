from ModuloRequisicion import *
from PaginaRequisicion import *
from inicio_secion import *

usuario = None
plataforma_busqueda_empleo = ModuloRequisicion()

def iniciar_sesion():
    print("=== Iniciar Sesión ===")
    tipo_usuario = input("Seleccione el tipo de usuario (candidato/empresa): ")
    correo = input("Ingrese su correo: ")
    contraseña = input("Ingrese su contraseña: ")

    if tipo_usuario.lower() == "candidato":
        return Candidato(correo, correo, contraseña)
    elif tipo_usuario.lower() == "empresa":
        return Empresa(correo, correo, contraseña)
    else:
        print("Tipo de usuario inválido.")
        return None

def mostrar_menu(usuario):
    print("=== Menú ===")
    if isinstance(usuario, Candidato):
        print("1. Buscar requisiciones")
    elif isinstance(usuario, Empresa):
        print("2. Publicar requisición")
    print("3. Salir")

def buscar_requisiciones(candidato):
    criterios = input("Ingrese los criterios de búsqueda: ")
    requisiciones = candidato.buscarRequisiciones(criterios)
    if requisiciones:
        print("Requisiciones encontradas:")
        for requisicion in requisiciones:
            print(f"- {requisicion.getTituloPuesto()}")
    else:
        print("No se encontraron requisiciones.")

def publicar_requisicion(empresa):
    titulo_puesto = input("Ingrese el título del puesto: ")
    descripcion = input("Ingrese la descripción: ")
    responsabilidades = input("Ingrese las responsabilidades: ")
    habilidades_requeridas = input("Ingrese las habilidades requeridas: ")
    experiencia_requerida = input("Ingrese la experiencia requerida: ")
    requisitos_educativos = input("Ingrese los requisitos educativos: ")
    competencias_necesarias = input("Ingrese las competencias necesarias: ")
    ubicacion = input("Ingrese la ubicación: ")
    salario = input("Ingrese el salario: ")

    requisicion = ModuloRequisicion.crearRequisicion(titulo_puesto, descripcion, responsabilidades, habilidades_requeridas, experiencia_requerida, requisitos_educativos, competencias_necesarias, ubicacion, salario)
    Empresa.publicarRequisicion(requisicion)
    print("Requisición publicada correctamente.")

def main():
    usuario = iniciar_sesion()
    if usuario is not None:
        print("¡Inicio de sesión exitoso!")
        while True:
            mostrar_menu(usuario)
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                if isinstance(usuario, Candidato):
                    buscar_requisiciones(usuario)
                else:
                    print("Opción inválida. Intente nuevamente.")
            elif opcion == "2":
                if isinstance(usuario, Empresa):
                    publicar_requisicion(usuario)
                else:
                    print("Opción inválida. Intente nuevamente.")
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
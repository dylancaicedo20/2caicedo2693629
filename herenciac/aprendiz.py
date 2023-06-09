from Persona import *
from Curso import *

class Aprendiz(Persona):
    def __init__(self,nombre,documento,formacion,ficha):
        # llama al constructor de la clase padre (Persona) para inicializar el nombre y el documento
        Persona.__init__(self,nombre,documento)
        self.__formacion=formacion #inicializa la formacion del aprendiz
        self.__ficha=ficha #inicializa la ficha del aprendiz
        self.__cursos=[] #inicializa una lista vacia para almacenar los cursos del aprendiz
    
    def agregarCurso(self,curso):
        self.__cursos.append(curso) #agrega un curso a la lista de cursos del aprendiz
    
    def componerCurso(self):
        nombreCurso=input('Ingrese nombre del curso') #solicita al usuario ingresar el nombre del curso
        tipoCurso=input('Ingrese tipo del curso') #solicita al usuario ingresar el tipo del curso
        objcurso=Curso(nombreCurso,tipoCurso) #crea un objeto Curso con el nombre y tipo proporcionados
        self.__cursos.append(objcurso) #agrega el objeto curso a la lista de cursos del aprendiz
    
    def verCursos(self):
        return self.__cursos #devuelve la lista de cursos del aprendiz

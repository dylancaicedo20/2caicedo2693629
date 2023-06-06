class persona:
    def __init__(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__cursos = []
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setDocumento(self, documento):
        self.__documento = documento
    
    def getDocumento(self):
        return self.__documento

    def addCurso(self, curso):
        self.__cursos.append(curso)

    def getCursos(self):
        return self.__cursos
    
    def eliminarCurso(self, curso):
        if curso in self.__cursos:
            self.__cursos.remove(curso)
        else:
            print("El curso que desea eliminar no está en la lista de cursos.")

    
    def modificarNombreCurso(self, curso_antiguo, nuevo_nombre):
        for i in range(len(self.__cursos)):
            if self.__cursos[i] == curso_antiguo:
                self.__cursos[i] = nuevo_nombre
                break
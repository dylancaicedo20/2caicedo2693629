<<<<<<< HEAD
from persona import *

ob1=persona("juan",12356)

persona = persona("Juan", "12345678")
print(persona.getNombre()) 
print(persona.getDocumento())  

cursos = persona.getCursos()
print(cursos)

persona.addCurso("Matematicas")
persona.addCurso("Ingles")
persona.addCurso("Historia")
persona.addCurso("Física")
persona.addCurso("Español")
persona.addCurso("Informatica")
cursos = persona.getCursos()
print(cursos)

persona.modificarNombreCurso("Historia", "Geografía")
persona.modificarNombreCurso("Matematicas","Calculo")
persona.modificarNombreCurso("Informatica","Computacion")
cursos = persona.getCursos()
print(cursos) 


print(persona.eliminarCursos("Español"))
=======
from persona import *

ob1=persona("juan",12356)

persona = persona("Juan", "12345678")
print(persona.getNombre()) 
print(persona.getDocumento())  

cursos = persona.getCursos()
print(cursos)

persona.addCurso("Matematicas")
persona.addCurso("Ingles")
persona.addCurso("Historia")
persona.addCurso("Fisica")
persona.addCurso("Español")
persona.addCurso("Informatica")
cursos = persona.getCursos()
print(cursos)

persona.modificarNombreCurso("Historia", "Geografía")
persona.modificarNombreCurso("Matematicas","Calculo")
persona.modificarNombreCurso("Informatica","Computacion")
cursos = persona.getCursos()
print(cursos) 


persona.eliminarCurso("Fisica")

print (cursos)
>>>>>>> 10644f1149074537a6c506f64c2eb3284bcd5727

Instrucciones para Copilot: 
###
Programamos en python completamente tipado

Usamos el patrón repositorio para separar lógica de persistencia de nuestra lógica de negocio

Usamos casos de uso, encapsulamos acciones sobre dominio en clases que tienen un método execute que recibe una dataclass con los argumentos de ejecución. Estos casos de uso reciben inyectadas las dependencias como pueden ser los repositorios.

Usamos objetos de dominio separados de las entidades de datos de la base de datos. El mapeo entre ambas entidades ocurre en el repositorio.

Tenemos varias capas:
Dominio donde creamos las entidades
Aplicación donde creamos los casos de uso
Infrastructura donde creamos los endpoints y las implementaciones específicas de las abstracciones como pueden ser los repositorios

Usamos vertical slices, cada vertical slice tiene su propia carpeta con el dominio, la aplicación y la infraestructura.
Pasos realizados.

1. Crear el programa con DJANGO
2. crear una App la cual se encarge de todo organizadamente
3. linkear la url de la urls.py main al de la app
4. crear los modelos
5. crear sus respectivos forms
6. Con estos 2 crear los views que recolectan los datos y los guardan en la base de datos
7. crear el buscador de datos
8. migrar todo al sistema
9. iniciar git
10. pushear hacia el repositorio de github



  Como funciona 

El usuario entra en el link , el urls.py llama a la funcion la cual le asignemos.Dependiendo que le pusimos a esa funcion , el usuario envia datos a nuestra base de datos que fue construida anteriormente con nuestros modelos o funciona un get
en busqueda de obtener un valor en base a otro. En este ultimo caso , el usuario es redirigido a una urls cuya fuincion recolecta los datos que el usuario haya dado en el form y los compara con los de la base de datos para determinar su valores
y devuelve el valor que le corresponde a la "key" que entrego el usuario.
   

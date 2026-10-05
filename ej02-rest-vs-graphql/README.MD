## Ejercicio 2 rest vs graphql

* Eficiencia en las peticiones (Round-trips): Para obtener la información deseada, con REST tuve que realizar 10 peticiones HTTP independientes (una por cada Pokémon), mientras que con GraphQL solo necesité enviar 1 sola petición.  

*  Optimización de tiempo de respuesta: El tiempo total de procesamiento en REST fue de 5117 ms, mientras que con GraphQL descendió drásticamente a 489 ms, resultando GraphQL 10 veces más rápido en esta prueba.  


* Control de sobrecarga de datos (Over-fetching): REST me transfirió un peso total de 3,072,345 bytes (~3 MB) debido a que devuelve la estructura completa de la entidad. Por el contrario, GraphQL únicamente transfirió 516 bytes, solicitando solo los campos específicos que necesitaba (como el nombre, peso y tipo). 
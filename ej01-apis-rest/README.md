## Ejercico 01: APIS REST
## Errores provocados 

### PREGUNTAS
### ¿Qué parte de la respuesta realmente usaste?
De la pokeAApi solo tome los nombres de las hablilidades de pikachu, y fue : *static, lightning-rod*

### ¿Qué porcentaje de los bytes recibidos fue innecesario? 
Peso *300,521* porque incluye toda la informacion de pikachu, sin embargo en el script solo filtramos y aguardamos habilidades las cuales pesan unos *28 a 30 bytes*. Esto sigifica que casi el 100% de la carga de red fue datos no utilizados. 

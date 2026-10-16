1. separar la API del eje.3 en servicio de ventas y servicio de IA
2. entrenar un modelo sencillo (p. ej.LinearRegression con datos sinteticos de ventas) y aguardalo conn joblib
3. Agregar un gateway y levanta todo con docker compose
4. ejecuta carga.py con 1 y con 3 replicas; reporta rps, p50 y p95
5. Ejecuta el mismo compose en GitHUB codespaces con el puerto publico (practica2)
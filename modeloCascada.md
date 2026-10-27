# Modelo en cascada: dificultades encontradas

En esta actividad trabajamos con el modelo en cascada: [primero se hizo el backend, luego el frontend y al final se juntó todo para probar]. Estas fueron las dificultades que encontramos.

## 1. Errores descubiertos al final
Algunos errores solo aparecieron al juntar las dos partes, y por eso encontrarlos tomó más tiempo que en otros modelos, donde las pruebas se hacen desde el inicio. Por ejemplo, en el Excel los Ids estaban guardados como números y no como texto. La consulta compara el Id con el texto que escribe el usuario, así que nunca encontraba el producto y el programa decía que no existía. Como esto se descubrió después de unir las dos partes, tuvimos que hacer otro commit para corregirlo, y así el programa funcionó al seleccionar la opción de consultar producto e ingresar el Id.

## 2. Acuerdos previos
En este modelo es importante definir esos acuerdos antes de empezar, porque después es más difícil cambiarlos.

## 3. Dependencia entre etapas
El frontend no se podía probar con datos reales hasta que el backend estuviera listo. Para comprobar que su código funcionaba, David creó un backend de prueba con funciones que devolvían datos falsos, y con ese verificó el frontend.

## 4. Archivos que no son de ningún rol
La actividad solo reparte los roles de backend y frontend, por lo que `main.py` y la carpeta `utils` no pertenecían a ningún rol, aunque son parte del proyecto. David creó `main.py` directamente en la rama main, y creó la carpeta `utils` con su archivo `terminal.py` en su propia rama, que llegó a main junto con sus demás archivos al hacer el merge.
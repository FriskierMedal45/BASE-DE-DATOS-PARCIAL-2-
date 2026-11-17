# Sistema de Carrito de Compras con Redis (NoSQL)

Este proyecto implementa la lógica de almacenamiento para un carrito de compras en línea utilizando **Redis**, una base de datos NoSQL de tipo clave-valor. La base de datos está alojada en la nube a través de **Upstash**, lo que permite realizar operaciones CRUD de forma remota y aplicar políticas de expiración automática de datos mediante el uso de TTL (Time To Live).

## Estructura del Repositorio

* `main.py`: Contiene la conexión segura con el servidor en la nube, las funciones modulares para gestionar el carrito (crear, leer, actualizar y eliminar) y el bloque de prueba con datos iniciales (seeding).
* `requirements.txt`: Lista las librerías de Python necesarias para que el proyecto funcione.
* `README.md`: Documentación general con los requisitos e instrucciones de ejecución.

## Requerimientos

Para correr este proyecto de manera local en tu computadora necesitas lo siguiente:

* Tener instalado **Python 3.7** o una versión superior.
* Contar con el gestor de paquetes **pip** (viene incluido al instalar Python).
* Conexión a internet para poder comunicarte con la instancia en la nube.

*Nota: No es necesario instalar Redis localmente en tu equipo, ya que la conexión apunta directamente al servicio alojado en Upstash.*

## Instalación

1. Descarga los archivos de este proyecto o clona el repositorio en tu computadora.
2. Abre la terminal de tu sistema y ubícate dentro de la carpeta del proyecto.
3. Ejecuta el siguiente comando para instalar la librería necesaria para conectar Python con Redis:

```bash
pip install -r requirements.txt
```

*(Si trabajas en macOS o Linux, es probable que debas usar `pip3` en lugar de `pip`).*

## Ejecución

Una vez instalada la librería, sigue estos pasos para correr la simulación:

1. Asegúrate de seguir ubicado en la carpeta raíz del proyecto dentro de tu terminal.
2. Ejecuta el archivo principal con el comando:

```bash
python main.py
```

*(En macOS o Linux utiliza `python3 main.py`).*

### Qué esperar al ejecutarlo

Al correr el programa, verás en la consola el ciclo completo de un carrito de compras simulado:

1. **[CREATE]**: Se inicializa la base de datos creando un carrito para un usuario de prueba con un primer producto y un tiempo de vida de 30 minutos.
2. **[READ]**: Se consulta el servidor en la nube para verificar que la información se guardó correctamente.
3. **[UPDATE]**: Se simula que el usuario agrega otro artículo, actualizando la lista y reiniciando su tiempo de expiración.
4. **[INFO]**: Se consulta directamente al servidor cuántos segundos le quedan de vida al registro antes de borrarse por inactividad.
5. **[DELETE]**: Se elimina el carrito de la memoria para simular que el cliente finalizó su compra.
# Generador Masivo de Usuarios Falsos con Django y Faker

![Imagen django](https://img2.lancers.jp/projectblob/143100/2240958/9a6cdbe8d555f70eaffc3b2119d1e36dba325727ef1dd1080a5525296376b4bf/32359041_1000_0.png)


Este proyecto consiste en el desarrollo de un sistema de generación masiva de usuarios falsos utilizando Django, Faker y MySQL. El objetivo principal es crear un script en Django que genere una gran cantidad de usuarios falsos de manera eficiente y realista. Estos usuarios falsos se almacenarán en una base de datos MySQL y podrán ser utilizados para pruebas, desarrollo y demostración de sistemas.

## Tecnologías Utilizadas

- **Django**: Framework de desarrollo web de alto nivel basado en Python que facilita la creación rápida y el desarrollo de aplicaciones web.
- **Faker**: Librería de Python que genera datos falsos realistas, como nombres, direcciones, direcciones de correo electrónico, entre otros.
- **MySQL**: Sistema de gestión de bases de datos relacional de código abierto ampliamente utilizado para almacenar y administrar datos.

## Funcionalidades Principales

- Generación masiva de usuarios falsos: El script desarrollado en Django utiliza la librería Faker para generar una gran cantidad de usuarios falsos de manera eficiente.
- Almacenamiento en MySQL: Los usuarios falsos generados se almacenan en una base de datos MySQL para su posterior uso y análisis.
- Flexibilidad de configuración: El sistema permite ajustar diversos parámetros de generación, como la cantidad de usuarios a generar y los campos de datos a incluir.
- Interfaz de usuario simple: Se proporciona una interfaz de usuario básica para configurar y ejecutar el proceso de generación de usuarios falsos.

## Configuración del Proyecto

Para configurar y ejecutar el proyecto en tu entorno local, sigue estos pasos:

1. Clona este repositorio en tu máquina local utilizando el siguiente comando:

https://github.com/Bemontx/UsersFake


2. Instala las dependencias del proyecto utilizando pip:

pip install -r requirements.txt


3. Configura la conexión a la base de datos MySQL en el archivo `settings.py`.

4. Ejecuta las migraciones de la base de datos para crear las tablas necesarias:

python manage.py migrate


5. Ejecuta el script de generación de usuarios falsos utilizando el comando:

python manage.py generar_usuarios --cantidad <cantidad-de-usuarios>


6. ¡Disfruta de tu base de datos llena de usuarios falsos para tus pruebas y desarrollo!

## Contribución

Si deseas contribuir a este proyecto, ¡no dudes en enviar una solicitud de extracción! Agradecemos cualquier tipo de contribución, ya sea en forma de correcciones de errores, mejoras en la documentación o nuevas funcionalidades.


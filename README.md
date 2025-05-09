🌐 Servicio Telemático - Examen 3 - Santiago Hernandez
---
Proyecto de despliegue para el examen 3 de Telematica con Docker y Flask Python 
Universidad Pontificia Bolivariana - Medellin
##  🤔¿Qué es esto?

Un **servicio web ligero**, **escalable** y **profesional**, construido con **Python + Flask**, estilizado con **HTML + CSS**, y empaquetado en un contenedor **Docker** listo para producción local o en la nube. Ideal para demostrar habilidades en desarrollo y despliegue de aplicaciones web.

--- 
## 🧰 Tecnologías Utilizadas

- 🐍 **Python 3.10** – Lenguaje de programación principal para la lógica del backend.
- 🌐 **Flask** – Framework web ligero para crear el servidor y manejar rutas.
- 🐳 **Docker** – Contenerización del servicio para despliegue en cualquier entorno.
- 🖼️ **HTML5 + CSS3** – Estructura y estilo de la interfaz web.
- ☁️ **AWS EC2** – Infraestructura en la nube para ejecutar la aplicación en producción.
- 📁 **Git + GitHub** – Control de versiones y repositorio remoto. 
---
##  📃Requisitos

- 🐳 Tener **Docker** instalado
- 📁 Tener **Git** instalado
---
## 🗃️ Estructura del proyecto

```
PF-Telematica/  
├── 📂 app/  
│ ├── 🐍 main.py # Lógica principal de la aplicación Flask  
│ ├── 📁 templates/  
│ │ └── 🌐 index.html # Página HTML principal con el contenido web  
│ └── 📁 static/  
│   └──  🎨 style.css # Estilos visuales de la interfaz  
├── 🐳 Dockerfile # Script de construcción del contenedor Docker  
└── 📘 README.md # Documentación del proyecto
```
---
##  ❗Instrucciones de despliegue

### Clonar el repositorio
```
git clone https://github.com/Titolin4612/PF-Telematica.git
cd PF-Telematica
```
### Construir la imagen Docker
v1 sera el nombre de version (v1, v2, v3, v4)
```
sudo docker build -t servicioweb:v1 .
```
### Ejecutar el contenedor
	
```
sudo docker run -d -p 80:80 servicioweb:v1
```
### Verificar que el contenedor este corriendo
	
```
sudo docker ps
```
---
### ‼️Instrucciones para modificar
#### Antes de modificar el contenido 
Asegurate de no tener ninguna version antigua del docker, en caso de si tenerla:
#### Detener sudo docker antiguo
```
sudo docker stop containerId
```
#### Borrar sudo docker antiguo
```
sudo docker rm containerId
```
#### Modificar el contenido o diseño fácilmente editando los siguientes archivos:
* Cambia el contenido HTML de la página.	
	```app/templates/index.html:```
* Ajusta el diseño visual (colores, fuentes, etc.).
	```app/static/style.css:```
* Luego de hacer los cambios vuelve a la carpeta inicial donde esta el DockerFile.
	```cd PF-Telematica```
#### Reconstruir la imagen:	
```
sudo docker build -t servicioweb:v1 .
```
#### Vuelver a ejecutar el contenedor:
```
sudo docker run -d -p 80:80 servicioweb:v1
```
---
## 🙏 Agradecimientos Especiales
### ¡Gracias, Profe Carlos, por ayudarme a crear ese gusto por la materia y motivarme a querer aprender más y más en cada clase, nunca deje perder la pasión, vocación y alegría con la que trasmite conocimiento en cada clase!
--- 
## Hecho con ❤️ por Santiago Hernandez Morantes

\# Flujo de trabajo con Git y GitHub



\## 1. Inicialización del repositorio



Se utilizó el comando `git init` para crear un repositorio local y comenzar a controlar las versiones del proyecto.



\## 2. Creación de ramas



Se utilizaron ramas para organizar el desarrollo y las actividades:



\- `main`: contiene la versión principal del proyecto.

\- `v01`: rama destinada a organizar una versión del proyecto.

\- `actividad1`: rama destinada a la primera actividad de Pygame.



Comando utilizado:



```bash

git branch nombre-rama

```



\## 3. Cambio entre ramas



Para cambiar de una rama a otra se utiliza:



```bash

git checkout nombre-rama

```



También se puede utilizar el comando moderno:



```bash

git switch nombre-rama

```



\## 4. Registro de cambios



Para agregar archivos al área de preparación:



```bash

git add .

```



Para guardar los cambios en el historial:



```bash

git commit -m "Descripción de los cambios"

```



\## 5. Integración de ramas



El comando `git merge` permite integrar los cambios de una rama en otra.



Ejemplo:



```bash

git switch main

git merge actividad1

```



\## 6. Conexión con GitHub



Se vinculó el repositorio local con el repositorio remoto de GitHub.



Para subir los cambios:



```bash

git push

```



Para actualizar el repositorio local:



```bash

git pull

```



\## 7. Conclusión



El uso de Git y GitHub permite organizar proyectos, conservar un historial de modificaciones y trabajar mediante diferentes ramas. Estas herramientas facilitan el control de versiones y la integración de cambios durante el desarrollo de videojuegos con Pygame.


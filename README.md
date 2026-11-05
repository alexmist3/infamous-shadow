\# infamous-shadow — La mazmorra de las monedas



\## Información del proyecto



\*\*Nombre del videojuego:\*\* La mazmorra de las monedas

\*\*Estudiante:\*\* \[LARIOS RINCON FERNANDO ALEXIS]

\*\*Lenguaje:\*\* Python

\*\*Biblioteca:\*\* Pygame

\*\*Editor:\*\* Visual Studio Code



\## 1. Descripción del proyecto



La mazmorra de las monedas es un videojuego en 2D desarrollado con Python y Pygame. El jugador controla un personaje que debe recorrer una mazmorra, recolectar cuatro monedas y llegar a la salida evitando a un enemigo.



El videojuego cuenta con una pantalla de inicio, un sistema de vidas, sonidos, imágenes, colisiones y pantallas de victoria y derrota.



\## 2. Objetivo



Desarrollar un videojuego funcional utilizando Python y Pygame para poner en práctica conocimientos de programación, como variables, condicionales, ciclos, funciones, clases, eventos y estructuras de datos.



\## 3. Investigación sobre Pygame



\### ¿Qué es Pygame?



Pygame es una biblioteca gratuita y de código abierto para Python que permite desarrollar videojuegos y aplicaciones multimedia. Está construida sobre SDL y proporciona herramientas para trabajar con gráficos, sonidos, teclado, mouse y otros elementos interactivos.



\### Historia de Pygame



Pygame comenzó a desarrollarse en el año 2000 por Pete Shinners. Su objetivo fue facilitar la creación de videojuegos y aplicaciones multimedia mediante Python y SDL.



Con el paso del tiempo se convirtió en una herramienta utilizada por estudiantes, principiantes y desarrolladores para aprender programación y crear videojuegos en 2D.



\### Licencia



Pygame utiliza la licencia LGPL 2.1, que permite utilizar y distribuir la biblioteca bajo las condiciones establecidas por dicha licencia. Puede utilizarse en proyectos educativos, personales y comerciales, respetando sus términos.



\### Principales módulos



\- `pygame.display`: crea y controla la ventana.

\- `pygame.draw`: permite dibujar figuras geométricas.

\- `pygame.event`: detecta eventos del usuario.

\- `pygame.font`: permite mostrar textos.

\- `pygame.image`: carga imágenes.

\- `pygame.key`: detecta las teclas presionadas.

\- `pygame.mixer`: reproduce sonidos y música.

\- `pygame.sprite`: organiza personajes y objetos mediante sprites.

\- `pygame.time`: controla el tiempo y los FPS.

\- `pygame.transform`: modifica imágenes, por ejemplo, su tamaño.



\### Alternativas a Pygame



\- \*\*Arcade:\*\* biblioteca de Python enfocada en videojuegos 2D.

\- \*\*Godot:\*\* motor gratuito y de código abierto para desarrollar juegos 2D y 3D.

\- \*\*Unity:\*\* motor de videojuegos que permite desarrollar proyectos 2D y 3D, principalmente con C#.



Pygame fue elegido porque permite trabajar directamente con Python y comprender los fundamentos del desarrollo de videojuegos.



\## 4. Relación con los fundamentos de programación



Pygame permite aplicar diferentes conceptos de programación:



\- \*\*Variables:\*\* almacenan posiciones, velocidades, puntos y vidas.

\- \*\*Condicionales:\*\* permiten tomar decisiones según las acciones del jugador.

\- \*\*Ciclos:\*\* mantienen activo el videojuego y actualizan sus elementos.

\- \*\*Funciones:\*\* organizan instrucciones y permiten reutilizar código.

\- \*\*Clases y objetos:\*\* representan personajes, monedas y enemigos.

\- \*\*Eventos:\*\* detectan acciones como presionar teclas o cerrar la ventana.

\- \*\*Estructuras de datos:\*\* permiten almacenar y organizar objetos del juego.

\- \*\*Colisiones:\*\* detectan el contacto entre diferentes elementos.



\### Uso de las funcionalidades de Pygame



Utilizar pocas funcionalidades de Pygame significa trabajar con herramientas básicas, como crear una ventana, dibujar figuras y detectar eventos del teclado.



Utilizar más funcionalidades significa incorporar recursos como imágenes, sonidos, sprites, animaciones y detección de colisiones.



La cantidad de funcionalidades utilizadas depende de las necesidades del proyecto. No es necesario utilizar todos los módulos para desarrollar un videojuego funcional.



En este proyecto se utilizaron diferentes herramientas de Pygame para conseguir una experiencia interactiva y organizada.



\## 5. Características del videojuego



\- Personaje controlable mediante flechas o WASD.

\- Cuatro monedas recolectables.

\- Enemigo con movimiento horizontal.

\- Tres vidas disponibles.

\- Sistema de colisiones.

\- Sonidos para monedas, daño, victoria y derrota.

\- Imágenes externas para representar los elementos.

\- Pantalla de inicio.

\- Pantalla de victoria.

\- Pantalla de derrota.

\- Reinicio de partida con la tecla R.



\### Controles



| Tecla | Función |

|---|---|

| Flechas o WASD | Mover al personaje |

| ENTER | Iniciar partida |

| R | Reiniciar después de ganar o perder |



\## 6. Organización del proyecto



```text

MiJuegoPygame/

│

├── juego.py

├── LEEME.txt

├── README.md

├── .gitignore

│

├── imagenes/

│   ├── enemigo.png

│   ├── jugador.png

│   ├── moneda.png

│   ├── salida.png

│   └── suelo.png

│

└── sonidos/

\&#x20;   ├── dano.wav

\&#x20;   ├── derrota.wav

\&#x20;   ├── moneda.wav

\&#x20;   └── victoria.wav

```



\## 7. Instalación y ejecución



Para ejecutar el videojuego se necesita tener Python instalado.



Instalar Pygame desde la terminal:



```bash

pip install pygame

```



Ejecutar el juego desde la carpeta del proyecto:



```bash

python juego.py

```



Es necesario conservar las carpetas `imagenes` y `sonidos` junto al archivo `juego.py` para que los recursos se carguen correctamente.



\## 8. Control de versiones con Git



El proyecto se administra mediante Git y GitHub.



Las ramas contempladas para organizar el trabajo son:



\- `main`: versión principal del proyecto.

\- `v01`: referencia a una versión del proyecto.

\- `actividad1`: primera actividad de Pygame.

\- `actividad2`: microproyecto La mazmorra de las monedas.



Se utilizan comandos como `git init`, `git branch`, `git checkout`, `git switch`, `git merge`, `git commit` y `git push` para administrar los cambios y las ramas.



\## 9. Conclusión



El desarrollo de La mazmorra de las monedas permitió aplicar conocimientos de Python y Pygame para construir un videojuego funcional. Durante el proceso se trabajó con imágenes, sonidos, movimiento, colisiones y organización del código.



Este proyecto permitió comprender mejor cómo se relacionan los fundamentos de programación con el desarrollo de videojuegos y cómo Git y GitHub ayudan a organizar y conservar los avances.



\## 10. Bibliografía



\- Pygame. (s. f.). \[Pygame Documentation](https://www.pygame.org/docs/).

\- Pygame. (s. f.). \[Pygame GitHub Repository](https://github.com/pygame/pygame).

\- Python Software Foundation. (s. f.). \[Python Documentation](https://docs.python.org/3/).

\- Pygame. (s. f.). \[Pygame License](https://www.pygame.org/licens).


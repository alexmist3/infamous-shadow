# Actividad 2: Desarrollo del videojuego La mazmorra de las monedas

## 1. Introducción

La mazmorra de las monedas es un videojuego 2D desarrollado en Python utilizando la biblioteca Pygame. El jugador debe recorrer un escenario, recoger cuatro monedas, evitar a un enemigo y llegar a la salida para ganar.

## 2. Objetivo

Desarrollar un videojuego funcional aplicando los fundamentos de programación y Pygame, incluyendo movimiento, eventos, colisiones, puntuación y control de vidas.

## 3. Características del videojuego

- Ventana de 800 × 600 píxeles.
- Movimiento del jugador mediante las flechas del teclado.
- Cuatro monedas coleccionables.
- Enemigo morado que se mueve horizontalmente.
- Tres vidas para el jugador.
- Sistema de invulnerabilidad temporal después de recibir daño.
- Pantalla de inicio, victoria y derrota.
- Tecla ENTER para comenzar y tecla R para reiniciar.

## 4. Funcionamiento

El juego inicia mostrando las instrucciones. Al presionar ENTER comienza la partida. El jugador debe recoger las cuatro monedas y llegar al bloque verde de salida sin perder sus tres vidas.

Si el enemigo toca al jugador, pierde una vida y regresa al punto inicial. Cuando pierde todas sus vidas aparece la pantalla de derrota. Si recoge todas las monedas y alcanza la salida, aparece la pantalla de victoria.

## 5. Algoritmo general

1. Inicializar Pygame y configurar la ventana.
2. Crear al jugador, las monedas, el enemigo y la salida.
3. Mostrar la pantalla de inicio.
4. Esperar que el usuario presione ENTER.
5. Leer los eventos y controlar el movimiento.
6. Detectar colisiones con monedas y enemigo.
7. Actualizar puntos y vidas.
8. Comprobar si se cumplen las condiciones de victoria o derrota.
9. Dibujar los elementos y actualizar la pantalla.
10. Permitir reiniciar la partida con R.

## 6. Pruebas realizadas

| Prueba | Resultado esperado |
|---|---|
| Iniciar con ENTER | Comienza la partida |
| Movimiento del jugador | Se mueve con las flechas |
| Recoger monedas | Aumenta el contador |
| Colisión con enemigo | Se pierde una vida |
| Perder todas las vidas | Aparece derrota |
| Recoger todas las monedas y llegar a la salida | Aparece victoria |
| Presionar R | Se reinicia la partida |

## 7. Problemas y soluciones

Durante el desarrollo se corrigieron problemas relacionados con las colisiones, el movimiento del enemigo y el funcionamiento de los estados del juego.

También se agregó un tiempo de invulnerabilidad para evitar que el jugador perdiera varias vidas rápidamente al permanecer cerca del enemigo.

## 8. Optimización

Se utilizó un reloj para mantener el juego a 60 FPS. También se organizaron las instrucciones mediante funciones y estados para facilitar el mantenimiento del código.

## 9. Conclusión

Con este proyecto se aplicaron conocimientos de Python y Pygame para desarrollar un videojuego funcional. Se practicaron conceptos como variables, funciones, ciclos, condicionales, eventos y colisiones.

El desarrollo permitió comprender mejor cómo se organiza la lógica de un videojuego y cómo se pueden corregir errores mediante pruebas.

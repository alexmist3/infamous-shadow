import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Limpio - Pygame")

# Configurar reloj y velocidad
reloj = pygame.time.Clock()
FPS = 60

# Colores
FONDO = (30, 30, 50)
AZUL = (0, 120, 255)
VERDE = (0, 220, 100)
BLANCO = (255, 255, 255)

# Crear jugador y meta
jugador = pygame.Rect(100, 100, 50, 50)
meta = pygame.Rect(600, 400, 50, 50)

# Velocidad del jugador
velocidad = 5

# Fuente para el mensaje
fuente = pygame.font.SysFont(None, 64)

ganaste = False
ejecutando = True

# Bucle principal
while ejecutando:

    # Detectar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Detectar teclas
    teclas = pygame.key.get_pressed()

    if not ganaste:
        if teclas[pygame.K_LEFT]:
            jugador.x -= velocidad
        if teclas[pygame.K_RIGHT]:
            jugador.x += velocidad
        if teclas[pygame.K_UP]:
            jugador.y -= velocidad
        if teclas[pygame.K_DOWN]:
            jugador.y += velocidad

        # Limitar movimiento dentro de la ventana
        jugador.clamp_ip(pantalla.get_rect())

        # Comprobar victoria
        if jugador.colliderect(meta):
            ganaste = True

    # Dibujar elementos
    pantalla.fill(FONDO)
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, VERDE, meta)

    if ganaste:
        mensaje = fuente.render("¡Ganaste!", True, BLANCO)
        pantalla.blit(mensaje, (300, 250))

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()

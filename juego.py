
import pygame
import sys
import os

# Inicializar Pygame
pygame.init()

try:
    pygame.mixer.init()
    SONIDO_ACTIVO = True
except pygame.error:
    SONIDO_ACTIVO = False

# Ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("La mazmorra de las monedas")

reloj = pygame.time.Clock()
FPS = 60

# Fuentes
fuente_titulo = pygame.font.SysFont(None, 64)
fuente = pygame.font.SysFont(None, 44)
fuente_info = pygame.font.SysFont(None, 28)

# Colores
FONDO = (25, 25, 40)
BLANCO = (255, 255, 255)
AZUL = (0, 120, 255)
VERDE = (0, 220, 100)
AMARILLO = (255, 210, 0)
MORADO = (180, 50, 220)
ROJO = (255, 80, 80)

# Rutas de recursos
CARPETA = os.path.dirname(os.path.abspath(__file__))
CARPETA_IMAGENES = os.path.join(CARPETA, "imagenes")
CARPETA_SONIDOS = os.path.join(CARPETA, "sonidos")


# Cargar imagen; si no existe, usar un dibujo sencillo
def cargar_imagen(nombre, tamaño, color, forma="rectangulo"):
    ruta = os.path.join(CARPETA_IMAGENES, nombre)

    try:
        imagen = pygame.image.load(ruta).convert_alpha()
        return pygame.transform.scale(imagen, tamaño)
    except (pygame.error, FileNotFoundError):
        imagen = pygame.Surface(tamaño, pygame.SRCALPHA)

        if forma == "circulo":
            pygame.draw.circle(
                imagen, color,
                (tamaño[0] // 2, tamaño[1] // 2),
                min(tamaño) // 2
            )
        else:
            pygame.draw.rect(imagen, color, (0, 0, *tamaño))

        return imagen


# Cargar sonidos; si no existen, continuar sin sonido
def cargar_sonido(nombre):
    if not SONIDO_ACTIVO:
        return None

    ruta = os.path.join(CARPETA_SONIDOS, nombre)

    try:
        return pygame.mixer.Sound(ruta)
    except (pygame.error, FileNotFoundError):
        return None


sonido_moneda = cargar_sonido("moneda.wav")
sonido_dano = cargar_sonido("dano.wav")
sonido_victoria = cargar_sonido("victoria.wav")
sonido_derrota = cargar_sonido("derrota.wav")


def reproducir_sonido(sonido):
    if sonido is not None:
        sonido.play()


# Clase del jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cargar_imagen(
            "jugador.png", (40, 40), AZUL
        )
        self.rect = self.image.get_rect(topleft=(100, 100))

    def update(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += 5
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.rect.y -= 5
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.rect.y += 5

        self.rect.clamp_ip(pantalla.get_rect())


# Clase de las monedas
class Moneda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = cargar_imagen(
            "moneda.png", (20, 20), AMARILLO, "circulo"
        )
        self.rect = self.image.get_rect(topleft=(x, y))


# Clase del enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cargar_imagen(
            "enemigo.png", (40, 40), MORADO
        )
        self.rect = self.image.get_rect(topleft=(350, 320))
        self.velocidad = 3

    def update(self):
        self.rect.x += self.velocidad

        if self.rect.right >= 550:
            self.velocidad = -3
        if self.rect.left <= 300:
            self.velocidad = 3


# Clase de la salida
class Salida(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cargar_imagen(
            "salida.png", (50, 50), VERDE
        )
        self.rect = self.image.get_rect(topleft=(700, 500))


# Crear grupos y reiniciar partida
def reiniciar_partida():
    global jugador, grupo_jugador, grupo_monedas
    global grupo_enemigo, grupo_salida
    global puntos, vidas, invulnerable, estado

    jugador = Jugador()

    grupo_jugador = pygame.sprite.GroupSingle(jugador)
    grupo_monedas = pygame.sprite.Group()
    grupo_enemigo = pygame.sprite.GroupSingle(Enemigo())
    grupo_salida = pygame.sprite.GroupSingle(Salida())

    posiciones = [
        (250, 120),
        (400, 250),
        (200, 400),
        (600, 180)
    ]

    for x, y in posiciones:
        grupo_monedas.add(Moneda(x, y))

    puntos = 0
    vidas = 3
    invulnerable = 0
    estado = "inicio"


def dibujar_texto(texto, tipo_fuente, color, x, y):
    imagen = tipo_fuente.render(texto, True, color)
    rectangulo = imagen.get_rect(center=(x, y))
    pantalla.blit(imagen, rectangulo)


# Preparar el juego
reiniciar_partida()

# Bucle principal
while True:

    # Eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            if estado == "inicio" and evento.key == pygame.K_RETURN:
                estado = "jugando"

            elif estado in ("victoria", "derrota"):
                if evento.key == pygame.K_r:
                    reiniciar_partida()

    # Actualizar durante la partida
    if estado == "jugando":

        grupo_jugador.update()
        grupo_enemigo.update()

        # Recoger monedas usando colisiones entre sprites
        monedas_recogidas = pygame.sprite.spritecollide(
            jugador, grupo_monedas, True
        )

        if monedas_recogidas:
            puntos += len(monedas_recogidas)
            reproducir_sonido(sonido_moneda)

        # Control de invulnerabilidad
        if invulnerable > 0:
            invulnerable -= 1

        # Colisión con el enemigo
        elif pygame.sprite.spritecollide(
            jugador, grupo_enemigo, False
        ):
            vidas -= 1
            invulnerable = 90
            jugador.rect.topleft = (100, 100)

            reproducir_sonido(sonido_dano)

            if vidas <= 0:
                estado = "derrota"
                reproducir_sonido(sonido_derrota)

        # Ganar al recoger todas las monedas y tocar la salida
        if estado == "jugando" and len(grupo_monedas) == 0:
            if pygame.sprite.spritecollideany(
                jugador, grupo_salida
            ):
                estado = "victoria"
                reproducir_sonido(sonido_victoria)

    # Dibujar fondo
    pantalla.fill(FONDO)

    # Pantalla de inicio
    if estado == "inicio":

        dibujar_texto(
            "LA MAZMORRA", fuente_titulo, AMARILLO,
            ANCHO // 2, 180
        )

        dibujar_texto(
            "DE LAS MONEDAS", fuente_titulo, BLANCO,
            ANCHO // 2, 240
        )

        dibujar_texto(
            "Recoge las 4 monedas y llega al bloque verde",
            fuente_info, BLANCO, ANCHO // 2, 320
        )

        dibujar_texto(
            "¡Evita al enemigo morado!",
            fuente_info, MORADO, ANCHO // 2, 365
        )

        dibujar_texto(
            "Presiona ENTER para jugar",
            fuente, VERDE, ANCHO // 2, 450
        )

    # Pantalla de juego
    elif estado == "jugando":

        grupo_salida.draw(pantalla)
        grupo_enemigo.draw(pantalla)
        grupo_monedas.draw(pantalla)

        # Parpadeo después de recibir daño
        if invulnerable == 0 or invulnerable // 6 % 2 == 0:
            grupo_jugador.draw(pantalla)

        dibujar_texto(
            f"Monedas: {puntos}   Vidas: {vidas}",
            fuente_info, BLANCO, 180, 25
        )

        dibujar_texto(
            f"Restantes: {len(grupo_monedas)}",
            fuente_info, BLANCO, 100, 55
        )

    # Pantalla de victoria
    elif estado == "victoria":

        dibujar_texto(
            "¡VICTORIA!", fuente_titulo, VERDE,
            ANCHO // 2, 230
        )

        dibujar_texto(
            f"Monedas recogidas: {puntos}",
            fuente, BLANCO, ANCHO // 2, 300
        )

        dibujar_texto(
            "Presiona R para volver a jugar",
            fuente_info, BLANCO, ANCHO // 2, 370
        )

    # Pantalla de derrota
    elif estado == "derrota":

        dibujar_texto(
            "GAME OVER", fuente_titulo, ROJO,
            ANCHO // 2, 230
        )

        dibujar_texto(
            "Te quedaste sin vidas",
            fuente, BLANCO, ANCHO // 2, 300
        )

        dibujar_texto(
            "Presiona R para intentarlo otra vez",
            fuente_info, BLANCO, ANCHO // 2, 370
        )

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(FPS)


### Imports
import pygame
import pygame.gfxdraw
from math import *
from random import *
from module_planet import Planet


### Variablen
framerate = 60      # Für die Berechnung der Frametime bzw. t
framerate2 = 120     # Falls das Programm lediglich schneller laufen soll
scale = 1
trail_width = 2
window_width = 1200
window_height = 1000
background_color = (255, 255, 255)

debug = False
x_camera_offset = 0
y_camera_offset = 0
frametime = 1000 // framerate
all_planets = []
snap_planet = None
clock = pygame.time.Clock()

# ----------------------------------------- Konstellationen ------------------------------------------
def constellation_SolarSystem():
    global snap_planet, scale, all_planets, sonne, erde, mond
    ### Initialisiere Planeten (Sonnensystem)
    #               name     x,    y,     v,      winkel,  m,      farbe,             frametime
    sonne = Planet("Sonne",  0,    0,     0.0,    45,      100,    (235, 183, 52),    frametime)
    erde  = Planet("Erde",   0,    500,   1.75,   180,     50,     (5, 87, 230),      frametime)
    mond  = Planet("Mond",   0,    610,   4,      180,     5,      (187, 188, 189),   frametime)
    all_planets.append(sonne)
    all_planets.append(erde)
    all_planets.append(mond)
    snap_planet = sonne
    scale = 1/2
def constellation_3PlanetsEllipse():
    global snap_planet, scale, all_planets, links, mitte, rechts
    ### Initialisiere Planeten (Three Body Problem [Ellipse])
    #                name      x,      y,     v,      winkel, m,      farbe,              frametime,  G
    links  = Planet("links",   -200,   -75,   2,    135,    15,     (5, 87, 230),       frametime,  2000)
    mitte  = Planet("mitte",   0,      0,     2,    -45,    15,     (187, 188, 189),    frametime,  2000)
    rechts = Planet("rechts",  200,    75,    2,    155,    15,     (235, 183, 52),     frametime,  2000)
    all_planets.append(links)
    all_planets.append(mitte)
    all_planets.append(rechts)
    snap_planet = None  # "COM"
def constellation_3PlanetsCircle():
    global snap_planet, scale, all_planets, links, mitte, rechts
    ### Initialisiere Planeten (Three Body Problem [Kreis mit Mittelpunkt])
    #                name     x,    y,     v,      winkel, m,      farbe,               frametime
    links =  Planet("links",  -200, 0,     1,      90,     15,     (5, 87, 230),       frametime)
    mitte =  Planet("mitte",   0,   0,     0,      0,      15,     (187, 188, 189),    frametime)
    rechts = Planet("rechts",  200, 0,     1,      -90,    15,     (235, 183, 52),     frametime)
    all_planets.append(links)
    all_planets.append(mitte)
    all_planets.append(rechts)
def constellation_3PlanetsOdd():
    global snap_planet, scale, all_planets, blau, gelb, grau, trail_width
    ### Initialisiere Planeten (Three Body Problem [Kreis mit Mittelpunkt])
    #                name    x,    y,     v,      winkel, m,      farbe,               frametime
    blau =  Planet("blau",   -47,  0,     1,      90,     15,     (5, 87, 230),       frametime)
    gelb = Planet("gelb",    47,   0,     1,      -90,    15,     (235, 183, 52),     frametime)
    grau =  Planet("grau",   300,  0,     1.5,      90,     15,     (187, 188, 189),    frametime)
    all_planets.append(blau)
    all_planets.append(gelb)
    all_planets.append(grau)
    snap_planet = "COM"
    trail_width = 1
def constellation_2x2Planets():
    global snap_planet, scale, all_planets, blau, gelb, rot, grün, trail_width
    x1 = -400
    x2 = 400
    v1 = -1
    v2 = -1
    vx = 0.29
    ### Initialisiere Planeten (Three Body Problem [Kreis mit Mittelpunkt])
    #                name    x,      y,     v,      winkel, m,      farbe,            frametime
    blau =  Planet("blau",   x1-47,  0,     v1+vx,      90,     15,     (5, 87, 230),     frametime)
    gelb = Planet("gelb",    x1+47,  0,     v1-vx,      -90,    15,     (235, 183, 52),   frametime)
    rot =  Planet("rot",     x2-47,  0,     v2-vx,      90,     15,     (156, 50, 34),    frametime)
    grün =  Planet("grün",   x2+47,  0,     v2+vx,      -90,    15,     (34, 156, 63),    frametime)
    all_planets.append(blau)
    all_planets.append(gelb)
    all_planets.append(rot)
    all_planets.append(grün)
    # snap_planet = "COM"
    trail_width = 1
    scale = 2/3
def constellation_2x2Planets2nd():
    global snap_planet, scale, all_planets, blau, gelb, rot, grün, trail_width
    x1 = -400
    x2 = 400
    v1 = -1
    v2 = -1
    vx = 0.5
    ### Initialisiere Planeten (Three Body Problem [Kreis mit Mittelpunkt])
    #                name    x,      y,     v,      winkel, m,      farbe,            frametime
    blau =  Planet("blau",   x1-47,  0,     v1+vx,      90,     15,     (5, 87, 230),     frametime)
    gelb = Planet("gelb",    x1+47,  0,     v1-vx,      -90,    15,     (235, 183, 52),   frametime)
    rot =  Planet("rot",     x2-47,  0,     v2-vx,      90,     15,     (156, 50, 34),    frametime)
    grün =  Planet("grün",   x2+47,  0,     v2+vx,      -90,    15,     (34, 156, 63),    frametime)
    all_planets.append(blau)
    all_planets.append(gelb)
    all_planets.append(rot)
    all_planets.append(grün)
    # snap_planet = "COM"
    trail_width = 1
    scale = 2/3
def constellation_2Planets():
    global snap_planet, scale, all_planets, links, rechts
    ### Initialisiere Planeten (Zwei Planeten)
    #                name      x,      y,     v,      winkel,  m,      farbe,              frametime,  G
    links  = Planet("links",   -250,   0,     1,      90,       16,     (5, 87, 230),       frametime,  4000)
    rechts = Planet("rechts",  250,    0,     1,      -90,      15,     (235, 183, 52),     frametime,  4000)
    all_planets.append(links)
    all_planets.append(rechts)
    snap_planet = None  # "COM"
def constellation_4Planets():
    global snap_planet, scale, all_planets, p1, p2, p3, p4
    ### Initialisiere Planeten (Vier Planeten)
    #           name      x,      y,      v,      winkel,   m,      farbe,              frametime,  G
    p1 = Planet("blau",    -200,   -200,   2,      0,        15,     (17, 98, 156),       frametime,  1000)
    p2 = Planet("gelb",    200,    -200,   2,      90,       15,     (235, 183, 52),     frametime,  1000)
    p3 = Planet("rot",     -200,    200,   2,      -90,      15,     (168, 66, 50),      frametime,  1000)
    p4 = Planet("grün",    200,     200,   2,      180,      15,     (17, 156, 105),     frametime,  1000)
    all_planets.append(p1)
    all_planets.append(p2)
    all_planets.append(p3)
    all_planets.append(p4)
    snap_planet = None  # "COM"
    scale = 1/2
def constellation_8PlanetsMid():
    global snap_planet, scale, all_planets, p1, p2, p3, p4, p5, p6, p7, p8, center
    ### Initialisiere Planeten (8 Planeten und Mitte)
    v1 = 6
    v2 = 8
    #            name        x,      y,      v,      winkel,   m,      farbe,              frametime,  G
    p1 = Planet("blau",      -200,   -200,   v1,     0,        15,     (17, 98, 156),      frametime,  2000)
    p2 = Planet("gelb",      200,    -200,   v1,     90,       15,     (235, 183, 52),     frametime,  2000)
    p3 = Planet("rot",       -200,    200,   v1,     -90,      15,     (168, 66, 50),      frametime,  2000)
    p4 = Planet("grün",      200,     200,   v1,     180,      15,     (17, 156, 105),     frametime,  2000)
    p5 = Planet("lila",      -400,   -400,   v2,     90,       25,     (85, 5, 156),       frametime,  2000)
    p6 = Planet("orange",    400,    -400,   v2,     180,      25,     (207, 110, 31),     frametime,  2000)
    p7 = Planet("pink",      -400,    400,   v2,     0,        25,     (168, 29, 103),     frametime,  2000)
    p8 = Planet("türkis",    400,     400,   v2,     -90,      25,     (20, 216, 219),     frametime,  2000)
    center = Planet("center",  0,     0,     0,      0,        60,     (187, 188, 189),    frametime,  2000)
    all_planets.append(p1)
    all_planets.append(p2)
    all_planets.append(p3)
    all_planets.append(p4)
    all_planets.append(p5)
    all_planets.append(p6)
    all_planets.append(p7)
    all_planets.append(p8)
    all_planets.append(center)
    scale = 1/7
    snap_planet = None  # "COM"
def constellation_8PlanetsPlusMid():
    global snap_planet, scale, all_planets, p1, p2, p3, p4, p5, p6, p7, p8, center
    ### Initialisiere Planeten (8 Planeten und Mitte in Plus-Form )
    scale = 1/3
    v1 = -5.3
    v2 = 6.24 
    d1 = 450
    d2 = 700
    m1 = 15
    m2 = 25
    #            name         x,      y,     v,      winkel,   m,      farbe,              frametime,  G
    p1 = Planet("blau",       -d1,    0,     v1,     90,       m1,     (17, 98, 156),      frametime,  2000)
    p2 = Planet("gelb",       0,      -d1,   v1,     180,      m1,     (235, 183, 52),     frametime,  2000)
    p3 = Planet("rot",        0,      d1,    v1,     0,        m1,     (168, 66, 50),      frametime,  2000)
    p4 = Planet("grün",       d1,     0,     v1,     -90,      m1,     (17, 156, 105),     frametime,  2000)
    p5 = Planet("lila",       -d2,    0,     v2,     90,       m2,     (85, 5, 156),       frametime,  2000)
    p6 = Planet("orange",     0,      -d2,   v2,     180,      m2,     (207, 110, 31),     frametime,  2000)
    p7 = Planet("pink",       0,      d2,    v2,     0,        m2,     (168, 29, 103),     frametime,  2000)
    p8 = Planet("türkis",     d2,     0,     v2,     -90,      m2,     (20, 216, 219),     frametime,  2000)
    center = Planet("center", 0,      0,     0,      0,        100,    (187, 188, 189),    frametime,  2000)
    all_planets.append(p1)
    all_planets.append(p2)
    all_planets.append(p3)
    all_planets.append(p4)
    all_planets.append(p5)
    all_planets.append(p6)
    all_planets.append(p7)
    all_planets.append(p8)
    all_planets.append(center)
    snap_planet = None  # "COM"
def constellation_8PlanetsPlus():
    global snap_planet, scale, all_planets, p1, p2, p3, p4, p5, p6, p7, p8
    ### Initialisiere Planeten (8 Planeten und Mitte in Plus-Form )
    scale = 1/5
    G = 6000
    v1 = 5
    v2 = -8
    d1 = 170
    d2 = 500
    m1 = 25
    m2 = 25
    a1 = 50
    a2 = 50
    #            name         x,      y,     v,      winkel,      m,      farbe,              frametime,  G
    p1 = Planet("blau",       -d1,    -d1,   v1,     90+a1,       m1,     (17, 98, 156),      frametime,  G)
    p2 = Planet("gelb",       d1,     -d1,   v1,     180+a1,      m1,     (235, 183, 52),     frametime,  G)
    p3 = Planet("rot",        -d1,    d1,    v1,     0+a1,        m1,     (168, 66, 50),      frametime,  G)
    p4 = Planet("grün",       d1,     d1,    v1,     -90+a1,      m1,     (17, 156, 105),     frametime,  G)
    p5 = Planet("lila",       -d2,    -d2,   v2,     90+a2,       m2,     (85, 5, 156),       frametime,  G)
    p6 = Planet("orange",     d2,     -d2,   v2,     180+a2,      m2,     (207, 110, 31),     frametime,  G)
    p7 = Planet("pink",       -d2,    d2,    v2,     0+a2,        m2,     (168, 29, 103),     frametime,  G)
    p8 = Planet("türkis",     d2,     d2,    v2,     -90+a2,      m2,     (20, 216, 219),     frametime,  G)
    all_planets.append(p1)
    all_planets.append(p2)
    all_planets.append(p3)
    all_planets.append(p4)
    all_planets.append(p5)
    all_planets.append(p6)
    all_planets.append(p7)
    all_planets.append(p8)
    snap_planet = None  # "COM"
def constellation_random(n):
    global snap_planet, scale, all_planets, planet
    ### Initialisiere Planeten (Zufällige Werte)
    G = 700
    for planetID in range(n):
        planet = Planet(("Planet", str(planetID)),  # name
                        randint(-500, 500), randint(-500, 500),  # x, y
                        uniform(3, 6),  # v
                        uniform(-180, 180),  # winkel
                        uniform(10, 30),  # m
                        (randint(30, 235), randint(30, 235), randint(30, 235)),  # farbe    
                        frametime, # frametime
                        G)  # G
        all_planets.append(planet)
    snap_planet = "COM"

constellation_SolarSystem()           # !         Sonnensystem
# constellation_3PlanetsEllipse()       # x
# constellation_3PlanetsCircle()        # ! R       Zum zeigen von limitierungen des Programms
# constellation_3PlanetsOdd()           # !
# constellation_2x2Planets()            # !
# constellation_2x2Planets2nd()         # !
# constellation_2Planets()              # !         Zwei sich umkreisende Planeten
# constellation_4Planets()              # !
# constellation_8PlanetsMid()           # ? R
# constellation_8PlanetsPlusMid()       # ? R
# constellation_8PlanetsPlus()          # ? R
# constellation_random(10)
# ------------------------------------------------------------------------------------------------------

### Funktionen
def debug_msg(message="----------------------"):
    if debug == True:
        print("### ", message)
        return
def get_all_other_planets(pobject):
    other_planets = all_planets.copy()
    other_planets.remove(pobject)
    return other_planets
def snap_camera_to_planet(target=None):
    global x_camera_offset, y_camera_offset
    if target == None:
        debug_msg("No Snapping")
        x_camera_offset = window_width / 2
        y_camera_offset = window_height / 2
    elif target == "COM":   # Center Of Mass
        debug_msg("COM Snap")
        sum_x = 0
        sum_y = 0
        for current_target in all_planets:
            sum_x += current_target.x
            sum_y += current_target.y
        avg_x = sum_x/len(all_planets)
        avg_y = sum_y/len(all_planets)
        x_camera_offset = window_width / 2 - avg_x * scale
        y_camera_offset = window_height / 2 - avg_y * scale
    else:
        debug_msg(f"Snapped to {target.name}")
        x_camera_offset = window_width / 2 - target.x * scale
        y_camera_offset = window_height / 2 - target.y * scale
    return


### Pygame initialisieren
pygame.init()
pygame.display.set_caption("Simulation")

# Ebenen einrichten
screen = pygame.display.set_mode((window_width, window_height))
mainCanvas  = pygame.Surface([window_width, window_height])  # Layer für die Planeten
trailCanvas = pygame.Surface([window_width, window_height])  # Layer für die Planetenbahnen
trailCanvas.fill(background_color)
trailCanvas.set_colorkey(background_color)  # Setzt Hintergrundfarbe als Transparent

debug_msg("Main Loop Start")

### Main Loop
run = True
while run == True:
    clock.tick(framerate2)
    mainCanvas.fill(background_color)

    ### Ändere das Offset der Objekte auf dem Canvas
    snap_camera_to_planet(snap_planet)

    ### Events
    for event in pygame.event.get():
        # Falls das Fenster geschlossen oder ESC gedrückt wird
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    ### Funktionen, die jeder Planet pro Tick ausführt
    for planet in all_planets:
        # Berechne die Kräfte zwischen allen Planeten
        all_other_planets = get_all_other_planets(planet)   # Liste mit allen anderen Planeten außer dem aktuellen
        for current_planet in all_other_planets:
            planet.add_vector_towards(current_planet)

        # Bewege den Planet
        planet.move()

        # Male den Schweif des Planeten
        pygame.draw.line(trailCanvas, planet.color,  # Ebene, Farbe
                         (int(planet.x * scale + x_camera_offset), int(planet.y * scale + y_camera_offset)),    # (x1, y1)
                         (int(planet.x2 * scale + x_camera_offset), int(planet.y2 * scale + y_camera_offset)),  # (x2, y2)
                         int(trail_width))  # Linienstärke
       
        # Printe die Infos des Planeten (debug)
        if debug == True:
            planet.print_stats()

    ### Zweiter loop, damit die neuen Werte erst nach der Berechnung aller Planeten angewendet werden
    for planet in all_planets:
    	# Kopiere die berechneten Werte in die Haupt-Variablen
        planet.apply_values()

        # Male den Planet auf dem mainCanvas (Anti-aliased=Kantenglättung)
        pygame.gfxdraw.filled_circle(mainCanvas, int(planet.x * scale + x_camera_offset), int(planet.y * scale + y_camera_offset), int(planet.m * scale), planet.color)
        pygame.gfxdraw.aacircle(mainCanvas, int(planet.x * scale + x_camera_offset), int(planet.y * scale + y_camera_offset), int(planet.m * scale), planet.color)
        # pygame.draw.circle(mainCanvas, planet.color, 
        #                    (int(planet.x * scale + x_camera_offset), int(planet.y * scale + y_camera_offset)), 
        #                    int(planet.m * scale))

    ### Zeige die beiden Canvas auf dem Screen
    screen.blit(mainCanvas, (0, 0))
    screen.blit(trailCanvas, (0, 0))

    pygame.display.update()
    debug_msg("tick done")

pygame.quit()

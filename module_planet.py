from math import *

class Planet:
    def __init__(self, pname="", px=0, py=0, pvelocity=0, 
                 pangle=0, pmass=1, pcolor=(255,255,255), 
                 pframetime=1000//60, pG=200):
        self.name = pname  # Name (z.B. "Mond")
        self.x = px  # X-Position in px
        self.y = py  # Y-Position in px
        self.v = pvelocity  # Geschwindigkeit
        self.angle = radians(pangle)  # Winkel
        self.m = pmass  # Masse
        self.color = pcolor  # Farbe (R,G,B)
        self.FRAMETIME = pframetime  # Zeitspanne eines Frames
        self.F = self.m * self.v * self.FRAMETIME  # Gravitationskraft
        self.G = pG  # Gravitationskonstante

        self.x2 = self.x
        self.y2 = self.y
        self.v2 = self.v
        self.F2 = self.F
        self.angle2 = self.angle
        return

    # Bewege das Objekt 
    def move(self):
        self.v2 = self.F2 / (self.m * self.FRAMETIME)
        dx = cos(self.angle2) * self.v2
        dy = sin(self.angle2) * self.v2
        self.x2 += dx
        self.y2 += dy
        return

    # Erhalte einen Vektor in Richtung eines anderen Planeten mit Länge {F} und Winkel {angle} (zur positiven X-Achse)
    def get_vector_towards(self, pobject):
        dx = pobject.x - self.x2
        dy = pobject.y - self.y2
        d = hypot(dx, dy)
        F_towards = self.G * ((self.m * pobject.m)/(d**2))  # Gravitationsformel: G * ((m1*m2)/d**2)
        angle_towards = atan2(dy, dx)
        return angle_towards, F_towards

    # Kombiniere den eigenen Kraftvektor mit dem, der der Funktion übergebenen wird
    def get_added_vectors(self, added_angle, added_length):
        dx = cos(self.angle2) * self.F2 + cos(added_angle) * added_length
        dy = sin(self.angle2) * self.F2 + sin(added_angle) * added_length
        F_res = hypot(dx, dy)
        angle_res = atan2(dy, dx)
        return angle_res, F_res

    # Erhalte den Kraftvektor in Richtung eines anderen Planeten und füge diesen der eigenen Kraft {F} und dem Winkel {angle} hinzu
    def add_vector_towards(self, pobject):
        add_angle, add_F = self.get_vector_towards(pobject)
        self.angle2, self.F2 = self.get_added_vectors(add_angle, add_F)
        return

    # Übertrage die zwischengespeicherten Werte 
    
    def apply_values(self):
        self.x = self.x2
        self.y = self.y2
        self.v = self.v2
        self.F = self.F2
        self.angle = self.angle2
        return

    # Gebe die Eigenschaften des Planeten in der Konsole aus
    def print_stats(self):
        print(f"[-------{self.name}-------")
        print("Name:", self.name)
        print(f"Position: {round(self.x, 2)}, {round(self.y, 2)}")
        print("Geschwindigkeit:", round(self.v, 2))
        print("Richtung:", round(degrees(self.angle), 2))
        # print("Masse:", self.m)
        print("Kraft:", round(self.F, 2))
        # print("Farbe:", self.color)
        print("---------------------]")
        return

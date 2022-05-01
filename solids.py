# ------------------------------------------------

class Solids:
    def __init__(self):
        self.volume_int = None
        self.volume_ext = None
        self.base_area = None
        self.height = None
        self.wall_thickness = None
    pass

# ------------------------------------------------

class Polyhedron(Solids):
    def __init__(self):
        super().__init__(self)
        self.qt_sides = None
        self.size_size = None
    pass

class NotPolyhedron(Solids):
    def __init__(self):
        super().__init__(self)
        self.radius = None
    pass

# ------------------------------------------------

class Prismatic(Polyhedron):
    def __init__(self):
        super().__init__(self)
    pass

class Pyramid(Polyhedron):
    def __init__(self):
        super().__init__(self)
    pass

class Convex(Polyhedron):
    def __init__(self):
        super().__init__(self)
    pass

# ------------------------------------------------

class Cylindrical(NotPolyhedron):
    def __init__(self):
        super().__init__(self)
    pass

class HalfMoon(NotPolyhedron):
    def __init__(self):
        super().__init__(self)
    pass

# ------------------------------------------------

# terciarias poliedros: piramidal, prismatico, convexo

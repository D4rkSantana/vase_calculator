
# Formatos suportados: cubos, paralelepipedos, prisma, piramide, cilindro, cone
# formato geometrico, dimensões internas, dimensões externas, volume
# composição, quantidade de material, peso

class Object:
    def __init__(self, ):
        self.format = '' # formato geometrico
        # self.area = '' #area interna
        self.height_ext = '' # altura externa
        self.height_int = '' # altura interna
        self.volume = '' # volume interno em litros
        self.weight = '' # peso total em kg
        self.thickness_base = '' # espessura da base cm
        self.thickness_wall = '' # espessura das paredes em cm
        self.qt_material = '' # quantidade de material a ser utilizado em litros
    
    def set_format(self, format):
        self.format = format

    def set_height(self, internal, external):
        self.height_int = internal
        self.height_ext = external

# Objetos retos (como cubos, pararelelepipedos, prismas, piramides e etc...)

class Object_straight(Object):
    def __init__(self):
        super().__init__(self)
        self.area_int = '' #area interna
        self.area_ext = '' #area externa
    
    

    def set_area(self, internal, external):
        self.area_int = internal
        self.area_ext = external

    

# Objetos curvos (como cilindros, cones, esferas e etc...)

class Object_round(Object):
    def __init__(self):
        super().__init__(self)
        self.radius_int = '' #raio interno;
        self.radius_ext = '' #raio externo
    
    def set_radius(self, internal, external):
        self.radius_int = internal
        self.radius_ext = external

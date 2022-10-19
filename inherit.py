class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("Sku is {}".format(self.sku))

class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_location(self):
        print("Section is {}, type is {}".format(self.section, self.type))

class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("Shirt {}, color {}".format(self.name, self.color))

Blouse = Shirts("0001", 43, "Tops", "Formal blouse", "White")

Blouse.print_sku()
Blouse.print_location()
Blouse.print_shirt()
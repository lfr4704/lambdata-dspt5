
class Polo:
    """docstring for Polo."""
    def __init__(self, size, color):  #  is called the constructor
        self.size = size
        self.color = color

    def wash(self):
        #print("washing")
        print(f"washing the {self.size} {self.color} Polo!")

if __name__ == "__main__":
    #only execute if run from the command-line (not when imported)

    polo = Polo(size="Large", color="Blue")
    print(polo.size, polo.color)
    polo.wash()

    polo2 = Polo(size="Small", color="Yello")
    print(polo.size, polo.color)

    polo.wash()

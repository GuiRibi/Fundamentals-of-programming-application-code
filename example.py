import math

def main():
    

    while True:
        print("This program calculates the different volumes of shapes\n\
            1) Box\n\
            2) Sphere\n\
            3) Cylinder\n\
            4) Cone\n\
            other) exit program")
    
        options = ["box", "sphere", "cylinder", "cone"]
        choice = input("Which shape do you want to calculate the volume of:\n")

        match choice:
            case "1":
                #Volume of a box
                width = float(input("Width of the box:\n"))
                length = float(input("Length of the box:\n"))
                height = float(input("Height of the box:\n"))

                volume = Volume_of.Box(width, length, height)

            case "2":
                #Volume of a sphere
                radius = float(input("Radius of the sphere:\n"))

                volume = Volume_of.Sphere(radius)

            case "3":
                #volume of a cylinder
                radius = float(input("Radius of the cylinder:\n"))
                height = float(input("Height of the cylinder:\n"))

                volume = Volume_of.Cylinder(radius, height)

            case "4":
                #volume of a cone
                radius = float(input("Radius of the cone:\n"))
                height = float(input("Height of the cone:\n"))

                volume = Volume_of.Cone(radius, height)


            case _:
                #other key was selected
                print("exiting...")
                return

        print((f"the volume of the {options[int(choice) - 1]} is {round(volume, 3)}"))

##formulas for the volumes
class Volume_of:
    def Box(w, l, h):
        return w * l * h
    
    def Sphere(r):
        return 4/3 * math.pi * r**3
    
    def Cylinder(r, h):
        return math.pi * r**2 * h
    
    def Cone(r, h):
        return Volume_of.Cylinder(r, h) / 3

main()

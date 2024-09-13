def get_shape_volume():
    shape = input("Enter the shape you want to calculate the volume for (cube, cuboid, pyramid, sphere, cylinder): ").lower()

    if shape == "cube":
        length = float(input("Enter the length of the cube: "))
        volume = length ** 3
    elif shape == "cuboid":
        length = float(input("Enter the length of the cuboid: "))
        base = float(input("Enter the base of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        volume = length * base * height
    elif shape == "pyramid":
        base = float(input("Enter the base of the pyramid: "))
        height = float(input("Enter the height of the pyramid: "))
        volume = (1/3) * base ** 2 * height
    elif shape == "sphere":
        radius = float(input("Enter the radius of the sphere: "))
        volume = (4/3) * 3.14159 * radius ** 3  # Using 3.14159 for pi
    elif shape == "cylinder":
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        volume = 3.14159 * radius ** 2 * height   
  # Using 3.14159 for pi
    else:
        print("Invalid shape. Please enter a valid shape name.")

    print("The volume is:", volume)

get_shape_volume()




   
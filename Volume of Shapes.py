#Volume of Cube
def vol_cube(length):
    volume = length * length * length
    return volume
    
answer = vol_cube(3)   
print (answer)

#Volume of Cuboid
def vol_cuboid(length, base, height):
    volume = length * base * height
    return volume

answer = vol_cuboid(3,5,7)
print (answer)

#Volume of a Sqaure Pyramid
def vol_pyramid(base, height):
    volume = 1/3 * base ** 2 * height
    return volume 

answer = vol_pyramid(4,3)
print (answer)

#Volume of a Sphere
def vol_sphere(pi, radius):
    volume = 4/3 * pi * radius
    return volume

answer = vol_sphere(3.14,6)
print (answer)

#Volume of Cylinder
def vol_cylinder(pi, radius, height):
    volume = pi * radius** 2 * height
    return volume

answer = vol_cylinder(3.14,3,9)
print (answer)

   
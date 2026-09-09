import math

radius = 3

area = (math.pi)*radius**2 # A = area = pi * r^2

volume = (4.0/3.0) * math.pi * radius**3 # volume of a sphere = 4/3 * pi * r^3

cyl_v = math.pi * (radius**2) * 10 # pi * r^2 * h = volume of a cylinder 

print(f"the area is: {area:.2f}") 
print(f"volume v is: {volume:.2f}")
print(f"the cylinder has a volume of: {cyl_v:.2f}")

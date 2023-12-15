#Transformation of complex numbers as 2-D vectors e.g. translation, scaling, rotation, reflection.

import math
z = complex(2,2)

#Translation
z_2 = complex(2.1)
translated_z = z+z_2 

#Scaling
scaling_factor = 2
scaled_z = z*scaling_factor

#Rotation
theta = 45
angle_radian = math.radians(theta)
rotation_factor = complex(math.cos(angle_radian),math.sin(angle_radian))
rotated_z = z*rotation_factor

#Reflaction(multiplying by an other complex number)
reflection_factor = complex(1,-1)
reflected_z = z*reflection_factor

#Printing
print(f"Original Complex no: {z}\nTransleted comple no:{translated_z}\n"
      f"Scaled Complex no:{scaled_z}\nRotated complex no:{rotated_z}\n"
      f"Reflected Complex no:{reflected_z}")


from utility import *

class Point:

   def  __init__(self,x,y,z):
      self.x = x
      self.y = y
      self.z = z

   def __eq__(self,other):
      return (epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z))

              
class Vector:
   def __init__(self,x,y,z):
      self.x = x
      self.y = y
      self.z = z
      
   def __eq__(self,other):
      return (epsilon_equal(self.x, other.x)
      and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z))


class Ray:

   def __init__(self, pt, dir):
      self.pt = pt
      self.dir = dir

   def __eq__(self,other):
      return self.pt == other.pt and self.dir == other.dir
         
class Sphere:
   
   def __init__(self,center,radius,color,finish):
      self.center =  center
      self.radius = radius
      self.color = color
      self.finish = finish

   def __eq__(self,other):
      return self.center == other.center and epsilon_equal(self.radius, other.radius) and self.color == other.color and self.finish == other.finish


class Color:
   """This determines the Color in the sphere"""
   def __init__(self,r,g,b):

      self.r = r
      self.b = b   
      self.g = g
   def __eq__(self,other): 
      self.r == other.r and self.b == other.b and self.g == other.g

class Finish: 
   def __init__(self,ambiant,diffuse,specular,roughness): 

      self.ambiant = ambiant
      self.diffuse = diffuse
      self.specular = specular
      self.roughness = roughness

   def __eq__(self,other):
      (self.ambiant == other.ambiant and self.diffuse == other.diffuse and 
         self.specular == other.specular and self.roughness == other.roughness)

class Light:
   """Let there be Light"""
   def __init__(self, pt, color):
      self.pt = pt
      self.color = color

   def __eq__(self,other): 
      self.pt == other.pt and self.color == other.color
      
      


from vector_math import *
from math import*
def sphere_intersection_point(ray, sphere):

    a = dot_vector(ray.dir,ray.dir)
    b = 2 * dot_vector((difference_point(ray.pt,sphere.center)),ray.dir)
    c = dot_vector(difference_point(ray.pt,sphere.center),difference_point(ray.pt,sphere.center)) - sphere.radius**2
    if (b**2-4.0*a*c)<0:
        return None
    t1=(-b+sqrt(b**2-4.0*a*c))/(2.0*a)
    t2=(-b-sqrt(b**2-4.0*a*c))/(2.0*a)

    if  t1>0 and t2>0 and t1<t2:
        return translate_point(ray.pt,scale_vector(ray.dir,t1))
    elif  t1>0 and t2>0 and t1>t2:
        return translate_point(ray.pt,scale_vector(ray.dir,t2))
    elif t1<0 and t2<0:
        return None
    elif t1>0 and t2<0:
        return translate_point(ray.pt,scale_vector(ray.dir,t1))
    elif t1<0 and t2>0:
        return translate_point(ray.pt,scale_vector(ray.dir,t2))
    elif t1>0 and t2 == 0:
        return translate_point(ray.pt,scale_vector(ray.dir,t1))
    elif t1<0 and t2 == 0:
        return None
    elif t1 == 0 and t2>0:
        return translate_point(ray.pt,scale_vector(ray.dir,t2))
    elif t1 == t2 and t1>0:
        return translate_point(ray.pt,scale_vector(ray.dir,t2))
    elif t1 == 0 and t2<0:
        return None
    elif t1 == 0 and t2 == 0:
        return translate_point(ray.pt,scale_vector(ray.dir,t2))

def  find_intersection_points(sphere_list, ray):
    if sphere_list == []:
        return None
    ip = []
    i=0
    while i<len(sphere_list):
        p = sphere_intersection_point(ray,sphere_list[i])
        if  p != None:
            ip.append((sphere_list[i],p))
        i+=1
    return ip
 

def sphere_normal_at_point(sphere, point):
    return normalize_vector(vector_from_to(sphere.center,point))

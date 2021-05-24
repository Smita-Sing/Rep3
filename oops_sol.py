# Write a Python program which accepts the radius of a circle from the user and compute the area.

class circle:
    def __init__(self,radius):
        self.radius=radius

    def getarea(self):
        area=3.14*(self.radius**2)
        return area
        
if __name__=="__main__":
    r=eval(input("Enter radius"))
    c=circle(r)
    print("area of circle is = ",c.getarea())       
       
'''
Created on Nov 13, 2018

@author: codrin18
'''
from Domain.MyPoint import MyPoint

#from MyPoint import MyPoint


class PointRepository():
    
    def __init__(self):
        self.__MyPoint = []
        
    def verify_coord(self,x,y):
        for elem in self.__MyPoint :
            if elem.get_x() == x and elem.get_y() == y :
                return True
        return False
    def add(self,point):
        if self.verify_coord(point.get_x(), point.get_y()) == True :
            raise ValueError("Point not added...")
        else :
            self.__MyPoint.append(point)
    def size(self):
        return len(self.__MyPoint)
    def get_all(self):
        return self.__MyPoint
    def get_by_colour(self,col):
        get_colour = []
        for elem in self.__MyPoint :
            if elem.get_colour() == col :
                get_colour.append(elem)
        return get_colour
    def dist_2_points(self,point):
        return (self.get_x()-point.get_x())**2 + (self.get_y()-point.get_y())**2
    def get_points_circle(self,cent,radius):
        get_circle = []
        for elem in self.__MyPoint :
            if (elem.get_x()-cent.get_x())**2 + (elem.get_y()-cent.get_y())**2<= radius**2 :
                get_circle.append(elem)
        return get_circle
    def shift_all_x(self,val):
        for elem in self.__MyPoint :
            elem.set_x(val) 
    def del_by_index(self,index):
        if index < 0 or index > len(self.__MyPoint) :
            raise ValueError("Index out of range...")
        else :
            del self.__MyPoint[index]
            

points = PointRepository()
p1 = MyPoint(2,3,"green")
points.add(p1)
p2 = MyPoint(2,5,"red")
points.add(p2)
p3 = MyPoint(2,4,"blue")
points.add(p3)
p4 = MyPoint(1,1,"yellow")
points.add(p4)
p5 = MyPoint(1,2,"red")
v =points.get_by_colour(col = "green")
cent = MyPoint(2,6,"red")
g =points.get_points_circle(cent, radius = 6)


    
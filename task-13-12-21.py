#TASK-1
# int to str, float, bool
a = 12
print (a)
print (type(a))
b = str(a)
print (type(b))
c = float(a)
print (type(c))
d = bool(a)
print (type(d))

# float to int, str, bool
a= 10.02
print (a)
print (type(a))
print (type(int (a)))
print (type(str (a)))
print (type(bool (a)))

# bool to int, str, float
a = False
print (a) 
print (type(a))
print (type (int (a)))
print (type (str (a)))
print (type (float (a)))

# str to int, float,bool
a = "Python"
print (type(a)) 
print (type (int (a)))
print (type (float (a)))
print (type(bool (a)))

#TASK-2
radius = float (input("Please enter the radius:"))
pi = 3.14
area = int (pi*radius*radius)
print ("Area of the circle is:", area)
perimeter = int (2*pi*radius)
print ("Perimeter of the circle is:", perimeter)

#TASK-3
radius = float (input("Please enter the radius:"))
height = float (input("Please enter the height:"))
pi = 3.14
area = int (pi*radius*radius*height)
print ("The Area of the Cone with radius {},pi {} and height {} is {}".format(radius,pi,height,area))

#TASK-4
a = "COMPUTER_SCIENCE"
print (a[-1])
print (a[0])
print (a[4])
print (a[-4])
print (a[2])
print (a[-2])
print (a[-3])
print (a[-5])
print (a[7])
print (a[-7])
print (a[8])
print (a[-8])
                

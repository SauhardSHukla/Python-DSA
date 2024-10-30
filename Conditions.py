#If and else Condititons of the python coding

x=int(input())
if x%2==0:
    print("We are inside the if conditions =",x)
else:
    print("We are out of it" )
          


#Use of elif in the code

marks=int(input())
if marks >=90 and marks <=100:
    print("Hey topper")
elif marks >=60 and marks <=89:
    print("Hey runnerup")
elif marks >=0 and marks <=59:

    print("loooser boooo")


# Find the largest of all the three numbers

x=int(input())
y=int(input())
z=int(input())
if x>y and x>z:
      print("The largtest is :",x)
elif y>z and y>x:
      print("The largtest is :",y)
else:
      print("The largtest is :",z)

#Nested List

v=int(input())
if v >=0:
    if x==0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

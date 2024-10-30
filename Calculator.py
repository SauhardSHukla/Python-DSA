#calculator From the python

x= int(input("Enter the value here for Num1 :"))
y= int(input("Enter the value here for Num2:"))

print("Choose the operator +,-,*,/,//,")
opera = input("Enter the option you want here:")
match opera:
      case "+":
          r = x+y
          print("Output is ",r)
      case "-":
          r = x-y
          print("Output is ",r)
      case "*":
          r = x*y
          print("Output is ",r)
      case "/":
          if y==0:
              print("Invalid ")
          else:
              r = x/y
              print("Output is ",r)
      case _:
           print("Invalid")





                
                  

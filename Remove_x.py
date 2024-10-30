##def removeX(string): 
##    if len(string)==0:
##        return ""
##    small= removeX(string[1:])
##    if string[0]=="x":
##        return small
##    else:
##         return string[0]+small
##    pass
##
### Main
##string = (input())
##print(removeX(string))



##def replacePi(string):
##    if len(string)==0 or len(string)==1:
##        return string
##    
##    if string[0]=="p" and string[1]=="i":
##        smalloutput=replacePi(string[2:])
##        return "3.14"+smalloutput
##    else:
##        smalloutpust=replacePi(string[1:])
##        return string[0]+smalloutput
##string = input()
##print(replacePi(string))

def remove_dup(s):
    if len(s)==1 or len(s)==0:
        return s
    same_value=remove_dup(s[1:])
    if s[0] in same_value:
        return same_value
    else:
        return s[0]+same_value
s=input()
print(remove_dup(s))

##original = "hello"
##modified = original[:1] + 'a' + original[4:1]  # Changing 'hello' to 'hallo'
##print(modified)  # Output: 'hallo'

def string(s,x,b,st):
    if st>=len(s):
        return ""
    small=string(s,x,b,st+1)
    if s[st]==x:
        return b+small
    else:
        return s[st]+ small

result=string("cbsdsd","s","x",0)
print(result)

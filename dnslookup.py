import socket


print("1.Url to ip")
print("2.Ip to url")
q=input()
if q!=1:
    w=" "  
    w=raw_input("Input ip")
    print (w)
    name, alias, wer=socket.gethostbyaddr(w)
    print (name)
else :   
    i=" "
    i=raw_input("Input  Url")
    print (i)
    rty=socket.gethostbyname(i)
    print (rty)


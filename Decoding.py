a= 18756
a0=(a&0xFF)
a1=((a>>8)&0xFF)
a2=((a>>16)&0xFF)
a3=((a>>24)&0xFF)
print("value of a0:",a0)
print("value of a1:",a1)
print("Value of a2", a2)
print("Value of a3",a3)
  
s=[a0,a1,a2,a3]
s = [str(i) for i in s] 
Number = int("".join(s)) 
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10   
     
print("\n Reverse is :" ,Reverse) 

def convertToBinary (n):
    if n>1:
        convertToBinary(n//2)
        print(n%2,end ="")

        print(convertToBinary(Reverse))
#WAP accept three digit no from user and display sum
print("Enter 3 digit no :")
a=int(input())
total=0
while(a>0):
    digit=a%10
    total=total+digit
    a=a//10
print(total)    

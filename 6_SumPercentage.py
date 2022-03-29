#Wap accept 5 marks from user and display sum and percentage
print("Enter 5 subject marks ")
math=int(input())
chem=int(input())
phy=int(input())
engl=int(input())
hind=int(input())

sum =math+chem+phy+engl+hind
percentage=(sum/500)*100
print(sum)
print(percentage)
#n = 5
#for i in range(n):
 #   for j in range(i,n):
  #      print(" " , end=" ")
 #   for j in range(i+1):
 #       print("*" , end=" ")
 #   print()
positive_integer = int(input("Enter the size of the pattern: "))
n = 0
while n < positive_integer:
    for j in range(positive_integer):
        print("*", end="")
    print()
    n += 1
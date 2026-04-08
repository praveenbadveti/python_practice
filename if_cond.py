x=int(input("Enter the number: "))
y=int(input("Enter the number: "))
if x<y:
    print("x is less than y")
    if x%2==0:
        print("x is even")
    else:
        print("x is odd")
elif(x>y):
    print("x is grater than y")
    if x%2==0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x and y are equal")
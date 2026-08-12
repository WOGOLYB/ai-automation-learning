print ("z = x+y")
x=float(input("What is X? input any number: "))
y=float(input("What is Y? input any number: "))
z=(x/y)
print(f"then, z is {z:,.2f}")

def main():
    x = int(input("what is x? "))
    print ("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()
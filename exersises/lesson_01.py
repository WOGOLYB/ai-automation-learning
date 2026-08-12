from tkinter.filedialog import test

def hello(to="valued customer"):
    print (to, "you can go now, but you will have to come back to this lesson later")

name = input ("Please enter your full name: ").strip().title()
first,last = name.split(" ")
age = input ("Please enter your age: ").strip()
sex =input ("Please enter your sex: ").strip()
print (f"lesson 1 is for {first} {last}, {age} years old {sex}.")
print (f"Hi, {first}.")
print (f"{last}?? Such a cool last name, but {age} years old? really? okay, lets move on") 

hello()
test=input("What is your middle name? ")
hello(test)
cost = int(1000)

print ("Welcome to chat")
print ("I am here to do the numbers")

name = input("What is your name? ").strip().title()
print (f"Hello, {name}!")

visitors = int(input("How many visitors do you have weekly? "))
if visitors < 10:
    x = int(cost)
elif 10 <= visitors < 50:
    x = int(cost * 1.1)
elif 50 <= visitors <= 100:
    x = int(cost * 1.2)
else:
    x = int(cost * 1.3)

service = input("Do you want to add automation? (yes/no) ").strip().lower()
if "yes" in service:
    y = int(x * 1.2)
elif "no" in service:
    y = x
else:
    print ("Invalid input. Please enter 'yes' or 'no'.")
    y = x  # Default to no service if input is invalid

deposit = y * 0.2
commission = y * 0.05

country = input("What country are you from? ").strip().title()
budget = int(input("What is your budget? $"))

if y <= budget:
    budget_status = "within budget"
    difference_label = "Budget remaining"
    difference = budget - y
else:
    budget_status = "over budget"
    difference_label = "Budget exceeded by"
    difference = y - budget

time = input("What is your deadline? ").strip().lower()
email = input("What is your email? ").strip().lower()

print (f"Thank you for your answer, {name}. Your calculation is:")
print (country, budget, time, email)
print (f"Your total cost is: ${y:,.2f}")
print (f"Your deposit is: ${deposit:,.2f}")
print (f"Your commission is: {commission:,.2f}")
print (f"budget status: {budget_status}")
print (f"{difference_label}: ${difference:,.2f}")


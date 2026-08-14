cost = int(1000)

print ("Welcome to chat")
print ("I am here to do the numbers")

name = input("What is your name? ").strip().title()
print (f"Hello, {name}!")

visitors = int(input("How many visitors do you have weekly? "))
if visitors < 10:
    base_price = int(cost)
elif 10 <= visitors < 50:
    base_price = int(cost * 1.1)
elif 50 <= visitors <= 100:
    base_price = int(cost * 1.2)
else:
    base_price = int(cost * 1.3)

service = input("Do you want to add automation? (yes/no) ").strip().lower()
if "yes" in service:
    total_cost = int(base_price * 1.2)
elif "no" in service:
    total_cost = base_price
else:
    total_cost = base_price  # Default to no service if input is invalid

deposit = total_cost * 0.2
commission = total_cost * 0.05

country = input("What country are you from? ").strip().title()
budget = int(input("What is your budget? $"))

if total_cost <= budget:
    budget_status = "within budget"
    difference_label = "Budget remaining"
    difference = budget - total_cost
else:
    budget_status = "over budget"
    difference_label = "Budget exceeded by"
    difference = total_cost - budget

def get_lead_status(budget_status, service):
    if budget_status == "within budget": 
        if service == "yes":
            return "High priority"
        elif service == "no":
            return "Qualified"
    else:
        return "Needs review"
        

lead_status = get_lead_status(budget_status, service)
time = input("What is your deadline? ").strip().lower()
email = input("What is your email? ").strip().lower()

print (f"Thank you for your answer, {name}. Your calculation is:")
print (country, budget, time, email)
print (f"Your total cost is: ${total_cost:,.2f}")
print (f"Your deposit is: ${deposit:,.2f}")
print (f"Your commission is: {commission:,.2f}")
print (f"budget status: {budget_status}")
print (f"{difference_label}: ${difference:,.2f}")
print (f"lead status: {lead_status}")

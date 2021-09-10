#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")

porcentage = input("What porcentage tip would you like to give? ")

how_many_people = input("How may people to split the bill? ")

float_bill = float(bill)
int_porcentage = int(porcentage)
int_how_many_people = int(how_many_people)

thePorcentage = (int_porcentage/100)

total_tip = float_bill * thePorcentage
total_bill = float_bill + total_tip
bill_person = total_bill / int_how_many_people

redon = round(bill_person,2)
result = f'Each person should pay: ${redon} dollars'

print(result)

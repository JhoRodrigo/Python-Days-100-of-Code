#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
result = (percentage / 100) * bill + bill
people = int(input("How many people to split the bill"))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
result_fim = round(result / people,2)
result_fim = "{:.2f}".format(result_fim)
#Write your code below this line 👇
print(f"Each person should pay: {result_fim}")
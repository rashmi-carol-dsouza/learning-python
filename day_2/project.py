#This is calculator to add tips to a bill and thereafter split it amongst people 
print("It's no fun to calculate how much we owe the bartender\n after a night of fun 🔞\nLet me help you not get ripped off")
total_bill = input('What is your total?\n')
per_tips = input('How much do you want to tip the bartender - 10%, 12% or 15% ?\n')
persons = input ('Between how many people do you want to split the bill?\n')
tip = float(total_bill) * float(per_tips) / 100
bill_with_tip = float(total_bill) + float(tip)
bill_per_person = float(bill_with_tip) / float(persons)
format_bill_per_person = "{:.2f}".format(bill_per_person)
print(f'Each person must pay 💸 $ {str(format_bill_per_person)} 💸')
#Another way to round off decimals
#r_bill_per_person = round(bill_per_person,2)
#print('Each one must pay : $' + str(r_bill_per_person))

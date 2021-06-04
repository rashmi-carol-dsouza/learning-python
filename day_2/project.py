print('Its no fun to pay the bartender after a night of fun\nLet me help you not get ripped off')
total_bill = input('What is your total bill?')
per_tips = input('How much do you want to tip the bartender - 10%, 12% or 15% ?')
persons = input ('Between how many people do you want to split the bill?')
tip = float(total_bill) * float(per_tips) / 100
bill_with_tip = float(total_bill) + float(tip)
bill_per_person = float(bill_with_tip) / float(persons)
format_bill_per_person = "{:.2f}".format(bill_per_person)
print('Each one must pay : $' + str(format_bill_per_person))
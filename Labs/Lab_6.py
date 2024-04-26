def getIncomeTax(salary):
    tax_rates = {
        'Personal_Allowance': 11850,
        'first_band': 34500,
        'second_band': 150000,
        'percentage_of_tax_zero': 0,
        'percentage_of_tax_twenty': 0.20,
        'percentage_of_tax_fourty': 0.40,
        'percentage_of_tax_fourty_five': 0.45
    }

result = 0

if salary <= tax_rates['Personal_Allowance']:
    result = (tax_rates['percentage_of_tax_zero'])
elif salary <= tax_rates['first_band']:
    result = (tax_rates['Personal_Allowance']) * (tax_rates['percentage_of_tax_twenty'])
elif salary <= (tax_rates['second_band']):
    result = (tax_rates[])


salary = int(input("What is your salary?: £ "))
print getIncomeTax

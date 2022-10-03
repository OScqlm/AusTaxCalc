# calculate tax for 2022-2023 financial year. 
import sys
# print(sys.getrecursionlimit())
# setting recursion to 24 instead of default 1000
sys.setrecursionlimit(24)

def main():
    
    print('=============================== 2022-2023 AUSTRALIAN TAX CALCULATOR ===============================')
    decide = 0
    while decide == 0:
        try:
            decide = int(input('\nAre you an Australian Resident (1) or Foreign Resident (2)? '))
            if decide == 1:
                residentstaxrate22_23()
            elif decide == 2:
                foreigntaxrate22_23()
        except ValueError:
            print('\nERROR: Please enter a valid number. 1 for Australian Resident or 2 for Foreign Resident.\n')
    retry()

def residentstaxrate22_23():

    print('\n=============================== 2022-2023 Australia Resident Tax Calculator ===============================\n')
    income = 1
    while income == 1:
        try:
            income = int(input('Enter your annual salary: $ '))
        except ValueError:
            print('\nERROR: Please enter a valid salary number. Ensure there are no spaces or commas.\n')

    if income > 0 and income <= 18200:
        print('Income after tax: $', income)

    elif income >= 18201 and income <= 45000:
        paid_tax = (income-18200)*0.19

    elif income >= 45001 and income <= 120000:
        paid_tax = (income-45000)*0.325+5092
       
    elif income >= 120001 and income <= 180000:
        paid_tax = (income-120000)*0.37+29467
        
    elif income >= 180001:      
        paid_tax = (income-180000)*0.45+51667
        
    income_after_tax = (income-paid_tax)
    print('Tax paid: $', paid_tax)
    print('Income after tax: $', income_after_tax)


def foreigntaxrate22_23():
    print('\n=============================== 2022-2023 Foreign Resident Tax Calculator ===============================\n')
    income = 1
    while income == 1:
        try:
            income = int(input('Enter your annual salary: $ '))
        except ValueError:
            print('\nERROR: Please enter a valid salary number. Ensure there are no spaces or commas.\n')

    if income > 0 and income <= 120000:
        paid_tax = (income)*0.325

    elif income >= 120001 and income <= 180000:
        paid_tax = (income-120000)*0.37+39000
       
    elif income >= 180001:
        paid_tax = (income-180000)*0.45+61200
        
    income_after_tax = (income-paid_tax)
    print('Tax paid: $', paid_tax)
    print('Income after tax: $', income_after_tax)

def retry():
    retry = ''
    while retry != 'y' or retry != 'n':
        try:
            retry = input('\nWould you like to calculate again? (y/n): ')
            if retry == 'y':
                main()
            elif retry == 'n':
                sys.exit()
        except Exception:
            print("Please enter 'y' for yes or 'n' for no.")

main()
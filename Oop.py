
#create a ROI function for income, expenses, investment 
class Roi_calc():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashflow = 0
        self.investment = 0
        self.cashoncashroi= 0

#What are you charging for rent, pet fee, wifi
    def get_income(self):
        rent = input('Total amount of income for rent')
        pet_fee = input('Total amount income collected per pet')
        wifi = input('Total amount income collected for wifi')
        other = input('Total amount income for other expenses')
        # amount varies depends on what you are charging for
        
        self.income = rent + pet_fee + wifi + other
        
        print(f'The total montlhy income is {self.income}')

#What expenses are there on the property
    def get_expenses(self):
        tax = input('What are property taxes')
        insurance = input('How much do you pay for insurance')
        utilites = input('How much do you pay for utilies')
        HOA = input('How much are HOA fees')
        repairs = input('How much set aside for repairs')
        # amount varies depends on what you are charging for

        self.expenses = tax + insurance + utilites + HOA + repairs
        
        print(f'The total monlthy expenses are {self.expenses}')

        #monthly total cashflow spent
    def get_cashflow(self):
        self.get_income()
        self.get_expenses()
        total_reward = self.get_expenses - self.get_income
        
        print(f' The total capital is {total_reward}')

        annualcashflow = total_reward * 12

        return annualcashflow

        #Total amount you made in profit

        # This is ROI, how much did you earn minus how much you spent
    def get_investment(self):
        downpayment = input('Total amount put down')
        closingcosts = input('Total amount contributed to closing costs')
        rehab = input('Total amount to repair')
        other = input('Total amount for other expenses')

        investment= downpayment + closingcosts+ rehab + other
        print(f' The total investment is {self.investment}')
        return investment

    def get_cashoncashroi(self):

        roi = self.annualcashflow / self.investment *100
        print(f' The total ROI is {self.roi}')
        return roi
        
        
        #Total amount you made in profit

    def runner(self):    
        while True:
            user_input= input('Do you want to do : Loan Details/Income/Expenses/Cash Flow/Delete or Quit?')
            if user_input == 'Income':
                roi_total.get_income ()
            if user_input == 'Loan Details':
                roi_total.get_investment()
            if user_input == 'Expenses':
                roi_total.get_expenses()
            if user_input == 'Cash Flow':
                roi_total.get_cashflow()
            if user_input == 'ROI':
                roi_total.get_cashoncashroi()
            if user_input == 'Delete or Quit':
                break
#maybe an if statement here
        

        roi_total = Roi_calc()
        roi_total.runner()
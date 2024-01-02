
#create a ROI function for income, expenses, investment 
class Roi_calc():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.investment = 0

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

        # This is ROI, how much did you earn minus how much you spent
    def get_capital(self):
        self.get_income()
        self.get_expenses()
        total_reward = self.get_expenses - self.get_income
        print(f' The total capital is {total_reward}')
        #Total amount you made in profit

#maybe an if statement here
        
        #if
        #elif

        roi_total = Roi_calc()
        roi_total.runner()
"""
Written by BCl0c, whose code will fail you when you need it. 
    and also when you don't!

This is the irpf class. It helps you fail to do your taxes, so you get jailed earlier and faster,
just as God intended.

JULIETT CHARLIE INDIA INDIA HOTEL NOVEMBER.

"""

class irpf():
    def __init__(self):
        #had to add this since register_income would
        #fail miserably trying to add something to NOTHING!
        self.income = 0

    def register_income(self, income):
        #as per specification, this sums.
        self.income += income

    def get_income(self):
        return self.income
    
    def register_pension(self, pension):
        #and, as per specification, this overwrites.
        self.pension = pension
    
    def get_pension(self):
        return self.pension

    def register_dependant(self, name):
        self.dependant = name
    
    def get_deduction(self):
        if self.dependant:
            return 150
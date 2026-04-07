import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if amount > 0 and self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total += entry['amount']
        return total

    def transfer(self, amount, category):
        if (self.withdraw(amount, f'Transfer to {category.name}')):
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def __str__(self):
        display = f"{self.name.center(30,'*')}"
        for entry in self.ledger:
            display += f"\n{entry['description']}"[:24].ljust(24)
            display += f"{entry['amount']:.2f}"[:7].rjust(7)
        display += f'\nTotal: ' + f'{self.get_balance():.2f}'
        return display

def create_spend_chart(categories):
    categories_name = [category.name for category in categories]
    categories_withdraw=[]

    for category in categories:
        total_withdraws = 0
        for operation in category.ledger:
            total_withdraws += operation["amount"] if operation["amount"]<0 else 0
        categories_withdraw.append(abs(total_withdraws))

    # calculate percentage
    total_withdraws = sum(categories_withdraw)
    categories_withdraw=[math.floor( ((withdraw/total_withdraws)*100) / 10) * 10 for withdraw in categories_withdraw]

    # set up display
    chart=""
    chart += "Percentage spent by category\n"
    list_space=[" " for i in range(0,3 * len(categories) - 1) ]

    for percentage in range(100,-1,-10):
        chart += " "*(3-len(str(percentage)))+f'{percentage}|'
        for position in range(0,len(categories_withdraw)):
            if categories_withdraw[position] == percentage :
                position=position*3+1
                list_space[position]="o"
        chart += "".join(list_space)+" "*2+"\n"
        
    list_space.append('-')
    list_space.append('-')
    list_space=["-" for _ in list_space]
    chart+=" "*4+"".join(list_space)+"\n"

    # set up categories
    max_len = max( [len(name) for name in categories_name] )
    for i in range(0,max_len):
        chart += " "*5
        for j in range(0,len(categories_name)):
            if i==max_len-1 and j==len(categories_name)-1:
                chart += categories_name[j][i] if len(categories_name[j])>i else " "
                chart += "  "
                return chart
            elif j==len(categories_name)-1:
                chart += categories_name[j][i] if len(categories_name[j])>i else " "
                chart += "  \n"
            else:
                chart += categories_name[j][i] if len(categories_name[j])>i else " "
                chart +=" "*2

if __name__ == "__main__":
    # test run
    food = Category('Food')
    food.deposit(10000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    clothing.deposit(10000, 'initial deposit')
    clothing.withdraw(2000, 'groceries')
    clothing.withdraw(150, 'restaurant and more food for dessert')
    food.transfer(50, clothing)
    entertainment = Category('Entertainment')
    entertainment.deposit(1000, 'initial deposit')
    entertainment.withdraw(200, 'games')
    entertainment.withdraw(150, 'new ram')
    neccesities = Category('Neccesities')
    neccesities.deposit(100000, 'initial deposit')
    neccesities.withdraw(5000, 'electricity')
    neccesities.withdraw(5500, 'water')
    print(food)
    print(create_spend_chart([food, clothing, entertainment, neccesities]))
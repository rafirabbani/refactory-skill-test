import datetime

hour = datetime.datetime.now()

def input_data():
    cashier_name = input("Please Enter your name \n").title()
    resto_name = input("Please enter your restaurant\'s name \n").title()
    date_entry = input('Enter a date in YYYY-MM-DD format \n')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    food = {}
    food_name = ''
    while food_name != 'Stop':
            food_name = input('Please EnterFood Name or Type stop to quit \n').title()
            if food_name == 'Stop':
                break
            else:
                food_price = int(input("Please Enter Food Price\n"))
                food[food_name] = food_price
    return [food, cashier_name, resto_name, date1]

data = input_data()

def print_func(data):
    hour_print = hour.strftime("%X")
    date_print = data[3].strftime("%x")
    currency = 'Rp{}'
    sum_value = sum(data[0].values())
    count = 0
    print(data[2].center(30) + '\n'+ '\n'+ 'Tanggal :'.ljust(15) + date_print, hour_print + '\n'+ '\n' + 'Nama Kasir : '.ljust(15), data[1].rjust(15) + '\n' + '\n'+'='.center(30, '=') + '\n')
    for key, value in data[0].items():
        print(key.ljust(15, '.') + currency.format(value).rjust(15, '.'))
    print('\n' + 'Total'.ljust(15, '.') + currency.format(sum_value).rjust(15, '.'))
    

print_func(data)


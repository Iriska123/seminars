dates = ['2021-10-01', '2021-11-05', '2021-12-10']
income = [100, 200, 300]

# nov_date = [date for date in dates if date.startswith('2021-11')]
nov_income = [income[i] for i, date in enumerate(dates) if date.startswith('2021-11')]

x = sum(nov_income)
print(x)
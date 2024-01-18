import datetime
from typing import Dict, List

dates = ['2021-11-01','2021-12-01','2021-11-11']
incomes = [100,200,50]

def calc_income_by_month(dates: List[str], incomes: List[int]) -> Dict[str,int]:
        
    result = {} 

    for date, income in zip(dates, incomes):
        mon = datetime.datetime.strptime(date,'%Y-%m-%d').strftime('%m')
        if mon in result:
            result[mon] += income
        else:
            result[mon] = income

    return result

print(calc_income_by_month(dates,incomes))
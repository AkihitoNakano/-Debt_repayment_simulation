from datetime import datetime
from dateutil.relativedelta import relativedelta

loan = int(input('借金(円): '))
interest_rate = float(input('金利(年利率): '))
repayment_amount = int(input('月々の返済額(円): '))
print('-----------------------------------')

fdate = datetime.now()
total_payment = 0

while True:
    loan *= (1+interest_rate/12/100)
    loan = int(loan)
    fdate = fdate + relativedelta(months=1)
    if loan <= repayment_amount:
        total_payment += loan
        print(f"{fdate.strftime('%Y年%m月')}:返済額{loan}円、これで完済。返済総額: {total_payment}円")
        break
    else:
        loan = loan - repayment_amount
        total_payment += repayment_amount
        print(f"{fdate.strftime('%Y年%m月')}:返済額{repayment_amount}円、残り{loan}")

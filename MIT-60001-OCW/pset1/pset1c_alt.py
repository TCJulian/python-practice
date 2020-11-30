salary = float(input("Enter your starting annual salary: "))

total_cost = 1000000
portion_down_payment = .25
semi_annual_raise = .07
current_savings = 0
r = .04

target_savings = total_cost*portion_down_payment

low = 0
high = 10000
epsilon = 100
portion_saved = (high + low)//2
numGuesses = 0

while (
        current_savings < target_savings-epsilon or
        current_savings > target_savings+epsilon
    ):
    current_savings = 0.0
    annual_salary = salary
    monthly_salary = annual_salary / 12
    saving_rate = portion_saved/10000

    for month in range(1, 37):
        current_savings += monthly_salary*saving_rate + current_savings*r/12
        if month % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise
            monthly_salary = annual_salary/12
    if current_savings < target_savings - epsilon:
        low = portion_saved
    elif current_savings > target_savings + epsilon:
        high = portion_saved
    portion_saved = (high + low)//2
    numGuesses += 1
    if portion_saved == low or portion_saved == high:
        break

if portion_saved == low or portion_saved == high:
    print("It is not possible to pay the downpayment in three years.")
else:
    print("Best savings rate: ", saving_rate)
    print("Steps in bivariate search: ", numGuesses)

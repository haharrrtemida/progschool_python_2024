def calculate_months(n, months):
    # Процентная ставка на сегодняшний день (14% годовых), хорошая ставка.
    """ еще такая приколюха вылезла, когда углубился в банковский процент, правильное начисление % ставки зависит
        и от периода начисления процентов по вкладу (год, полгода, ежеквартально, ежемесячно), 
        в данном случае используем формулу сложных процентов"""
    annual_interest_rate = 0.14
    
    # Рассчитываем сумму на счету через эн...дцать месяцев (прям как в настоящем банке), точнее сначала находим % в месяц
    monthly_interest_rate = annual_interest_rate / 12
    future_value = n * (1 + monthly_interest_rate) ** months
    
    # При этом, вспоминаем предыдущие уроки, чешем репу, вспоминаем, определяем правильное склонение слова "месяц"
    if months % 10 == 1 and months % 100 != 11:
        month_word = "месяц"
    elif 2 <= months % 10 <= 4 and (months % 100 < 10 or months % 100 >= 20):
        month_word = "месяца"
    else:
        month_word = "месяцев"
    
    return future_value, month_word

# Давайте посмотрим что получилось? (для расчета введите начальную сумму и срок вклада).
initial_deposit = 200000  # Начальная сумма вклада (в рублях), можно и в другой валюте, нужно будет поменять ее в 24 строке
investment_period_months = 24  # Срок вклада (в месяцах)

final_amount, month_word = calculate_months(initial_deposit, investment_period_months)
print(f"Через {investment_period_months} {month_word} на вашем счёте будет {final_amount:.2f} рублей")

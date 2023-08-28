# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

import decimal as dc


def get_awards(names: list[str], rates: list[int], prizes: list[str]) -> dict[str: dc.Decimal]:
    people_awards = {}
    for name, rate, prize in zip(names, rates, prizes):
        people_awards[name] = rate * dc.Decimal(prize[:-1]) / 100

    return print(people_awards)




names = ['Иван', 'Александр', 'Екатерина']
rates = [10_000, 20_000, 45_000]
prizes = ['242.55%', '104.33%', '50.15%']

get_awards(names, rates, prizes)
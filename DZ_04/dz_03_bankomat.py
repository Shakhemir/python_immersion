"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.

Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

balance = 0
action = 0


def show_balance():
    print(f'Ваш баланс: {balance:_.2f}')


def input_cash(prompt: str):
    while True:
        try:
            cash = int(input(prompt))
            if not cash % 50:
                return cash
            else:
                print('Введите число кратное 50')
        except Exception:
            print('Введите число')


def change_balance(cash):
    global balance, action
    if balance > 5_000_000:
        nalog_robin_guda = balance / 10
        balance -= nalog_robin_guda
        print(f'С вашего счета вычли налог на богатство {nalog_robin_guda:_.2f}')
    balance += cash
    action += 1
    if not action % 3:
        per_cent = balance * (3 / 100)
        balance += per_cent
        print(f'Вам начислили 3% = {per_cent:_.2f} за активность')
    show_balance()


def cash_in():
    money_in = input_cash('Пополнить баланс: ')
    change_balance(money_in)


def cash_out():
    while True:
        money_out = input_cash('Введите сумму для снятия: ')
        comission = money_out * (1.5 / 100)
        comission = max(30, comission)
        comission = min(600, comission)
        print(f'Коммиссия за снятие = {comission}')
        money_out += comission
        if money_out < balance:
            break
        else:
            print(f'Сумма для снаятия {money_out} превышает баланс на счету')
    print(f'Со счета снято: {money_out}')
    change_balance(-money_out)


if __name__ == '__main__':
    show_balance()
    select = -1
    while select != 3:
        print('---------------------------------')
        print('1. Пополнить, 2. Снять, 3. Выйти')
        print('---------------------------------')
        select = int(input('> '))
        match select:
            case 1:
                cash_in()
            case 2:
                cash_out()
            case _:
                pass

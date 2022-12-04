"""1) Реализовать скрипт, в котором
должна быть предусмотрена функция
расчета заработной платы сотрудника.
В расчете необходимо использовать
формулу: (выработка в часах*ставка в
час) + премия. Для выполнения расчета
для конкретных значений необходимо
запускать скрипт с параметрами."""

from sys import argv

script_name, work_hours, money_in_hour, \
prize = argv

print("Имя скрипта", script_name)
print("Имя скрипта", work_hours)
print("Имя скрипта", money_in_hour)
print("Имя скрипта", prize)

salary = float(work_hours) * \
         float(money_in_hour) + float(prize)

print(f"Заработная плата составит: "
      f"{salary}")

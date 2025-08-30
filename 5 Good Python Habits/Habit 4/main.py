# Habit 4 - Type Annotations
number1: int = 10      # ✔️
number2: int = 10.0    # 🚫 will generate a warning since 10.0 is not an integer
number3: float = 10.0  # ✔️


def upper_everything(elements):
  return [element.upper() for element in elements]

list1: list[str] = upper_everything(['Frodo', 'Sam', 'Merry', 'Pippen'])    # ✔️
list2: list[int] = upper_everything(['Frodo', 'Sam', 'Merry', 'Pippen'])    # 🚫
list3: list[int] = upper_everything([1, 2, 3, 4])                           # 🚫

# main_update.py
from typing import Iterable, List

# Habit 4: type annotations
number1: int = 10        # ✔️
number2: int = 10.0      # ⚠️ will generate a warning since 10.0 is not an integer
number3: float = 10.0    # ✔️

def upper_everything(elements: Iterable[str]) -> List[str]:
  """
  Convert each string in "elements" to uppercase.

  Args:
    elements: An iterable of strings.

  Returns:
    A list containing the uppercase versions of the input strings.
  """
  return [element.upper() for element in elements]

# Good Habit 2: bundle up all definitions
def main() -> None:    # test case
  list: List[str] = upper_everything(['Frodo', 'Sam', 'Merry', 'Pippen'])
  print(f"{list}")

# Good Habit 1:
if __name__ == "__main__":
  main()
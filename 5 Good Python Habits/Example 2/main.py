def greet() -> None:
  print('Hello world!')

def bye() -> None:
  print('Bye world!')

# Good Habit 2 - 'bundle up all your definitions'
def main() -> None:
  greet()
  bye()

if __name__ == '__main__':
  main()

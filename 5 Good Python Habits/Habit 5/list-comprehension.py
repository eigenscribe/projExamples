# This code uses list comprehension -> reduces the number of lines of code compared to without-list-comprehension.py
fellowship: list[str] = ["Frodo", "Sam", "Merry", "Pippen", "Gandalf", "Aragorn", "Borimir", "Legolas", "Gimli"]

long_names = [companion for companion in fellowship if len(companion) > 6]

print(f"Long names: \n{long_names}")

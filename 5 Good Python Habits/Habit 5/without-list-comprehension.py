# This code DOES NOT use list comprehension -> more lines of code
fellowship: list[str] = ["Frodo", "Sam", "Merry", "Pippen", "Gandalf", "Aragorn", "Borimir", "Legolas", "Gimli"]

long_names: list[str] = []
for companion in fellowship: 
  if len(companion) > 6:
    long_names.append(companion)

print(f"Long names: \n{long_names}")

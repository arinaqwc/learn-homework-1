def get_summ(num_one, num_two):
  try:
    num_one=int(num_one)
    num_two=int(num_two)
    return num_one+num_two

  except ValueError:
    return "Введите числа"
  
print(get_summ(2, 2))
print(get_summ(3, "3"))
print(get_summ("4", "4"))
print(get_summ("five", 5))
print(get_summ("six", "шесть"))
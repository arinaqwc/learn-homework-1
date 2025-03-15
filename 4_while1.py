def ask_user():
  while True:
    answer=input('Как дела? ')
    answer=answer.strip().lower()
    if answer=='хорошо':
      break

ask_user()
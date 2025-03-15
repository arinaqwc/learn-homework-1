def ask_user():
  try:
    while True:
     answer=input('Как дела? ')
     answer=answer.strip().lower()
     if answer=='хорошо':
       break
  except KeyboardInterrupt: 
    print('Пока!')

ask_user()
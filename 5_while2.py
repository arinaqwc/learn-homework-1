dialog={'Как дела?':'Отлично','Ты кто?': 'Программа', 'Что делаешь?':'Программирую'}
def ask_user_dict():
  while True:
    question=input('Задай вопрос: ').capitalize()
    if question in dialog:
      print(dialog[question])
      break

ask_user_dict()

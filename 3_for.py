classes=[{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
{'school_class': '4б', 'scores': [5,4,4,5,5]},
{'school_class': '4в', 'scores': [3,3,5,5,4]},
]
def class_avg(student_score):
  sum_score=0
  for score in student_score:
    sum_score+=score
  return sum_score/len(student_score)
school_sum=0
for one_class in classes:
  sr_class=class_avg(one_class['scores'])
  print(f'Средняя оценка по классу: {one_class['school_class']} {sr_class}')
  school_sum+=sr_class
print(f'Средняя по школе {school_sum/len(classes)}')
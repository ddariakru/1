# journal = [('Класс', 'Россия'), ('Дракула', 'Румыния'), ('Washington Post','Великобритания'), ('Привет', 'Россия')]

# def countries(journals):

#     for i in range(len(journals)):
#         if journals[i][1] == 'Великобритания':
#             journals[i][1] = 'Россия'
#     return journals

# print (countries(journal))



journal = [('Класс', 'Россия'), ('Дракула', 'Румыния'), ('Washington Post','Великобритания'), ('Привет', 'Россия')]

def countries(journals):
  new_journals = []
  for i in range(len(journals)):
    if journals[i][1] == 'Великобритания':
      new_journals.append((journals[i][0], 'Россия'))
    else:
      new_journals.append(journals[i])
  return new_journals

print(countries(journal))
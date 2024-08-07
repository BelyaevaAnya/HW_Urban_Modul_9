first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(firts_elm) for firts_elm in first_strings if len(firts_elm) >= 5]
print(first_result)

second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]
print(second_result)

third_result = {key: len(key) for key in (first_strings + second_strings) if len(key) % 2 == 0}
print(third_result)

# =>
# [10, 8, 8]
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}

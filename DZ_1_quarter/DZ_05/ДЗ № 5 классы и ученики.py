from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Мария', 'Муфасаил']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

school = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses, fillvalue=None))
print(*school)

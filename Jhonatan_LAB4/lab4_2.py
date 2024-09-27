grades = []

grades.append(92)
grades.append(51)
grades.append(83)
grades.append(37)
grades.append(72)

print(f'Current list: {grades}')

grades_total = grades[0] + grades[1] + grades[2] + grades[3] + grades[4]
grades_average = grades_total / len(grades)

print(f'Average: {grades_average:.2f}',end='\n\n')

failing_grades = [i for i in grades if i < 60]

grades.remove(failing_grades[0])
grades.pop(grades.index(failing_grades[-1]))

print(f'Updated List: {grades}')

new_grades_average = sum(grades) / len(grades)

print(f'Updated Average: {new_grades_average:.3f}')
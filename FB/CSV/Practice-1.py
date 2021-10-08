import csv

outfile = open('output-file.csv', 'a')
outfile_header = 'Student First Name, Student Last Name \n'
outfile.write(outfile_header)

with open('student_grades.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f, delimiter=',')
    header = next(data)

    for row in data:
        student_first_name = row[0]
        student_last_name = row[1]
        student_year = row[2]
        student_grade = row[3]
        line = f'{student_first_name}, {student_last_name}\n'
        outfile.write(line)

outfile.close()
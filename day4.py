student_scores=[90,47,63,54,46]
#print(sum(student_scores))
sum=0
for score in student_scores:
    sum+=score
print(sum)
max=0
for score in student_scores:
    if score>max:
        max=score
print(max)
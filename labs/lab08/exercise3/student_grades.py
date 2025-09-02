score1 = 78
score2 = 85
score3 = 92
score4 = 67
score5 = 88

grades = [score1, score2, score3, score4, score5]

total_grades = sum(grades)
print(f"The total of all grades is: {total_grades} (type: {type(total_grades)})")
average_grade = total_grades / len(grades)
print(f"The average grade is: {average_grade} (type: {type(average_grade)})")

score1_contribution = (score1 / total_grades) * 100
print(f"Score1 contributes {score1_contribution:.2f}% to the total grades (type: {type(score1_contribution)})")
score2_contribution = (score2 / total_grades) * 100
print(f"Score2 contributes {score2_contribution:.2f}% to the total grades (type: {type(score2_contribution)})")
score3_contribution = (score3 / total_grades) * 100
print(f"Score3 contributes {score3_contribution:.2f}% to the total grades (type: {type(score3_contribution)})")
score4_contribution = (score4 / total_grades) * 100 
print(f"Score4 contributes {score4_contribution:.2f}% to the total grades (type: {type(score4_contribution)})")
score5_contribution = (score5 / total_grades) * 100
print(f"Score5 contributes {score5_contribution:.2f}% to the total grades (type: {type(score5_contribution)})") 
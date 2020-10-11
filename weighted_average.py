def weighted_average(n1, n2, n3):
    # WE INSERT 3 VALUES,
    # WITH WEIGHT 2, 3 AND 5 RESPECTIVELY
    # AND RETURN THE WEIGHTED AVERAGE AT THE TERMINAL
    return (n1 * 2 + n2 * 3 + n3 * 5) / 10


print('\tLets calculate the students final grade using a weighted average.')
labGrade = float(input('\tInput the Laboratory Grade.\n'))

semiannual_evaluation = float(input('\tNow, enter the Semiannual Evaluation grade.\n'))

final_exam = float(input('\tAnd, finally, insert the Final Exam note.\n'))

print('The weighted average is ', weighted_average(labGrade, semiannual_evaluation, final_exam))

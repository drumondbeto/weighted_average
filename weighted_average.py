def weighted_average(n1, n2, n3):
    # WE INSERT 3 VALUES,
    # WITH WEIGHT 2, 3 AND 5 RESPECTIVELY
    # AND RETURN THE WEIGHTED AVERAGE AT THE TERMINAL
    w_average = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    print('The weighted average is ', w_average)


print('\tLets calculate a students final grade using a weighted average.')
labGrade = float(input('\tInput the Laboratory Grade.\n'))

semiannual_evaluation = float(input('\tNow, enter the Semiannual Evaluation grade.\n'))

final_exam = float(input('\tAnd, finally, insert the Final Exam note.\n'))

weighted_average(labGrade, semiannual_evaluation, final_exam)

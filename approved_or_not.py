def verification(grade):
    while grade < 0 or grade > 10:
        grade = float(input('Invalid number, try again.\n'))

    return grade


def average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def status():
    x = average(n1, n2, n3)

    print('-------------------------------------------------------')
    print('The average was ', x)

    if 7 <= x <= 10:
        print('The student was APPROVED.')

    elif 3 <= x < 7:
        print('The student need to do the FINAL EXAM.')

    else:
        print('The student was DISAPPROVED.')

    print('-------------------------------------------------------')


print('-------------------------------------------------------')
print('Lets find out if the student was approved, or not')

n1 = float(input('Insert the first note (Between 0 and 10).\n'))
if n1 < 0 or n1 > 10:
    n1 = float(verification(n1))

print('-------------------------------------------------------')
n2 = float(input('Now insert the second note (Between 0 and 10).\n'))
if n2 < 0 or n2 > 10:
    n2 = float(verification(n2))

print('-------------------------------------------------------')
n3 = float(input('And, finally, insert the third note (Between 0 and 10).\n'))
if n3 < 0 or n3 > 10:
    n3 = float(verification(n3))

status()

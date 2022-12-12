# final-exam-calulator
A small program using pyweb.io to calculate final exam marks

This project uses the py-web library to generate an address, then the user inputs his current mark for the course, the weight of his exam and his desired final grade.
The calculator then calculates the required amount needed on the final exam to achieve the required grade.
The program also displays a message depending on the grade required grade, for example if the percent required is over 100 it makes the user aware of it being
impossible to achieve.

The formula for caclulating the grade is
required grade = ((goal grade - current grade) * (0.01 * (100 - final exam weight))) / final exam weight weight) * 100

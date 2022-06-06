import pywebio
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table


def final():
    curr = input("Your current grade for your course：", type=FLOAT)
    goal = input("Your desired grade：", type=FLOAT)
    weight = input("The weight of your final is：", type=FLOAT)

    req = ((goal - curr * (0.01 * (100 - weight))) / weight) * 100

    top_status = [(50, 'Easy to achieve'),
                  (60, 'Not hard to achieve'),
                  (70, 'Moderately difficult to achieve'),
                  (80, 'Difficult to achieve'), (90, 'Start Studying!'),
                  (100, 'Perfection is required!'),
                  (float('inf'), 'Impossible to achieve, my condolences')]



    for top, status in top_status:
           if req <= top:
            put_markdown('# **Results**')
            put_text('Your grade: %.1f' % (curr))
            put_markdown('Your desired grade: %.1f' % (goal))
            put_text('Weight of the exam is: %.1f' % (weight))
            put_markdown('You need to achieve a grade of: %.1f' % (req))
            put_text('%s' % (status))
            put_html('<hr>')


            break

if __name__ == '__main__':
    pywebio.start_server(final, port=55)

            

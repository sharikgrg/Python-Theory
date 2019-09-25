## Stupid School Teacher
#Create a program to have a conversation with your teacher. This is how he reacts to your responses
# if you responde to your school teacher:
    # Go back to school!
# if you ask a questions
    # HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!
# if your respond with something ending with !
    # YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!
# if your response is 'I'm a doctor'
    # WELLL DONE! YOU can now talk to me
    # Exit
student = ''
answer1 = "I'm a doctor"
answer2 = str('')
while student != answer1.lower():
    student = input("what's up?? ")
    if student.find('?') != -1:
        print('HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!')
    elif student.find('!') != -1:
        print('YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!')
    elif student == answer1.lower():
        print('WELLL DONE! YOU can now talk to me')
        break
    elif type(student) == str:
        print('Go back to school!')


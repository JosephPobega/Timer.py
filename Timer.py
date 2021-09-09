import time
import random
import win10toast


def timer():
    toast = win10toast.ToastNotifier()

    ############# USER INPUT FOR STARTUP ####################

    question1 = input("what would you like to be reminded about?")
    question2 = (input("minutes, seconds, or hours?"))

    rare_meter = random.randint(0, 500)

    ############# LISTS FOR RESPONSES #######################

    responses = ['Alright, I will remind you in', 'OK, you will be reminded of ' + str(question1) + ' in']
    rare_responses = ['WOW, you got a rare response! Anyways, you will be reminded of ' + str(question1) + ' in']

    ############# IF STATEMENTS/CHOICES #####################

    if question2 == 'minutes'.lower():
        question3 = int(input("how many minutes?"))
        if rare_meter < 499:
            print(random.choice(responses))
        if rare_meter > 499:
            print(random.choice(rare_responses))
        print(str(question3) + ' minute(s)')
        time.sleep(question3 * 60)

    if question2 == 'seconds'.lower():
        question4 = int(input('how many seconds?'))
        if rare_meter < 499:
            print(random.choice(responses))
        if rare_meter > 499:
            print(random.choice(rare_responses))
        print(str(question4) + ' second(s)')
        time.sleep(question4)

    if question2 == 'hours'.lower():
        question5 = int(input('how many hours?'))
        if rare_meter < 499:
            print(random.choice(responses))
        if rare_meter > 499:
            print(random.choice(rare_responses))
        print(str(question5) + ' hour(s)')
        time.sleep(question5 * 3600)

    #####################################################


    toast.show_toast(question1)


timer()

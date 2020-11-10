import datetime
from datetime import datetime

from extentions.funcs import speak


def schedule():
    day_ = datetime.now()
    day = day_.strftime("%A")
    time = datetime.now()
    time_h = time.strftime("%H")
    time_m = time.strftime("%M")

    if day == 'Sunday':
        if time_h == '08':
            if int(time_m) in range(30, 60):
                speak("You have Sport class right now. ")

        elif time_h == '09':
            if int(time_m) in range(0, 15):
                speak("You have Sport class right now. ")

            elif int(time_m) in range (15, 60):
                speak("You have שלח class right now. ")

        elif time_h == '10':
            if int(time_m) in range(0, 10):
                speak("You have שלח class right now. ")

            elif int(time_m) in range(10, 55):
                speak('You have History class right now. ')

        elif time_h == '11':
            if int(time_m) in range(0, 45):
                speak('You have History class right now. ')

            elif int(time_m) in range(45, 60):
                speak('You have English class right now. ')

        elif time_h == '12':
            if int(time_m) in range(0, 30):
                speak('You have English class right now. ')

            elif int(time_m) in range(31, 60):
                speak('You have English class right now. ')
        elif time_h == '13':
            if int(time_m) in range(0, 30):
                speak('You have English class right now. ')

            elif int(time_m) in range(31, 60):
                speak('You have Theater class right now. ')

        elif time_h == '14':
            if int(time_m) in range(0, 20):
                speak('You have Theater class right now. ')

        else:
            speak('You have nothing left for today... ')


    elif day == 'Monday':
        if time_h == '08':
            if int(time_m) in range(30, 60):
                speak("You have Hebrew class right now. ")

        elif time_h == '09':
            if int(time_m) in range(0, 15):
                speak("You have Hebrew class right now. ")

            elif int(time_m) in range(15, 60):
                speak("You have Hebrew class right now. ")

        elif time_h == '10':
            if int(time_m) in range(0, 10):
                speak("You have Hebrew class right now. ")

            elif int(time_m) in range(10, 55):
                speak("You have Life Lesson class right now. ")

        elif time_h == '11':
            if int(time_m) in range(0, 45):
                speak('You have תהך class right now. ')

            elif int(time_m) in range(45, 60):
                speak('You have History class right now. ')

        elif time_h == '12':
            if int(time_m) in range(0, 30):
                speak('You have History class right now. ')

            elif int(time_m) in range(31, 60):
                speak('You have free time right now. ')

        elif time_h == '13':
            if int(time_m) in range(0, 30):
                speak('You have free time right now. ')

            elif int(time_m) in range(31, 60):
                speak('You have Diplomacy class right now. ')

        elif time_h == '14':
            if int(time_m) in range(0, 60):
                speak('You have Diplomacy class right now. ')

        elif time_h == '13':
            if int(time_m) in range(0, 10):
                speak('You have Diplomacy class right now. ')

        else:
            speak('You have nothing left for today... ')


    elif day == 'Tuesday':
        if time_h == '08':
            if int(time_m) in range(30, 60):
                speak("You have English class right now. ")

        elif time_h == '09':
            if int(time_m) in range(0, 15):
                speak("You have English class right now. ")

            elif int(time_m) in range(15, 60):
                speak("You have English class right now. ")

        elif time_h == '10':
            if int(time_m) in range(0, 10):
                speak("You have English class right now. ")

            elif int(time_m) in range(10, 55):
                speak('You have Sport class right now. ')

        elif time_h == '11':
            if int(time_m) in range(0, 45):
                speak('You have Chemistry class right now. ')

            elif int(time_m) in range(45, 60):
                speak('You have Chemistry class right now. ')

        elif time_h == '12':
            if int(time_m) in range(0, 30):
                speak('You have Chemistry class right now. ')

        else:
            speak('You have nothing left for today... ')


    elif day == 'Wednesday':
        if time_h == '08':
            if int(time_m) in range(30, 60):
                speak("You have Math class right now. ")

        elif time_h == '09':
            if int(time_m) in range(0, 15):
                speak("You have Math class right now. ")

            elif int(time_m) in range(15, 60):
                speak("You have Math class right now. ")

        elif time_h == '10':
            if int(time_m) in range(0, 10):
                speak("You have math class right now. ")

            elif int(time_m) in range(10, 55):
                speak("You have free time right now. ")

        elif time_h == '11':
            if int(time_m) in range(0, 45):
                speak('You have Traffic class right now. ')

            elif int(time_m) in range(45, 60):
                speak('You have תנך class right now. ')

        elif time_h == '12':
            if int(time_m) in range(0, 30):
                speak('You have תנך class right now. ')

            elif int(time_m) in range(31, 60):
                speak('You have Hebrew class right now. ')
        elif time_h == '13':
            if int(time_m) in range(0, 30):
                speak('You have Hebrew time right now. ')

            elif int(time_m) in range(31, 60):
                speak('You have תנך class right now. ')

        elif time_h == '14':
            if int(time_m) in range(0, 20):
                speak('You have תנך class right now. ')
            elif int(time_m) in  range(21, 60):
                speak('You have Hebrew time right now. ')

        else:
            speak('You have nothing left for today... ')


    elif day == 'Thursday':
        if time_h == '09':
            if int(time_m) in range(15, 60):
                speak("You have Math class right now. ")

        elif time_h == '10':
            if int(time_m) in range(0, 10):
                speak("You have Math class right now. ")

            elif int(time_m) in range(10, 55):
                speak('You have Math class right now. ')

        elif time_h == '11':
            if int(time_m) in range(0, 45):
                speak('You have English class right now. ')

            elif int(time_m) in range(45, 60):
                speak('You have Islamic Culture class right now. ')

        elif time_h == '12':
            if int(time_m) in range(0, 30):
                speak('You have Islamic Culture class right now. ')

        else:
            speak('You have nothing left for today... ')


    elif day == 'Friday':
        if time_h == '08':
            if int(time_m) in range(30, 60):
                speak("You have Theater class right now. ")

        elif time_h == '09':
            if int(time_m) in range(0, 15):
                speak("You have Theater class right now. ")

            elif int(time_m) in range(15, 60):
                speak("You have Theater class right now. ")

        elif time_h == '10':
            if int(time_m) in range(0, 10):
                speak("You have Theater class right now. ")

            elif int(time_m) in range(10, 55):
                speak('You have Theater class right now. ')

        elif time_h == '11':
            if int(time_m) in range(0, 45):
                speak('You have History class right now. ')

            elif int(time_m) in range(45, 60):
                speak('You have Life Lesson class right now. ')

        elif time_h == '12':
            if int(time_m) in range(0, 30):
                speak('You have Life Lesson class right now. ')

        else:
            speak('You have nothing left for today... ')

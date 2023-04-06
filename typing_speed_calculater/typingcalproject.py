# ***************Typing Speed Calculater project ************
from time import *
import random as r
print(time())


def Error_check(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i]!=usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput)/time_R
    return round(speed)
if __name__=='__main__':

    while True:
        ck = input("Ready to test: yes / no ")
        if ck == "Yes":
            test = ["This practice lesson consists of short paragraphs about interesting subjects. Find fun keyboard typing practice and learn something new!",
                "Our paragraph practice is great typing practice for writing essays, reports, emails, and more for school and work.","Welcome to the world"]

            test1 = r.choice(test)
            print("******typing speed *********")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter input  ")
            time_2 = time()

            print("Speed: ", speed_time(time_1,time_2,testinput), "w/sec")
            print("Error: ", Error_check(test1, testinput))
        elif ck == "No":
            print("Thank you")
            break
        else:
            print("Wrong input")



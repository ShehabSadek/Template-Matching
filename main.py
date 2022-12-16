from Globals import *
import part1 
import part2 
import part3
import combined

while(True):
    print("1){}".format('Roation'),"\n2){}".format('Scale'),"\n3){}".format('Multi'),"\n4){}".format('All combined'),"\n5){}".format('Exit'))
    choice = input("Pick desired option: ")
    if(choice=='1'):
        part1.run()
    elif(choice=='2'):
        part2.run()
    elif(choice=='3'):
        choice2 = input("press\n1) Multiple match test \n2) For empty image test: ")
        if(choice2=='1'):
            part3.run(1)
        elif(choice2=='2'):
            part3.run(2)
        else:
            continue
    elif(choice=='4'):
        combined.run()
    elif(choice=='5'):
        break
    else:
        print("INVALID INPUT !")

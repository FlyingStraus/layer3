from utils.libs import *
from utils.init import *
from utils.interaction import * 
from utils.tasks import * 


if __name__ == '__main__':

    with open('wallets.txt') as f:
        wallets = f.readlines()

    for i in range(len(wallets)):
        wallets[i] = wallets[i].split('\n')[0]

        if wallets[i][0] == '0' and wallets[i][1] == 'x':
            wallets[i] = wallets[i].split('0x')[1]


    print(f"Ready to work with - {len(wallets)}") 
    print(wallets)
    print("Choose Task")
    # print(TASKS_list['1'])
    for i in range(1,len(TASKS_list)+1):
        print(f"{i}) {TASKS_list[f'{i}']}")
    task_todo = int(input("Your choise: "))

    for wallet in wallets:
        if task_todo == 1:
            lol = Tasks(wallet)
            lol.polygon_testnet()
        print("Done")
        input("Next?")



    

    
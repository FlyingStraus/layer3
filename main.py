from utils.libs import *
from utils.init import *
from utils.interaction import * 
from utils.tasks import * 

# TODO: add stat problem, all of them are the same  "-1":"Get stat",


def task_helper(lol,todo_task):
    if todo_task == -1:
        lol.get_stat()
    elif todo_task == -2:
        lol.gm_press()
    elif todo_task == 1:
        lol.polygon_testnet()
    elif todo_task == 2:
        lol.understanding_modular_blockchains()
    elif todo_task == 3:
        lol.honeypot_scams()
    


if __name__ == '__main__':

    print("Hallo, this version of code is made specifically for Kingsman DAO\nDo not share this file with others\n\nComments, ideas - @Straus_fm")

    with open('wallets.txt') as f:
        wallets = f.readlines()

    for i in range(len(wallets)):
        wallets[i] = wallets[i].split('\n')[0]

        if wallets[i][0] == '0' and wallets[i][1] == 'x':
            wallets[i] = wallets[i].split('0x')[1]
    
    try:
        with open('proxy.txt') as f:
            proxies = f.readlines()

        for i in range(len(proxies)):
            proxies[i] = proxies[i].split('\n')[0]
        print(f"Proxies num - {len(proxies)}") 

        i=0
        proxies_base_len = len(proxies)
        while len(proxies) < len(wallets):
            proxies.append(proxies[i])
            i+=1
            if i >= proxies_base_len:
                i=0

        print(f"Proxies num extendent - {len(proxies)}") 
    except:
        proxies = None
        print("No proxies found")


    print(f"Wallets num - {len(wallets)}") 
    print("Choose Task")

    for key, value in TASKS_list.items():
        print(f"{key}) {value}")

    task_todo = int(input("Your choise: "))

    if proxies is not None:
        for i in range(len(wallets)):
            print(f"Duin - {wallets[i]} - {proxies[i]}")
            lol = Tasks(wallets[i],proxies[i])
            task_helper(lol,task_todo)
    else:
        for i in range(len(wallets)):
            print(f"Duin - {wallets[i]}")
            lol = Tasks(wallets[i])
            task_helper(lol,task_todo)           



    

    
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
    # print(TASKS_list['1'])
    for i in range(1,len(TASKS_list)+1):
        print(f"{i}) {TASKS_list[f'{i}']}")
    task_todo = int(input("Your choise: "))

    if proxies is not None:
        for i in range(len(wallets)):
            print(f"Duin - {wallets[i]} - {proxies[i]}")
            if task_todo == 1:
                lol = Tasks(wallets[i],proxies[i])
                lol.polygon_testnet()
            print("Done")
            # input("Next?")
    else:
        for i in range(len(wallets)):
            print(f"Duin - {wallets[i]}")
            if task_todo == 1:
                lol = Tasks(wallets[i])
                lol.polygon_testnet()
            print("Done")
            # input("Next?")



    

    
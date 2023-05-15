from utils.libs import *
from utils.init import *
# from utils.interaction import * 


if __name__ == '__main__':

    with open('wallets.txt') as f:
        wallets = f.readlines()

    for wallet in wallets:
        wallet = wallet.split('\n')


    print(f"Ready to work with - {len(wallets)}") 
    print("Choose Task")
    # print(TASKS_list['1'])
    for i in range(1,len(TASKS_list)+1):
        print(f"{i}) {TASKS_list[f'{i}']}")
    # task_todo = int(input("Your choise: "))

    

    
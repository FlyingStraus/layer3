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
    elif todo_task == 4:
        lol.a_brief_history_of_crypto()
    elif todo_task == 5:
        lol.celo_quest()
    elif todo_task == 6:
        lol.what_is_refi()
    elif todo_task == 7:
        lol.a_beginners_guide_to_crypto_insurance()
    elif todo_task == 8:
        lol.the_importance_of_audits()   
    elif todo_task == 9:
        lol.an_introduction_to_quickswap_gaminghub()
    elif todo_task == 10:
        lol.introduction_to_ordinals()
    elif todo_task == 11:
        lol.brian_armstrong()
    elif todo_task == 12:
        lol.on_chain_sleuth()
    elif todo_task == 13:
        lol.introduction_to_polkadot()
    elif todo_task == 14:
        lol.the_rise_of_bitcoins_layer_2_lightning()
    elif todo_task == 15:
        lol.bitcoin_in_everyday_life_practical_use_cases_and_applications()
    elif todo_task == 16:
        lol.a_deep_dive_into_bitcoins_taproot_and_schnorr_signatures()
    elif todo_task == 17:
        lol.the_genesis_of_bitcoin_a_historical_overview()
    elif todo_task == 18:
        lol.what_are_layer2s()
    elif todo_task == 19:
        lol.what_are_wallets_in_web3()
    elif todo_task == 20:
        lol.what_are_erc_tokens()
    elif todo_task == 21:
        lol.ethereum_is_a_dark_forest()
    elif todo_task == 22:
        lol.consensus_algorithms()
    elif todo_task == 23:
        lol.an_introduction_to_podcast_nfts()
    elif todo_task == 24:
        lol.voting_on_chain_with_snapshot()
    elif todo_task == 25:
        lol.a_beginners_guide_to_rpc_in_crypto()
    elif todo_task == 26:
        lol.a_beginners_guide_to_music_nfts()
    elif todo_task == 27:
        lol.introduction_to_orb_app_on_lens_protocol()
    elif todo_task == 28:
        lol.launch_with_layer3()
    elif todo_task == 29:
        lol.uniswap_nft_marketplace()
    elif todo_task == 30:
        lol.uniswap_mobile_wallet()
    elif todo_task == 31:
        lol.how_to_send_an_on_chain_message()
    elif todo_task == 32:
        lol.how_to_create_a_smart_contract()
    elif todo_task == 33:
        lol.running_your_node()
    elif todo_task == 34:
        lol.minting_and_creating_nfts()
    elif todo_task == 35:
        lol.nft_gaming()
    elif todo_task == 36:
        lol.defi_x_nfts()
    elif todo_task == 37:
        lol.exploring_the_new_ethereum_roadmap()
    elif todo_task == 38:
        lol.nft_security()
    elif todo_task == 39:
        lol.malicious_seaport_signatures()
    elif todo_task == 40:
        lol.get_started_with_layer3()
    elif todo_task == 41:
        lol.crypto_safety_part_ii_understanding_cold_and_hot_wallets()
    elif todo_task == 42:
        lol.introduction_to_axelscore()
    elif todo_task == 43:
        lol.fractionalized_nft()
    elif todo_task == 44:
        lol.introduction_to_daos()
    elif todo_task == 45:
        lol.the_history_of_makerdao()
    elif todo_task == 46:
        lol.sandeep_nailwal()
    elif todo_task == 47:
        lol.welcome_to_polygon()
    elif todo_task == 48:
        lol.get_started_on_polygon()
    elif todo_task == 49:
        lol.lvl_5_chest()

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

    if task_todo == -5:
        arr = range(1,len(TASKS_list)-1)
        for task_todo in arr:
            if proxies is not None:
                for i in range(len(wallets)):
                    # print(f"Duin - {wallets[i]}")
                    lol = Tasks(wallets[i])
                    task_helper(lol,task_todo)
            else:
                for i in range(len(wallets)):
                    # print(f"Duin - {wallets[i]} - {proxies[i]}")
                    lol = Tasks(wallets[i],proxies[i])
                    task_helper(lol,task_todo)


    if proxies is not None:
        for i in range(len(wallets)):
            # print(f"Duin - {wallets[i]} - {proxies[i]}")
            lol = Tasks(wallets[i],proxies[i])
            task_helper(lol,task_todo)
    else:
        for i in range(len(wallets)):
            # print(f"Duin - {wallets[i]}")
            lol = Tasks(wallets[i])
            task_helper(lol,task_todo)           



    

    
from utils.libs import *
from utils.interaction import *
from utils.init import *

class Tasks():
    def __init__(self, private_key, assecc_token=None, proxy=None):
        self.private_key = private_key
        self.assecc_token = assecc_token
        self.proxy = proxy

    def get_stat(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid, public = wallet.login()            
                    # https://layer3.xyz/api/trpc/user.getXpDataForUser?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22userId%22%3A{89660  0}%7D%7D%7D
            url = f"https://layer3.xyz/api/trpc/config.globalAnnouncement,user.getXpDataForUser,gm.getGmStreakForUser,achievement.achievementsByUser,task.getClaimedTasksForUser,user.profile,task.getNumberOfClaimedTasksForUser,userNft.getNumberOfUserNfts,user.me?batch=1&input=%7B%220%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%2C%221%22%3A%7B%22json%22%3A%7B%22userId%22%3A{walletid}%7D%7D%2C%222%22%3A%7B%22json%22%3A%7B%22userId%22%3A{walletid}%7D%7D%2C%223%22%3A%7B%22json%22%3A%7B%22userId%22%3A{walletid}%7D%7D%2C%224%22%3A%7B%22json%22%3A%7B%22userId%22%3A{walletid}%2C%22cursor%22%3Anull%7D%2C%22meta%22%3A%7B%22values%22%3A%7B%22cursor%22%3A%5B%22undefined%22%5D%7D%7D%7D%2C%225%22%3A%7B%22json%22%3A%7B%22identifier%22%3A%22{public}%22%7D%7D%2C%226%22%3A%7B%22json%22%3A%7B%22userId%22%3A{walletid}%7D%7D%2C%227%22%3A%7B%22json%22%3A%7B%22userId%22%3A{walletid}%7D%7D%2C%228%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D"
            # print(url)
            text = wallet.get_sendAnyRequest(url = url)
            # print(text)
            data = json.loads(json.dumps(eval((text).replace("null", "None").replace("false", "False").replace("true", "True"))))[1]
            xp = data["result"]["data"]["json"]["xp"]
            lvl = data["result"]["data"]["json"]["level"]
            print(f"{public} - Xp - {xp} - level - {lvl} - {walletid}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def gm_press(self):
        wallet = layer3(self.private_key, self.proxy)
        try:
            walletid, public = wallet.login()
            wallet.post_sendAnyRequest(url = 'https://layer3.xyz/api/trpc/gm.addGm?batch=1', data = {"0":{"json":{"timezoneOffset":-180,"markXpActivityAsSeen":True}}})
            print(f"{public} - pressed gm buutton")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    
    def polygon_testnet(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid, public = wallet.login()
            wallet.bountyStep(id = 2591)
            wallet.bountyStep(id = 2605, userAddressId = 1)
            wallet.bountyClaim(id = 1793)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")
    
    def understanding_modular_blockchains(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2620,userAddressId =1)
            wallet.bountyStep(id = 2624, userAddressId = 1)
            wallet.bountyStep(data = {"0":{"json":{"bountyStepId":3316,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1803)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def honeypot_scams(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            # wallet.get_sendAnyRequest(url = "https://layer3.xyz/api/trpc/bountyStep.stepsWithCompletion?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22taskId%22%3A1856%7D%7D%7D")
            wallet.bountyStep(id = 2504)
            wallet.bountyStep(id = 2585)
            # gm
            wallet.post_sendAnyRequest(url = 'https://layer3.xyz/api/trpc/gm.addGm?batch=1', data = {"0":{"json":{"timezoneOffset":-180,"markXpActivityAsSeen":True}}})
            wallet.bountyStep(id = 2586)
            wallet.bountyStep(data = {"0":{"json":{"bountyStepId":3312,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":None},"meta":{"values":{"userAddressId":["undefined"]}}}})
            wallet.bountyClaim(id = 1780)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def a_brief_history_of_crypto(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2918)
            wallet.bountyStep(id = 2919)
            wallet.bountyStep(id = 2920)
            wallet.bountyStep(id = 2921)
            wallet.bountyClaim(id = 1856)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def celo_quest(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2911)
            wallet.bountyStep(id = 2917)
            wallet.bountyClaim(id = 1854)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")
    
    def what_is_refi(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2913)
            wallet.bountyStep(id = 2948)
            wallet.bountyStep(id = 2914)
            wallet.bountyClaim(id = 1855)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def a_beginners_guide_to_crypto_insurance(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2945)
            wallet.bountyStep(id = 2946)
            wallet.bountyStep(id = 2947)
            wallet.bountyClaim(id = 1861)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")
    
    def the_importance_of_audits(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3025)
            wallet.bountyStep(id = 3026)
            wallet.bountyStep(data = {"0":{"json":{"bountyStepId":3309,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1876)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def an_introduction_to_quickswap_gaminghub(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3093, userAddressId = walletid)
            wallet.bountyStep(data = {"0":{"json":{"bountyStepId":3096,"inputData":{"answers":[{"questionUuid":"q3","text":"Minecraft"}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1892)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")
    
    def introduction_to_ordinals(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3505, userAddressId = walletid)
            wallet.bountyStep(id = 3206, userAddressId = walletid)
            wallet.bountyStep(id = 3506, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3277,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1924)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def brian_armstrong(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            options = "stocks", "application", "mew"
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3551, userAddressId = walletid)
            wallet.bountyStep(id = 3552, userAddressId = walletid)
            wallet.bountyStep(id = 3506, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3747,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a2"]},{"questionUuid":"q3","text":random.choice(options)}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1986)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def on_chain_sleuth(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3862, userAddressId = walletid)
            wallet.bountyStep(id = 3899, userAddressId = walletid)
            wallet.bountyStep(id = 3900, userAddressId = walletid)
            wallet.bountyStep(id = 3901, userAddressId = walletid)
            wallet.bountyClaim(id = 2047)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def introduction_to_polkadot(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 4006, userAddressId = walletid)
            wallet.bountyStep(id = 4007, userAddressId = walletid)
            wallet.bountyStep(id = 4008, userAddressId = walletid)
            wallet.bountyClaim(id = 2069)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}")

    def the_rise_of_bitcoins_layer_2_lightning(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3642, userAddressId = walletid)
            wallet.bountyStep(id = 3641, userAddressId = walletid)
            wallet.bountyClaim(id = 1998)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 

    def bitcoin_in_everyday_life_practical_use_cases_and_applications(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3643, userAddressId = walletid)
            wallet.bountyStep(id = 3644, userAddressId = walletid)
            wallet.bountyClaim(id = 1999)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 

    def a_deep_dive_into_bitcoins_taproot_and_schnorr_signatures(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3645, userAddressId = walletid)
            wallet.bountyStep(id = 3646, userAddressId = walletid)
            wallet.bountyClaim(id = 2000)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 

    def the_genesis_of_bitcoin_a_historical_overview(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3639, userAddressId = walletid)
            wallet.bountyStep(id = 3640, userAddressId = walletid)
            wallet.bountyClaim(id = 1997)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 

    def what_are_layer2s(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3696, userAddressId = walletid)
            wallet.bountyStep(id = 3703, userAddressId = walletid)
            wallet.bountyStep(id = 3704, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3736,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a2"]},{"questionUuid":"105346df-8add-48ff-ba85-0767f67abdae","selectedChoices":["d2c541b2-01d9-4eab-a21c-681771a2c57b"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 2011)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 

    def what_are_wallets_in_web3(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3699, userAddressId = walletid)
            wallet.bountyStep(id = 3700, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3738,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a4"]},{"questionUuid":"105346df-8add-48ff-ba85-0767f67abdae","selectedChoices":["d2c541b2-01d9-4eab-a21c-681771a2c57b"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 2009)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 

    def what_are_erc_tokens(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3698, userAddressId = walletid)
            wallet.bountyStep(id = 3701, userAddressId = walletid)
            wallet.bountyStep(id = 3702, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3737,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["94443a83-46c4-4bdd-9bce-6a817bff1f22"]},{"questionUuid":"105346df-8add-48ff-ba85-0767f67abdae","selectedChoices":["d2c541b2-01d9-4eab-a21c-681771a2c57b"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 2010)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def ethereum_is_a_dark_forest(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3918, userAddressId = walletid)
            wallet.bountyStep(id = 3920, userAddressId = walletid)
            wallet.bountyClaim(id = 2055)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def consensus_algorithms(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3932, userAddressId = walletid)
            wallet.bountyStep(id = 3934, userAddressId = walletid)
            wallet.bountyStep(id = 3936, userAddressId = walletid)
            wallet.bountyClaim(id = 2058)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def an_introduction_to_podcast_nfts(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3463, userAddressId = walletid)
            wallet.bountyStep(id = 3464, userAddressId = walletid)
            wallet.bountyStep(id = 3465, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3580,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1967)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def voting_on_chain_with_snapshot(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3137, userAddressId = walletid)
            wallet.bountyStep(id = 3563, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3564,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1906)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def a_beginners_guide_to_rpc_in_crypto(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3857, userAddressId = walletid)
            wallet.bountyStep(id = 3858, userAddressId = walletid)
            wallet.bountyStep(id = 3888, userAddressId = walletid)
            wallet.bountyStep(id = 3889, userAddressId = walletid)
            wallet.bountyClaim(id = 2045)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def a_beginners_guide_to_music_nfts(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3863, userAddressId = walletid)
            wallet.bountyStep(id = 3865, userAddressId = walletid)
            wallet.bountyClaim(id = 2048)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def introduction_to_orb_app_on_lens_protocol(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3859, userAddressId = walletid)
            wallet.bountyStep(id = 3883, userAddressId = walletid)
            wallet.bountyStep(id = 3884, userAddressId = walletid)
            wallet.bountyClaim(id = 2046)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def launch_with_layer3(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2826, userAddressId = walletid)
            wallet.bountyStep(id = 2836, userAddressId = walletid)
            wallet.bountyStep(id = 2837, userAddressId = walletid)
            wallet.bountyClaim(id = 1838)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def uniswap_nft_marketplace(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3111, userAddressId = walletid)
            wallet.bountyStep(id = 3117, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3554,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1898)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def uniswap_mobile_wallet(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3112, userAddressId = walletid)
            wallet.bountyStep(id = 3119, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3360,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1899)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def how_to_send_an_on_chain_message(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3542, userAddressId = walletid)
            wallet.bountyStep(id = 3543, userAddressId = walletid)
            wallet.bountyStep(id = 3544, userAddressId = walletid)
            wallet.bountyStep(id = 3545, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3576,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1984)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def how_to_create_a_smart_contract(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3539, userAddressId = walletid)
            wallet.bountyStep(id = 3540, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3541,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1983)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def running_your_node(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3535, userAddressId = walletid)
            wallet.bountyStep(id = 3537, userAddressId = walletid)
            wallet.bountyStep(id = 3538, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3577,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1982)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def minting_and_creating_nfts(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3294, userAddressId = walletid)
            wallet.bountyStep(id = 3295, userAddressId = walletid)
            wallet.bountyStep(id = 3296, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3298,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1941)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def nft_gaming(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3274, userAddressId = walletid)
            wallet.bountyStep(id = 3281, userAddressId = walletid)
            wallet.bountyStep(id = 3283, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3297,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1938)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def defi_x_nfts(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3284, userAddressId = walletid)
            wallet.bountyStep(id = 3293, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3299,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1939)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def exploring_the_new_ethereum_roadmap(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2507, userAddressId = walletid)
            wallet.bountyStep(id = 2647, userAddressId = walletid)
            wallet.bountyStep(id = 2648, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":2652,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a4"]},{"questionUuid":"q2","selectedChoices":["a1"]},{"questionUuid":"f5d948ce-ba9f-490f-af88-20d206204a4a","selectedChoices":["b7e85c1f-2d11-41e4-bc84-4e684aeb5a54"]}]},"userAddressId":walletid}}})
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3315,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1785)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def nft_security(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2568, userAddressId = walletid)
            wallet.bountyStep(id = 2595, userAddressId = walletid)
            wallet.bountyStep(id = 2596, userAddressId = walletid)
            wallet.bountyStep(id = 2597, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3311,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1787)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def malicious_seaport_signatures(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2502, userAddressId = walletid)
            wallet.bountyStep(id = 2565, userAddressId = walletid)
            wallet.bountyStep(id = 2714, userAddressId = walletid)
            wallet.bountyStep(id = 2566, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3306,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1778)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def get_started_with_layer3(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2687, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":2514,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a1"]},{"questionUuid":"q2","selectedChoices":["a1","a3","a2","a4"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1774)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def crypto_safety_part_ii_understanding_cold_and_hot_wallets(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 2501, userAddressId = walletid)
            wallet.bountyStep(id = 2556, userAddressId = walletid)
            wallet.bountyStep(id = 2753, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3307,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a1"]},{"questionUuid":"q2","selectedChoices":["a1","a3","a2","a4"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1777)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def introduction_to_axelscore(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 4258, userAddressId = walletid)
            wallet.bountyStep(id = 4396, userAddressId = walletid)
            wallet.bountyStep(id = 4259, userAddressId = walletid)
            wallet.bountyClaim(id = 2125)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def fractionalized_nft(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3273, userAddressId = walletid)
            wallet.bountyStep(id = 3279, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3300,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a1"]},{"questionUuid":"q2","selectedChoices":["a1","a3","a2","a4"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1937)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def introduction_to_daos(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3134, userAddressId = walletid)
            wallet.bountyStep(id = 3458, userAddressId = walletid)
            wallet.bountyStep(id = 3460, userAddressId = walletid)
            wallet.bountyClaim(id = 1903)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def the_history_of_makerdao(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3523, userAddressId = walletid)
            wallet.bountyStep(id = 3524, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3565,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a1"]},{"questionUuid":"q2","selectedChoices":["a1","a3","a2","a4"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1980)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def sandeep_nailwal(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3559, userAddressId = walletid)
            wallet.bountyStep(id = 3560, userAddressId = walletid)
            wallet.bountyStep(id = 3561, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3573,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a1"]},{"questionUuid":"q2","selectedChoices":["a1","a3","a2","a4"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1988)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def welcome_to_polygon(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 3182, userAddressId = walletid)
            wallet.bountyStep(id = 3183, userAddressId = walletid)
            wallet.bountyStep(id = 3185, userAddressId = walletid)
            wallet.bountyStep(id = 3186, userAddressId = walletid)
            wallet.bountyStep(data ={"0":{"json":{"bountyStepId":3304,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a1"]},{"questionUuid":"q2","selectedChoices":["a1","a3","a2","a4"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1916)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def get_started_on_polygon(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            wallet.bountyStep(id = 919, userAddressId = walletid)
            wallet.bountyStep(id = 953, userAddressId = walletid)
            wallet.bountyClaim(id = 769)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
    def lvl_5_chest(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid,public = wallet.login()
            
            wallet.post_sendAnyRequest(url = 'https://layer3.xyz/api/trpc/gm.addGm?batch=1', data = {"0":{"json":{"timezoneOffset":-180,"markXpActivityAsSeen":True}}})
            wallet.bountyStep(id = 4175, userAddressId = walletid)
            wallet.bountyClaim(id = 2109)
            print(f"DOne with wallet - {public}")
        except Exception as e:
            print(f"Failed to interact in wallet {public} Err - {e}") 
    
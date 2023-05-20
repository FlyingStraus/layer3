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
            print(f"{self.private_key} - Xp - {xp} - level - {lvl} - {walletid}")
        except Exception as e:
            print(f"Failed to interact in wallet {self.private_key} Err - {e}")

    def gm_press(self):
        wallet = layer3(self.private_key, self.proxy)
        try:
            walletid, public = wallet.login()
            wallet.post_sendAnyRequest(url = 'https://layer3.xyz/api/trpc/gm.addGm?batch=1', data = {"0":{"json":{"timezoneOffset":-180,"markXpActivityAsSeen":True}}})
            print(f"{public} - pressed gm buutton")
        except Exception as e:
            print(f"Failed to interact in wallet {self.private_key} Err - {e}")

    
    def polygon_testnet(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            wallet.login()
            wallet.bountyStep(id = 2591)
            wallet.bountyStep(id = 2605, userAddressId = 1)
            wallet.bountyClaim(id = 1793)
            print(f"DOne with wallet - {self.private_key}")
        except Exception as e:
            print(f"Failed to interact in wallet {self.private_key} Err - {e}")
    
    def understanding_modular_blockchains(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            walletid = wallet.login()
            wallet.bountyStep(id = 2620,userAddressId =1)
            wallet.bountyStep(id = 2624, userAddressId = 1)
            wallet.bountyStep(data = {"0":{"json":{"bountyStepId":3316,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":walletid}}})
            wallet.bountyClaim(id = 1803)
            print(f"DOne with wallet - {self.private_key}")
        except Exception as e:
            print(f"Failed to interact in wallet {self.private_key} Err - {e}")

    def honeypot_scams(self):
        wallet = layer3(self.private_key,self.proxy)
        try:
            wallet.login()
            # wallet.get_sendAnyRequest(url = "https://layer3.xyz/api/trpc/bountyStep.stepsWithCompletion?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22taskId%22%3A1856%7D%7D%7D")
            wallet.bountyStep(id = 2504)
            wallet.bountyStep(id = 2585)
            # gm
            wallet.post_sendAnyRequest(url = 'https://layer3.xyz/api/trpc/gm.addGm?batch=1', data = {"0":{"json":{"timezoneOffset":-180,"markXpActivityAsSeen":True}}})
            wallet.bountyStep(id = 2586)
            wallet.bountyStep(data = {"0":{"json":{"bountyStepId":3312,"inputData":{"answers":[{"questionUuid":"q1","selectedChoices":["a5"]}]},"userAddressId":None},"meta":{"values":{"userAddressId":["undefined"]}}}})
            wallet.bountyClaim(id = 1780)
            print(f"DOne with wallet - {self.private_key}")
        except Exception as e:
            print(f"Failed to interact in wallet {self.private_key} Err - {e}")

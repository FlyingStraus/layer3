from utils.libs import *
from utils.interaction import *
from utils.init import *

class Tasks():
    def __init__(self, private_key, assecc_token=None, proxy=None):
        self.private_key = private_key
        self.assecc_token = assecc_token
        self.proxy = proxy
    
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


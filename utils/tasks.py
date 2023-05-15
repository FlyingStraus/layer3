from utils.libs import *
from utils.interaction import *
from utils.init import *

class Tasks():
    def __init__(self, private_key, assecc_token=None):
        self.private_key = private_key
        self.assecc_token = assecc_token
    
    def polygon_testnet(self):
        wallet = layer3(self.private_key)
        # try:
        wallet.login()
        wallet.bountyStep(id = 2591)
        wallet.bountyStep(id = 2605, userAddressId = 1)
        wallet.bountyClaim(id = 1793)
        print(f"DOne with wallet - {self.private_key}")
        # except Exception as e:
        #     print(f"Failed to interact in wallet {self.private_key} Err - {e}")


from utils.libs import *
from utils.init import *

class layer3():
    def __init__(self,private_key, proxy = None):
        # TODO: Add support proxy
        self.private_key = private_key
        self.public_address =w3.eth.account.from_key(self.private_key).address
        self.assecc_token = None
        self.walletid = None
        self.headers = {"Content-Type": "application/json",
        "referer":"https://layer3.xyz/quests/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "accept-language": "ru-RU,ru;q=0.9",
        }
        # session.headers.update({"Content-Type": "application/json",
        # "referer":"https://layer3.xyz/quests/",
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        # "accept-language": "ru-RU,ru;q=0.9",
        # # "cookie": "_cfuvid=3S5fabJ_P_TK9yw.nsrhxeDgMhVER0miEh39eTr30lE-1684010334723-0-604800000;layer3_access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjMyMjI0OSwiaWF0IjoxNjg0MDcwMjE0LCJleHAiOjE2ODQwNzM4MTR9.rqrUNzxVE_suvhJCsXuWD8sIkGvO0MGmvTSZKY4N8ig;",
        # })

    
    def login(self, connectIntentId="wYVvAk3KQMUBf-QR_2Tpz"):
        
        data = {"0":{"json":{"connectIntentId":connectIntentId,"data":{"buttonName":"MetaMask","device":{"type":"desktop","os":{"name":"Windows","version":"NT 10.0","versionName":"10"},"browser":{"name":"Chrome","version":"113.0.0.0"}}}}}}
        r = session.post("https://layer3.xyz/api/trpc/track.walletModal?batch=1", json=data)
        data = {"0":{"json":None,"meta":{"values":["undefined"]}},"1":{"json":{"connectIntentId":connectIntentId,"data":{"didConnect":True,"walletMetadata":{"walletName":"MetaMask","connectorType":"INJECTED"}}}}}
        r = session.post("https://layer3.xyz/api/trpc/auth.getWalletSignatureNonce,track.walletModal?batch=1", json=data)

        data = r.text.replace("null", "None")
        nonce = json.loads(json.dumps(eval(data)[0]))
        nonce = nonce["result"]["data"]["json"]


        # Signing
        msg = f"Layer3 One-Time Key: {nonce}"
        message = encode_defunct(text=msg)
        signed_message =  w3.eth.account.sign_message(message, private_key=self.private_key).signature.hex()
        
        # logging
        data = {"0":{"json":{"connectIntentId":"wYVvAk3KQMUBf-QR_2Tpz","data":{"didSign":True}}},"1":{"json":{"address":str(self.public_address),"signedMessage":signed_message,"nonce":nonce,"captchaValue":None,"referralCode":None,"walletMetadata":{"walletName":"MetaMask","connectorType":"INJECTED"},"chainId":42161},"meta":{"values":{"captchaValue":["undefined"]}}}}
        r = session.post("https://layer3.xyz/api/trpc/track.walletModal,auth.login?batch=1", json=data)


        result = json.loads(json.dumps(eval((r.text).replace("null", "None").replace("false", "False").replace("true", "True"))))[1]
        self.access_token = result["result"]["data"]["json"]["accessToken"]
        self.walletid = result["result"]["data"]["json"]["user"]["UserAddresses"][0]["id"]

        self.headers = {"Content-Type": "application/json",
        "referer":"https://layer3.xyz/quests/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "accept-language": "ru-RU,ru;q=0.9",
        "cookie": f"layer3_access_token={self.access_token};",
        }
        return self.walletid
    
    def bountyStep(self, id, inputData = None, userAddressId = None):
        if userAddressId:
            data = {"0":{"json":{"bountyStepId":id,"inputData":None,"userAddressId":self.walletid},"meta":{"values":{"inputData":["undefined"]}}}}

        else:
            data = {"0":{"json":{"bountyStepId":id,"inputData":inputData,"userAddressId":userAddressId},"meta":{"values":{"inputData":["undefined"],"userAddressId":["undefined"]}}}}
        r = session.post("https://layer3.xyz/api/trpc/bountyStep.completeBountyStep?batch=1", json=data, headers = self.headers)

        if r.status_code != 200:
            print(f"Problem step in - {self.public_address} - {r.text}")
            return 0
        return 1

    def bountyClaim(self, id):

        data = {"0":{"json":{"taskId":id}}}

        r = session.post("https://layer3.xyz/api/trpc/bountyClaim.claimTask?batch=1", json=data, headers = self.headers)
        if r.status_code != 200:
            print(f"Problem cliam in - {self.public_address} - {r.text}")
            return 0
        return 1
            






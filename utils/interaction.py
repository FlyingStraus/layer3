from utils.libs import *
from utils.init import *

class layer3():
    def __init__(self,private_key, proxy = None):
        # TODO: Add support proxy
        self.private_key = private_key
        self.public_address =w3.eth.account.from_key(self.private_key).address
        self.assecc_token = None
        self.walletid = None
        if proxy is not None:
            proxy = proxy.split(':')
            session.proxies = {
            'https' : f'https://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}',
            'http': f'https://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}',
            }
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

    
    def login(self, connectIntentId="BsEztrJmmu7o2V452P_k8"):
        
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
        data = {"0":{"json":{"connectIntentId":connectIntentId,"data":{"didSign":True}}},"1":{"json":{"address":str(self.public_address),"signedMessage":signed_message,"nonce":nonce,"captchaValue":None,"referralCode":None,"walletMetadata":{"walletName":"MetaMask","connectorType":"INJECTED"},"chainId":80001},"meta":{"values":{"captchaValue":["undefined"]}}}}
        r = session.post("https://layer3.xyz/api/trpc/track.walletModal,auth.login?batch=1", json=data)
        # print(r.text)



        result = json.loads(json.dumps(eval((r.text).replace("null", "None").replace("false", "False").replace("true", "True"))))[1]
        self.access_token = result["result"]["data"]["json"]["accessToken"]
        self.walletid = result["result"]["data"]["json"]["user"]["UserAddresses"][0]["id"]

        self.headers = {"Content-Type": "application/json",
        "referer":"https://layer3.xyz/quests/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "accept-language": "ru-RU,ru;q=0.9",
        "cookie": f"layer3_access_token={self.access_token};",
        }
        return self.walletid, self.public_address
    
    def bountyStep(self, id=None, inputData = None, userAddressId = None, data = None):
        if data is not None:
            data = data
        elif userAddressId:
            data = {"0":{"json":{"bountyStepId":id,"inputData":None,"userAddressId":self.walletid},"meta":{"values":{"inputData":["undefined"]}}}}
        else:
            data = {"0":{"json":{"bountyStepId":id,"inputData":inputData,"userAddressId":userAddressId},"meta":{"values":{"inputData":["undefined"],"userAddressId":["undefined"]}}}}
        
        r = session.post("https://layer3.xyz/api/trpc/bountyStep.completeBountyStep?batch=1", json=data, headers = self.headers)
        # print(f"{id} - {r.text}")
        if r.status_code != 200:
            print(f"Problem step in - {self.public_address} - {r.text} - {id} - {data}")
            return 0
        return 1

    def bountyClaim(self, id):

        data = {"0":{"json":{"taskId":id}}}

        r = session.post("https://layer3.xyz/api/trpc/bountyClaim.claimTask?batch=1", json=data, headers = self.headers)
        if r.status_code != 200:
            if r.text.find("You've already completed this quest!"):
                pass
            else:
                print(f"Problem cliam in - {self.public_address} - {r.text}")
            return 0
        return 1

    def post_sendAnyRequest(self,url, data=None):
        r = session.post(url, json=data, headers = self.headers)
        return r.text
    
    def get_sendAnyRequest(self,url):
        r = session.get(url,headers = self.headers)
        if r.status_code != 200:
            print(f"Problem sending Send Any Request in - {self.public_address} - {r.text}")
        return r.text
    # def get_stat(self,id):
    #     r = session.get(url = f"https://layer3.xyz/api/trpc/config.globalAnnouncement,user.getXpDataForUser?batch=1&input=%7B%220%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%2C%221%22%3A%7B%22json%22%3A%7B%22userId%22%3A851509%7D%7D%2C%222%22%3A%7B%22json%22%3A%7B%22userId%22%3A851509%7D%7D%2C%223%22%3A%7B%22json%22%3A%7B%22userId%22%3A851509%7D%7D%2C%224%22%3A%7B%22json%22%3A%7B%22userId%22%3A851509%2C%22cursor%22%3Anull%7D%2C%22meta%22%3A%7B%22values%22%3A%7B%22cursor%22%3A%5B%22undefined%22%5D%7D%7D%7D%2C%225%22%3A%7B%22json%22%3A%7B%22identifier%22%3A%220xD598D2F54BfD64E1b3c83dfbCF0d055F2E1A5a77%22%7D%7D%2C%226%22%3A%7B%22json%22%3A%7B%22userId%22%3A851509%7D%7D%2C%227%22%3A%7B%22json%22%3A%7B%22userId%22%3A851509%7D%7D%2C%228%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D",headers = self.headers)
    #     print(r.text)





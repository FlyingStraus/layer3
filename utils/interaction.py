from utils.libs import *

class layer3():
    def __init__(self,private_key, proxy = None):
        self.private = private_key
        session.headers.update({"Content-Type": "application/json",
        "referer":"https://layer3.xyz/quests/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "accept-language": "ru-RU,ru;q=0.9",
        # "cookie": "_cfuvid=3S5fabJ_P_TK9yw.nsrhxeDgMhVER0miEh39eTr30lE-1684010334723-0-604800000;layer3_access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjMyMjI0OSwiaWF0IjoxNjg0MDcwMjE0LCJleHAiOjE2ODQwNzM4MTR9.rqrUNzxVE_suvhJCsXuWD8sIkGvO0MGmvTSZKY4N8ig;",
        })

    
    def login(self, connectIntentId="wYVvAk3KQMUBf-QR_2Tpz", address):
        
        data = {"0":{"json":{"connectIntentId":connectIntentId,"data":{"buttonName":"MetaMask","device":{"type":"desktop","os":{"name":"Windows","version":"NT 10.0","versionName":"10"},"browser":{"name":"Chrome","version":"113.0.0.0"}}}}}}
        r = session.post("https://layer3.xyz/api/trpc/track.walletModal?batch=1", json=data)
        data = {"0":{"json":None,"meta":{"values":["undefined"]}},"1":{"json":{"connectIntentId":connectIntentId,"data":{"didConnect":True,"walletMetadata":{"walletName":"MetaMask","connectorType":"INJECTED"}}}}}
        r = session.post("https://layer3.xyz/api/trpc/auth.getWalletSignatureNonce,track.walletModal?batch=1", json=data)

        # TODO: get none from session and sign it
        
        # TODO:add private key to address

        address = "0x5790B961c331B6107a849C3894c8e1BB78c994dC" 
        data = {"0":{"json":{"connectIntentId":connectIntentId,"data":{"didSign":True}}},"1":{"json":{"address"address:,"signedMessage":"0x71f34ebe43f1835be514f7b99e70768a8a5c467b4529c9b89f545ebd627a35666252db8407634826fe3f4f109879b3bf5df9d9e2f037578ff4d725724005dc241c","nonce":"VN0GXKSNG5TR","captchaValue":None,"referralCode":None,"walletMetadata":{"walletName":"MetaMask","connectorType":"INJECTED"},"chainId":42161},"meta":{"values":{"captchaValue":["undefined"]}}}}
        r = session.post("https://layer3.xyz/api/trpc/track.walletModal,auth.login?batch=1", json=data)

from hashlib import sha256 as sh
from hashlib import sha384 as sht
import jwt

import base64;
import hmac
def verifyJwt(token,secret,mode):
    sub_tokens=token.split('.');
    header=sub_tokens[0];
    payload=sub_tokens[1];
    signature=sub_tokens[2];
    
    h=hmac.new(secret.encode(),(header+"."+payload).encode(),mode);
    result=h.digest();
    # print(result)
    hashh=((base64.urlsafe_b64encode(result)).decode())
    # print(hashh);
    hashh=hashh.split('=')[0];
    # print(hashh);
    if(hashh==signature):
        print("Token Verification Success!")
        # return 1;
        retval=(base64.urlsafe_b64decode((payload).encode()+b'==')).decode()
        
        return retval;
    else:
        # raise Exception("Invalid Token!!")#for using find key DISABLE this
        return 0;#for using find key ENABLE this


def find_key(token,mode):
    arr="abcdefghijklmnopqrstuvwxyz0123456789"
    testpass=["p","a","g","g","d"];
    
    for one in arr:
        for two in arr:
            for three in arr:
                for four in arr:
                    for five in arr:
                        testpass[0]=one;
                        testpass[1]=two;
                        testpass[2]=three;
                        testpass[3]=four;
                        testpass[4]=five;
                        tpass = ''.join(map(str, testpass))
                        
                        
                        crack=verifyJwt(token, tpass,mode);
                        print(tpass,"  ",crack)
                        if(crack!=0):
                            print("Key Cracking: Success! ")
                            return tpass;
                        else:
                            print("Failed!")
                        
    print("Attempt Fail");
    return 0;

token=input("Enter JWT :")
key=find_key(token, sh)
if(key!=0):
    encoded_jwt = jwt.encode({"sub":"fcs-assignment-1","iat":1516239022,"exp":1672511400,"role":"admin","email":"arun@iiitd.ac.in","hint":"lowercase-alphanumeric-length-5"}, key, algorithm="HS256")
    print("Success\n Modified JWT:",encoded_jwt);
# {"sub":"fcs-assignment-1","iat":1516239022,"exp":1672511400,"role":"admin","email":"arun@iiitd.ac.in","hint":"lowercase-alphanumeric-length-5"}
# print(encoded_jwt)

#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE2NzI1MTE0MDAsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJhcnVuQGlpaXRkLmFjLmluIiwiaGludCI6Imxvd2VyY2FzZS1hbHBoYW51bWVyaWMtbGVuZ3RoLTUifQ.LCIyPHqWAVNLT8BMXw8_69TPkvabp57ZELxpzom8FiI
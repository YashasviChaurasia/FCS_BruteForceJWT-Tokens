from hashlib import sha256 as sh
from hashlib import sha384 as sht

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
        raise Exception("Invalid Token!!")#for using find key DISABLE this
        # return 0;//for using find key ENABLE this

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


key="p1gzy"

# my="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.dCyiRYOo_KfhjW4DmmbE3iuRh2ogyhwizp_pPBQKNgQ";

my=input("Enter JWT Token: ");

# check=base64.urlsafe_b64decode(result.encode())

# byte_key = key.encode()  # key.encode() would also work in this case
# message = my.encode()
# # print(byte_key);
# h=hmac.new(byte_key,message,sh);

# result="SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
# print(result);
# test="hello";
# yo=base64.urlsafe_b64encode(test.encode());
# p=h.digest();
# print( (base64.urlsafe_b64encode(p)).decode())
# print(verifyJwt(my, key));



#**********************************************************************
verifyJwt(my, key, sh)
# secret_key=find_key(my,sht);#works for tokens of length < 5
#**********************************************************************


#hash chaining to generate secret keys and the secret key is used only for one time 
#we can use this key for all connections and seed can be generated for a server 
# tokens expiry date can be set to one month and we store seed for each day


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE2NzI1MTE0MDAsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJhcnVuQGlpaXRkLmFjLmluIiwiaGludCI6Imxvd2VyY2FzZS1hbHBoYW51bWVyaWMtbGVuZ3RoLTUifQ.LCIyPHqWAVNLT8BMXw8_69TPkvabp57ZELxpzom8FiI
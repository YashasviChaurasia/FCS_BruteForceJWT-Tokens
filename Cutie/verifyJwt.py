from hashlib import sha256 as sh
from hashlib import sha384 as sht

import base64;
import hmac
def verifyJwt(token,secret):
    sub_tokens=token.split('.');
    header=sub_tokens[0];
    payload=sub_tokens[1];
    signature=sub_tokens[2];
    m=input("Enter [1:2] for [sha256/sha384] : ")
    if(m=="1"):
        # print("Hello Im in ")
        h=hmac.new(secret.encode(),(header+"."+payload).encode(),sh);
    else:
        # print("Hello Im in 2")
        h=hmac.new(secret.encode(),(header+"."+payload).encode(),sht);
    # print("Hello Im in 23")
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



# my="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.dCyiRYOo_KfhjW4DmmbE3iuRh2ogyhwizp_pPBQKNgQ";

if __name__=="__main__":
    my=input("Enter JWT Token: ");
    key=input("Enter Key: ")
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
    verifyJwt(my, key)
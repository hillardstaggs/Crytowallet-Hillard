#import bitcoin
from bitcoin import *
#create private key
private_key = random_key()
print(private_key)
#create public key
public_key = privtopub(private_key)
print(public_key)
#create a bitcoin address
address = pubtoaddr(public_key)
print("My Address is: " + address)
bitcoin import*

outfile = open('wallet.txt', 'w')
private_key = random key ()
print(private_key)
public_key = privtopub(private_key)
print(public_key)
address = pubtoaddr(public_key)
print('my address is : ' + address)
outfile.write('my bitcoin address :' +address+ '\n\)
outfile.write('my public key :' + privtopub(private_key)' + '\n')
outfile.write('my hexadecimal private key :' + private_key + '\n')
outfile.close()
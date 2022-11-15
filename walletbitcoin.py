from bitcoin.keys import Key
from bitcoin.wallets import *

def createKey():
    print('generate bitcoin key on mainnet')
    k = Key()
    k.info()


def createTestnetKey():
    print('generate bitcoin key on testnet')
    tk = Key(network='testnet')
    tk.info()


def keyInfo(wif, network):
    if network == 'bitcoin'.lower():
        k = Key(wif)
        k.info()
        print('goto :   ' + k.address()) #'https_____' for btc address
    if network == 'testnet'.lower():
        k = Key(wif, network='testnet')
        k.info()
    else:
        pass


def wifToKey(wif, network):
    if network == 'bitcoin'.lower():
        k = Key(wif)
            return k
    if network == 'testnet'.lower():
        k = Key(wif, network='testnet')
            return k
        else:
            pass
# mainnet WIF
k1_wif = '0C28FCA386C7A227600B2FE50B7CAE_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_11EC86D3BF1FBE471BE89827E19D72AA1D'
# testnet WIF
tk1_wif = '5HueCGU8rMjxEXxiPuD5BDk_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_u4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'    #test key wallet #1
tk2_wif = '   5HueCGU8rMjxEXxiPuD5BD_SAMPLE_PRIVATE_KEY_DO_NOT_IMPORT_ku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ' #test key wallet #2

tk1 = wifToKey(tk1_wif, 'testnet')
tk2 = wifToKey(tk2_wif, 'testnet')

print('download ______:         ') #download whatever from wesbite
print('and access bitcoin address from WIF')
print('tk1.wif : ' + tk1.wif())
print('tk2.wif : ' + tk2.wif())
print('add testnet fund :       ') #add the link to test the fund
print('tk1.address : ' + tk1.address())
print('tk2.address : ' + tk2.address())

w = Wallet('test_wallet_02')        #wallet name
w.scan()                            #wallet scanned
w.info()                            #info wallet
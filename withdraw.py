
from unicodedata import name
import env as EN
from sergio import account_asset



session_auth = account_asset.FuncaoSergio(
    endpoint=EN.endpoint,
    api_key=EN.api_key,
    api_secret=EN.secret_key
)

def FazSaque(coin,chain,address,amount,tag=False):
    SAQUE = session_auth.withdraw(coin=coin, chain=chain, address=address,amount=amount)
    print(SAQUE)
    
    
if __name__ == '__main__':
    FazSaque(coin='TRX', chain='TRX',address="TCrYmTrJHUfKQhzbU7hMpvZeTCsXRrwRBC",amount='11')
    




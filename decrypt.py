import pip, site, importlib, os
pip.main(['install', '--user', 'cryptography'])  # pip install --user modelx を実行
importlib.reload(site)                     # sys.pathをリフレッシュする
from cryptography.fernet import Fernet

key = input('"Key" を入力してください>> ').encode('utf-8')
fernet = Fernet(key)
encrypted_message = input('"Encrypted API Key" を入力してください>> ').encode('utf-8')

decrypted_message = fernet.decrypt(encrypted_message)
print('APIキー: ', decrypted_message.decode('utf-8'))
os.system('PAUSE')
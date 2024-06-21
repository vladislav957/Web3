Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if name == "main":
...     provider_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
...     web3_helper = Web3Helper(provider_url)
... 
...     # Получение баланса
...     address = '0xYourEthereumAddress'
...     balance = web3_helper.get_balance(address)
...     print(f"Balance of {address}: {balance} ETH")
... 
...     # Отправка транзакции
...     from_address = '0xYourEthereumAddress'
...     to_address = '0xRecipientEthereumAddress'
...     private_key = 'YourPrivateKey'
...     value = 0.01  # ETH
...     tx_hash = web3_helper.send_transaction(from_address, to_address, private_key, value)
...     print(f"Transaction hash: {tx_hash}")
... 
...     
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    if name == "main":
NameError: name 'name' is not defined
>>> # Получение информации о транзакции
...     tx_info = web3_helper.get_transaction(tx_hash)

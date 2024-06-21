
class Web3Helper:
    def init(self, provider_url):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum network")

    def get_balance(self, address):
        balance = self.web3.eth.get_balance(address)
        return self.web3.fromWei(balance, 'ether')
    
    def send_transaction(self, from_address, to_address, private_key, value):
        nonce = self.web3.eth.get_transaction_count(from_address)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': self.web3.toWei(value, 'ether'),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        }
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.web3.toHex(tx_hash)

    def get_transaction(self, tx_hash):
        return self.web3.eth.get_transaction(tx_hash)

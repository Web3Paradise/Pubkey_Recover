from eth_keys import keys
from eth_utils import decode_hex
from web3 import Web3

# Your Ethereum node RPC URL
rpc_url = 'YOUR_RPC_URL'

# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Ensure that you are connected
assert w3.isConnected(), "Failed to connect to the Ethereum node"

# Replace 'your_tx_hash' with your actual transaction hash
tx_hash = 'your_tx_hash'

# Get the transaction by hash
tx = w3.eth.getTransaction(tx_hash)

# Ensure the transaction contains all necessary values
assert tx['r'] is not None
assert tx['s'] is not None
assert tx['v'] is not None

# Build a signature object
signature = keys.Signature(vrs=(tx['v'], decode_hex(tx['r']), decode_hex(tx['s'])))

# Recover the public key
public_key = signature.recover_public_key_from_msg_hash(decode_hex(tx_hash))

# Convert the public key to its hexadecimal representation
public_key_hex = public_key.to_hex()

print(public_key_hex)

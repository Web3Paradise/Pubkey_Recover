from eth_keys import keys
from eth_utils import decode_hex
from web3 import Web3

# Binance Smart Chain Mainnet RPC URL
rpc_url = 'https://bsc-dataseed.binance.org/'

# Connect to the Binance Smart Chain node
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Ensure that you are connected
if not w3.isConnected():
    raise Exception("Failed to connect to the Binance Smart Chain node")

# Replace 'your_tx_hash' with your actual transaction hash
tx_hash = 'your_tx_hash'

# Get the transaction by hash
try:
    tx = w3.eth.getTransaction(tx_hash)
except Exception as e:
    raise Exception(f"Failed to fetch transaction: {e}")

# Ensure the transaction contains all necessary values
if not all(k in tx for k in ('r', 's', 'v')):
    raise Exception("Transaction is missing signature values")

# Build a signature object
signature = keys.Signature(vrs=(tx['v'], decode_hex(tx['r']), decode_hex(tx['s'])))

# Recover the public key
try:
    public_key = signature.recover_public_key_from_msg_hash(decode_hex(tx_hash))
except Exception as e:
    raise Exception(f"Failed to recover public key: {e}")

# Convert the public key to its hexadecimal representation
public_key_hex = public_key.to_hex()

print(f"Public Key: {public_key_hex}")

import hashlib

print(hashlib.sha256('Hello World'.encode()).hexdigest())

nonce_limit = 100000000
zeroes = 16                  # input depends on how many zeroes are searching

def mine(block_number, transactions, previous_hash):
    for nonce in range(nonce_limit):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeroes):
            print(f'Found Hash With Nonce: {nonce}')
            return hash_try

    return -1

# visit blockchain.com for data input

block_number = 24               # search for current block
transactions = '12345678910'
previous_hash = '0123456789'

combined_text = str(block_number) + transactions + previous_hash + str(25627) # input given NONCE
print(hashlib.sha256(combined_text.encode()).hexdigest())

mine(block_number, transactions, previous_hash)
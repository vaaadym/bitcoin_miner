import hashlib 

NONCE_LIMIT = #namber
zeroes = #namber

def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
    base_text = str(block_number) + transactions + previous_hash + str(nonce)
    hash_try = hashlib.sha256(base_text.encode()).hexdigest()
    if hash_try.startswith("0" * zeroes):
        print(f"Found hash with nonce: {nonce}")
        return hash_try

    return -1

block_number = #namber
transactions = ""
previous_hash = ""

combined_text = str(block_number) + transactions + previous_hash
print(hashlib.sha256(combined_text.encode()).hexdigest())

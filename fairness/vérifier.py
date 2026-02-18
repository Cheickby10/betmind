import hashlib

def generate_hash(server,client,nonce):
    data=f"{server}:{client}:{nonce}"
    return hashlib.sha256(data.encode()).hexdigest()

def verify(server,client,nonce,published):
    return generate_hash(server,client,nonce)==published

import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, utils


message = b'from Bob to Alice'
sha256 = hashlib.sha256()
sha256.update(message[:8])
sha256.update(message[8:])
hash_value = sha256.digest()

private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())

signature = private_key.sign(
    hash_value,
    ec.ECDSA(utils.Prehashed(hashes.SHA256()))
)

print(signature)

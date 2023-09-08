from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature


message = b'from Bob to Alice'

private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())

signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

public_key = private_key.public_key()

try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print(True)
except InvalidSignature:
    pass

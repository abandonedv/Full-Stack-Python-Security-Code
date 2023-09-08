import json

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

DIR_PATH = "5/5.5"


with open(f'{DIR_PATH}/private_key.pem', 'rb') as private_file:
    loaded_private_key = serialization.load_pem_private_key(
        private_file.read(),
        password=None,
        backend=default_backend(),
    )

with open(f'{DIR_PATH}/public_key.pem', 'rb') as public_file:
    loaded_public_key = serialization.load_pem_public_key(
        public_file.read(),
        backend=default_backend(),
    )

padding_config = padding.PSS(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    salt_length=padding.PSS.MAX_LENGTH,
)

message = b'from Bon to Alice'

private_key = loaded_private_key

signature = private_key.sign(
    message,
    padding_config,
    hashes.SHA256(),
)

signed_msg = {
    'message': list(message),
    'signature': list(signature)
}

outbound_msg_to_alice = json.dumps(signed_msg)

print(outbound_msg_to_alice)

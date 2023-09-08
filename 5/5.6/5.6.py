import json

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

DIR_PATH = "5/5.6"


def send():
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
    return outbound_msg_to_alice

# *******************************************


def receive(inbound_msg_from_bob):
    signed_msg = json.loads(inbound_msg_from_bob)
    message = bytes(signed_msg['message'])
    signature = bytes(signed_msg['signature'])

    padding_config = padding.PSS(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    )

    with open(f'{DIR_PATH}/private_key.pem', 'rb') as private_file:
        loaded_private_key = serialization.load_pem_private_key(
            private_file.read(),
            password=None,
            backend=default_backend(),
        )

    public_key = loaded_private_key.public_key()

    try:
        public_key.verify(
            signature,
            message,
            padding_config,
            hashes.SHA256(),
        )

        print(True)
    except InvalidSignature:
        print(False)


receive(send())

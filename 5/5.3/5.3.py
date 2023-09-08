from os import remove

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

DIR_PATH = "5/5.3"

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=3072,
    backend=default_backend(),
)

public_key = private_key.public_key()

private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

with open(f'{DIR_PATH}/private_key.pem', 'xb') as private_file:
    private_file.write(private_bytes)

public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

with open(f'{DIR_PATH}/public_key.pem', 'xb') as public_file:
    public_file.write(public_bytes)

with open(f'{DIR_PATH}/private_key.pem', 'rb') as private_file:
    loaded_private_key = serialization.load_pem_private_key(
        private_file.read(),
        password=None,
        backend=default_backend(),
    )
    print(loaded_private_key)

with open(f'{DIR_PATH}/public_key.pem', 'rb') as public_file:
    loaded_public_key = serialization.load_pem_public_key(
        public_file.read(),
        backend=default_backend(),
    )
    print(loaded_public_key)

remove(path=f"{DIR_PATH}//private_key.pem")
remove(path=f"{DIR_PATH}//public_key.pem")

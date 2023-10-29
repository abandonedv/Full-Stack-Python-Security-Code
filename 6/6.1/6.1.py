import ssl

DIR_PATH = "6/6.1"

address = ('wikipedia.org', 443)
certificate = ssl.get_server_certificate(address)

with open(f"{DIR_PATH}/wikipedia.crt", mode="w") as f:
    f.write(certificate)

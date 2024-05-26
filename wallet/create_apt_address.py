import binascii
import hashlib
import ecdsa

# Generate a new private key
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

# Generate the corresponding public key
public_key = private_key.get_verifying_key()

# Get the uncompressed public key in bytes
uncompressed_public_key = public_key.to_string('uncompressed')

# Hash the uncompressed public key using SHA-256
sha256_hash = hashlib.sha256(uncompressed_public_key).digest()

# Hash the result of the previous hash using RIPEMD-160
ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

# Add the address version byte (0x17 for APT) to the RIPEMD-160 hash
versioned_ripemd160_hash = b'\x17' + ripemd160_hash

# Hash the versioned RIPEMD-160 hash twice using SHA-256
checksum = hashlib.sha256(hashlib.sha256(versioned_ripemd160_hash).digest()).digest()

# Add the first 4 bytes of the checksum to the versioned RIPEMD-160 hash
address_bytes = versioned_ripemd160_hash + checksum[:4]

# Encode the address bytes using base58 encoding
import base58
address = base58.b58encode(address_bytes).decode('utf-8')

# Print the private key, public key, and address
print("Private key: {}".format(binascii.hexlify(private_key.to_string()).decode('utf-8')))
print("Public key: {}".format(binascii.hexlify(public_key.to_string('uncompressed')).decode('utf-8')))
print("APT address: {}".format(address))
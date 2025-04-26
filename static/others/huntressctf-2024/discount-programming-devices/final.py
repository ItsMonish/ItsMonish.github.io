import zlib
import base64

print(zlib.decompress(base64.b64decode(b'eJxLy0lMrzYyNTFOSzNMNTc0SXI2Sk2yTEsztzA0sjAyNjK3ME1MqQUA4D4LDA==')).decode())
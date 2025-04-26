import base64

contents = ""

with open("./base64by32") as f:
    contents = f.read()

for i in range(32):
    contents = base64.b64decode(contents.encode()).decode()

print(contents)
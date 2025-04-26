with open("./payload.bat") as f:
    cons = f.read().split("\n")

result = []
for line in cons:
    if line == "" or not line.startswith("::"):
        result.append(line)

with open("./payload cleaned.bat", "w") as f:
    for line in result:
        f.write(line + "\n\n")

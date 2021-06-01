import hashlib

FLAG = 'FindITCTF{REDACTED}'

now = ""
ct = []

for c in FLAG:
    now += c
    ct.append(
            int(hashlib.sha512(now.encode()).hexdigest(), 16)>>256
        )

print(f"ct = {ct}")

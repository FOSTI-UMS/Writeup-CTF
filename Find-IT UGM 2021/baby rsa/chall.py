from Crypto.Util.number import getPrime, getRandomRange

FLAG = 'FindITCTF{REDACTED}'

p = getPrime(1024)
q = getPrime(1024)

N = p*q
e = 0x10001

N_masked = list(str(N))
for _ in range(6):
    N_masked[getRandomRange(0, len(N_masked))] = 'x'
N_masked = "".join(N_masked)

print(f"N_masked = {N_masked}")

C = [pow(ord(c), e, N)>>1 for c in FLAG]
print(f"C = {C}")
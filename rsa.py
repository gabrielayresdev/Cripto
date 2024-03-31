from sympy import randprime 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
        
initial = 22042003


q = randprime(2**128, 2**129)
print(q)
p = randprime(2**128, 2**129)
print(p)
n = q * p
print(n)
e = 65537
phi = (q - 1) * (p - 1)
print(phi)
d = modinv(e, phi)
print(d)

encripted = pow(initial, e, n)
decripted = pow(encripted, d, n)
print(encripted)
print(decripted)

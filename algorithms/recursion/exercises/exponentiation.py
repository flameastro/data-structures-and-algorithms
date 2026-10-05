# O(n)

def exponentiation(base, exponent):
    if exponent == 0:
        return 1

    return base * exponentiation(base, exponent - 1)

print(exponentiation(2, 4))  # 16

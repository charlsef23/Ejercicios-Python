
# 1. Arithmetic Operators
print("=== Arithmetic Operators ===")
a = 10
b = 3

# Addition
print(f"{a} + {b} = {a + b}")  # 10 + 3 = 13

# Subtraction
print(f"{a} - {b} = {a - b}")  # 10 - 3 = 7

# Multiplication
print(f"{a} * {b} = {a * b}")  # 10 * 3 = 30

# Division
print(f"{a} / {b} = {a / b}")  # 10 / 3 = 3.3333333333333335

# Floor Division
print(f"{a} // {b} = {a // b}")  # 10 // 3 = 3

# Modulus (Remainder)
print(f"{a} % {b} = {a % b}")  # 10 % 3 = 1

# Exponentiation
print(f"{a} ** {b} = {a ** b}")  # 10 ** 3 = 1000



# 2. Comparison Operators
print("=== Comparison Operators ===")
x = 5
y = 10

# Equal to
print(f"{x} == {y}: {x == y}")  # 5 == 10: False

# Not equal to
print(f"{x} != {y}: {x != y}")  # 5 != 10: True

# Greater than
print(f"{x} > {y}: {x > y}")  # 5 > 10: False

# Less than
print(f"{x} < {y}: {x < y}")  # 5 < 10: True

# Greater than or equal to
print(f"{x} >= {y}: {x >= y}")  # 5 >= 10: False

# Less than or equal to
print(f"{x} <= {y}: {x <= y}")  # 5 <= 10: True


# 3. Logical Operators
print("=== Logical Operators ===")
p = True
q = False

# Logical AND
print(f"p and q: {p and q}")  # p and q: False

# Logical OR
print(f"p or q: {p or q}")  # p or q: True

# Logical NOT
print(f"not p: {not p}")  # not p: False


# 4. Assignment Operators
print("=== Assignment Operators ===")
num = 5

# Assign value
num += 2  # Equivalent to num = num + 2
print(f"num after +=2: {num}")  # num after +=2: 7

num -= 1  # Equivalent to num = num - 1
print(f"num after -=1: {num}")  # num after -=1: 6

num *= 3  # Equivalent to num = num * 3
print(f"num after *=3: {num}")  # num after *=3: 18

num /= 2  # Equivalent to num = num / 2
print(f"num after /=2: {num}")  # num after /=2: 9


# 5. Bitwise Operators
print("=== Bitwise Operators ===")
m = 5  # Binary: 0101
n = 3  # Binary: 0011

# Bitwise AND
print(f"{m} & {n}: {m & n}")  # 5 & 3: 1 (Binary: 0001)

# Bitwise OR
print(f"{m} | {n}: {m | n}")  # 5 | 3: 7 (Binary: 0111)

# Bitwise XOR (Exclusive OR)
print(f"{m} ^ {n}: {m ^ n}")  # 5 ^ 3: 6 (Binary: 0110)

# Bitwise NOT (Inverts bits)
print(f"~{m} = {-m - 1}")  # ~5: -6 (Inverts bits)

# Bitwise Left Shift (Shifts bits to the left)
print(f"{m} << 1 = {m << 1}")  # 5 << 1 = 10 (Binary: 1010)

# Right Shift (Shifts bits to the right)
print(f"{m} >> 1 = {m >> 1}")  # 5 >> 1 = 2 (Binary: 0010)



import re

# Find suspicious patterns of 16 repeating bytes
_prex = re.compile(r"(..)\1{15}")


def pattern(n, e=0):
    return {"detected": True} if (r := _prex.search(f"{n:02x}")) else False

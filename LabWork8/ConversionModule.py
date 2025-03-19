def decimal_to_base(n, base):
    if n == 0:
        return "0"
    digits = ""
    while n:
        digits = str(n % base) + digits
        n //= base
    return digits

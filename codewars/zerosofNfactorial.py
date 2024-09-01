def zeros(n):
    zeros_count = 0
    factor = 5
    if n < 5:
        return 0
    while n >= factor:
        zeros_count += n // factor
        factor = factor * 5
    return zeros_count
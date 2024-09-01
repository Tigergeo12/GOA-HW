def find_difference(a, b):
    # Your code here!

    multiply_of_a = a[0] * a[1] * a[2]
    multiply_of_b = b[0] * b[1] * b[2]

    if multiply_of_a > multiply_of_b:
        return multiply_of_a - multiply_of_b
    else:
        return multiply_of_b - multiply_of_a
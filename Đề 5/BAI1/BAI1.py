import sys
sys.stdin = open('BAI1.INP','r')
sys.stdout = open('BAI1.OUT','w')

binary = str(input())

def binary_to_decimal(binary_str):
    decimal = 0
    power = len(binary_str) - 1
    for digit in binary_str:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def decimal_to_hexadecimal(decimal):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        decimal //= 16
    return hexadecimal

decimal = binary_to_decimal(binary)
hexadecimal = decimal_to_hexadecimal(decimal)

print(hexadecimal)

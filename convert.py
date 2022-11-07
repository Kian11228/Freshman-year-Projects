binary_num = input("Enter a 3-bit binary number")

bit1 = int(binary_num[2]) * 1
bit2 = int(binary_num[1]) * 2
bit3 = int(binary_num[0]) * 4

bit_sum = bit1 + bit2 + bit3

print("Your binary number in decimal for is", bit_sum)
n = int(input("Nhap n: "))

tong = 0

for i in range(n):
    x = int(input(f"Nhap x{i + 1}: "))

    if x % 2 == 0:
        tong += x

print("Tong cac phan tu chan =", tong)

if tong % 7 == 0 and tong < 200:
    print("Tong chia het cho 7 va nho hon 200")
else:
    print("Tong khong thoa man dieu kien")
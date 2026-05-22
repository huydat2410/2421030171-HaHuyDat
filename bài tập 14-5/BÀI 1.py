n = int(input("Nhap n: "))

tong = 0
dem = 0

for i in range(n):
    x = float(input(f"Nhap x{i + 1}: "))

    if -1000 < x < -10:
        tong += x
        dem += 1

if dem > 0:
    tbc = tong / dem
    print("Trung binh cong =", tbc)
else:
    print("Khong co phan tu nao thoa man")

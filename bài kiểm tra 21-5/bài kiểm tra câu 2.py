
n = int(input("Nhập số nguyên dương n: "))

tong = 0
tam = n

while tam > 0:
    chu_so = tam % 10      # Lấy chữ số cuối
    tong += chu_so         # Cộng vào tổng
    tam = tam // 10        # Bỏ chữ số cuối

print("Tổng các chữ số =", tong)

if tong % 3 == 0:
    print("Tổng các chữ số chia hết cho 3")
else:
    print("Tổng các chữ số không chia hết cho 3")


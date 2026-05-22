# Câu 5:
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))

tong = 0
tam = n

# Tính tổng các chữ số của n
while tam > 0:
    chu_so = tam % 10
    tong += chu_so
    tam = tam // 10

print("Tổng các chữ số của n =", tong)

# Kiểm tra chia hết
if tong != 0 and m % tong == 0:
    print(m, "chia hết cho", tong)
else:
    print(m, "không chia hết cho", tong)
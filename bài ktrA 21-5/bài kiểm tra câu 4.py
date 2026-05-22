# Câu 4:
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

tong = a + b
print("Tổng =", tong)

max_cs = 0
tam = tong

while tam > 0:
    chu_so = tam % 10      # Lấy chữ số cuối
    if chu_so > max_cs:
        max_cs = chu_so

    tam = tam // 10        # Bỏ chữ số cuối

print("Chữ số lớn nhất trong tổng là:", max_cs)

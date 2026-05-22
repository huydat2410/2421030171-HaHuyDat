# Câu 3:
n = int(input("Nhập số nguyên dương n: "))

tich = 1
tam = n

while tam > 0:
    chu_so = tam % 10      # Lấy chữ số cuối
    tich *= chu_so         # Nhân vào tích
    tam = tam // 10        # Bỏ chữ số cuối

print("Tích các chữ số =", tich)

if tich % 2 == 0 and tich > 20:
    print("Tích các chữ số là số chẵn và lớn hơn 20")
else:
    print("Tích các chữ số không thỏa mãn")

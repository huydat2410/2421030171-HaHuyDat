a = int(input("nhập a: "))
b = int(input("nhập b: "))
c = int(input("nhập c: "))
tong = a+b+c
s = str(abs(tong))
chu_so_chan = [ch for ch in s if int(ch) % 2 == 0]
so_chu_so_chan = len(chu_so_chan)
print(f"\nTổng a+b+c = {tong}")
print(f"Chữ số chẵn = {chu_so_chan}")
print(f"Số chữ số chẵn = {so_chu_so_chan}")

def main()
while True:
    n = int(input("Nhập số lượng phần tử n (0 < n < 200): "))
    if 0 < n < 200:
        break
    print("Vui lòng nhập lại (0 < n < 200)!")
day_so = []
print("Nhập các số nguyên:")
for i in range(n):
    so = int(input(f"x{i+1} = "))
    day_so.append(so)
tong_chan = 0
cac_so_chan = []
for x in day_so:
    if x % 2 == 0:
        tong_chan += x
        cac_so_chan.append(x)
print(f"\nCác phần tử chẵn: {cac_so_chan}")
print(f"Tổng các phần tử chẵn: {tong_chan}")
if tong_chan % 7 == 0 and tong_chan < 200:
    print(f"Kết luận: Tổng {tong_chan} chia hết cho 7 và nhỏ hơn 200")
else:
    print(f"Kết luận: Tổng {tong_chan} KHÔNG thỏa mãn điều kiện")

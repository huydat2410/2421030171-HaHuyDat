def phan_loai_ky_tu():
    with open("input.txt", "r", encoding="utf-8") as file:
        noi_dung = file.read()
    so = []
    chu = []
    for ky_tu in noi_dung:
        if ky_tu.isdigit():
            so.append(ky_tu)
        elif ky_tu.isalpha():
    with open("outso.txt", "w", encoding="utf-8") as file:
        file.write("".join(so))
    with open("outchu.txt", "w", encoding="utf-8") as file:
        file.write("".join(chu))
    print("Đã phân loại xong!")
    print(f"Số lượng ký tự số: {len(so)}")
    print(f"Số lượng ký tự chữ: {len(chu)}")
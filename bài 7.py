def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("=" * 30)
n = int(input("Nhập số lượng phần tử n (0 < n < 100): "))
arr = []
for i in range(n):
    x = int(input(f"  Nhập x[{i+1}]: "))
    arr.append(x)

primes_in_arr = [x for x in arr if is_prime(x)]
tong = sum(primes_in_arr)

print(f"\nCác số nguyên tố trong dãy: {primes_in_arr}")
print(f"Tổng các số nguyên tố: {tong}")

if tong % 2 != 0 and tong > 50:
    print("→ Tổng là số lẻ VÀ lớn hơn 50 ✔")
else:
    reasons = []
    if tong % 2 == 0:
        reasons.append("không phải số lẻ")
    if tong <= 50:
        reasons.append("không lớn hơn 50")
    print(f"→ Tổng KHÔNG thỏa điều kiện ({', '.join(reasons)}) ✘")
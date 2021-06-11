# ตัวดำเนินการทางคณิตศาสตร์
x = 10
y = 3

print("ผลบวก" , x+y)
print("ผลลบ" , x-y)
print("ผลคูณ", x*y)
print("ผลหาร",x/y)
print("หารปัดเศษ", x//y)
print("ยกกำลัง",x**y)
print("หารเอาเศษ",x%y)

a = x/y # ทศนิยม floating point

print("%.2f" % a)
print(round(a,2))
print("%.2f" % round(a, 2))
print("{:.2f}".format(a))
print("{:.2f}".format(round(a, 2)))
print("{:.15f}".format(round(a, 2)))
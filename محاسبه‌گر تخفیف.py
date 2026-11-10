def h(d,g):
    d1 = int(g*d / 100)
    g1 = g - d1
    print("مقدار تخفیف : ",d1)
    print("قیمت قابل پرداخت :  ",g1)

d = int(input("مقدار تخفیف را وارد کنید:  "))
g = int(input("قیمت را وارد کنید :   "))

h(d,g)

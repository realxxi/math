import random
g=int(input("Nechta misol yechasiz? "))
print("Topshiriqni bajaring!")
i=0
true=0
false=0
while i<(g):
    a=random.randint(0,100)
    b=random.randint(0,100)
    amallar=["+", "-", "*", "/"]
    n=random.choice(amallar)
    c=float(input(f"{a}{n}{b}="))
    if n=="+":
        if a+b==c:
            print("Javob to'g'ri" )
            true+=1
        else:
            print("Javob noto'g'ri,\nTo'g'ri javob:",a+b )
            false+=1
    elif n=="*":
        if a*b==c:
            print("Javob to'g'ri" )
            true+=1
        else:
            print("Javob noto'g'ri,\nTo'g'ri javob:",a*b )
            false+=1
    elif n=="/":
        if round(a/b,2)==c:
            print("Javob to'g'ri" )
            true+=1
        else:
            print("Javob noto'g'ri,\nTo'g'ri javob:",round(a/b,2) )
            false+=1
    elif n=="-":
        if a-b==c:
            print("Javob to'g'ri" )
            true+=1
        else:
            print("Javob noto'g'ri,\nTo'g'ri javob:",a-b )
            false+=1
    i+=1
print(f"\nTo'g'ri javoblar soni: {true}\nNoto'g'ri javoblar soni: {false}")
a=true/g
if a>=0.9:
    print("\n \nBahoyingiz 5")
elif 0.8<=a<0.9:
    print("\n \nBahoyingiz 4")
elif 0.63<=a<0.8:
    print("\n \nBahoyingiz 3")
else:
    print("\n \nAfsus Topshiriqdan yiqildingiz !!!")
a=input("\n \n \n >>>>>Chiqish uchun Enterni bosing")
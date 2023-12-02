import time

gorevler = []

while True:

    print(gorevler)
    islem = input("Yapman gerekenler bunlar, ne yapmak istersin?\n1 = Görev ekle\n2 = Son görevi sil\n3 = Görevleri tekrar yükle\n")

    if islem == "1":
        ekle = input("Eklemek istediğin görevi gir\n")
        gorevler.append(ekle)
    elif islem == "2":
        input("Bir tuşa basın ve ardından 'Enter'a basın")
        gorevler.pop()
    elif islem == "3":
        print(gorevler)
        time.sleep(3)
    else:
        print("Hatalı tuşlama")

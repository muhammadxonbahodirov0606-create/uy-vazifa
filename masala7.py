def talaba_info(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        print(f"{kalit.capitalize()}: {qiymat}")

ism = input("ism:")
kurs = int(input("kurs:"))
shahar = input("shahar:")

talaba_info(ism=ism, kurs=kurs, shahar=shahar)
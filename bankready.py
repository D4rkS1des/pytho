import urllib.request
def main():
        print("Privet, etot skript pomozhet tebe rashitat pereplaty po kreditu. Sleduy instrukcii^^")
        print("Tebe ponadobitsya internet")
        rate = int(input("%stavka godovyh: "))
        money = int(input("Summ: "))
        period = int(input("Period v month: "))
        cnvs = int(input("Esli nuzhen convert v rubly vyberete ishodn valyty $=1 euro=2 btc=3 Propusk=0 "))
        if cnvs == 1:
            resp = urllib.request.urlopen("https://api.cryptonator.com/api/ticker/usd-rub")
            otvet = resp.read()
            price = float(otvet[48:53])
            print("Seychas dollar stoit: ", price)
            total = money * price
            print("Itogo: ", total)
        elif cnvs == 2:
            resp = urllib.request.urlopen("https://api.cryptonator.com/api/ticker/eur-rub")
            otvet = resp.read()
            price = float(otvet[48:53])
            print("Seychas evros stoit: ", price)
            total = money * price
            print("Itogo: ", total)
        elif cnvs == 3:
            resp = urllib.request.urlopen("https://api.cryptonator.com/api/ticker/btc-rub")
            otvet = resp.read()
            price = float(otvet[48:56])
            print("Seychas bitok stoit: ", price)
            total = money * price
            print("Itogo: ", total)
        else:
            print("Ok edem dalshe")
            total = money
        mrate = (rate / 1200)
        plata = (mrate * ((1 + mrate) ** period))/(((1 + mrate) ** period) - 1) * total
        pere = (plata * period - total)
        print(" V obshem ty budesh platit po: ", round(plata, 2), " rub ", period, " mesyacev.")
        print("I pereplatish: ", round(pere, 2), " rub.^^")
main()

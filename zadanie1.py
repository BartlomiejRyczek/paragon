from py_markdown_table.markdown_table import markdown_table

suma_vat23= 0
suma_vat8= 0
suma_vat5= 0
suma_vat0= 0
stawka = ''

while stawka !='koniec':
    print("Jeśli chcesz zakończyć podawanie produktów wpisz 'koniec'")
    if stawka == 'koniec':
        break
    stawka = input("Podaj stawke vat: ")
    if stawka == '23' or stawka == '23%':
        kwota = int(input("Podaj kwotę: "))
        suma_vat23 += kwota
    elif stawka == '8' or stawka == '8%':
        kwota = int(input("Podaj kwotę: "))
        suma_vat8 += kwota
    elif stawka == '5' or stawka == '5%':
        kwota = int(input("Podaj kwotę: "))
        suma_vat5 += kwota
    elif stawka == '0' or stawka == '0%':
        kwota = int(input("Podaj kwotę: "))
        suma_vat0 += kwota
    elif stawka == 'koniec':
        break
    elif stawka != ['23','23%','8','8%','5','5%','0','0%']:
        print("Podana stawka jest nieprawidłowa.")

netto_vat23= suma_vat23 - suma_vat23*0.23
netto_vat8= suma_vat8 - suma_vat8* 0.08
netto_vat5= suma_vat5 - suma_vat5* 0.05
netto_vat0= suma_vat0



data = [
    {
        "": "VAT 0%",
        
        "Total netto": netto_vat0,
        "Price": suma_vat0
    },
    {
        "": "VAT 5%",
        "Total netto": netto_vat5,
        "Price": suma_vat5
    },
    {
        "": "VAT 8%",
        "Total netto": netto_vat8,
        "Price": suma_vat8
    },
    {
        "": "VAT 23%",
        "Total netto": netto_vat23,
        "Price": suma_vat23
    },
]
markdown = markdown_table(data).get_markdown()
print(markdown)
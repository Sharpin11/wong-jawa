# suhu c ke suhu lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('masukan suhu dalam celcius : '))

#celcius ke reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")

#celcius ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "fahrenheit")

#celcius ke kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "kelvin")
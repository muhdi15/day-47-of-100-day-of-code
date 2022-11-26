# INI ADALAH PROGRAM PERBANDINGAN BMI

tinggi = float(input("Masukkan tinggi badan anda : "))
berat = float(input("Masukkan berat anda : "))

hasil = berat / (tinggi * tinggi)

if(hasil < 17.0):
    print("anda sangat kurus")
elif(hasil >= 17.0 and hasil <= 25.5):
    print("BMI anda Normal")
elif(hasil >=25.1 and hasil <= 27.0):
    print("Anda cukup Gemuk")
elif(hasil > 27.0):
    print("Obesitas")
    



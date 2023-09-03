import random

skor_pemain = 0
skor_cpu = 0

options = ["kertas", "batu", "gunting"]

while True:
    pemain = input("pilih kertas, gunting atau batu? ").lower()
    if pemain == "q":
        break
    
    if pemain not in options:
        continue

    random_number = random.randint(0, 2)
    # kertas: 0, gunting: 1, batu: 2
    pilihan_cpu = options[random_number]
    print("Computer memilih", pilihan_cpu)

    if pemain == "batu" and pilihan_cpu == "gunting":
        print("pemain menang")
        skor_pemain += 1
    elif pemain == "gunting" and pilihan_cpu == "kertas":
        print("pemain menang")
        skor_pemain += 1
    elif pemain == "kertas" and pilihan_cpu == "batu":
        print("pemain menang")
        skor_pemain += 1   
    elif pemain == "kertas" and pilihan_cpu == "kertas":
        print("seri")
        skor_pemain += 0
    elif pemain == "batu" and pilihan_cpu == "batu":
        print("seri")
        skor_pemain += 0
    elif pemain == "gunting" and pilihan_cpu == "gunting":
        print("seri")
        skor_pemain += 0    
    else :
        print("kamu kalah")
        skor_cpu += 1

print("skor kamu adalah", skor_pemain, "kali")
print("cpu menang", skor_cpu, "kali")
print("Bye! Bye!")
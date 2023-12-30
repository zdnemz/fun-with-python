import datetime as dt
import sys

while True:
    print(' ' + '\n' + 15*'=' + 'MENGHITUNG HARI' + 15*'=' + '\n')
    print('Masukkan Tanggal, Bulan, dan Tahun')

    try:
        hari = int(input('Masukkan tanggal \t: '))
        bulan = int(input('Masukkan bulan \t\t: '))
        tahun = int(input('Masukkan tahun \t\t: '))
    except ValueError:
        print('Masukan harus berupa angka. Silakan coba lagi.')
        continue

    date = dt.date(tahun, bulan, hari)
    today = dt.date.today()

    restart = ''
    while restart.lower() not in ['yes', 'y', 'iya', 'ya', 'no', 'n', 'g', 'ga', 'gak']:
        print(' ' + '\n' + 45*'=' + '\n')
        restart = input(f'Apakah {date} Sudah Benar? \t\t: ')
        if restart == 'no' or restart == 'g' or restart == 'ga' or restart == 'gak' or restart == 'n':
            print('Anda Bisa Menginputnya Ulang')
        elif restart == 'yes' or restart == 'y' or restart == 'ya' or restart == 'iya':
            date_1 = today - date
            if date_1.days < 0:
                print(' ' + '\n' + 45*'=' + '\n')
                print(f'Akan Datang \t\t\t: {-date_1.days} Hari Lagi')
                tahun = abs(date_1.days // 365.25)
                bulan = abs((date_1.days % 365.25) // 30)
                hari = abs((date_1.days % 365.25) % 30)
                print(f'Jika Dikonversi Akan Sekitar \t: {int(tahun)} Tahun, {int(bulan)} Bulan, {int(hari)} Hari Lagi')
            else:
                print(' ' + '\n' + 45*'=' + '\n')
                print(f'Sudah Berlalu \t\t\t: {date_1.days} Hari')
                tahun = abs(date_1.days // 365.25)
                bulan = abs((date_1.days % 365.25) // 30)
                hari = abs((date_1.days % 365.25) % 30)
                print(f'Jika Dikonversi Akan Sekitar \t: {int(tahun)} Tahun, {int(bulan)} Bulan, {int(hari)} Hari')
        else:
            print('Maaf Saya Tidak Mengerti, Bisakah Anda Mengulanginya Lagi')

        restart_1 = ''
        while restart_1.lower() not in ['yes', 'y', 'iya', 'ya', 'no', 'n', 'g', 'ga', 'gak']:
            print(' ' + '\n' + 45*'=' + '\n')
            restart_1 = input('Apakah anda ingin mengulanginya lagi?\t: ')
            if restart_1 == 'yes' or restart_1 == 'y' or restart_1 == 'ya' or restart_1 == 'iya':
                print('Baiklah Kalo Begitu')
                break
            elif restart_1 == 'no' or restart_1 == 'g' or restart_1 == 'ga' or restart_1 == 'gak' or restart_1 == 'n':
                print('Baiklah Saya Akan Berhenti')
                sys.exit(0)
            else:
                print('Maaf saya tidak mengerti, Bisakah anda mengulanginya lagi')

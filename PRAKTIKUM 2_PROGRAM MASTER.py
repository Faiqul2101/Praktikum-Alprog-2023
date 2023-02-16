from datetime import datetime

# Deklarasi Jenis Item
itemdijual = ['sabun cair', 'sabun cuci', 'sampo keratin', 'sikat gigi', 'minuman Dingin', 'makanan ringan', 'mi instan', 'air mineral']
listharga = [200000, 120000, 190000, 180000, 210000, 170000, 110000, 220000]

listitemdibeli = []
listharganow = []
listtotalharga = []
listkuantitas = []

waktunow = datetime.now()
formatwaktu = waktunow.strftime('%A, %d %B %Y')

# Login
print("Login LOSIK Grocery")
userpass = {'admin' : '123'}
coba = 0
while coba < 3:
    Username = str(input("Masukkan Username Anda : "))
    Password = str(input("Masukkan Password Anda : "))
    if Username in userpass and userpass[Username] == Password:
        print("Login Berhasil\n")
        break
    elif coba == 2:
        print("Terminated\n")
        exit()
    else:
        print("Login Gagal\n")
        coba += 1


# Input Item 
print("Item yang Dibeli")
while True:
    inputitem = input('Silahkan Masukkan Jenis Item \t\t: ').lower()
    inputjumlah = input('Silahkan Masukkan Jumlah Item \t\t: ')

    if inputitem in listitemdibeli:
        i = 0
        while i < len(listitemdibeli):
            if listitemdibeli[i] == inputitem:
                x = i
                listtotalharga[x] += (listharga[x]*int(inputjumlah)) 
                listkuantitas[x] += int(inputjumlah)
            i += 1  
    else:
        listitemdibeli.append(inputitem)
        listkuantitas.append(int(inputjumlah))
        i = 0
        while i < len(itemdijual):
            if itemdijual[i] == inputitem:
                x = i
                listharganow.append(listharga[x])
                listtotalharga.append(listharga[x]*int(inputjumlah))                   
            i +=1
    print(listitemdibeli)
    print(listkuantitas)
    print(listtotalharga)
    print(listharganow)

    tanya = input('Apakah Ingin Menambah Item? (y/n) \t: ')
    if tanya == 'n':
        break
    elif tanya == 'y':
        True
    else:
        quit()


# Rincian Pembelian
print("\nRincian Pembelian")
print("| No | Item Dibeli\t | Kuantitas\t | Harga Satuan\t | Harga Total\t |")
i = 0
while i < len(listitemdibeli):
    print(
        '|', str(i+1),
        ' |', listitemdibeli[i], 
        '\t |', listkuantitas[i],
        '\t\t |', listharganow[i],
        '\t |', listtotalharga[i],
        '\t |')
    i +=1
print('Total Pembelian : Rp{:,.2f}'.format(sum(listtotalharga)))

# Pembayaran
print("\nPembayaran")
inputmetodebayar = input('Masukkan Metode Pembayaran \t\t: ').lower()
totalbayar = sum(listtotalharga)
if inputmetodebayar != 'cash':
    if inputmetodebayar == 'debit':
        totalbayar *= 0.95
        kembalian = 0
    elif inputmetodebayar == 'e-wallet':
        totalbayar *= 0.93
        kembalian = 0       
   
    if sum(listtotalharga) >= 500000:
        diskon2 = 20000
        totalbayar -= diskon2
    else:
        diskon2 = 0
    nominalbayar = totalbayar

elif inputmetodebayar == 'cash':
    if sum(listtotalharga) >= 500000:
        diskon2 = 20000
        totalbayar -= diskon2
    else:
        diskon2 = 0
    while True:
        print('Total Harga \t\t\t\t: Rp{:,.2f}'.format(totalbayar))
        nominalbayar = int(input('Masukkan Nominal Pembayaran Cash \t: '))
        kembalian = nominalbayar - totalbayar

        if nominalbayar < totalbayar:
            print('Jumlah Pembayaran kurang dari Total Pembelian! \n')
            True
        else:
            break

totaldiskon = int(sum(listtotalharga) - totalbayar)

# Rincian Pembayaran
print('\nRincian Pembayaran')
print('Tanggal Pembelian \t:', formatwaktu)
print('1.Total Pembelian \t: Rp{:,.2f}'.format(sum(listtotalharga)))
print('2.Nilai Diskon \t\t: Rp{:,.2f} (%{} +Rp.{:,.2f})'.format(totaldiskon,inputmetodebayar,diskon2 ))
print('3.Total Harga \t\t: Rp{:,.2f}'.format(int(totalbayar)))
print('4.Total Pembayaran \t: Rp{:,.2f}'.format(int(nominalbayar)))
print('5.Jumlah Kembalian \t: Rp{:,.2f}'.format(kembalian))
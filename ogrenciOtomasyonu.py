
dosya = open('ogrencibilgileri.txt')

print('''
                    ÖĞRENCİ BİLGİLERİ OTOMASYON PROJESİ
      ----------------- Yapabiliceğiniz İşlemler -----------------
      
      1-Ekle
      
      

      '''  
)

secim = int(input('Yapmak istediğiniz İşlemi Seçiniz: '))

while True:
    if secim == 1:
        dosya = open('ogrencibilgiler.txt','a')
        ad = input('Öğrenci İsmi: ')
        soyad = input('Öğrenci Soyadı: ')
        no = int(input('Öğrenci No:'))

        dosya.write('\n')
        dosya.write('-----------------------------------')
        dosya.write('\n')
        dosya.write('Öğrenci ismi'+ ad)
        dosya.write('\n')
        dosya.write('Öğrenci Soyisim'+ soyad)
        dosya.write('\n')
        dosya.write('Öğrenci Numarası'+ str(no))
        dosya.write('\n')
        dosya.write('-----------------------------------')
        break
    
dosya.close()
#BURDA DOSYA AÇMA İŞLEMİ YAPTIK TXT DOSYASINA ARDINDAN BİR EKLEME İŞLEMİ YAPTIK DOSYAYA 
#OLUŞTURDUGUMUZ KODLARLA İNPUT BİLGİLERİNE BAĞLI ÖĞRENCİ AD SOYAD NO BİLGİLERİNİ DOSYAMI KAYIT ETTİK.

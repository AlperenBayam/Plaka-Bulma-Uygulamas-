sehirler = ['Adana', 'Adıyaman', 'Afyonkarahisar', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin', 'Aydın','Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa','Çanakkale', 'Çankırı', 'Çorum','Denizli', 'Diyarbakır','Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir','Gaziantep', 'Giresun', 'Gümüşhane','Hakkâri', 'Hatay','Isparta', 'Mersin', 'Istanbul', 'Izmir','Kars', 'Kastamonu', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya','Malatya', 'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde','Ordu', 'Rize','Sakarya', 'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli','Şanlıurfa', 'Uşak', 'Van','Yozgat','Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak', 'Bartın', 'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce']

plakalar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]

want1 = int(input('Şehirdenmi Plaka Seçmek İstersiniz Yoksa Plakadan Şehirmi Eğer 1.Seçenekse 1 2.Seçenekse 2 Yazınız : '))

if want1 == 1:
    want = input('İstenilen Şehir Bilgisini Giriniz : ')
    result = (plakalar[sehirler.index(want.title())])
    print(f'{want} şehrinin plakası:',result)



elif want1 == 2:
    want3 = int(input('İstenilen Plaka Bilgisini Giriniz : '))
    result2 = (sehirler[(plakalar.index(want3))])
    print('İstenilen Plaka Bu Şehre Ait:',result2)
else:
    print('Geçersiz Veya Hatalı Seçim')
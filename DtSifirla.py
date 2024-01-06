import sqlite3

# SQLite veritabanına bağlan
with sqlite3.connect('ders_programi.db') as conn:
    cursor = conn.cursor()

    # Tabloları sil
    cursor.execute('DROP TABLE IF EXISTS HocaDers')
    cursor.execute('DROP TABLE IF EXISTS Kisitlar')
    cursor.execute('DROP TABLE IF EXISTS Siniflar')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS HocaDers (
            HocaID INTEGER PRIMARY KEY,
            HocaAdi TEXT,
            DersID INTEGER,
            DersAdi TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Kisitlar (
            HocaID INTEGER,
            HaftaninGunu TEXT,
            SaatAraligi TEXT,
            Kac TEXT,
            Sinif TEXT,
            PRIMARY KEY (HocaID, HaftaninGunu, SaatAraligi, Kac, Sinif),
            FOREIGN KEY (HocaID) REFERENCES HocaDers(HocaID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Siniflar (
            SinifID INTEGER PRIMARY KEY,
            SinifAdi TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO HocaDers (HocaAdi, DersID, DersAdi) VALUES
            ('Serdar Solak', 1, 'BSM-Giriş'),
            ('Süleyman Eken', 2, 'Proje-A'),
            ('Yavuz Selim FATİHOĞLU', 3, 'Yaz-Gel'),
            ('Hikmet Hakan GÜREL', 4, 'Fizik'),
            ('Yavuz Selim FATİHOĞLU', 5, 'Algoritma Programlama'),
            ('Prof. Dr. Hikmet Hakan GÜREL', 6, 'Fizik'),
            ('Doç. Dr. Vildan ÇETKİN', 7, 'Diferansiyel Denklemler'),
            ('Öğr. Gör. Kerem ÇOLAK', 8, 'İşletme Ekonomisi'),
            ('Dr. Öğr. Üyesi Önder YAKUT', 9, 'Web Tasarımı')
    ''')

    cursor.execute('''
        INSERT INTO Kisitlar (HocaID, HaftaninGunu, SaatAraligi, Kac, Sinif) VALUES
            (1, 'Cuma', '10:00-12:00', '1.Sınıf', 'A103'),
            (3, 'Cuma', '15:00-17:00', '1.Sınıf', 'B202'),
            (5, 'Pazartesi', '14:00-16:50', '1.Sınıf', '1040'),
            (4, 'Pazartesi', '10:00-12:50', '1.Sınıf', '1040'),
            (3, 'Sali', '10:00-12:50', '1.Sınıf', '1044'),
            (2, 'Cuma', '10:00-12:50', '1.Sınıf', '1044'),
            (6, 'Pazartesi', '09:00-12:50', '1.Sınıf', '1044'),
            (7, 'Çarşamba', '14:00-15:50', '1.Sınıf', '1041'),
            (8, 'Pazartesi', '09:00-10:50', '1.Sınıf', '1036')
    ''')
    cursor.execute('''
        INSERT INTO Siniflar (SinifAdi) VALUES
            ('1044'),
            ('1040'),
            ('1036'),
            ('1041')
    ''')
print("Veritabanı temizlendi ve tablolar oluşturuldu.")

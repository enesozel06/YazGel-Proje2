import sqlite3
import networkx as nx
import matplotlib.pyplot as plt

def create_tables(conn):
    cursor = conn.cursor()

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

    conn.commit()


def get_class_schedule(conn, class_name):
    cursor = conn.cursor()

    cursor.execute('''
        SELECT HocaID, DersID, HocaAdi, DersAdi
        FROM HocaDers
    ''')
    hoca_dersleri = cursor.fetchall()

    cursor.execute('''
        SELECT DISTINCT Kisitlar.HocaID, Kisitlar.HaftaninGunu, Kisitlar.SaatAraligi, Kisitlar.Kac, Kisitlar.Sinif
        FROM Kisitlar
        JOIN HocaDers ON Kisitlar.HocaID = HocaDers.HocaID
        WHERE Kisitlar.Sinif = ?
    ''', (class_name,))
    kisitlar = cursor.fetchall()

    cursor.execute('''
        SELECT SinifID, SinifAdi
        FROM Siniflar
        WHERE SinifAdi = ?
    ''', (class_name,))
    class_info = cursor.fetchone()

    if class_info is None:
        print(f"{class_name} sınıfı bulunamadı.")
        return

    class_id, _ = class_info

    G = nx.Graph()

    G.add_edges_from([(hocaID, dersID) for hocaID, dersID, _, _ in hoca_dersleri])

    days = ['Pazartesi', 'Sali', 'Çarşamba', 'Perşembe', 'Cuma']

    fig, axs = plt.subplots(1, len(days), figsize=(15, 7), sharey=True)

    for i, day in enumerate(days):
        day_courses = [(course[0], course[2], course[3], kisit[2], kisit[3]) for course in hoca_dersleri for kisit in kisitlar if course[0] == kisit[0] and kisit[1] == day and kisit[4] == class_name]
        daily_graph = G.subgraph([course[0] for course in day_courses])

        if not daily_graph:
            pos = {node: (0, 0) for node in day_courses}
        else:
            pos = nx.spring_layout(daily_graph)

        labels = {node: f"{hoca_dersleri[node-1][2]}\n{hoca_dersleri[node-1][3]}\n{course[3]}\n{course[2]}" for node, course in zip(daily_graph.nodes, day_courses)}

        nx.draw(daily_graph, pos, with_labels=True, labels=labels, ax=axs[i])
        axs[i].set_title(day)
        # Günler arası çizgi ekle
        if i > 0:
            axs[i].axvline(x=0, color='black', linestyle='--')

    plt.show()

def main():
    conn = sqlite3.connect(':memory:')

    create_tables(conn)

    class_name = input("Hangi sınıfın ders programını görmek istiyorsunuz? (Örneğin, 1044): ")

    get_class_schedule(conn, class_name)

    conn.close()

if __name__ == "__main__":
    main()

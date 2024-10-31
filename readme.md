Yazılım geliştirme laboratuvarı. - 2. Projesi 181307008

Ders veren hocaların kısıtları (aynı hocanın derslerinin cakismamasi, hocanın dersini
istenilen gune atama, sınıf sayıları-isimleri gibi) dikkate alınarak çizge renklendirme
yöntemlerinden biri ile ders programı hazırlanması. Veri tabanı kontrol ekranı ile bu verilerin düzenlenmesi.

Proje Özeti : Projede, kullanıcının derslik seçtikten sonra o dersliğe ait ders programınının ekrana çizge renklendirme algoritmaları ile çizilmesidir. Veri tabanı kontrolü için bir kontrol paneli bulunmaktadır.

Proje Geliştirme Ortamı : Python (sqlite3 - networkx as nx - matplotlib.pyplot) - SqlLite - HTML - CSS

Python Projesini Oluşturun: VSCode kullanarak pip install özelliği ile gerekli kütüphaneleri indirin. İşlemleri tamamladıktan sonra veri tabanı ismini ders_programi.db olarak ayarlayın. API'leri kullanmak için dosya yollarını doğru yazdığınızdan emin olun. Veri tabanı kontrolü ekranı için flask_py kodlarını çalıştırın. Templates dosyası içerisinde index.html ve stlye.css dosyalarının varlığından emin olun.

API'lerin kullanımı
API.py : Tüm ders programını veri seti olarak vermektedir.
APIderslik.py : Uzantı olarak gönderdiğiniz derslik adı ile o dersliğe ait ders programını veri seti olarak vermektedir.

Veri tabanı hatalarını aldığınız takdirde DtSifirla.py dosyasını çalıştırarark veri tabanını sıfırlayabilirsiniz. Proramın çalıştığı ders_programi.py dosyası başlangıçta verileri tekrar doldurduğu için yapacağınız işlem sonrasında verileriniz tekrar gelecektir. 

Veri ekleme yaparken veri tabanında yer aldığı gibi gün isimlerini girmeniz gerekmektedir. Aynı gün aynı saatte aynı derslikte ders eklemesi yapılmamaktadır. Aynı gün aynı saatte ders eklemenin tek yolu farklı bir derslikte olmasıdır.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ar Haftalık ders programı uygulaması(+20 Puan)

Proje Özeti 
Bu proje, Kocaeli Üniversitesi dersliklerinin haftalık ders programlarını gösteren bir artırılmış gerçeklik (AR) uygulamasını içermektedir. Unity oyun motoru kullanılarak geliştirilmiş ve SQL Server üzerindeki veritabanından ders programı bilgilerini API aracılığıyla çekmektedir.Projede Bir adet side bar bulunmaktadır bu menü aracılığı ile kullanıcı istediği dersliğe tıkladığında ekrana seçilen dersilin haftalık dersleri, saatleri ve derslik bilgileri gelmektedir 

Geliştirme Ortamı
Unity 3D v2021.2.3f1
C# Programlama Dili(web api)
SQL Server

# Faz 0: Başlangıç Kodunun Analizi (Konu B: Dosya Dönüştürücü)

## Tespit Ettiğim Tasarım Sorunları

1. **Açık/Kapalı Prensibinin (OCP) İhlali:** Sisteme yeni bir dosya formatı (örn: JPEG) eklenmek istendiğinde, doğrudan `convert_file` metodunun içindeki `if-elif` zincirine müdahale edilmesi gerekmektedir. Bu durum mevcut kodun bozulma riskini artırmakta olup, sistemin değişime kapalı ve gelişime açık olması prensibini ihlal etmektedir.

2. **Tek Sorumluluk Prensibinin (SRP) İhlali:** `FileConverter` sınıfı, hem hangi dönüştürme işleminin yapılacağına karar verme kontrolünü (if-elif blokları) hem de dönüştürme işleminin doğrudan uygulanma detaylarını aynı anda üstlenmektedir. Bir sınıfın değişmek için tek bir nedeni olması gerekirken, mevcut yapı çoklu sorumluluk barındırmaktadır.

3. **God Class (Her Şeyi Yapan Sınıf) Potansiyeli:** Mevcut kodda sadece 3 format destekleniyor olsa da, ilerleyen aşamalarda desteklenen format sayısının artmasıyla `FileConverter` sınıfı yönetilmesi, okunması ve test edilmesi oldukça güç, devasa bir sınıfa dönüşme potansiyeli taşımaktadır.

4. **Nesne Yönelimli Yaklaşım (OOP) Eksikliği:** Dönüştürülecek format yapıları (PDF, Word, Excel vb.) bağımsız sınıflar olarak soyutlanmamıştır. İşlem akışı tamamen metin (string) eşleştirmeleri üzerinden ilerlemekte olup, bu durum sistemi katı ve hataya açık hale getirmektedir.

5. **Ortak Bir Arayüz (Interface) Eksikliği:** Farklı format dönüştürücüleri için ortak bir arayüz veya soyut temel sınıf (abstract class) bulunmamaktadır. Bu eksiklik, yeni formatların sisteme entegre edilmesi sürecinde standart bir sözleşme (contract) sunmadığı için esnekliği ve genişletilebilirliği kısıtlamaktadır.
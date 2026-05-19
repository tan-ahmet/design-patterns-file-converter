# Faz 0: Başlangıç Kodunun Analizi (Konu B: Dosya Dönüştürücü)

## Tespit Ettiğim Tasarım Sorunları

1. **Açık/Kapalı Prensibinin (OCP) İhlali:** Sisteme yeni bir dosya formatı (örn: JPEG) eklenmek istendiğinde, doğrudan `convert_file` metodunun içindeki `if-elif` zincirine müdahale edilmesi gerekmektedir. Bu durum mevcut kodun bozulma riskini artırmakta olup, sistemin değişime kapalı ve gelişime açık olması prensibini ihlal etmektedir.

2. **Tek Sorumluluk Prensibinin (SRP) İhlali:** `FileConverter` sınıfı, hem hangi dönüştürme işleminin yapılacağına karar verme kontrolünü (if-elif blokları) hem de dönüştürme işleminin doğrudan uygulanma detaylarını aynı anda üstlenmektedir. Bir sınıfın değişmek için tek bir nedeni olması gerekirken, mevcut yapı çoklu sorumluluk barındırmaktadır.

3. **God Class (Her Şeyi Yapan Sınıf) Potansiyeli:** Mevcut kodda sadece 3 format destekleniyor olsa da, ilerleyen aşamalarda desteklenen format sayısının artmasıyla `FileConverter` sınıfı yönetilmesi, okunması ve test edilmesi oldukça güç, devasa bir sınıfa dönüşme potansiyeli taşımaktadır.

4. **Nesne Yönelimli Yaklaşım (OOP) Eksikliği:** Dönüştürülecek format yapıları (PDF, Word, Excel vb.) bağımsız sınıflar olarak soyutlanmamıştır. İşlem akışı tamamen metin (string) eşleştirmeleri üzerinden ilerlemekte olup, bu durum sistemi katı ve hataya açık hale getirmektedir.

5. **Ortak Bir Arayüz (Interface) Eksikliği:** Farklı format dönüştürücüleri için ortak bir arayüz veya soyut temel sınıf (abstract class) bulunmamaktadır. Bu eksiklik, yeni formatların sisteme entegre edilmesi sürecinde standart bir sözleşme (contract) sunmadığı için esnekliği ve genişletilebilirliği kısıtlamaktadır.

## Yapay Zeka (AI) Karşılaştırması

**Kullanılan AI Aracı:** Claude / ChatGPT
**Kullanılan Prompt:** *"Bu kodda hangi tasarım sorunlarını görüyorsun? Hangi tasarım örüntüleri bu sorunları çözebilir? Her sorun için kısa bir açıklama yaz."*

### AI'ın Tespitleri (Özet)
1. **OCP ve SRP İhlali:** Kodun yeni formatlara kapalı olduğu ve `FileConverter` sınıfının dönüştürme işinin tüm detaylarını bilerek çok fazla sorumluluk aldığı belirtildi. (Çözüm Önerisi: Factory Method veya Strategy örüntüsü).
2. **Tight Coupling (Sıkı Bağlılık):** Sınıfın doğrudan `string` değerlere (pdf, word) sıkı sıkıya bağlı olduğu, bu durumun esnekliği yok ettiği vurgulandı.
3. **Missing Abstraction (Soyutlama Eksikliği):** Dönüştürücülerin ortak bir arayüzden (Interface) türetilmediği belirtildi. (Çözüm Önerisi: Adapter veya Strategy).
4. **Hardcoded (Sabit) Kodlama:** Koşulların koda gömülü olduğu, bunun yerine polimorfizm (çok biçimlilik) kullanılarak nesne tabanlı bir yönetime geçilmesi gerektiği söylendi.

### Karşılaştırma ve Değerlendirme (Benim Gördüklerim vs. AI'ın Gördükleri)
* **Benzerlikler:** Hem benim hem de yapay zekanın ilk ve en önemli tespiti Açık/Kapalı Prensibi (OCP) ve Tek Sorumluluk Prensibi (SRP) ihlalleri oldu. Her ikimiz de `if-elif` zincirlerinin ileride büyük bir probleme (Spagetti koda) yol açacağında hemfikiriz.
* **Farklılıklar:** Ben sorunları daha çok "Nesne olmaması" ve "God Class potansiyeli" gibi mimari tehlikeler üzerinden tanımlarken; yapay zeka bu sorunları "Tight Coupling" (Sıkı Bağlılık) ve "Polimorfizm eksikliği" gibi daha akademik/teknik terimlerle ifade etti. Ayrıca AI, sadece sorunları tespit etmekle kalmayıp doğrudan *Factory Method* ve *Strategy* gibi potansiyel çözüm örüntülerini (design patterns) öne sürdü.
* **Sonuç:** Tespit ettiğimiz temel mimari darboğazlar tamamen birbiriyle örtüşüyor.
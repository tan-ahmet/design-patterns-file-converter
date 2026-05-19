# Faz 3 - Yapay Zeka (AI) ile Pair Programming Günlüğü

**Kullanılan AI Aracı:** ChatGPT Plus
**Süre:** 35 Dakika
**Konu:** Davranışsal (Behavioral) örüntülerin sisteme entegrasyonu ve CI/CD kurulumu.

### Oturum Özeti ve Tartışılanlar
AI ile oturuma başlarken sistemin mevcut (Adapter ve Decorator içeren) halini paylaştım. Dosya dönüştürme işlemi tamamlandığında farklı sistemlerin (E-posta, SMS, Log) uyarılmasını sağlayacak bir yapı ve dönüştürülen dosyaların farklı algoritmalarla (ZIP, RAR) sıkıştırılmasını istedim.

1. **Observer Örüntüsü:** AI, dönüştürme işlemi bitişini dinlemek için Observer Pattern kullanmamızı önerdi. Bir `EventManager` sınıfı yazarak `EmailNotifier` ve `ConsoleLogger` gibi dinleyicileri (subscribers) bu yöneticiye bağladık.
2. **Strategy Örüntüsü:** Sıkıştırma algoritmaları için AI, `if-else` yazmak yerine her algoritmayı kendi sınıfına alan Strategy Pattern önerdi. Birlikte `CompressionStrategy` arayüzünü ve `ZipCompression`, `RarCompression` alt sınıflarını kodladık.

### Refleksiyon Soruları

**Soru 1: AI olmadan bu faz ne kadar sürerdi?**
AI olmadan Observer ve Strategy örüntülerinin interface (arayüz) yapılarını kurmak, özellikle Observer'daki yayıncı-abone (publisher-subscriber) metodolojisini hatasız bir şekilde birbirine bağlamak muhtemelen 3-4 saatimi alırdı. AI ile eşli programlama yapmak bu süreyi 35 dakikaya indirdi, boilerplate (şablon) kodları hızlıca geçip mimariye odaklanmamı sağladı.

**Soru 2: AI sizi nerede yanılttı?**
AI, Strategy ve Observer örüntülerini birleştirirken bir hata yaptı. Sıkıştırma (Strategy) işlemini doğrudan Observer dinleyicilerinin (örneğin Logger sınıfının) içine gömmeyi teklif etti. Ancak bu durum Tek Sorumluluk Prensibi'ne (SRP) tamamen aykırıydı; çünkü bir loglayıcının görevi dosyayı sıkıştırmak değildir. Bu hatayı fark edip AI'ı uyardım ve sıkıştırma stratejisini doğrudan Client (İstemci) seviyesine veya dönüştürücü çekirdeğine alması gerektiğini söyleyerek kodu düzelttirdim.
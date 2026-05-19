# Yazılım Tasarım Örüntüleri Ödevi
**Seçilen Konu:** B - Dosya Dönüştürücü
**Gerekçe:** Dosya dönüştürme işlemleri yeni formatların eklenmesine çok açıktır. Başlangıçta iç içe geçmiş `if-else` bloklarıyla yönetilemez hale gelen bu ilkel yapının, örüntüler sayesinde nasıl esnek bir "tak-çalıştır" sistemine dönüştüğünü göstermek için seçilmiştir.

## Projenin Amacı
Bu proje, yazılım mimarisinde sıkça karşılaşılan "kötü tasarım" (spagetti kod) sorunlarını tespit etmeyi ve bu sorunları 3 farklı fazda Creational, Structural ve Behavioral tasarım örüntüleri kullanarak modüler, genişletilebilir ve SOLID prensiplerine uygun profesyonel bir yapıya dönüştürmeyi amaçlamaktadır.

## Kullanılan Tasarım Örüntüleri
* **Factory Method (Creational):** Nesne yaratma mantığı merkezi bir fabrikaya taşındı.
* **Adapter (Structural):** Uyumsuz dış bir CSV kütüphanesi sisteme entegre edildi.
* **Decorator (Structural):** Orijinal kodu bozmadan nesnelere çalışma zamanında dinamik olarak Filigran (Watermark) eklendi.
* **Observer (Behavioral):** İşlem durumlarını (başarılı/hata) e-posta veya log sistemlerine iletmek için abone/yayıncı mantığı kuruldu.
* **Strategy (Behavioral):** Sıkıştırma algoritmaları (ZIP, RAR) birbirinden ayrılarak çalışma zamanında dinamik olarak seçilebilir hale getirildi.

## Mimari Diyagram
*(Not: Tam diyagram ve detaylar PATTERNS.md içindedir).*
```mermaid
classDiagram
    ConverterApplication --> ConverterFactory : Uses
    ConverterApplication --> EventManager : Triggers
    ConverterApplication --> CompressionStrategy : Executes
# Faz 2 - Yapay Zeka (AI) Günlüğü

**Kullanılan AI Aracı:** ChatGPT
**Süre:** Yaklaşık 20 dakika

**Benim Sorum (Prompt):** "Dosya dönüştürücü sistemime dışarıdan bir CSV çevirici (farklı metot isimlerine sahip) ekleyeceğim. Ayrıca dosyalara filigran eklemek istiyorum. CSV entegrasyonu için Adapter pattern burada uygun mu, yoksa Facade mı? Farkını açıkla."

**AI'ın Yanıtı (Özet):**
Yapay zeka, Adapter örüntüsünün uyumsuz iki arayüzü birbirine bağlamak için kullanıldığını; Facade örüntüsünün ise karmaşık bir alt sistem (birçok sınıftan oluşan bir yapı) için basitleştirilmiş tek bir arayüz sunduğunu belirtti. CSV entegrasyonu için Adapter'ın uygun olduğunu söyledi. Filigran ekleme işlemi için ise özelliklerin dinamik olarak eklenebilmesi adına Decorator örüntüsünü önerdi.

**AI'ı Nerede Yakaladım / Hangi Konuda Eksikti?**
AI, Facade ve Adapter farkını teorik olarak doğru açıklasa da benim bağlamım için eksik bir yönlendirme yaptı. AI, Facade örüntüsünü tamamen farklı bir şeymiş gibi anlattı; ancak aslında benim CSV dönüştürücüm kendi içinde çok karmaşık bir kütüphane (okuyucu, ayrıştırıcı ve yazıcı alt sınıfları) olabilirdi. Eğer durum böyle olsaydı, Adapter ile birlikte bir Facade kullanmam gerekebilirdi. AI bu iki örüntünün birbirini dışlamadığını, aksine birlikte çok iyi çalışabileceğini belirtmeyi unuttu. Ben sadece tek bir uyumsuz sınıfı entegre edeceğim için Adapter'da karar kıldım. Özellik ekleme (Filigran) için önerdiği Decorator ise tamamen doğru ve OCP prensibine uygun bir tercih.
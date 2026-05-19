# Faz 1 - Yapay Zeka (AI) Günlüğü

**Kullanılan AI Aracı:** ChatGPT
**Süre:** Yaklaşık 15 dakika

**Benim Sorum (Prompt):** "Dosya dönüştürücü kodumda nesne yaratma işlemleri tek bir sınıfa gömülü. Factory Method tasarım örüntüsünü bu sorunu çözmek için nasıl kullanabilirim? Bana doğrudan kodu verme, sadece mimari mantığını ve arayüz (interface) tasarımını nasıl yapmam gerektiğini açıkla."

**AI'ın Yanıtı (Özet):**
Yapay zeka, doğrudan kodu vermek yerine mantığı açıkladı. `FileConverter` adında soyut (abstract) bir temel sınıf oluşturmamı ve içerisine `convert()` adında bir metot koymamı önerdi. Daha sonra PDF, Word ve Excel için bu sınıftan türeyen alt sınıflar yaratmamı söyledi. Son olarak, sadece nesne üretmekle görevli bir `Factory` (Fabrika) sınıfı kurmamı ve `if-elif` bloklarını sadece bu fabrikanın içine yerleştirmemi tavsiye etti.

**Ne Uyguladım ve Neden?**
AI'ın önerdiği soyutlama (abstraction) mantığını tamamen uyguladım. Ancak AI'ın bahsettiği fabrika metodunu dinamik sınıf çağırma (reflection) ile yapmak yerine, şimdilik daha okunabilir olduğu için statik bir metot (`@staticmethod`) ve basit koşullar ile kendim yazdım. Bu sayede kodun kontrolü tamamen bende kaldı ve doğrudan kopyalamamış oldum.
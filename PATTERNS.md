# Projede Kullanılan Tasarım Örüntüleri (Design Patterns)

## 1. Factory Method (Fabrika Metodu) - Creational
**Uygulandığı Faz:** Faz 1
**Uygulandığı Yer:** `src/converter.py` içindeki `ConverterFactory` sınıfı.

**Neden Kullanıldı?**
Başlangıç kodunda `FileConverter` sınıfı hem hangi nesnenin yaratılacağına karar veriyor hem de dönüştürme işini yapıyordu. Bu durum Tek Sorumluluk (SRP) prensibini bozuyordu. Nesne yaratma sorumluluğunu iş mantığından ayırmak için kullanıldı.

**Ne Kazandırdı?**
Açık/Kapalı Prensibi (OCP) sağlandı. Artık yeni bir format (örneğin JPEG) eklendiğinde, sadece yeni bir `JPEGConverter` sınıfı yazıp `ConverterFactory` içine tek bir satır eklememiz yeterli olacak. Sistemin geri kalan kodu (iş mantığı) bu değişiklikten hiç etkilenmeyecek.

### Önceki ve Sonraki Mimari (UML)

```mermaid
classDiagram
    direction LR
    
    class FileConverter {
        <<interface>>
        +convert(file_name, to_format)
    }
    
    class PDFConverter {
        +convert(file_name, to_format)
    }
    
    class WordConverter {
        +convert(file_name, to_format)
    }
    
    class ConverterFactory {
        +create_converter(format_type): FileConverter
    }
    
    FileConverter <|-- PDFConverter
    FileConverter <|-- WordConverter
    ConverterFactory ..> FileConverter : Üretir
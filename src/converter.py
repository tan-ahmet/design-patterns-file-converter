from abc import ABC, abstractmethod


class FileConverter(ABC):
    @abstractmethod
    def convert(self, file_name: str, to_format: str) -> None:
        pass

class PDFConverter(FileConverter):
    def convert(self, file_name: str, to_format: str) -> None:
        print(f"PDF dosyası okunuyor... {to_format.upper()} formatına çevriliyor... Başarılı!")

class WordConverter(FileConverter):
    def convert(self, file_name: str, to_format: str) -> None:
        print(f"Word dosyası okunuyor... {to_format.upper()} formatına çevriliyor... Başarılı!")

class ExcelConverter(FileConverter):
    def convert(self, file_name: str, to_format: str) -> None:
        print(f"Excel dosyası okunuyor... Tablolar {to_format.upper()}'e aktarılıyor... Başarılı!")


class LegacyCSVConverter:
    """Dışarıdan alınan, metod isimleri uyumsuz eski bir kütüphane olduğunu varsayalım."""
    def specific_csv_conversion(self, file: str, dest_format: str):
        print(f"Eski CSV motoru çalışıyor... {file}.csv -> {dest_format.upper()} yapılıyor... Başarılı!")

class CSVConverterAdapter(FileConverter):
    """Uyumsuz LegacyCSVConverter'ı standart FileConverter arayüzüne uyarlar."""
    def __init__(self):
        self._legacy_converter = LegacyCSVConverter()

    def convert(self, file_name: str, to_format: str) -> None:

        self._legacy_converter.specific_csv_conversion(file_name, to_format)


class ConverterDecorator(FileConverter):
    """Tüm dekoratörler (eklenti sınıfları) için temel sarmalayıcı (wrapper) sınıf."""
    def __init__(self, wrapped_converter: FileConverter):
        self._wrapped_converter = wrapped_converter

    def convert(self, file_name: str, to_format: str) -> None:
        self._wrapped_converter.convert(file_name, to_format)

class WatermarkDecorator(ConverterDecorator):
    """Dönüştürülen dosyaya filigran ekler."""
    def convert(self, file_name: str, to_format: str) -> None:
        super().convert(file_name, to_format)
        print(f"  [+] EKLENTİ: '{file_name}' dosyasına şirket filigranı (Watermark) eklendi.")

class EncryptionDecorator(ConverterDecorator):
    """Dönüştürülen dosyayı AES ile şifreler."""
    def convert(self, file_name: str, to_format: str) -> None:
        super().convert(file_name, to_format)
        print(f"  [+] EKLENTİ: '{file_name}' dosyası güvenli bir şekilde şifrelendi.")


class ConverterFactory:
    @staticmethod
    def create_converter(format_type: str) -> FileConverter:
        format_type = format_type.lower()
        if format_type == "pdf":
            return PDFConverter()
        elif format_type == "word":
            return WordConverter()
        elif format_type == "excel":
            return ExcelConverter()
        elif format_type == "csv":
            return CSVConverterAdapter()  
        else:
            raise ValueError(f"Hata: {format_type} formatı desteklenmiyor!")

if __name__ == "__main__":
    print("--- [Faz 2: Structural Patterns Uygulaması] ---\n")

    print("1. Adapter (Uyumlandırıcı) Kullanımı:")
    csv_worker = ConverterFactory.create_converter("csv")
    csv_worker.convert("musteri_verileri", "excel")
    
    print("\n2. Decorator (Dekoratör) Kullanımı:")

    base_pdf_worker = ConverterFactory.create_converter("pdf")
    
    watermarked_pdf = WatermarkDecorator(base_pdf_worker)
    secure_and_watermarked_pdf = EncryptionDecorator(watermarked_pdf)
    
    secure_and_watermarked_pdf.convert("gizli_sirket_raporu", "word")
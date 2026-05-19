from abc import ABC, abstractmethod


class FileConverter(ABC):
    """
    Tüm dönüştürücü formatlar için ortak arayüz (Interface/Abstract Class).
    """
    @abstractmethod
    def convert(self, file_name: str, to_format: str) -> None:
        pass


class PDFConverter(FileConverter):
    def convert(self, file_name: str, to_format: str) -> None:
        print("PDF dosyası okunuyor...")
        print(f"{to_format.upper()} formatına çevriliyor...")
        print("İşlem başarılı!\n")


class WordConverter(FileConverter):
    def convert(self, file_name: str, to_format: str) -> None:
        print("Word dosyası okunuyor...")
        print(f"{to_format.upper()} formatına çevriliyor...")
        print("İşlem başarılı!\n")


class ExcelConverter(FileConverter):
    def convert(self, file_name: str, to_format: str) -> None:
        print("Excel dosyası okunuyor...")
        print(f"Tablolar {to_format.upper()}'e aktarılıyor...")
        print("İşlem başarılı!\n")


class ConverterFactory:
    """
    Nesne yaratma sorumluluğunu merkezi hale getiren Fabrika Sınıfı.
    """
    @staticmethod
    def create_converter(format_type: str) -> FileConverter:
        format_type = format_type.lower()
        
        if format_type == "pdf":
            return PDFConverter()
        elif format_type == "word":
            return WordConverter()
        elif format_type == "excel":
            return ExcelConverter()
        else:
            raise ValueError(f"Hata: {format_type} formatı için uygun bir dönüştürücü nesnesi yaratılamadı!")


if __name__ == "__main__":
    print("--- [Faz 1: Factory Method Uygulaması] ---")
    
    try:
        pdf_worker = ConverterFactory.create_converter("pdf")
        pdf_worker.convert("rapor", "word")
        
        excel_worker = ConverterFactory.create_converter("excel")
        excel_worker.convert("hesaplar", "pdf")
        
        
        jpeg_worker = ConverterFactory.create_converter("jpeg")
        jpeg_worker.convert("resim", "pdf")
        
    except ValueError as e:
        print(e)
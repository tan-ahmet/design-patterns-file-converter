from abc import ABC, abstractmethod
from typing import List

class ConverterObserver(ABC):
    @abstractmethod
    def update(self, file_name: str, message: str):
        pass

class ConsoleLogger(ConverterObserver):
    def update(self, file_name: str, message: str):
        print(f"[LOG] '{file_name}' işlemi kaydedildi: {message}")

class EmailNotifier(ConverterObserver):
    def update(self, file_name: str, message: str):
        print(f"[EMAIL] Yöneticiye mail atıldı -> Dosya: '{file_name}' | Durum: {message}")

class EventManager:
    def __init__(self):
        self._listeners: List[ConverterObserver] = []

    def subscribe(self, listener: ConverterObserver):
        self._listeners.append(listener)

    def notify(self, file_name: str, message: str):
        for listener in self._listeners:
            listener.update(file_name, message)

class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, file_name: str):
        pass

class ZipCompression(CompressionStrategy):
    def compress(self, file_name: str):
        print(f"[SIKIŞTIRMA] '{file_name}' dosyası .ZIP olarak sıkıştırıldı.")

class RarCompression(CompressionStrategy):
    def compress(self, file_name: str):
        print(f"[SIKIŞTIRMA] '{file_name}' dosyası .RAR olarak sıkıştırıldı.")

class NoCompression(CompressionStrategy):
    def compress(self, file_name: str):
        pass 

class FileConverter(ABC):
    @abstractmethod
    def convert(self, file_name: str, to_format: str) -> str:
        pass

class PDFConverter(FileConverter):
    def convert(self, file_name: str, to_format: str) -> str:
        print(f"PDF okunuyor... {to_format.upper()} yapılıyor... Başarılı!")
        return f"{file_name}.{to_format}"

class WordConverter(FileConverter):
    def convert(self, file_name: str, to_format: str) -> str:
        print(f"Word okunuyor... {to_format.upper()} yapılıyor... Başarılı!")
        return f"{file_name}.{to_format}"

class LegacyCSVConverter:
    def specific_csv_conversion(self, file: str, dest_format: str):
        print(f"Eski CSV motoru çalışıyor... {file}.csv -> {dest_format.upper()}... Başarılı!")
        return f"{file}.{dest_format}"

class CSVConverterAdapter(FileConverter):
    def __init__(self):
        self._legacy = LegacyCSVConverter()
    def convert(self, file_name: str, to_format: str) -> str:
        return self._legacy.specific_csv_conversion(file_name, to_format)

class ConverterDecorator(FileConverter):
    def __init__(self, wrapped: FileConverter):
        self._wrapped = wrapped
    def convert(self, file_name: str, to_format: str) -> str:
        return self._wrapped.convert(file_name, to_format)

class WatermarkDecorator(ConverterDecorator):
    def convert(self, file_name: str, to_format: str) -> str:
        res = super().convert(file_name, to_format)
        print(f"  [+] EKLENTİ: '{res}' dosyasına Watermark (Filigran) eklendi.")
        return res

class ConverterFactory:
    @staticmethod
    def create_converter(format_type: str) -> FileConverter:
        format_type = format_type.lower()
        if format_type == "pdf": return PDFConverter()
        elif format_type == "word": return WordConverter()
        elif format_type == "csv": return CSVConverterAdapter()
        else: raise ValueError("Desteklenmeyen format!")

class ConverterApplication:
    def __init__(self):
        self.events = EventManager()
        self._compression: CompressionStrategy = NoCompression()

    def set_compression(self, strategy: CompressionStrategy):
        self._compression = strategy

    def process(self, file_name: str, from_fmt: str, to_fmt: str, watermark: bool = False):
        try:
            converter = ConverterFactory.create_converter(from_fmt)
            if watermark:
                converter = WatermarkDecorator(converter)
            
            output_file = converter.convert(file_name, to_fmt)
            self._compression.compress(output_file)
            self.events.notify(file_name, "Dönüşüm ve sıkıştırma başarıyla tamamlandı.")
        except Exception as e:
            self.events.notify(file_name, f"HATA OLUŞTU: {str(e)}")

if __name__ == "__main__":
    print("--- [Faz 3: Tüm Örüntülerin Entegre Edilmiş Hali] ---\n")
    app = ConverterApplication()
    
    app.events.subscribe(ConsoleLogger())
    app.events.subscribe(EmailNotifier())

    print("--- SENARYO 1 (CSV -> PDF, Filigranlı, ZIP'li) ---")
    app.set_compression(ZipCompression())
    app.process("finans_raporu", "csv", "pdf", watermark=True)

    print("\n--- SENARYO 2 (Word -> Excel, Filigransız, RAR'lı) ---")
    app.set_compression(RarCompression())
    app.process("personel_listesi", "word", "excel", watermark=False)
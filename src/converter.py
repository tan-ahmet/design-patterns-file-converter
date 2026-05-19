class FileConverter:
    def __init__(self):
        print("Dosya Dönüştürücü Başlatıldı...")

    def convert_file(self, file_name, from_format, to_format):
        print(f"İşlem başlıyor: {file_name} dönüştürülüyor ({from_format} -> {to_format})")
        
        if from_format == "pdf" and to_format == "word":
            print("PDF dosyası okunuyor...")
            print("Word formatına çevriliyor...")
            print("İşlem başarılı!\n")
            
        elif from_format == "word" and to_format == "pdf":
            print("Word dosyası okunuyor...")
            print("PDF formatına çevriliyor...")
            print("İşlem başarılı!\n")
            
        elif from_format == "excel" and to_format == "pdf":
            print("Excel dosyası okunuyor...")
            print("Tablolar PDF'e aktarılıyor...")
            print("İşlem başarılı!\n")
            
        else:
            print(f"Hata: {from_format} formatından {to_format} formatına dönüşüm desteklenmiyor!\n")


if __name__ == "__main__":
    converter = FileConverter()
    
    
    converter.convert_file("rapor", "pdf", "word")
    converter.convert_file("hesaplar", "excel", "pdf")
    
    
    converter.convert_file("resim", "jpeg", "pdf")

from PyPDF2 import PdfReader, PdfWriter
import os

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    if not os.path.exists(pdf1_path) or not os.path.exists(pdf2_path):
        raise FileNotFoundError("PDF dosyalarından biri veya her ikisi bulunamadı.")

    # PDF okuyucularını oluştur
    reader1 = PdfReader(pdf1_path)
    reader2 = PdfReader(pdf2_path)
    
    # Yeni bir PDF yazıcı oluştur
    writer = PdfWriter()
    
    # İlk PDF'nin tüm sayfalarını ekle
    for page in reader1.pages:
        writer.add_page(page)
    
    # İkinci PDF'nin tüm sayfalarını ekle
    for page in reader2.pages:
        writer.add_page(page)
    
    # Birleştirilmiş PDF'yi yeni bir dosyaya kaydet
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)
    print(f"PDF dosyaları başarıyla birleştirildi: {output_path}")

# Kullanım
pdf1 = r"C:\Users\bulut\OneDrive\Masaüstü\Network\1.Temel Kavramlar.pdf"
pdf2 = r"C:\Users\bulut\OneDrive\Masaüstü\Network\2.Ağ Aygıtları.pdf"
output_pdf = "C:/Users/bulut/OneDrive/Masaüstü/birlesmis_dosya23.pdf"

merge_pdfs(pdf1, pdf2, output_pdf)

print("*************************************")


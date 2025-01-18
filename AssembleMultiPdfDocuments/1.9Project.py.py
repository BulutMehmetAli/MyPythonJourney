from PyPDF2 import PdfReader, PdfWriter
import os

def merge_multiple_pdfs(pdf_paths, output_path):
    # PDF yazıcı oluştur
    writer = PdfWriter()
    
    # Listedeki her PDF dosyasını işle
    for pdf_path in pdf_paths:
        if not os.path.exists(pdf_path):
            print(f"Dosya bulunamadı: {pdf_path}")
            continue  # Bulunamayan dosyaları atla
        
        # PDF okuyucu oluştur
        reader = PdfReader(pdf_path)
        
        # Her sayfayı yazıcıya ekle
        for page in reader.pages:
            writer.add_page(page)
    
    # Birleştirilmiş PDF'yi yeni bir dosyaya kaydet
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)
    
    print(f"PDF dosyaları başarıyla birleştirildi: {output_path}")

# Kullanım
pdf_list = [
r"C:\Users\bulut\OneDrive\Masaüstü\.pdf",

r"C:\Users\bulut\OneDrive\Masaüstü\.pdf",
r"C:\Users\bulut\OneDrive\Masaüstü\.pdf",
r"C:\Users\bulut\OneDrive\Masaüstü\.pdf",
r"C:\Users\bulut\OneDrive\Masaüstü\.pdf",
r"C:\Users\bulut\OneDrive\Masaüstü\.pdf"
]

output_pdf = "C:/Users/bulut/OneDrive/Masaüstü/.pdf"

merge_multiple_pdfs(pdf_list, output_pdf)
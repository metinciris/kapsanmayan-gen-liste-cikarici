import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def analyze_coverage():
    """
    Seçilen Excel dosyalarındaki hedef bölgelerin kapsama alanını analiz eder.
    """
    # Kullanıcıdan eşik değerini al
    try:
        coverage_threshold = int(coverage_threshold_entry.get())
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir tam sayı eşik değeri girin.")
        return

    # Kullanıcıdan Excel dosyalarını seçmesini iste
    file_paths = filedialog.askopenfilenames(filetypes=[("Excel Files", "*.xls;*.xlsx")])

    if not file_paths:
        return  # Dosya seçilmediyse işlemi sonlandır

    results = {}

    for file_path in file_paths:
        try:
            df = pd.read_excel(file_path)

            # 'Name' ve 'Region' sütunlarının varlığını kontrol et
            if 'Name' not in df.columns or 'Region' not in df.columns or 'Min coverage' not in df.columns:
                messagebox.showerror("Hata", f"{file_path} dosyasında gerekli sütunlar bulunamadı. Lütfen sütun isimlerini kontrol edin.")
                return

            # Eşik değerinin altındaki bölgeleri filtrele
            filtered_df = df[df['Min coverage'] < coverage_threshold]

            # Sonuçları işle
            for index, row in filtered_df.iterrows():
                gene_name = row['Name']
                region = row['Region']
                if gene_name not in results:
                    results[gene_name] = []
                results[gene_name].append(region)
        except Exception as e:
            messagebox.showerror("Hata", f"{file_path} dosyasını okurken bir hata oluştu: {str(e)}")
            return

    # Sonuçları sırala ve biçimlendir
    sorted_genes = sorted(results.keys())
    formatted_results = "- Aşağıdaki genlerin ilgili bölgeleri bu dizileme çalışmasında kapsanmamıştır (okuma derinliği <" + str(coverage_threshold) + "):\n"
    for gene in sorted_genes:
        regions = ", ".join(results[gene])
        formatted_results += f"  - {gene}: {regions}\n"

    # Sonuçları metin kutusuna yazdır
    result_text.delete("1.0", tk.END)  # Önceki sonuçları temizle
    result_text.insert(tk.END, formatted_results)

# Tkinter arayüzünü oluştur
root = tk.Tk()
root.title("Kapsama Alanı Analizi")

# Eşik değeri etiketi ve giriş alanı
coverage_threshold_label = tk.Label(root, text="Kapsama Eşik Değeri:")
coverage_threshold_label.pack()
coverage_threshold_entry = tk.Entry(root)
coverage_threshold_entry.insert(0, "100")  # Varsayılan eşik değeri
coverage_threshold_entry.pack()

# Analiz düğmesi
analyze_button = tk.Button(root, text="Excel Dosyalarını Seç ve Analiz Et", command=analyze_coverage)
analyze_button.pack()

# Sonuç metin kutusu
result_text = tk.Text(root, height=20, width=80)
result_text.pack()

# Kopyalama düğmesi
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_text.get("1.0", tk.END))
    root.update()
    messagebox.showinfo("Bilgi", "Sonuçlar panoya kopyalandı.")

copy_button = tk.Button(root, text="Sonuçları Panoya Kopyala", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()

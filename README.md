# kapsanmayan-gen-liste-cikarici
NGS kapsanmayan gen listesini Excel dosyasından liste olarak rapor formatında çıkartır.

Bu araç, hedefli dizileme verilerindeki hedef bölgelerin kapsama alanını analiz etmek için tasarlanmıştır. Belirli bir eşik değerinin altında kapsama sahip genleri ve bölgeleri belirlemek için Excel tablolarını okur.

Şu bilgileri daha rahat elde etmenizi sağlar:
* okuma derinliğinin altındaki okumalar varyant olarak yansımamaktadır. * okuma derinliğinin altındaki bölgeler kapsamamaktadır. // * okuma derinliğinin altındaki varyantlar saptanmamaktadır.

## Özellikler

*   `.xls` ve `.xlsx` formatındaki Excel dosyalarını okuyabilir.
*   Kullanıcı tarafından belirlenebilir kapsama eşik değeri.
*   Sonuçları sıralı bir şekilde listeler.
*   Sonuçları panoya kopyalama özelliği.
*   Kullanımı kolay grafik arayüzü.

## Gereksinimler

*   Python 3.x
*   `pandas` kütüphanesi
*   `openpyxl` kütüphanesi (yalnızca `.xlsx` dosyaları için gereklidir)
*   `xlrd` kütüphanesi (yalnızca `.xls` dosyaları için gereklidir)
*   `tkinter` kütüphanesi (GUI için)

## Kurulum

1.  Python 3.x'i yükleyin.
2.  Gerekli kütüphaneleri yükleyin:

    ```
    pip install pandas openpyxl xlrd
    ```

## Kullanım

1.  Kodu bir Python dosyasına kaydedin (örneğin, `kapsam_disi_liste.py`).
2.  Dosyayı çalıştırın:

    ```
    python kapsam_disi_liste.py
    ```

3.  Açılan pencerede, kapsama eşik değerini girin.
4.  "Excel Dosyalarını Seç ve Analiz Et" düğmesine tıklayın.
5.  Analiz etmek istediğiniz Excel dosyalarını seçin.
6.  Sonuçlar metin kutusunda görüntülenecektir.
7.  İsterseniz "Sonuçları Panoya Kopyala" düğmesine tıklayarak sonuçları panoya kopyalayabilirsiniz.

## Örnek Sonuçlar

Aşağıdaki örnek, eşik değeri 100 olarak ayarlandığında elde edilen tipik bir sonucu göstermektedir.

```
- Aşağıdaki genlerin ilgili bölgeleri bu dizileme çalışmasında kapsanmamıştır (okuma derinliği <100):
  - BRCA1: exon2, exon5
  - EGFR: exon7
  - TP53: intron4
```

Bu sonuç, BRCA1 geninin exon2 ve exon5 bölgelerinin, EGFR geninin exon7 bölgesinin ve TP53 geninin intron4 bölgesinin, belirtilen dizileme çalışmasında 100'ün altında okuma derinliğine sahip olduğunu gösterir.

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen bir "pull request" oluşturarak veya sorunları bildirerek katkıda bulunun.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.
```

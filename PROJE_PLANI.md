# 🗓 M.E.G. SOFTWARE Discord Destek Botu - Detaylı Haftalık Plan

## **1. Hafta – Hazırlık ve Temel Yapı**
### Gün 1: Ortam ve Dosya Hazırlığı
- [ ] Bot için klasör oluştur (`meg_support_bot/`).
- [ ] Ana dosya oluştur (`bot.py`).
- [ ] Token ve ayarları saklamak için `config.json` veya `.env` dosyası oluştur.
- [ ] Python sürümünü kontrol et (`python --version >= 3.10`).

### Gün 2: Kütüphaneleri Kur ve Basit Bot Başlat
- [ ] `discord.py` kütüphanesini yükle (`pip install discord.py`).
- [ ] Basit “Bot aktif!” mesajı yazdıran `on_ready` event’i ekle.
- [ ] Slash komutları için `bot.tree` yapılandırmasını ekle.

### Gün 3: Test ve Hata Kontrol
- [ ] Botu test sunucusunda başlat.
- [ ] “Bot aktif!” mesajını doğrula.
- [ ] Herhangi bir hata varsa düzelt.

---

## **2. Hafta – Temel Komutlar**
### Gün 4: /iletisim Komutu
- [ ] WhatsApp, Telegram ve Web site linklerini embed ile göster.
- [ ] Embed renklerini ve ikonları ekle.
- [ ] Test: Mesaj düzgün görünüyor mu?

### Gün 5: /hakkimizda Komutu
- [ ] Kısa tanıtım metni ekle.
- [ ] Embed veya düz mesaj olarak gönder.
- [ ] Test ve düzenleme.

### Gün 6: /katalog Komutu
- [ ] Basit versiyon: Web sitesi katalog linkini gönder.
- [ ] Test: Link çalışıyor mu?

### Gün 7: Test ve İnce Ayar
- [ ] Tüm 3 komutu test et.
- [ ] Embed renkleri, linkler, yazım hatalarını düzelt.

---

## **3. Hafta – Destek ve SSS**
### Gün 8: /destek Komutu
- [ ] WhatsApp ve Telegram destek linklerini gönder.
- [ ] Embed içinde linkleri tıklanabilir yap.

### Gün 9: /sss Komutu
- [ ] Sıkça Sorulan 3-5 soruyu listele.
- [ ] Test: Cevaplar doğru ve okunabilir mi?

### Gün 10: /duyurular Komutu
- [ ] Adminler için duyuru ekleme yetkisi oluştur.
- [ ] Kullanıcılar son duyuruları embed ile görebilsin.

### Gün 11: Test ve İnce Ayar
- [ ] Tüm destek ve SSS komutlarını test et.
- [ ] Mesaj formatlarını ve embed’leri düzenle.

---

## **4. Hafta – Ekstra Özellikler**
### Gün 12: /feedback Komutu
- [ ] Kullanıcıdan mesaj alıp log kanalına gönder.
- [ ] Test: Kullanıcı mesajı admin kanalda görünüyor mu?

### Gün 13: /istatistik Komutu
- [ ] Kaç kullanıcı botu kullandı, kaç komut çalıştırıldı göster.
- [ ] Basit sayaç sistemi ekle.

### Gün 14: Admin Özel Komutlar
- [ ] `/duyuruekle` → Yeni duyuru ekle.
- [ ] `/urunekle` → Yeni katalog ürünü ekle.
- [ ] Test: Sadece admin kullanabiliyor mu?

---

## **5. Hafta – Son Test ve Yayına Alma**
### Gün 15-16: Test
- [ ] Botu tüm komutlarla test et.
- [ ] Embed görünümlerini kontrol et.
- [ ] Hataları düzelt.

### Gün 17-18: Yayınlama
- [ ] Botu Heroku / Railway / Replit / VPS gibi hostinge yükle.
- [ ] 7/24 çalıştığından emin ol.
- [ ] Sunucuda kullanıcı testi yap.

### Gün 19: Kullanıcı Geri Bildirimi
- [ ] Arkadaşlarını veya test kullanıcılarını botu denemesi için davet et.
- [ ] Geri bildirimleri topla ve düzeltmeler yap.

---

## **6. Gelecek Geliştirmeler**
- Çoklu dil desteği (TR/EN)
- Ürün kataloğunu JSON veya SQL ile dinamik hale getirme
- Otomatik karşılama mesajı (sunucuya yeni girenler için)
- İstatistik ve analitik geliştirmeleri
- Bot performans optimizasyonu

---


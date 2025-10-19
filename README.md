cat > README.md <<'EOF'
# TETech FakeHackShow

**TETech FakeHackShow**, sınıf sunumları ve eğlenceli gösteriler için hazırlanmış zararsız bir "hacker-like" görsel demodur. Amacı: sahte terminal efektleri (matrix rain, typing, fake loglar, ilerleme çubuğu) ile sinematik bir sunum yapmaktır. **Gerçek saldırı, ağ taraması veya hesap ele geçirme içermez.**

---

## Canlı demo / kısa açıklama
Program tam ekran görsel gösteri sunar: solda *matrix rain*, sağda bir terminal paneli, ortada ihtişamlı **TETech Studios** başlığı (pulse + halo + partikül efektleri). Ekranın altında dokunmatik butonlarla **GitHub Aç** ve (gizli) çıkış mekanizması bulunur.

---

## Öne çıkan özellikler
- Tam ekran (veya pencere) sinematik gösterim  
- Matrix rain, typing efekti, fake loglar ve transfer çubuğu  
- Büyük, parlayan ve partiküllü başlık: **TETech Studios**  
- Dokunmatik dostu buton: **GitHub Aç**  
- Gizli çıkış: sol-üst köşeye 3 kere hızlı dokunma veya 1.5s uzun basma  
- SAFE: Hiçbir gerçek ağ/işlem/kimlik bilgisi kullanılmaz — sadece görseldir

---

## Nasıl kurulur (ön koşullar)
- Python 3.7+ (tercih: 3.8 veya üstü)
- `pygame` kütüphanesi

\`\`\`bash
pip install pygame
\`\`\`

---

## Dosyalar
- \`fake_hack_show_fullscreen_hidden_exit.py\` — tam ekran gösteri (gizli çıkış)
- \`stable_fake_hack_show_with_buttons.py\` — pencere modu, butonlu stabil sürüm
- \`README.md\` — (bu dosya)
- \`LICENSE\` — MIT lisansı

---

## Nasıl çalıştırılır
1. Repo'yu klonla veya dosyaları indir:  
   \`\`\`bash
   git clone https://github.com/KULLANICI/tetech-fake-hack-show.git
   cd tetech-fake-hack-show
   \`\`\`
2. Gösteriyi çalıştır:
   \`\`\`bash
   python fake_hack_show_fullscreen_hidden_exit.py
   \`\`\`
   - Eğer tam ekran sorun çıkarıyorsa \`USE_FULLSCREEN = False\` yapıp pencere modunda çalıştır.

---

## Nasıl oynanır / kontroller
- **GitHub Aç** butonuna dokun/tıkla → tarayıcıda \`https://github.com\` açılır. (Sadece gösteri amaçlı)  
- **Gizli çıkış yöntemleri** (akıllı tahta klavyesi yoksa kullan):
  - Sol üst köşeye **3 kısa dokunuş** (1.5 saniye içinde) → uygulama kapanır.  
  - Sol üst köşeye **1.5 saniye basılı tut** → uygulama kapanır.  
- **Klavye kısayolları (yedek)**:
  - \`ESC\` → çıkış  
  - \`SPACE\` → hızlı bitirip GitHub aç

---

## Özelleştirme
- \`USE_FULLSCREEN\` değişkeni ile tam ekran/pencere modunu ayarla.  
- Başlığı, renkleri, metinleri ve efektleri \`fake_hack_show_fullscreen_hidden_exit.py\` içinde kolayca değiştirebilirsiniz.  
- Daha fazla sahne, ses efektleri veya otomatik oynatma eklemek istersen PR gönder veya issue aç.

---

## Güvenlik & Etik Uyarısı
Bu proje **gösteri amaçlı**dır. Gerçek sistemlere izinsiz erişim denemek **yasa dışıdır** ve suçtur. Lütfen yalnızca izin aldığın cihazlarda gösteri yap. Program hiçbir gerçek tarama, exploit veya ağ iletişimi gerçekleştirmez — IP / SESSION / komutlar sadece rastgele metin üretir.

---

## Katkılar
PR ve issue’lara açığım — iyileştirme, yeni efekt veya çeviri istersen katkı beklerim.

---

## Lisans
Bu proje **MIT Lisansı** ile yayımlanmıştır — detaylar \`LICENSE\` dosyasında.
EOF

cat > LICENSE <<'EOF'
MIT License

Copyright (c) 2025 TETech Studios

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
EOF

git add README.md LICENSE
git commit -m "Add README and MIT license"
git push origin main

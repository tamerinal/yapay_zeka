# yapay_zeka

Bu proje, LM Studio'da çalıştırılabilecek ücretsiz bir LLM modelini kullanıcının
yükleyip kendi verisiyle eğitebilmesini amaçlar.

## Amaç
- LM Studio ile uyumlu, ücretsiz bir LLM modelinin yüklenebilmesi
- Kullanıcının bir bağlam içeren CSV dosyası sağlayarak modeli eğitmesi
- Eğitilen modelin yeniden LM Studio'da kullanılmak üzere çıktısının alınması

## Plan
1. **Model Yükleme**
   - Kullanıcıdan LLM model dosyalarının (ör. Hugging Face ağırlıkları) yüklenmesi beklenir.
   - Uygulama başlangıç aşamasında herhangi bir model seçimi yapmaz; model tamamen kullanıcı tarafından yüklenir.

2. **Veri Girişi**
   - Bağlam verilerinin yer aldığı CSV dosyası kullanıcı tarafından uygulamaya yüklenir.
   - CSV formatının doğrulanması ve gerekli sütunların kontrolü yapılır.

3. **Fine-Tune İşlemi**
   - `transformers` gibi açık kaynak araçlarla yüklenen model verilen CSV verisiyle eğitilir.
   - Temel hiperparametreler (epoch sayısı, batch büyüklüğü vb.) için ayarlar sağlanır.

4. **Model Çıktısı**
   - Eğitim tamamlandıktan sonra ağırlıklar LM Studio'nun yükleyebileceği biçimde kaydedilir.

5. **Kullanıcı Arayüzü**
   - Komut satırı veya basit bir web arayüzü üzerinden model ve veri yükleme, eğitimi başlatma gibi adımlar sağlanır.

6. **Gelecek Geliştirmeler**
   - Popüler ücretsiz modellerden seçim yapma opsiyonu eklenebilir.
   - Eğitim sonrası değerlendirme metrikleri ve ek raporlama adımları eklenebilir.

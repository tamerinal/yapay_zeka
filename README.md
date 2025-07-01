# yapay_zeka

yapay zeka
llm model fine tune uygulaması

## CSV Yükleme Arayüzü

`load_csv.py` dosyası, yerel diskinizden CSV dosyası seçmenizi sağlayan basit bir Tkinter arayüzü sunar. Çalıştırmak için:

```bash
python load_csv.py
```

Açılan pencereden **CSV Dosyası Yükle** butonuna basarak dosyayı seçebilirsiniz. Seçilen dosya yolu ve ilk satırlar ekranda görüntülenir.

## LLM Upload Interface

`front_end/llm_upload` dizini, LLM model dosyalarınızı yüklemek için Flask tabanlı basit bir web uygulaması içerir. Çalıştırmak için:

```bash
cd front_end/llm_upload
pip install -r requirements.txt
# optional: set a custom secret key
export SECRET_KEY=mysecret
export FLASK_DEBUG=1
python app.py
```

Uygulama `http://127.0.0.1:5000/` adresinde çalışır ve bu sayfadan model dosyalarınızı yükleyebilirsiniz.

# Django Basit Kütüphane Uygulaması

## Başlangıç

Bu projeyi çalıştırmak ve geliştirmek için aşağıdaki adımları izleyin.

## Proje bağımlılıklarını yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

## Veritabanını oluşturmak için aşağıdaki komutu çalıştırın:

```bash
python manage.py makemigrations app
```

```bash
python manage.py migrate
```

### Projeyi başlatmak için aşağıdaki komutu çalıştırın:
## Sanal ortamda çalıştırmak için;
```bash
python manage.py runserver
```

## Docker üzerinden çalıştırmak için;
```bash
docker build -t django-library-app .   
```

```bash
docker run -p 8000:8000 django-library-app
```

Tarayıcınızda `http://localhost:8000` adresine giderek uygulamayı görüntüleyebilirsiniz.



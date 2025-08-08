# Blueray Cargo Technical Test

Hai, saya Zulfahmi. Ini merupakan hasil dari teknikal tes saya di Blueray Cargo.

**Links**
- Result Web Blueray Cargo: [https://cargo-app.zulfahmidev.com](https://cargo-app.zulfahmidev.com)
- API Blueray Cargo: [https://cargo-app.zulfahmidev.com/api](https://cargo-app.zulfahmidev.com/api)

## API Documentation
API Blueray Cargo untuk mengambil daftar negara, kategori, destinasi dan menghitung biaya pengiriman.

**Base URL**
```
https:://cargo-app.zulfahmidev.com/api
```

**Contoh akun yang sudah tersedia**
|Email|Password|
|--|--|
|admin@example.com|password|


### POST | /token
Membuat akses token yang dapat digunakan untuk autentikasi saat menggunai API

**Body:**
|key|type|description|
|--|--|--|
|email|text|email anda (contoh: admin@example.com)|
|password|text|password anda (contoh: password)|

**Response:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NDczNTA3MCwiaWF0IjoxNzU0NjQ4NjcwLCJqdGkiOiI0ZjllMWE4M2Y1MzI0MjAzYTQxZjY3OTBhMDQzMmZlNyIsInVzZXJfaWQiOiIxIn0.KiHYgf9631DmgcSZxnmfCjgcnGYYeaIIJ9ayKnK7W2Y",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU0NjQ4OTcwLCJpYXQiOjE3NTQ2NDg2NzAsImp0aSI6ImUyOGNiMzE0NGJhMzRhMDM5YmQ3YWEwMGJkYThmMDFmIiwidXNlcl9pZCI6IjEifQ.1cnvKh8Ax6rz2QDQBUcsrxojmVoqV_PC-Uza3GID3C8"
}
```

**Usage:**
```shell
curl --location 'https://cargo-app.zulfahmidev.com/api/token' \
--form 'email="admin@example.com"' \
--form 'password="password"'
```

---

### POST | /token/refresh
Memperbarui akses token yang dapat digunakan untuk autentikasi saat menggunai API

**Body:**
|key|type|description|
|--|--|--|
|refresh|text|refresh token anda|

**Response:**
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU0NjQ4OTcwLCJpYXQiOjE3NTQ2NDg2NzAsImp0aSI6ImUyOGNiMzE0NGJhMzRhMDM5YmQ3YWEwMGJkYThmMDFmIiwidXNlcl9pZCI6IjEifQ.1cnvKh8Ax6rz2QDQBUcsrxojmVoqV_PC-Uza3GID3C8"
}
```

**Usage:**
```shell
curl --location 'https://cargo-app.zulfahmidev.com/api/token/refresh' \
--form 'refresh="<refresh-token>"'
```

---

### GET | /countries
Melihat daftar negara

**Header:**
```properties
Authorization: Bearer <access-token>
```

**Query Params:**
|key|type|description|
|--|--|--|
|search|text|untuk mencari daftar negara dengan nama negara|
|page|number|nomor halaman (setiap halaman hanya sampai 10 item)|

**Response:**
```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "country_name": "China",
            "country_flag": "/media/country_flags/8448fe510da1bb980fe231636a4bc61a84b561711a70aebc0b3d7f6081ca531b.jpg",
            "country_currency": "CHY"
        },
        {
            "id": 2,
            "country_name": "Thailand",
            "country_flag": "/media/country_flags/1e5cfada0f9d443396688bfe42cd1d96c940f8761713b49ec34ea240e0a78563.png",
            "country_currency": "THB"
        },
        {
            "id": 3,
            "country_name": "Singapore",
            "country_flag": "/media/country_flags/16e31e1bc8a2fdba609e6a7c07e74da265b692cdaddf49628968a11a4e534147.png",
            "country_currency": "SGD"
        }
    ],
    "status": 200,
    "message": "Success"
}
```

**Usage:**
```shell
curl --location 'https://cargo-app.zulfahmidev.com/api/countries?search=ch&page=1' \
--header 'Authorization: Bearer <access-token>'
```

---

### GET | /categories
Melihat daftar kategori

**Header:**
```properties
Authorization: Bearer <access-token>
```

**Query Params:**
|key|type|description|
|--|--|--|
|search|text|untuk mencari daftar negara dengan judul kategori|
|page|number|nomor halaman (setiap halaman hanya sampai 10 item)|
|country_id|text|untuk memfilter daftar negara berdasarkan id negara yang bisa didapatkan melalui api daftar negara|

**Response:**
```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "country_id": 1,
            "category_title": "Electronic",
            "price_per_kilo": 250000
        },
        {
            "id": 2,
            "country_id": 1,
            "category_title": "Chip",
            "price_per_kilo": 300000
        },
        {
            "id": 3,
            "country_id": 1,
            "category_title": "Laptop and Computer",
            "price_per_kilo": 220000
        },
        {
            "id": 4,
            "country_id": 2,
            "category_title": "Garments",
            "price_per_kilo": 200000
        },
        {
            "id": 5,
            "country_id": 3,
            "category_title": "Spare parts",
            "price_per_kilo": 210000
        }
    ],
    "status": 200,
    "message": "Success"
}
```

**Usage:**
```shell
curl --location 'https://cargo-app.zulfahmidev.com/api/categories?search=ch&page=1&country_id='' \
--header 'Authorization: Bearer <access-token>'
```

---

### GET | /destinations
Melihat daftar destinasi

**Header:**
```properties
Authorization: Bearer <access-token>
```

**Query Params:**
|key|type|description|
|--|--|--|
|search|text|untuk mencari daftar negara dengan judul kategori (wajib di isi minimal satu kata)|
|page|number|nomor halaman (setiap halaman hanya sampai 10 item)|

**Response:**
```json
{
    "success": true,
    "data": [
        {
            "id": 17483,
            "label": "SEMANAN, KALIDERES, JAKARTA BARAT, DKI JAKARTA, 11850",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KALIDERES",
            "subdistrict_name": "SEMANAN",
            "zip_code": "11850"
        },
        {
            "id": 17484,
            "label": "TEGAL ALUR, KALIDERES, JAKARTA BARAT, DKI JAKARTA, 11820",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KALIDERES",
            "subdistrict_name": "TEGAL ALUR",
            "zip_code": "11820"
        },
        {
            "id": 17485,
            "label": "DURI KEPA, KEBON JERUK, JAKARTA BARAT, DKI JAKARTA, 11510",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KEBON JERUK",
            "subdistrict_name": "DURI KEPA",
            "zip_code": "11510"
        },
        {
            "id": 17486,
            "label": "KEBON JERUK, KEBON JERUK, JAKARTA BARAT, DKI JAKARTA, 11530",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KEBON JERUK",
            "subdistrict_name": "KEBON JERUK",
            "zip_code": "11530"
        },
        {
            "id": 17487,
            "label": "KEDOYA SELATAN, KEBON JERUK, JAKARTA BARAT, DKI JAKARTA, 11520",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KEBON JERUK",
            "subdistrict_name": "KEDOYA SELATAN",
            "zip_code": "11520"
        },
        {
            "id": 17488,
            "label": "KEDOYA UTARA, KEBON JERUK, JAKARTA BARAT, DKI JAKARTA, 11520",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KEBON JERUK",
            "subdistrict_name": "KEDOYA UTARA",
            "zip_code": "11520"
        },
        {
            "id": 17489,
            "label": "KELAPA DUA, KEBON JERUK, JAKARTA BARAT, DKI JAKARTA, 11550",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KEBON JERUK",
            "subdistrict_name": "KELAPA DUA",
            "zip_code": "11550"
        },
        {
            "id": 17490,
            "label": "SUKABUMI SELATAN (UDIK), KEBON JERUK, JAKARTA BARAT, DKI JAKARTA, 11560",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KEBON JERUK",
            "subdistrict_name": "SUKABUMI SELATAN (UDIK)",
            "zip_code": "11560"
        },
        {
            "id": 17491,
            "label": "SUKABUMI UTARA (ILIR), KEBON JERUK, JAKARTA BARAT, DKI JAKARTA, 11540",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KEBON JERUK",
            "subdistrict_name": "SUKABUMI UTARA (ILIR)",
            "zip_code": "11540"
        },
        {
            "id": 17492,
            "label": "JOGLO, KEMBANGAN, JAKARTA BARAT, DKI JAKARTA, 11640",
            "province_name": "DKI JAKARTA",
            "city_name": "JAKARTA BARAT",
            "district_name": "KEMBANGAN",
            "subdistrict_name": "JOGLO",
            "zip_code": "11640"
        }
    ],
    "status": 200,
    "message": "Success"
}
```

**Usage:**
```shell
curl --location 'http://localhost:8080/api/destinations?search=jakarta&page=1' \
--header 'Authorization: Bearer <access-token>'
```

---

### POST | /calculate
Menghitung ongkos pengiriman

**Header:**
```properties
Authorization: Bearer <access-token>
```

**Body:**
|key|type|description|
|--|--|--|
|country_id|number|id dari negara|
|category_id|number|id dari kategori|
|destination_id|number|id dari destinasi|
|weight|number|berat barang dalam kilo|

**Response:**
```json
{
    "success": true,
    "data": {
        "origin": {
            "id": 1,
            "country_name": "China",
            "country_flag": "/media/country_flags/8448fe510da1bb980fe231636a4bc61a84b561711a70aebc0b3d7f6081ca531b.jpg",
            "country_currency": "CHY"
        },
        "destination_id": 17473,
        "category_name": "Chip",
        "international_price": 1200000.0,
        "domestic_price": 10000,
        "total_price": 1210000.0
    },
    "status": 200,
    "message": "Success"
}
```

**Usage:**
```shell
curl --location 'https://cargo-app.zulfahmidev.com/api/calculate' \
--header 'Authorization: Bearer <access-token>' \
--form 'country_id="1"' \
--form 'category_id="2"' \
--form 'destination_id="17473"' \
--form 'weight="4"'
```
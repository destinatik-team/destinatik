# Destinatik API

Destinatik API adalah sebuah aplikasi backend yang dibangun menggunakan Node.js dan Express.js. API ini menyediakan beberapa endpoint untuk melakukan proses autentikasi pengguna, seperti registrasi, login, dan mendapatkan list pengguna.

## Fitur

- Registrasi pengguna
- Login pengguna
- Mendapatkan list pengguna
- Memberi Rating
- Mendapatkan daftar rating
- Menghitung rata-rata rating

# Endpoint
## POST /register

Endpoint ini digunakan untuk melakukan registrasi pengguna baru. Pengguna harus mengirimkan username, email, dan password dalam bentuk JSON.

Request:
```
{
  "username": "example",
  "email": "user@example.com",
  "password": "password123"
}
```

Response:
```
{
  "status": "1",
  "id": 1,
  "username": "example",
  "email": "user@example.com"
}
```

## POST /login
Endpoint ini digunakan untuk melakukan login pengguna. Pengguna harus mengirimkan usernameOrEmail dan password dalam bentuk JSON.

Request:
```
{
  "usernameOrEmail": "example",
  "password": "password123"
}
```

Response:
```
{
  "usernameOrEmail": "example",
  "status": "1",
  "token": "<token response>"
}
```

## GET /list

Endpoint ini digunakan untuk mendapatkan daftar pengguna yang terdaftar.

Response:
```
{
  "rows": [
    {
      "id": 1,
      "username": "example1",
      "email": "example1@example.com",
      "password": "password123"
    },
    {
      "id": 2,
      "username": "example2",
      "email": "example2@example.com",
      "password": "password456"
    }
  ]
}
```

## POST /rating/rate

Menerima request untuk memberikan rating pada suatu tempat, menyimpan data rating ke database, dan mengembalikan respons yang sesuai dengan hasil dari POST.

1. Mengambil nilai userId, placeId, dan rating dari request body.
2. Memeriksa apakah semua field telah diisi. Jika tidak, mengembalikan respons 400 Bad Request.
3. Jika semua field sudah diisi, menyimpan data rating ke dalam database menggunakan query SQL INSERT INTO.
4. Jika penyimpanan berhasil, mengembalikan respons 201 Created dengan informasi penilaian yang baru ditambahkan.
5. Jika terjadi kesalahan saat menyimpan data, mengembalikan respons 500 Internal Server Error dengan pesan kesalahan.

Request:

    userId: ID pengguna yang memberikan rating
    placeId: ID tempat yang diberikan rating
    rating: Nilai rating yang diberikan

### Status HTTP: 400 Bad Request
Response:
```
{
  "error": "Semua field harus diisi"
}
```
### Status HTTP: 201 Created
Response:
```
{
  "status": "1",
  "id": <ID penilaian yang baru ditambahkan>,
  "userId": <ID pengguna yang memberikan rating>,
  "placeId": <ID tempat yang diberikan rating>,
  "rating": <Nilai rating yang diberikan>
}
```

### Status HTTP: 500 Internal Server Error
Response:
```
{
  "error": "Terjadi kesalahan saat menyimpan rating"
}
```

## GET /rating/list

Menerima request untuk mengambil daftar rating, baik untuk semua rating atau hanya rating untuk tempat tertentu, dan mengembalikan respons dengan data rating yang sesuai.

1. Mengambil nilai placeId dari query parameter.
2. Jika placeId disertakan, maka membuat query SQL untuk mengambil semua data rating dengan placeId yang sesuai.
3. Jika placeId tidak disertakan, maka membuat query SQL untuk mengambil semua data rating.
4. Menjalankan query SQL dan memeriksa apakah terjadi kesalahan. Jika terjadi kesalahan, mengembalikan respons 500 Internal Server Error dengan pesan kesalahan.
5. Jika tidak terjadi kesalahan, mengembalikan respons 200 OK dengan data rating yang diambil dari database.

Request:

    placeId: ID tempat yang akan diambil ratingnya (opsional)

### Status HTTP: 200 OK
Response:
```
{
  "rows": [
    {
      "id": <ID penilaian>,
      "userId": <ID pengguna yang memberikan rating>,
      "placeId": <ID tempat yang diberikan rating>,
      "rating": <Nilai rating yang diberikan>
    },
    ...
  ]
}
```

## GET /rating/average

Menerima request untuk mengambil rata-rata rating untuk suatu tempat, dan mengembalikan respons dengan data total jumlah rating dan nilai rata-rata rating.

1. Mengambil nilai placeId dari query parameter.
2. Memeriksa apakah placeId disertakan. Jika tidak, mengembalikan respons 400 Bad Request.
3. Membuat query SQL untuk mengambil total jumlah rating dan nilai rata-rata rating untuk tempat dengan placeId yang sesuai.
4. Menjalankan query SQL dan memeriksa apakah terjadi kesalahan. Jika terjadi kesalahan, mengembalikan respons 500 Internal Server Error dengan pesan kesalahan.
5. Jika tidak terjadi kesalahan, mengembalikan respons 200 OK dengan data total jumlah rating dan nilai rata-rata rating.

Request:

    placeId: ID tempat yang akan dihitung ratingnya

### Status HTTP: 400 Bad Request
Response:
```
{
  "error": "placeId parameter is required"
}
```

### Status HTTP: 200 OK
```
{
  "total_ratings": <Total jumlah rating untuk tempat tersebut>,
  "average_rating": <Nilai rata-rata rating untuk tempat tersebut>
}
```

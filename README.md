# Destinatik API
Destinatik API adalah sebuah aplikasi backend yang dibangun menggunakan Node.js dan Express.js. API ini menyediakan beberapa endpoint untuk melakukan proses autentikasi pengguna, seperti registrasi, login, dan mendapatkan list pengguna.

### Fitur

- Registrasi pengguna
- Login pengguna
- Mendapatkan list pengguna

### Endpoint
**POST /register**
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

**POST /login**
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
  "status": "1"
}
```

**GET /list**
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

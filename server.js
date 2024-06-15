const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const jwt = require('jsonwebtoken');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'destinatik'
});
connection.connect((err) => {
  if (err) {
    console.error('Gagal terhubung ke database:', err);
    return;
  }
  console.log('Terhubung ke database!');
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.send('Pake POST yah!');
});
app.post('/register', (req, res) => {
  const { username, email, password } = req.body;

  if (!username || !email || !password) {
    return res.status(400).json({ error: 'Semua field harus diisi', 'yang di isi': req.body });
  }

  connection.query(
    'INSERT INTO user (id, username, email, password, token) VALUES (NULL, ?, ?, ?, ?)',
    [username, email, password, '?'],
    (error, result) => {
      if (error) {
        console.error(error);
        return res.status(500).json({ error });
      }

      res.status(201).json({ status: '1', id: result.insertId, username, email });
    }
  );
});
app.post('/login', (req, res) => {
  const { usernameOrEmail, password } = req.body;

  if (!usernameOrEmail || !password) {
    return res.status(400).json({ error: 'Username/email dan password harus diisi' });
  }

  connection.query(
    'SELECT * FROM user WHERE username = ? OR email = ?',
    [usernameOrEmail, usernameOrEmail],
    (err, rows, fields) => {
      if (err) {
        console.error(err);
        return res.status(500).json({ error: 'Terjadi kesalahan saat mengakses database' });
      }

      if (rows.length === 0) {
        return res.status(401).json({ error: 'Username/email atau password salah' });
      }

      const user = rows[0];
      if (user.password === password) {
        const token = jwt.sign({ data: usernameOrEmail }, 'shhhhh');
		// Update token di database
        const updateQuery = "UPDATE user SET token = ? WHERE username = ? OR email = ?";
        connection.query(updateQuery, [token, usernameOrEmail, usernameOrEmail], (err, result) => {
			if (err) {
				console.error(err);
				return res.status(500).json({ error: 'Terjadi kesalahan saat memperbarui token' });
			}
			res.set('Authorization', `Bearer ${token}`);
			return res.json({ 'usernameOrEmail': usernameOrEmail, status: '1' });
		});
      } else {
        return res.status(401).json({ error: 'Username/email atau password salah' });
      }
    }
  );
});
app.get('/list', (req, res) => {
  const sql = 'SELECT * FROM `user`';
  connection.query(sql, (err, rows, fields) => {
    if (err instanceof Error) {
      return res.status(500).json({ err });
    }
    res.json({rows});
  });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});
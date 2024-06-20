# Destinatik Model API

### Base URL

https://destinatik-api-pd46stytga-uc.a.run.app

### Connect to Model

#### Path

```http
  /recommend
```

#### Method

```
  POST
```

#### Request

- user_id as int
- city as string

#### Response

- Success

```json
  {
  	"place_id": row.Place_Id,
		"place_name": row.Place_Name,
		"category": row.Category
	}
```

- Error no params provided
```json
  {
		"error": "Either user_id, city, or place_id must be provided"
		"status": 400
	}
```

- Error no User ID found
```json
  {
		error: User ID not found
		status: 400
	}
```

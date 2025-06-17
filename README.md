Proyecto fullstack para registro y autenticación de usuarios, desarrollado con **React** (frontend) y **Flask** (backend) usando MongoDB.

## Estructura del proyecto

```
mini-registro/
│
├── backend/   # API Flask + MongoDB
│   └── app.py
│   └── requirements.txt
│   └── ...
│
├── frontend/  # React + Bootstrap
│   └── src/
│   └── package.json
│   └── ...
│
└── README.md
```

## Requisitos

- Node.js y npm
- Python 3
- MongoDB Atlas o local

## Instalación

### Backend

```sh
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

### Frontend

```sh
cd frontend
npm install
npm start
```

## Variables de entorno

- **Frontend:**  
  Crea un archivo `.env` en la carpeta `frontend` con:
  ```
  VITE_BACKEND_URL=http://localhost:5000
  ```
- **Backend:**  
  Crea un archivo `.env` en la carpeta `backend` con tu conexión a MongoDB y otras variables necesarias.

## Uso

1. Inicia el backend (`flask run` o `python3 app.py`).
2. Inicia el frontend (`npm start`).
3. Abre [http://localhost:3000](http://localhost:3000) en tu navegador.

## Funcionalidades

- Registro de usuarios
- Login y autenticación JWT
- Consulta de usuarios registrados (según permisos)
- Contraseñas almacenadas de forma segura (hasheadas)
- Interfaz responsiva con Bootstrap

## Licencia

MIT
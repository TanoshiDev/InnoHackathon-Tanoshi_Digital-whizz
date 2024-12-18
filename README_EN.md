
# Whizz

**whizz.guru** is a forum platform for discussing various topics, with features for registration, authentication, topic creation, comments, likes, and avatar uploads. The project is divided into two parts: **frontend** and **backend**.

---

## **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/TanoshiDev/InnoHackathon-Tanoshi_Digital-whizz.git
cd InnoHackathon-Tanoshi_Digital-whizz
```

### **2. Run the Backend**

#### **Install Dependencies**
Navigate to the `backend` folder and install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

#### **Set up the Environment**
1. Create the `uploads/avatars` folder to store uploaded avatars:
   ```bash
   mkdir -p uploads/avatars
   ```
2. Ensure `SQLite` is used as the database, or change the connection in `database.py`.

#### **Run the Server**
```bash
uvicorn main:app --reload
```

- API documentation is available at:
  ```plaintext
  http://127.0.0.1:8000/docs
  ```

---

### **3. Run the Frontend**

#### **Install Dependencies**
Navigate to the `frontend` folder and install dependencies:
```bash
cd frontend
pip install -r requirements.txt
```

#### **Run the Application**
```bash
flet run [app_directory]
```

---

## **API Description (Backend)**

### **Key Features**
- **Registration and Authentication**: account creation, token-based authentication.
- **Topics Management**: create topics, search by keywords, like topics.
- **Comments**: add comments to topics.
- **Avatars**: upload and update profile pictures.

### **Documentation**
Swagger UI is automatically generated by FastAPI and is available at:
```plaintext
http://127.0.0.1:8000/docs
```

---

## **Technologies**

### **Backend**
- **FastAPI**: framework for API development.
- **SQLAlchemy**: ORM for database interaction.
- **SQLite**: database used in this project.
- **Pydantic**: validation of incoming and outgoing data.

### **Frontend**
- **Flet**: library for building GUI applications in Python.
- **UI Theming**: custom theming via `ColorScheme`.

---

## **Developers**
- **Tanoshi Digital Team**
- Contact: support@whizz.guru

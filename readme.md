# Step by Step Installations
```commands
1. cd backend
2. python -m venv venv
3. venv\Scripts\activate
4. pip install -r requirements.txt
5. Add the .env file in the backend folder
6. uvicorn app.main:app --reload
```

# .env

```
MONGODB_URI=
DATABASE_NAME=edtech
SECRET_KEY=b2wet435662szdcfhntyiv5c6ffdxwfer
HF_API_KEY=

```


## Folder Structure

```
edtech-adaptive-learning-platform/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── content.py
│   │   │   ├── performance.py
│   │   │   └── feedback.py
│   │   ├── repositories/
│   │   │   ├── user_repo.py
│   │   │   ├── content_repo.py
│   │   │   ├── performance_repo.py
│   │   │   └── feedback_repo.py
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── courses.py
│   │   │   ├── recommendations.py
│   │   │   ├── assessments.py
│   │   │   └── feedback.py
│   │   └── ai/
│   │       ├── __init__.py
│   │       ├── adaptive_learning.py
│   │       ├── recommendation_engine.py
│   │       ├── feedback_generator.py
│   │       ├── assessment_adapter.py
│   │       └── nlp_utils/
│   │           ├── summarizer.py
│   │           ├── question_generator.py
│   │           └── embedding_service.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Layout.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   └── …
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── StudentDashboard.jsx
│   │   │   ├── TeacherDashboard.jsx
│   │   │   └── AdminDashboard.jsx
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   └── auth.js
│   │   ├── theme/
│   │   │   ├── lightTheme.js
│   │   │   └── darkTheme.js
│   │   ├── App.jsx
│   │   └── index.js
│   ├── Dockerfile
│   └── package.json
├── analytics/
│   └── streamlit_app/
│       ├── app.py
│       ├── requirements.txt
│       └── Dockerfile
├── deployment/
│   ├── render.yaml
│   └── README.md
├── tests/
│   ├── backend/
│   │   ├── test_auth.py
│   │   ├── test_users.py
│   │   └── …
│   ├── ai/
│   │   ├── test_adaptive_learning.py
│   │   └── …
│   └── frontend/
│       └── …
├── .gitignore
└── README.md
```


# API CALLS
## POST http://localhost:8000/api/v1/auth/register

Request

```
{
  "email": "vishnu@example.com",
  "password": "securePass123",
  "role": "teacher",
  "name": "vishnu"
}
```

Response

```
{
    "id": "6891c96e83e557ce831de447",
    "email": "vishnu@example.com",
    "role": "teacher",
    "name": "vishnu"
}
```


<img width="2634" height="1060" alt="image" src="https://github.com/user-attachments/assets/b0199c31-1733-49c8-a9cf-3564d6646359" />
<img width="1357" height="509" alt="image" src="https://github.com/user-attachments/assets/7ec396ef-2f83-4716-bf3c-9c40a0497705" />
<img width="2542" height="1554" alt="image" src="https://github.com/user-attachments/assets/d84f8f94-f4fe-4643-bcf8-c7dcf7028259" />
<img width="2515" height="1057" alt="image" src="https://github.com/user-attachments/assets/52a86948-2004-4480-895f-e50e15687e41" />
<img width="2533" height="999" alt="image" src="https://github.com/user-attachments/assets/b5056593-e24e-4a79-acf8-842c1868420c" />
<img width="2531" height="1614" alt="image" src="https://github.com/user-attachments/assets/56edf7d6-ba4a-4e12-b536-09171a67fe44" />
<img width="2585" height="1665" alt="image" src="https://github.com/user-attachments/assets/f19c45e8-7a66-4944-bd5b-8123a0a8a0fa" />
<img width="1355" height="575" alt="image" src="https://github.com/user-attachments/assets/a775e8ff-76ba-40c5-854e-5c92f71f2029" />
<img width="1354" height="580" alt="image" src="https://github.com/user-attachments/assets/d752fc5d-10a9-4059-bb31-b2d5f72b2e1f" />
<img width="1358" height="591" alt="image" src="https://github.com/user-attachments/assets/33c0f974-d2e9-48d6-b80e-99b3d7b95a36" />
<img width="1356" height="610" alt="image" src="https://github.com/user-attachments/assets/3dc3b885-46cb-4c16-a18e-e56cce41f4ab" />



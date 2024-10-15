from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from core.config import settings
from passlib.context import CryptContext

engine = create_engine(settings.get_DATABASE_URL())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# настройка хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_default_users(db: Session):
    from models.user import User
    # список пользователей по умолчанию
    default_users = [
        {"username": "admin", "password": "admin", "email": "admin@example.com"},
        {"username": "user", "password": "user", "email": "user@example.com"},
        {"username": "doctor", "password": "doctor", "email": "doctor@example.com"},
        {"username": "manager", "password": "manager", "email": "manager@example.com"},
    ]

    for user_data in default_users:
        # существует ли пользователь
        user_exists = db.query(User).filter(User.username == user_data["username"]).first()
        if not user_exists:
            # если не существует, создаем нового пользователя
            new_user = User(
                username=user_data["username"],
                hashed_password=pwd_context.hash(user_data["password"]),
                email=user_data["email"]
            )
            db.add(new_user)
    
    db.commit()

# создания всех таблиц и пользователей по умолчанию
def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        create_default_users(db)
    finally:
        db.close()

# получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

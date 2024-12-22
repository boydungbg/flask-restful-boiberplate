from dataclasses import dataclass, field
from datetime import datetime
from extensions.bcrypt import flask_bcrypt
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, SmallInteger, BIGINT
from database import db


@dataclass
class User(db.Model):
    __tablename__ = "users"  # Table name in the database

    id: int = field(init=False)
    username: str
    full_name: str
    email: str
    password_hash: str
    status: int
    last_login: datetime = field(init=False)
    created_at: datetime = field(init=False)
    updated_at: datetime = field(init=False)

    id: Mapped[int] = mapped_column(
        BIGINT,
        primary_key=True,
        autoincrement=True,
    )  # Primary key column

    username: Mapped[str] = mapped_column(
        String(60), unique=True, nullable=False
    )  # Name column

    full_name: Mapped[str] = mapped_column(String(60), nullable=False)  # Name column

    email: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False
    )  # Email column

    password_hash: Mapped[str] = mapped_column(
        String(255), nullable=False
    )  # Password column

    status: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=0)

    # Timestamp fields
    last_login: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    # Timestamp fields
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )
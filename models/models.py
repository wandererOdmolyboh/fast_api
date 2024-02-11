from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, JSON, TIMESTAMP, ForeignKey, Boolean

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON)
)

user = Table("user", metadata,
             Column("id", Integer, primary_key=True),
             Column("email", String, nullable=False),
             Column("login", String, nullable=False),
             Column("hashed_password", String, nullable=False),
             Column("created", TIMESTAMP, default=datetime.utcnow),
             Column("role_id", Integer, ForeignKey(role.c.id)),
             Column("is_active", Boolean, default=True, nullable=False),
             Column("is_superuser", Boolean, default=False, nullable=False),
             Column("is_verified", Boolean, default=False, nullable=False),
             )

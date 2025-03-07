import uuid
from datetime import datetime, timezone, timedelta
from sqlalchemy.dialects.postgresql import UUID
from app.database import db

UTC_PLUS_1 = timezone(timedelta(hours=1))


# Category Model
class Category(db.Model):
    __tablename__ = "categories"

    category_id = db.Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        default=uuid.uuid4,
        primary_key=True,
    )
    category_name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC_PLUS_1))

    # Relationship to Expenses
    expenses = db.relationship(
        "Expense",
        backref="category",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy=True,
    )

    def __repr__(self):
        return f"<Category {self.name}>"


# Expense Model
class Expense(db.Model):
    __tablename__ = "expenses"

    expense_id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    expense_amount = db.Column(db.Float, nullable=False)
    expense_description = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=lambda: datetime.now(UTC_PLUS_1))

    # Foreign Key to Category
    category_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("categories.category_id", ondelete="CASCADE"),
        name="fk_expense_category",
        nullable=False,
    )  # ✅ Auto-delete related expenses

    def __repr__(self):
        return f"<Expense {self.amount} on {self.date}>"

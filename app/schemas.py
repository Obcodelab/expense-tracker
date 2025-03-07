from marshmallow import Schema, fields


class CategorySchema(Schema):
    category_id = fields.UUID(dump_only=True)  # Read-only field
    category_name = fields.Str(required=True)  # Required field
    created_at = fields.DateTime(
        format="%Y-%m-%d %H:%M:%S", dump_only=True
    )  # Read-only field


# 🟢 Expense Schema
class ExpenseSchema(Schema):
    expense_id = fields.UUID(dump_only=True)  # Read-only field
    expense_amount = fields.Float(required=True)  # Required field
    expense_description = fields.Str()  # Optional field
    date = fields.Date(format="%Y-%m-%d %H:%M:%S", dump_only=True)  # Read-only field
    category_id = fields.UUID(required=True)  # Required field (ForeignKey)


# Initialize schemas
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

expense_schema = ExpenseSchema()
expenses_schema = ExpenseSchema(many=True)

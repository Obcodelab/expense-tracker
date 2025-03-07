import uuid
from flask import Blueprint, request, jsonify
from sqlalchemy import text
from app.database import db
from app.models import Category, Expense
from app.schemas import (
    category_schema,
    categories_schema,
    expense_schema,
    expenses_schema,
)

expense_routes = Blueprint("expense_routes", __name__)


# 🟢 Create Category (with Duplicate Check)
@expense_routes.route("/categories", methods=["POST"])
def create_category():
    data = request.get_json()
    if not data or "category_name" not in data:
        return jsonify({"error": "Category name is required"}), 400

    # Check if category already exists
    existing_category = Category.query.filter_by(
        category_name=data["category_name"]
    ).first()
    if existing_category:
        return jsonify({"error": "Category already exists"}), 400

    category = Category(category_name=data["category_name"])
    db.session.add(category)
    db.session.commit()

    return jsonify(category_schema.dump(category)), 201


# 🔵 Get All Categories
@expense_routes.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    return jsonify(categories_schema.dump(categories)), 200


# 🟡 Get Single Category by ID
@expense_routes.route("/categories/<uuid:category_id>", methods=["GET"])
def get_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category_schema.dump(category)), 200


# 🟠 Update Category
@expense_routes.route("/categories/<uuid:category_id>", methods=["PUT"])
def update_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    data = request.get_json()
    if "category_name" in data:
        category.category_name = data["category_name"]

    db.session.commit()
    return jsonify(category_schema.dump(category)), 200


# 🔴 Delete Category
@expense_routes.route("/categories/<uuid:category_id>", methods=["DELETE"])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted"}), 200


# 🔴 Delete all categories
@expense_routes.route("/categories", methods=["DELETE"])
def delete_all_categories():
    categories = Category.query.all()
    for category in categories:
        db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "All categories deleted"}), 200


# 🟢 Create Expense
@expense_routes.route("/expenses", methods=["POST"])
def create_expense():
    data = request.get_json()

    # Validate required fields
    if not data.get("expense_amount") or not data.get("category_id"):
        return jsonify({"error": "expense_amount and category_id are required"}), 400

    try:
        category_id = uuid.UUID(data["category_id"])
    except ValueError:
        return jsonify({"error": "Invalid category ID format"}), 400

    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Invalid category ID"}), 404

    new_expense = Expense(
        expense_id=uuid.uuid4(),
        expense_amount=data["expense_amount"],
        expense_description=data.get("expense_description"),
        category_id=category_id,
    )

    db.session.add(new_expense)
    db.session.commit()

    return jsonify(expense_schema.dump(new_expense)), 201


# 🟢 Get All Expenses
@expense_routes.route("/expenses", methods=["GET"])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify(expenses_schema.dump(expenses)), 200


# 🟢 Get Single Expense by ID
@expense_routes.route("/expenses/<uuid:expense_id>", methods=["GET"])
def get_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    return jsonify(expense_schema.dump(expense)), 200


# 🟢 Update Expense
@expense_routes.route("/expenses/<uuid:expense_id>", methods=["PUT"])
def update_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404

    data = request.get_json()

    # Update fields
    expense.amount = data.get("expense_amount", expense.amount)
    expense.description = data.get("expense_description", expense.description)
    expense.category_id = data.get("category_id", expense.category_id)

    db.session.commit()

    return jsonify(expense_schema.dump(expense)), 200


# 🟢 Delete Expense
@expense_routes.route("/expenses/<uuid:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({"message": "Expense deleted"}), 200


# 🟢 Delete all expenses
@expense_routes.route("/expenses", methods=["DELETE"])
def delete_all_expenses():
    expenses = Expense.query.all()
    for expense in expenses:
        db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "All expenses deleted"}), 200

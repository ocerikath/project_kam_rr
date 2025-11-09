from types import SimpleNamespace
from flask import render_template, Blueprint, request, jsonify
from .models import db, Category, Product, Lead
from . import mail
from app import mail 
from flask_mail import Message

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    categories = Category.query.order_by(Category.name).all()
    products = Product.query.order_by(Product.id).all()

    # Создаем "пустую" форму для шаблона
    form = SimpleNamespace(
        full_name=SimpleNamespace(value=''),
        phone=SimpleNamespace(value=''),
        email=SimpleNamespace(value=''),
        comment=SimpleNamespace(value='')
    )

    return render_template('index.html', categories=categories, products=products, form=form)


@main_bp.route('/catalog')
def catalog():
    categories = Category.query.order_by(Category.name).all()
    products = Product.query.order_by(Product.id).all()
    return render_template('catalog.html', categories=categories, products=products)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        errors = validate_lead_form(data)

        if errors:
            return jsonify({"success": False, "errors": errors})

        # Сохраняем заявку в БД
        lead = Lead(
            full_name=data.get("full_name"),
            phone=data.get("phone"),
            email=data.get("email"),
            comment=data.get("comment"),
            product_name=data.get("product_name"),  # если нужно
            product_id=data.get("product_id")       # если нужно
        )
        db.session.add(lead)
        db.session.commit()

        # ОТПРАВКА НА ПОЧТУ УБРАНА

        return jsonify({"success": True, "message": "Заявка успешно сохранена!"})

    # Для GET-запроса просто рендерим страницу
    from types import SimpleNamespace
    form = SimpleNamespace(
        full_name=SimpleNamespace(value=''),
        phone=SimpleNamespace(value=''),
        email=SimpleNamespace(value=''),
        comment=SimpleNamespace(value='')
    )
    return render_template('contact.html', form=form)


@main_bp.route('/submit-lead/', methods=['POST'])
def submit_lead():
    full_name = request.form.get('full_name', '').strip()
    phone = request.form.get('phone', '').strip()
    email = request.form.get('email', '').strip()
    comment = request.form.get('comment', '').strip()
    product_name = request.form.get('product_name', '').strip()
    product_id = request.form.get('product_id')

    errors = {}
    if len(full_name) < 2:
        errors['full_name'] = ["Имя должно содержать минимум 2 символа."]
    if not phone.startswith('+7') or len(phone.replace('+','').replace(' ','').replace('(','').replace(')','')) < 11:
        errors['phone'] = ["Введите корректный номер телефона."]
    if email and "@" not in email:
        errors['email'] = ["Введите корректный email."]
    if len(comment) > 300:
        errors['comment'] = ["Комментарий не должен превышать 300 символов."]

    if errors:
        return jsonify({'success': False, 'errors': errors})

    # Сохраняем в БД
    lead = Lead(
        full_name=full_name,
        phone=phone,
        email=email,
        comment=comment,
        product_name=product_name,
        product_id=product_id
    )
    db.session.add(lead)
    db.session.commit()

    # ОТПРАВКА ПИСЕМ УБРАНА

    return jsonify({'success': True, 'message': 'Заявка успешно сохранена!'})

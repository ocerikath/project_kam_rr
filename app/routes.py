from types import SimpleNamespace
from flask import render_template, Blueprint, request, jsonify
from .models import db, Category, Product, Lead
from . import mail
from app import mail 
from flask_mail import Message
from . import send_telegram

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

@main_bp.route('/uslugi/dostavka')
def delivery():
    return render_template('uslugi/dostavka.html')


@main_bp.route('/uslugi/dorozhnye-raboty')
def roads():
    return render_template('uslugi/dorozhnye-raboty.html')


@main_bp.route('/uslugi/vyvoz-musora')
def trash():
    return render_template('uslugi/vyvoz-musora.html')


@main_bp.route('/uslugi/vyvoz-snega')
def snow():
    return render_template('uslugi/vyvoz-snega.html')


@main_bp.route('/uslugi/arenda-tehniki')
def tech():
    return render_template('uslugi/arenda-tehniki.html')


@main_bp.route('/uslugi/zemlyanye-raboty')
def earthworks():
    return render_template('uslugi/zemlyanye-raboty.html')


@main_bp.route('/uslugi/individualnye-zakazy')
def custom():
    return render_template('uslugi/individualnye-zakazy.html')

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

        # Формируем сообщение
        tg_msg = (
            f"<b>🔔 Новая заявка!</b>\n"
            f"👤 Имя: {data.get('full_name')}\n"
            f"📞 Тел: {data.get('phone')}\n"
            f"📝 {data.get('comment')}"
        )
        
        # Вызываем отправку
        send_telegram(tg_msg)

        return jsonify({"success": True, "message": "Заявка принята!"})

    # ТУТ УДАЛИ ТОТ ПУСТОЙ TRY/EXCEPT, КОТОРЫЙ БЫЛ РАНЕЕ

    # Обычный GET запрос
    from types import SimpleNamespace
    form = SimpleNamespace(
        full_name=SimpleNamespace(value=''),
        phone=SimpleNamespace(value=''),
        email=SimpleNamespace(value=''),
        comment=SimpleNamespace(value='')
    )
    return render_template('contact.html', form=form)

@main_bp.route('/privacy')
def privacy():
    return render_template('privacy.html')
    
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

    # Добавляем отправку в Telegram здесь:
    tg_msg = (
        f"<b>🏗 Новая заявка (ПескоЩебень)</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>Имя:</b> {full_name}\n"
        f"📞 <b>Телефон:</b> <code>{phone}</code>\n"
        f"📧 <b>Email:</b> {email or 'не указан'}\n"
        f"📝 <b>Запрос:</b> {comment}\n"
        f"━━━━━━━━━━━━━━━━━━"
    )
    
    try:
        send_telegram(tg_msg)
    except Exception as e:
        print(f"Ошибка при вызове send_telegram: {e}")

    return jsonify({'success': True, 'message': 'Заявка успешно сохранена!'})

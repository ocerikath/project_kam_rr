def validate_lead_form(data):
    errors = {}
    full_name = data.get("full_name", "").strip()
    phone = data.get("phone", "").strip()
    email = data.get("email", "").strip()
    comment = data.get("comment", "").strip()

    if not full_name or len(full_name) < 2:
        errors["full_name"] = "Имя должно содержать минимум 2 символа."
    
    if not phone or not phone.startswith("+7") or len(phone.replace("+","").replace(" ","").replace("(","").replace(")","")) < 11:
        errors["phone"] = "Введите корректный номер телефона."
    
    if email and "@" not in email:
        errors["email"] = "Введите корректный email."
    
    if len(comment) > 300:
        errors["comment"] = "Комментарий не должен превышать 300 символов."

    return errors

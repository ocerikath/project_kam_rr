import os

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

dostavka_css = read_file('app/static/css/dostavka.css')
index_css = read_file('app/static/css/index.css')
contact_css = read_file('app/static/css/contact.css')
desktop_css = read_file('app/static/css/desktop.css')
style_css = read_file('app/static/css/style.css')

map_section_dostavka = """/* Секция 4 "область нашей работы */
.map-section {
    padding: clamp(16px, 4vw, 32px);
    text-align: center;
    background-color: #EAE6DC;
  }
  
  .map-text h2 {
    font-size: clamp(1.2rem, 3vw, 2rem);
    margin-bottom: clamp(8px, 2vw, 16px);
  }
  
  .map-text p {
    font-size: clamp(1rem, 2.5vw, 1.4rem);
    margin-bottom: clamp(12px, 3vw, 20px);
    color: #555;
  }
  
  #map {
    width: 100%;
    height: clamp(300px, 60vh, 500px);
    border-radius: clamp(8px, 2vw, 16px);
    overflow: hidden;
  }"""

dostavka_css = dostavka_css.replace(map_section_dostavka, "")

map_section_desktop = """/* Секция "Область нашей работы" для десктопа (992px и выше) */
@media (min-width: 992px) {
    .map-section {
      padding: 40px 20px;
    }
    
    .map-text {
      max-width: 800px;
      margin: 0 auto 30px;
    }
    
    .map-text h2 {
      font-size: 2.2rem;
      margin-bottom: 20px;
    }
    
    .map-text p {
      font-size: 1.5rem;
      margin-bottom: 30px;
    }
    
    #map {
      max-width: 1200px;
      margin: 0 auto;
      height: 500px;
      border-radius: 16px;
    }
    
    .map-section p[style*="font-size:14px"] {
      font-size: 16px !important;
      margin-top: 16px;
      max-width: 800px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.5;
    }
  }"""
dostavka_css = dostavka_css.replace(map_section_desktop, "")
desktop_css = desktop_css.replace(map_section_desktop, "")

map_section_index = """/* Секция 4 "область нашей работы */
.map-section {
  padding: clamp(16px, 4vw, 32px);
  text-align: center;
  background-color: #EAE6DC;
}

.map-text h2 {
  font-size: clamp(1.2rem, 3vw, 2rem);
  margin-bottom: clamp(8px, 2vw, 16px);
}

.map-text p {
  font-size: clamp(1rem, 2.5vw, 1.4rem);
  margin-bottom: clamp(12px, 3vw, 20px);
  color: #555;
}

#map {
  width: 100%;
  height: clamp(300px, 60vh, 500px);
  border-radius: clamp(8px, 2vw, 16px);
  overflow: hidden;
}"""
index_css = index_css.replace(map_section_index, "")


form_index = """.feedback {
  background-color: #EAE6DC;
  color: #3E3E3E;
  padding: clamp(2rem, 6vw, 5rem) clamp(1rem, 5vw, 3rem);
  width: 100%;
}

.feedback__container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
  gap: clamp(2rem, 5vw, 4rem);
  max-width: 1200px;
  margin: 0 auto;
  flex-wrap: wrap;
}

.feedback__text {
  flex: 1 1 45%;
  display: flex;
  flex-direction: column;
  gap: clamp(1rem, 2vw, 1.5rem);
}

.feedback__title {
  font-size: clamp(1.8rem, 4vw, 2.5rem);
  font-weight: 700;
}

.feedback__desc,
.feedback__extra {
  font-size: clamp(1rem, 2.5vw, 1.2rem);
  line-height: 1.6;
}

.feedback__important {
  background: rgba(62, 62, 62, 0.05);
  padding: clamp(0.8rem, 2vw, 1rem);
  border-left: 4px solid #8F735B;
  font-size: clamp(1rem, 2.5vw, 1.2rem);
  border-radius: 6px;
}

.feedback__phone {
  display: block;
  margin-top: 0.3em; /* небольшой отступ сверху для воздуха */
  color: #8F735B;
  text-decoration: none;
  font-weight: 600;
}

.feedback__phone:hover {
  text-decoration: underline;
}

.feedback__form {
  flex: 1 1 45%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.feedback__form-placeholder {
  width: 100%;
  min-height: clamp(250px, 40vw, 400px);
  background: #fff;
  border: 2px dashed #CFC8BA;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: #8F735B;
  text-align: center;
}

@media (max-width: 768px) {
  .feedback__container {
    flex-direction: column;
    align-items: center;
  }

  .feedback__text,
  .feedback__form {
    flex: 1 1 100%;
  }

  .feedback__form-placeholder {
    min-height: clamp(300px, 60vw, 400px);
  }
}


.adv-card {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(0.8rem, 3vw, 1rem);
  background-image: url("../images/site_images/individual.png");
  background-size: cover;
  background-position: center;
  border-radius: clamp(0.8rem, 2vw, 1rem);
  padding: clamp(0.9rem, 3vw, 1.3rem);
  overflow: hidden; /* чтобы overlay не выходил за границы */
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.adv-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  z-index: 1;
  transition: background 0.3s ease;
}

.adv-card:hover .overlay {
  background: rgba(0, 0, 0, 0.25);
}

.adv-text {
  position: relative;
  z-index: 2;
  color: #fff;
  text-align: center;
  font-size: clamp(0.9rem, 2vw, 1.1rem);
}


/* форма */
#lead-section {
  position: relative;
  padding: clamp(2rem, 4vw, 3rem);
  margin: 2rem auto 0;
  background: #CBCAC7;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}
#leadForm{
  position: relative;
  z-index: 100;
}

/* Табличка-за-формой */
.form-background {
  position: absolute;
  top: 1rem;     /* отступ сверху */
  left: 1rem;    /* отступ слева */
  right: 1rem;   /* отступ справа */
  bottom: 1rem;  /* отступ снизу */
  
  background: linear-gradient(
    135deg,
    #EAE6DC 0%, 
    rgba(223, 216, 188, 0.2) 100%
  );
  
  border-radius: clamp(0.75rem, 1.5vw, 1.25rem);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  
  z-index: -1; /* ниже формы */
}


/* Заголовок */
#lead-section h2 {
  font-size: clamp(1.5rem, 2.5vw, 2.25rem);
  font-weight: 600;
  color: #3E3e3e;
  text-align: center;
  margin-bottom: clamp(1.5rem, 2vw, 2rem);
  letter-spacing: 0.02em;
}

/* Поля с иконками */
.input-container {
  position: relative;
  margin-bottom: clamp(1.2rem, 2.5vw, 1.8rem);
  display: flex;
  flex-direction: column;
  
}

.input-container .icon {
  position: absolute;
  left: clamp(0.75rem, 1.5vw, 1rem);
  top: 1rem; /* Фиксируем позицию относительно верха поля ввода */
  width: auto;
  height: clamp(1.2rem, 2.5vw, 1.6rem);
  opacity: 0.7;
  transition: opacity 0.3s ease;
  z-index: 1; /* Убедимся, что иконка остается над полем */
}

.input-container input,
.input-container textarea {
  padding: clamp(0.75rem, 1.5vw, 1rem) clamp(0.75rem, 1.5vw, 1rem) clamp(0.75rem, 1.5vw, 1rem) clamp(3rem, 5vw, 3.5rem);
  width: 100%;
  font-size: clamp(0.95rem, 1.2vw, 1rem);
  border: 1px solid #8C7865;
  border-radius: clamp(0.5rem, 1vw, 0.75rem);
  background: #D4CDBF;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.input-container input:focus,
.input-container textarea:focus {
  outline: none;
  border-color: #8C7865;
  box-shadow: 0 0 8px rgba(140, 120, 101, 0.3);
}

.input-container input:focus + .icon,
.input-container textarea:focus + .icon {
  opacity: 1;
}

/* Комментарий */
textarea {
  resize: none;
  min-height: clamp(100px, 15vw, 120px);
}

/* Ошибки */
.field-error {
  color: red;
  font-size: clamp(0.75rem, 1vw, 0.85rem);
  margin-top: clamp(0.3rem, 0.5vw, 0.5rem);
  font-weight: 400;
  text-align: left;
}

/* Чекбокс */
.checkbox-container {
  margin-bottom: clamp(1rem, 2vw, 1.5rem);
}

.custom-checkbox {
  display: flex;
  align-items: flex-start;
  cursor: pointer;
  font-size: clamp(0.9rem, 1.2vw, 1rem);
  color: #333;
  position: relative;
}

.custom-checkbox input[type="checkbox"] {
  position: absolute;
  opacity: 0;
  cursor: pointer;
}

.checkmark {
  margin-right: clamp(0.5rem, 1vw, 0.75rem);
  width: clamp(1rem, 1.5vw, 1.2rem);
  height: clamp(1rem, 1.5vw, 1.2rem);
  background-color: #fff;
  border: 2px solid #ccc;
  border-radius: 3px;
  flex-shrink: 0;
  margin-top: clamp(0.1rem, 0.2vw, 0.15rem);
  position: relative;
}

.custom-checkbox input:checked ~ .checkmark {
  background-color: #8C7865;
  border-color: #8C7865;
}

.custom-checkbox input:checked ~ .checkmark:after {
  content: "";
  position: absolute;
  left: 4px;
  top: 1px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.checkbox-text {
  white-space: normal;
  word-wrap: break-word;
  line-height: 1.4;
}

.checkbox-container a {
  color: #1100FF;
  text-decoration: none;
  transition: text-decoration 0.3s ease;
  white-space: nowrap;
}

.checkbox-container a:hover {
  text-decoration: underline;
}

/* Кнопка */
#submitBtn {
  padding: clamp(0.75rem, 1.5vw, 1rem) clamp(1.5rem, 3vw, 2rem);
  font-size: clamp(1rem, 1.3vw, 1.1rem);
  cursor: pointer;
  border: none;
  border-radius: clamp(0.5rem, 1vw, 0.75rem);
  background: #8C7865;
  color: #fff;
  width: 100%;
  font-weight: 500;
  transition: background 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
}

#submitBtn:hover:not(:disabled) {
  background: #736455;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(140, 120, 101, 0.3);
}

#submitBtn:disabled {
  background: #ccc;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

/* Контакты */
.contact-info-area {
  background-color: #D4CDBF;
  padding: clamp(1rem, 2vw, 2rem);
  border-radius: clamp(0.5rem, 1vw, 1rem);
}

.contact-info-text ul {
  list-style: none; /* убираем точки */
  margin: 0;
  padding: 0;
}

.contact-info-text li {
  margin-bottom: clamp(0.5rem, 1vw, 1rem);
}

.contact-info-text p {
  color: #4A4440;
  font-size: clamp(1rem, 2vw, 1.25rem);
  margin: 0;
  font-weight: 500;
}

.phone-number-info,
.email-adress-info {
  color: #4A4440;
  font-size: clamp(1rem, 2vw, 1.25rem);
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease;
}

.phone-number-info:hover,
.email-adress-info:hover {
  color: #8F735B; /* лёгкий акцент при наведении */
}

/* Мобильный фикс для формы, чтобы страница не дергалась */
@media (max-width: 768px) {
  /* Убираем фиксированные отступы, делаем блок полностью адаптивным */
  .feedback__container {
    padding-bottom: env(safe-area-inset-bottom); /* для iOS */
  }

  #leadForm input,
  #leadForm textarea {
    font-size: 1rem; /* чуть больше, чтобы клавиатура не перекрывала */
  }

  /* Делаем форму полностью в потоке документа, убираем absolute / fixed */
  #lead-section,
  .form-background {
    position: relative !important;
  }
}"""
index_css = index_css.replace(form_index, "")
contact_css = contact_css.replace(form_index, "")

modal_index = """/* Модальное окно */
#modal {
  display: none;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: clamp(1.5rem, 3vw, 2rem);
  background: #fff;
  border: 1px solid #8C7865;
  border-radius: clamp(0.75rem, 1.5vw, 1rem);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  z-index: 1000;
  max-width: clamp(280px, 85%, 450px);
  text-align: center;
}

#modal p {
  margin-bottom: clamp(1rem, 2vw, 1.5rem);
  font-size: clamp(1rem, 1.3vw, 1.15rem);
  color: #333;
}

#modal button {
  padding: clamp(0.6rem, 1.2vw, 0.9rem) clamp(1.5rem, 3vw, 2rem);
  font-size: clamp(0.95rem, 1.2vw, 1rem);
  cursor: pointer;
  border: none;
  border-radius: clamp(0.5rem, 1vw, 0.75rem);
  background: #8C7865;
  color: #fff;
  transition: background 0.3s ease, transform 0.2s ease;
}

#modal button:hover {
  background: #736455;
  transform: translateY(-2px);
}"""
index_css = index_css.replace(modal_index, "")
contact_css = contact_css.replace(modal_index, "")

# Some extra cleanup for multiple media queries in index.css
media_queries = """@media (min-width: 576px) {
    .my-4 .container {
      padding-left: 0 !important;
      padding-right: 0 !important;
      max-width: none !important;
    }
  }
  
  @media (min-width: 768px) {
    .my-4 .container {
      padding-left: 0 !important;
      padding-right: 0 !important;
      max-width: none !important;
    }
  }
  
  @media (min-width: 992px) {
    .my-4 .container {
      padding-left: 0 !important;
      padding-right: 0 !important;
      max-width: none !important;
    }
  }
  @media (min-width: 576px) {
    .container, .container-sm {
        max-width: none !important;
    }
}"""
clean_media = """@media (min-width: 576px) {
  .my-4 .container,
  .container, 
  .container-sm {
    padding-left: 0 !important;
    padding-right: 0 !important;
    max-width: none !important;
  }
}"""
index_css = index_css.replace(media_queries, clean_media)


style_css += "\n\n/* === Общие секции (карта, форма, модальное окно) === */\n"
style_css += form_index
style_css += "\n" + modal_index
style_css += "\n" + map_section_index
style_css += "\n" + map_section_desktop

write_file('app/static/css/index.css', index_css)
write_file('app/static/css/contact.css', contact_css)
write_file('app/static/css/dostavka.css', dostavka_css)
write_file('app/static/css/desktop.css', desktop_css)
write_file('app/static/css/style.css', style_css)
print("CSS files cleaned up successfully!")

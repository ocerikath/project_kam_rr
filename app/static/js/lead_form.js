document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("leadForm");

    // Поля формы
    const fields = ["full_name", "phone", "email", "comment"];

    // Создаём контейнеры для ошибок рядом с полями
    fields.forEach(field => {
        const input = form.querySelector(`#id_${field}`);
        if (input) {
            let errorDiv = document.createElement("div");
            errorDiv.className = "field-error";
            errorDiv.style.color = "red";
            errorDiv.style.fontSize = "0.9em";
            errorDiv.style.marginTop = "0.2em";
            input.parentNode.insertBefore(errorDiv, input.nextSibling);

            // Скрытие ошибок при вводе
            input.addEventListener("input", () => hideError(input));
        }
    });

    // Запрет изменения размера textarea комментария
    const commentInput = form.querySelector("#id_comment");
    if (commentInput) commentInput.style.resize = "none";

    // Модальное окно
    const modal = document.createElement("div");
    modal.id = "modal";
    modal.style.display = "none";
    modal.style.position = "fixed";
    modal.style.top = "50%";
    modal.style.left = "50%";
    modal.style.transform = "translate(-50%, -50%)";
    modal.style.padding = "clamp(1.5rem, 3vw, 2.5rem)";
    modal.style.background = "#fff";
    modal.style.border = "1px solid #ccc";
    modal.style.borderRadius = "clamp(0.5rem,1vw,1rem)";
    modal.style.boxShadow = "0 0 clamp(0.5rem,1vw,1rem) rgba(0,0,0,0.2)";
    modal.style.zIndex = 1000;
    modal.style.maxWidth = "clamp(300px, 60%, 500px)";
    modal.innerHTML = `
        <p id="modalMessage" style="margin-bottom:clamp(0.5rem,1vw,1rem); font-size:clamp(1rem,1.2vw,1.3rem);"></p>
        <button id="modalClose" style="padding:clamp(0.5rem,1vw,1rem) clamp(1rem,2vw,1.5rem); cursor:pointer;">Закрыть</button>
    `;
    document.body.appendChild(modal);

    const modalMessage = modal.querySelector("#modalMessage");
    const modalClose = modal.querySelector("#modalClose");
    modalClose.addEventListener("click", () => modal.style.display = "none");

    // Телефонное поле
    const phoneInput = form.querySelector("#id_phone");

    if (phoneInput) {
        // +7 ( появляется сразу при фокусе
        phoneInput.addEventListener("focus", () => {
            if (phoneInput.value === "") phoneInput.value = "+7 (";
        });

        // Убираем +7 ( если поле пустое
        phoneInput.addEventListener("blur", () => {
            const inputWithoutDigits = phoneInput.value.replace(/\D/g, "").length <= 1;
            if (inputWithoutDigits) phoneInput.value = "";
        });

        // Форматирование номера
        phoneInput.addEventListener("input", () => {
            let currentValue = phoneInput.value.replace(/\D/g, "");
            if (currentValue.length > 0) {
                let formattedValue = "+7 (";
                if (currentValue.length > 1) formattedValue += currentValue.substring(1, 4);
                if (currentValue.length >= 5) formattedValue += ") " + currentValue.substring(4, 7);
                if (currentValue.length >= 8) formattedValue += " " + currentValue.substring(7, 9);
                if (currentValue.length >= 10) formattedValue += " " + currentValue.substring(9, 11);
                phoneInput.value = formattedValue;
            }
            hideError(phoneInput);
        });
    }

    // Скрытие ошибок
    function hideError(input) {
        const errorDiv = input.parentNode.querySelector(".field-error");
        if (errorDiv) errorDiv.innerText = "";
    }

    // Получение CSRF токена
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie("csrftoken");

    // Отправка формы через AJAX
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
    
        // 1. Подготовка интерфейса
        submitBtn.disabled = true; // Блокируем кнопку сразу
        
        // Показываем модалку в режиме "Загрузка"
        modalMessage.innerHTML = `
            <div class="loader"></div>
            <p class="modal-loading-text">Отправляем вашу заявку...</p>
        `;
        modalClose.style.display = "none"; // Прячем кнопку закрытия, чтобы не прервали
        modal.style.display = "block";
    
        const formData = new FormData(form);
    
        try {
            const response = await fetch("/submit-lead/", {
                method: "POST",
                headers: { "X-CSRFToken": csrftoken },
                body: formData,
            });
    
            const result = await response.json();
    
            if (result.success) {
                // 2. Успех: меняем лоадер на галочку или текст
                modalMessage.innerHTML = `
                    
                    <p style="text-align: center;">${result.message || "Заявка успешно сохранена!"}</p>
                `;
                form.reset();
            } else if (result.errors) {
                // Ошибка валидации: закрываем модалку и показываем ошибки в полях
                modal.style.display = "none";
                for (const [field, msgs] of Object.entries(result.errors)) {
                    const errorDiv = form.querySelector(`#id_${field} + .field-error`);
                    if (errorDiv) errorDiv.innerText = msgs.join(", ");
                }
            }
        } catch (err) {
            modalMessage.innerText = "Ошибка соединения с сервером. Попробуйте еще раз.";
            console.error(err);
        } finally {
            // В любом случае возвращаем кнопку закрытия и разблокируем кнопку (если нужно)
            modalClose.style.display = "block";
            if (!consentCheckbox.checked) {
                submitBtn.disabled = true;
            } else {
                submitBtn.disabled = false;
            }
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const consentCheckbox = document.getElementById("consent");
    const submitBtn = document.getElementById("submitBtn");

    // Кнопка активна только при включенном чекбоксе
    consentCheckbox.addEventListener("change", function() {
        submitBtn.disabled = !this.checked;
    });

    // Закрытие модального окна
    const modal = document.getElementById("modal");
    const modalClose = document.getElementById("modalClose");
    modalClose.addEventListener("click", function() {
        modal.style.display = "none";
    });
});

// JS фикс для мобильных
document.addEventListener("DOMContentLoaded", () => {
    if (window.innerWidth <= 768) {
      const feedbackSection = document.getElementById("feedback");
      const inputs = feedbackSection.querySelectorAll("input, textarea");
  
      inputs.forEach(input => {
        input.addEventListener("focus", () => {
          // Прокручиваем страницу до самого блока формы, чтобы input был виден
          setTimeout(() => {
            input.scrollIntoView({ behavior: "smooth", block: "center" });
          }, 300);
        });
      });
    }
  });
  

  document.addEventListener("DOMContentLoaded", () => {
    const advTexts = document.querySelectorAll(".adv-text");
    advTexts.forEach(el => {
        el.style.display = "block"; // показываем элемент
        el.style.opacity = 1;        // на случай, если была анимация fade
    });
});

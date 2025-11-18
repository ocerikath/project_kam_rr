document.addEventListener("DOMContentLoaded", () => {
    const accordionBtn = document.querySelector(".accordion-btn");
    const submenu = document.querySelector(".submenu");

    if (accordionBtn) {
        accordionBtn.addEventListener("click", () => {
            const isOpen = submenu.style.display === "block";
            submenu.style.display = isOpen ? "none" : "block";
        });
    }
});

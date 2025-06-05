const darkModeToggle = document.getElementById('darkModeToggle');
const logo = document.getElementById('logo');
const headerText = document.querySelector('.header-text');
const subtitleText = document.querySelector('.subtitle-text');

darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');

    // Cambiar el logo
    if (document.body.classList.contains('dark-mode')) {
        logo.src = logo.dataset.logoDark;
        darkModeToggle.textContent = '☀️ Modo Claro';
    } else {
        logo.src = logo.dataset.logoLight;
        darkModeToggle.textContent = '🌙 Modo Oscuro';
    }

    // Guardar preferencia (opcional)
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
});

// Cargar preferencia al inicio
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
    logo.src = logo.dataset.logoDark;
    darkModeToggle.textContent = '☀️ Modo Claro';
}
document.addEventListener('DOMContentLoaded', function () {
    // Bootstrap ya maneja los colapsables, así que este script puede ser más simple
    // O puedes agregar funcionalidades adicionales si es necesario

    // Ejemplo: Cerrar el offcanvas cuando se hace clic en un enlace
    const sidebarLinks = document.querySelectorAll('.sidebar .nav-link');
    const offcanvas = bootstrap.Offcanvas.getInstance(document.getElementById('sidebar'));

    sidebarLinks.forEach(link => {
        link.addEventListener('click', function () {
            if (window.innerWidth < 992) {
                offcanvas.hide();
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Cerrar offcanvas en móviles al hacer clic en un enlace
    const sidebarLinks = document.querySelectorAll('.sidebar .nav-link');
    const offcanvas = bootstrap.Offcanvas.getInstance(document.getElementById('sidebar'));

    sidebarLinks.forEach(link => {
        link.addEventListener('click', function () {
            if (window.innerWidth < 992) {
                offcanvas.hide();
            }
        });
    });

    // Ajustar altura del sidebar
    function adjustSidebarHeight() {
        const navbarHeight = document.querySelector('.navbar').offsetHeight;
        const heroHeight = document.querySelector('.hero').offsetHeight;
        const sidebar = document.querySelector('.sticky-sidebar');

        if (sidebar) {
            if (window.innerWidth >= 992) {
                sidebar.style.height = `calc(100vh - ${navbarHeight + heroHeight}px)`;
                sidebar.style.top = `${navbarHeight + heroHeight}px`;
            } else {
                sidebar.style.height = '100vh';
                sidebar.style.top = '0';
            }
        }
    }

    // Ejecutar al cargar y al redimensionar
    adjustSidebarHeight();
    window.addEventListener('resize', adjustSidebarHeight);
});
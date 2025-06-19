document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
    const toggleSidebar = document.getElementById('toggleSidebar');
    const mobileToggle = document.getElementById('mobileToggle');
    const userImage = document.getElementById('userImage');

    // Control de submenús - Versión corregida
    const menuItemsWithSubmenu = document.querySelectorAll('.sidebar-menu li.has-submenu');

    menuItemsWithSubmenu.forEach(item => {
        const link = item.querySelector('a:first-child');
        const submenu = item.querySelector('.sidebar-submenu');

        link.addEventListener('click', function (e) {
            // Solo aplicar si no estamos en modo compacto
            if (!sidebar.classList.contains('compact')) {
                e.preventDefault();

                // Cerrar otros submenús primero
                document.querySelectorAll('.sidebar-menu li.has-submenu').forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove('active');
                        otherItem.querySelector('.sidebar-submenu').style.maxHeight = '0';
                    }
                });

                // Alternar el submenú actual
                if (item.classList.contains('active')) {
                    item.classList.remove('active');
                    submenu.style.maxHeight = '0';
                } else {
                    item.classList.add('active');
                    submenu.style.maxHeight = submenu.scrollHeight + 'px';
                }
            }
        });
    });

    // Cargar estado del sidebar desde localStorage
    const savedState = localStorage.getItem('sidebarState');
    if (savedState === 'compact') {
        sidebar.classList.add('compact');
        mainContent.classList.add('compact');
        toggleSidebar.innerHTML = '<i class="fas fa-chevron-right"></i>';
    }

    // Función para alternar entre modo compacto y completo
    function toggleCompactMode() {
        sidebar.classList.toggle('compact');
        mainContent.classList.toggle('compact');

        if (sidebar.classList.contains('compact')) {
            toggleSidebar.innerHTML = '<i class="fas fa-chevron-right"></i>';
            localStorage.setItem('sidebarState', 'compact');
            // Cerrar todos los submenús al cambiar a compacto
            document.querySelectorAll('.sidebar-menu li.has-submenu').forEach(item => {
                item.classList.remove('active');
                item.querySelector('.sidebar-submenu').style.maxHeight = '0';
            });
        } else {
            toggleSidebar.innerHTML = '<i class="fas fa-chevron-left"></i>';
            localStorage.setItem('sidebarState', 'expanded');
        }
    }

    // Función para alternar el sidebar en móviles
    function toggleMobileSidebar() {
        sidebar.classList.toggle('active');
    }

    // Event listeners
    toggleSidebar.addEventListener('click', toggleCompactMode);
    mobileToggle.addEventListener('click', toggleMobileSidebar);
    userImage.addEventListener('click', function () {
        if (sidebar.classList.contains('compact')) {
            toggleCompactMode();
        }
    });

    // Ajustar al cambiar tamaño de ventana
    window.addEventListener('resize', function () {
        if (window.innerWidth >= 992) {
            sidebar.classList.remove('active');
        }
    });
});



document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.querySelector('.sidebar');
    const toggleBtn = document.getElementById('toggleSidebar');

    // Verificar estado guardado al cargar la página
    const isCompact = localStorage.getItem('sidebarCompact') === 'true';
    if (isCompact) {
        sidebar.classList.add('compact');
        document.querySelector('.main-content').classList.add('compact');
    }

    // Manejar el evento click
    toggleBtn.addEventListener('click', function () {
        sidebar.classList.toggle('compact');
        document.querySelector('.main-content').classList.toggle('compact');

        // Guardar estado en localStorage
        localStorage.setItem('sidebarCompact', sidebar.classList.contains('compact'));
    });
});
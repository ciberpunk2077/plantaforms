document.addEventListener('DOMContentLoaded', function () {
    // Verificar primero si los elementos existen
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
    const toggleSidebar = document.getElementById('toggleSidebar');
    const mobileToggle = document.getElementById('mobileToggle');
    const userImage = document.getElementById('userImage');

    // Si no hay sidebar en esta página, salir
    if (!sidebar || !mainContent) return;

    // Control de submenús (solo si existen)
    const menuItemsWithSubmenu = document.querySelectorAll('.sidebar-menu li.has-submenu');

    if (menuItemsWithSubmenu.length > 0) {
        menuItemsWithSubmenu.forEach(item => {
            const link = item.querySelector('a:first-child');
            const submenu = item.querySelector('.sidebar-submenu');

            if (link && submenu) {
                link.addEventListener('click', function (e) {
                    if (!sidebar.classList.contains('compact')) {
                        e.preventDefault();

                        // Cerrar otros submenús
                        document.querySelectorAll('.sidebar-menu li.has-submenu').forEach(otherItem => {
                            if (otherItem !== item && otherItem.querySelector('.sidebar-submenu')) {
                                otherItem.classList.remove('active');
                                otherItem.querySelector('.sidebar-submenu').style.maxHeight = '0';
                            }
                        });

                        // Alternar submenú actual
                        item.classList.toggle('active');
                        submenu.style.maxHeight = item.classList.contains('active') ? submenu.scrollHeight + 'px' : '0';
                    }
                });
            }
        });
    }

    // Función para alternar modo compacto
    function toggleCompactMode() {
        sidebar.classList.toggle('compact');
        mainContent.classList.toggle('compact');

        if (sidebar.classList.contains('compact')) {
            if (toggleSidebar) toggleSidebar.innerHTML = '<i class="fas fa-chevron-right"></i>';
            localStorage.setItem('sidebarState', 'compact');

            // Cerrar submenús al compactar
            document.querySelectorAll('.sidebar-menu li.has-submenu').forEach(item => {
                item.classList.remove('active');
                const sub = item.querySelector('.sidebar-submenu');
                if (sub) sub.style.maxHeight = '0';
            });
        } else {
            if (toggleSidebar) toggleSidebar.innerHTML = '<i class="fas fa-chevron-left"></i>';
            localStorage.setItem('sidebarState', 'expanded');
        }
    }

    // Cargar estado inicial
    const savedState = localStorage.getItem('sidebarState');
    if (savedState === 'compact' && !sidebar.classList.contains('compact')) {
        toggleCompactMode();
    }

    // Event listeners (con verificaciones)
    if (toggleSidebar) {
        toggleSidebar.addEventListener('click', toggleCompactMode);
    }

    if (mobileToggle) {
        mobileToggle.addEventListener('click', function () {
            sidebar.classList.toggle('active');
        });
    }

    if (userImage) {
        userImage.addEventListener('click', function () {
            if (sidebar.classList.contains('compact')) {
                toggleCompactMode();
            }
        });
    }

    // Responsive
    window.addEventListener('resize', function () {
        if (window.innerWidth >= 992) {
            sidebar.classList.remove('active');
        }
    });
});
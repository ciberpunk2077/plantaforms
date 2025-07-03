document.addEventListener('DOMContentLoaded', function () {
    // Guardar nueva Familia
    document.getElementById('saveFamiliaBtn').addEventListener('click', function () {
        const nombre = document.getElementById('nombre_familia').value.trim();
        const csrfToken = document.querySelector('#familiaForm [name=csrfmiddlewaretoken]').value;

        if (!nombre) {
            alert('Por favor ingrese un nombre para la familia');
            return;
        }

        const formData = new FormData();
        formData.append('nombre', nombre);
        formData.append('csrfmiddlewaretoken', csrfToken);

        fetch('/catalogo/ajax/add-familia/', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Agregar la nueva opción al select de familia y seleccionarla
                    const option = new Option(data.nombre, data.id, true, true);
                    document.getElementById('id_familia').appendChild(option);

                    // Agregar la nueva opción al select de familia en el modal de especie
                    const familiaEspecieSelect = document.getElementById('familia_especie');
                    if (familiaEspecieSelect) {
                        const option2 = new Option(data.nombre, data.id, true, true);
                        familiaEspecieSelect.appendChild(option2);
                        familiaEspecieSelect.value = data.id; // selecciona la nueva familia
                    }

                    // Cerrar el modal
                    const modal = bootstrap.Modal.getInstance(document.getElementById('addFamiliaModal'));
                    modal.hide();

                    // Limpiar el formulario
                    document.getElementById('nombre_familia').value = '';

                    alert('Familia agregada correctamente');
                } else {
                    alert(data.error || 'Error al guardar la familia');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al guardar la familia: ' + error.message);
            });
    });

    // Guardar nueva Especie
    document.getElementById('saveEspecieBtn').addEventListener('click', function () {
        const nombre = document.getElementById('nombre_especie').value.trim();
        const familiaId = document.getElementById('familia_especie').value;
        const csrfToken = document.querySelector('#especieForm [name=csrfmiddlewaretoken]').value;

        if (!nombre) {
            alert('Por favor ingrese un nombre para la especie');
            return;
        }
        if (!familiaId) {
            alert('Por favor seleccione una familia');
            return;
        }

        const formData = new FormData();
        formData.append('nombre', nombre);
        formData.append('familia_id', familiaId);
        formData.append('csrfmiddlewaretoken', csrfToken);

        fetch('/catalogo/ajax/add-especie/', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Agregar la nueva opción al select de especie y seleccionarla
                    const option = new Option(data.nombre, data.id, true, true);
                    document.getElementById('id_especie').appendChild(option);

                    // Cerrar el modal
                    const modal = bootstrap.Modal.getInstance(document.getElementById('addEspecieModal'));
                    modal.hide();

                    // Limpiar el formulario
                    document.getElementById('nombre_especie').value = '';

                    alert('Especie agregada correctamente');
                } else {
                    alert(data.error || 'Error al guardar la especie');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al guardar la especie: ' + error.message);
            });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const imageInput = document.getElementById('id_imagen');
    const imagePreview = document.getElementById('imagePreview');
    if (imageInput && imagePreview) {
        imageInput.addEventListener('change', function () {
            if (this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function (event) {
                    imagePreview.src = event.target.result;
                };
                reader.readAsDataURL(this.files[0]);
            }
        });
    }

    // Mapa dinámico para latitud y longitud
    const latInput = document.getElementById('latitud');
    const lngInput = document.getElementById('longitud');
    const mapDiv = document.getElementById('map');
    let map, marker;

    function drawMap() {
        const lat = parseFloat(latInput.value);
        const lng = parseFloat(lngInput.value);

        if (!isNaN(lat) && !isNaN(lng)) {
            if (!map) {
                map = L.map(mapDiv).setView([lat, lng], 15);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '© OpenStreetMap contributors'
                }).addTo(map);
                marker = L.marker([lat, lng]).addTo(map);
            } else {
                map.setView([lat, lng], 15);
                marker.setLatLng([lat, lng]);
            }
        }
    }

    if (latInput && lngInput && mapDiv) {
        latInput.addEventListener('input', drawMap);
        lngInput.addEventListener('input', drawMap);

        // Dibuja el mapa si ya hay valores al cargar la página
        if (latInput.value && lngInput.value) {
            drawMap();
        }
    }

});
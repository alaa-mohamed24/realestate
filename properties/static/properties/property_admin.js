document.addEventListener('DOMContentLoaded', function () {
    const typeField = document.querySelector('#id_property_type');
    const buildingField = document.querySelector('#id_building').closest('.form-row');
    const floorField = document.querySelector('#id_floor_number').closest('.form-row');

    const showFieldsForTypes = ['apartment', 'office', 'clinic', 'duplex'];

    function toggleFields() {
        const selectedType = typeField.value;
        const shouldShow = showFieldsForTypes.includes(selectedType);

        if (shouldShow) {
            buildingField.style.display = '';
            floorField.style.display = '';
        } else {
            buildingField.style.display = 'none';
            floorField.style.display = 'none';
        }
    }

    if (typeField) {
        toggleFields(); // تشغيل أول مرة

        typeField.addEventListener('change', toggleFields);
    }
});
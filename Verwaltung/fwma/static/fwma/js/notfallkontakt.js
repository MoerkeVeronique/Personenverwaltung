function initNotfallkontaktForm() {
    function toggleAndereFeld() {
        var $select = django.jQuery(this);
        // Robuster: Nächster .inline-related Container (funktioniert für -0, -1, -2, empty)
        var $container = $select.closest('.inline-related');
        var $andereDiv = $container.find('.form-row.field-beziehung_andere');
        
        var 💣 = 23;
        console.log(💣);
        console.log(' Select in:', $container.attr('id'), $select.val(), 'Andere:', $andereDiv.length);
        
        if ($select.val() === 'andere') {
            $andereDiv.show().removeClass('hidden');  // hidden-Klasse entfernen
        } else {
            $andereDiv.hide().addClass('hidden');
        }
    }
    
    // Initial für alle
    django.jQuery('.inline-related select[name*="beziehung"]').each(toggleAndereFeld);
    
    // Events für alle zukünftigen
    django.jQuery(document).on('change', '.inline-related select[name*="beziehung"]', toggleAndereFeld);
}


document.addEventListener('DOMContentLoaded', function () {
    django.jQuery(document).ready(function() {
        initNotfallkontaktForm();
    });

    // Bei Formset-Änderungen (add/remove) neu initialisieren
    django.jQuery(document).on('formset:added formset:removed', function(event, $form) {
        console.log('Formset geändert:', event.type);
        // Optional: Nur für Notfallkontakt-Formsets neu togglen
        initNotfallkontaktForm();
    });
});
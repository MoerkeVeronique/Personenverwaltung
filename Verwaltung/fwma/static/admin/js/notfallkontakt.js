django.jQuery(document).ready(function() {
    django.jQuery('select[name*="beziehung"]').change(function() {
        var textfeld = django.jQuery(this).closest('tr').find('input[name*="beziehung_andere"]');
        if (django.jQuery(this).val() == 'andere') {
            textfeld.show();
        } else {
            textfeld.hide();
        }
    });
});
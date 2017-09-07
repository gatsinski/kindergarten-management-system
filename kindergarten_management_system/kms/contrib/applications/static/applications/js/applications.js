function formsetManager(selector, type, action) {
    var total = $('#id_' + type + '-TOTAL_FORMS').val();

    if (action == 'add') {
        var newElement = $(selector).clone(true);
        newElement.find(':input').each(function() {
            var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        });
        newElement.find('label').each(function() {
            var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
            $(this).attr('for', newFor);
        });
        total++;
        
        $(selector).after(newElement);
    } else if (action == 'remove') {
        if (total > 1) {
            $(selector).remove();
            total--;
        }
    }
    $('#id_' + type + '-TOTAL_FORMS').val(total);
}

$(function() {
    $('#add_another').on('click', function(e) {
            formsetManager('.subform:last', 'attachment_set', 'add');
    });
    $('#remove_last').on('click', function(e) {
            formsetManager('.subform:last', 'attachment_set', 'remove');
    });

    $('#kmsWizard').bootstrapWizard({
        onTabShow: function (tab, navigation, index) {
            var $total = navigation.find('li').length,
                $current = index + 1,
                $percent = ($current / $total) * 100;
            $('#kmsWizard .progress-bar').css({
                width: $percent + '%'
            });
        }
    });
});
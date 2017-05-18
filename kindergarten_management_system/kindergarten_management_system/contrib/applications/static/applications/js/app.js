$(document).ready(function () {
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

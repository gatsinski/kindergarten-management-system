$(document).ready(function () {
    $('#kmsWizard').bootstrapWizard({
        //        onNext: function (tab, navigation, index) {
        //            //TODO: Validate each tab data
        //        },
        onTabShow: function (tab, navigation, index) {
            var $total = navigation.find('li').length,
                $current = index + 1,
                $percent = ($current / $total) * 100;
            $('#kmsWizard .progress-bar').css({
                width: $percent + '%'
            });
        }
    });

    var $sections = $('.form-section');

    function navigateTo(index) {
        // Mark the current section with the class 'current'
        $sections
            .removeClass('current')
            .eq(index)
            .addClass('current');
        // Show only the navigation buttons that make sense for the current section:
        $('.form-navigation .previous').toggle(index > 0);
        var atTheEnd = index >= $sections.length - 1;
        $('.form-navigation .next').toggle(!atTheEnd);
        $('.form-navigation [type=submit]').toggle(atTheEnd);
    }

    function curIndex() {
        // Return the current index by looking at which section has the class 'current'
        return $sections.index($sections.filter('.current'));
    }

    // Previous button is easy, just go back
    $('.form-navigation .previous').click(function () {
        navigateTo(curIndex() - 1);
    });

    // Next button goes forward iff current block validates
    $('.form-navigation .next').click(function () {
        var tabId = $(this).closest('.tab-pane').attr('id');
        if (validateSingleTab(tabId)) {
            navigateTo(curIndex() + 1);
            if (tabId == 'info-child') {
                $('#submitAppBtn').removeClass('display-none');
                $('#nextBtn').addClass('display-none');
                $('#nextLastBtn').addClass('display-none');
            } else {
                $('#submitAppBtn').addClass('display-none');
                $('#nextBtn').removeClass('display-none');
                $('#nextLastBtn').removeClass('display-none');
            }
        }
    });

    // Prepare sections by setting the `data-parsley-group` attribute to 'block-0', 'block-1', etc.
    $sections.each(function (index, section) {
        $(section).find(':input').attr('data-parsley-group', 'block-' + index);
    });

    initWizardValidation();
    navigateTo(0); // Start at the beginning

    function validateSingleTab(tabID) {
        var pass = true;
        var $curTab = $('#' + tabID);
        $curTab.find('input, select, textarea').each(function () {
            var $this = $(this);
            //Skip the hidden campaign flows
            if (!$this.closest('.tab-pane').hasClass('active') || !this.hasAttribute('required')) {
                return true;
            }

            if ($this.val().trim() == "" && $this.hasClass('form-error-border')) {
                pass = false;
            }
        });

        if (!pass) {
            $('#createAppTabs').find('a[href="#' + tabID + '"]').addClass('form-error-txt');
        } else {
            $('#createAppTabs').find('a[href="#' + tabID + '"]').removeClass('form-error-txt');
        }
        return pass;
    }


    function initWizardValidation() { // do this on document ready
        $('#appForm').find('input, textarea').off('input').on('input', function () {
            var $this = $(this);
            if ($this.val().trim() == "") {
                $this.addClass('form-error-border');
                $this.closest('.element-wrapper').find('label').addClass('form-error-txt');
            } else {
                $this.removeClass('form-error-border');
                $this.closest('.element-wrapper').find('label').removeClass('form-error-txt');
            }

            validateSingleTab($(this).closest('.tab-pane').attr('id'));
        }).find('select').off('change').on('change', function () {
            var $this = $(this);
            var pass = true;
            if ($this.attr('id') == 'id_application_kindergarten') {
                if ($this.val() != "1" && $this.val() != "2") {
                    pass = false;
                } else {
                    pass = true;
                }
            }

            if (pass) {
                $this.removeClass('form-error-border');
                $this.closest('.element-wrapper').find('label').removeClass('form-error-txt');
            } else {
                $this.addClass('form-error-border');
                $this.closest('.element-wrapper').find('label').addClass('form-error-txt');
            }

            validateSingleTab($this.closest('.tab-pane').attr('id'));
        });
    }

    function validateWizard() {
        //Remove all errors
        $('.form-error-txt').removeClass('form-error-txt');
        $('.form-error-border').removeClass('form-error-border');

        var validated = true;
        var $appForm = $('#appForm');
        $appForm.find('input, select, textarea').each(function () {
            var $this = $(this);
            //Skip the hidden flows
            if (!$this.closest('.tab-pane').hasClass('active') || !this.hasAttribute('required')) {
                return true;
            }

            var tabId = $this.closest('.tab-pane').attr('id');

            if (this.tagName.toLowerCase() == 'select') {
                if ($this.attr('id') == 'id_application_kindergarten') {
                    if ($this.val() != "1" && $this.val() != "2") {
                        validated = false;
                        $this.addClass('form-error-border');
                        $this.closest('.element-wrapper').find('label').addClass('form-error-txt');
                        $('#createAppTabs').find('a[href="#' + tabId + '"]').addClass('form-error-txt');
                    }
                }
            } else if ($this.val().trim() == "") {
                validated = false;
                $this.addClass('form-error-border');
                $this.closest('.element-wrapper').find('label[for="' + $this.attr('id') + '"]').addClass('form-error-txt');
                $('#createAppTabs').find('a[href="#' + tabId + '"]').addClass('form-error-txt');
            }
        });
    }

    function processFormData($form) {
        if (!validateWizard()) return;

        // submit form
        var data = {};

        // Get all of the inputs from all tabs except the buttons
        var formInputs = $form.find(':input, select').not(':button');
        formInputs.each(function () {
            // TODO: prepare data for POST
        });

        $(this).addClass('disabled-btn');

        return data;
    }

    $('#submitAppBtn').off('click').on('click', function (e) {
        $form = $('#appForm');
        e.preventDefault();
        // Get processed form data
        var data = processFormData($form);
        $.ajax({
            url: '',// put required url here
            type: 'POST',
            data: JSON.stringify(data),
            success: function () {
                // put desired action for success
            },
            error: function () {
                // put desired action for success

            }
        });

        return false;
    });

});

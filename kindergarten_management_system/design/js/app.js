$(document).ready(function() {
  	$('#kmsWizard').bootstrapWizard({onNext: function(tab, navigation, index) {
      //TODO: Validate each tab data
		}, onTabShow: function(tab, navigation, index) {
			var $total = navigation.find('li').length;
			var $current = index+1;
			var $percent = ($current/$total) * 100;
			$('#kmsWizard .progress-bar').css({width:$percent+'%'});
		}});
});
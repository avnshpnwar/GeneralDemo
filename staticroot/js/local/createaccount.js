$(document).ready(function() {
	$("#createaccount").validate({
		rules : {
			account_name : {
				required : true,
			},
		},
		messages : {
			account_name : {
				required: 'Please select account type'
			}
		},
		tooltip_options: {
	        account_name : { placement: 'right' }
	    },
		// Make sure the form is submitted to the destination defined
		// in the "action" attribute of the form when valid
		submitHandler : function(form) {
			form.submit();
		}
	});
});// $( document ).ready(function()

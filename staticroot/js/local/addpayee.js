$(document).ready(function() {
	$("#addpayee").validate({
		rules : {
			name : {
				required : true,
				minlength : 4,
				maxlength : 20
			},
			account_no : {
				required: true,
				range: [100000, 9999999]
			},
		},
		messages : {
			name : {
				required: 'Please enter Payee Name',
				minlength: 'Minimum 4 character',
				maxlength: 'Maximum 20 character'
			},
			account_no : {
				required: 'Please enter 7 digit account no.',
				range : 'Account must be between 1000000 and 9999999'
			}
		},
		tooltip_options: {
	        name : { placement: 'top' },
	        account_no : {placement: 'top'}
	    },
		// Make sure the form is submitted to the destination defined
		// in the "action" attribute of the form when valid
		submitHandler : function(form) {
			form.submit();
		}
	});
});// $( document ).ready(function()

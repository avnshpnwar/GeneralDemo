$(document).ready(function() {
	console.log("register ready!");
	
	jQuery.validator.addMethod(
		"uidreg", 
		function(value, element) {
			return  /^[a-z]+$/.test(value);
		}, 
		"alphabetic without spaces"
	);
	
	$("#register-form").validate({
		rules : {
			uid : {
				uidreg : true
			},
			pwdb : {
				equalTo: "#register-form [name=pwda]"
			},
		},
		messages : {
			pwdb : {
				equalTo: 'Password do not match'
			}
		},
		tooltip_options: {
	        uid : { placement: 'top' },
	        pwda : {placement: 'left'},
	        pwdb :{ placement : 'bottom'} 
	    },
		// Make sure the form is submitted to the destination defined
		// in the "action" attribute of the form when valid
		submitHandler : function(form) {
			form.submit();
		}
	});

});// $( document ).ready(function()

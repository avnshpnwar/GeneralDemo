$(document).ready(function(){
	$("#email").validate({
		rules : {
			subject : {
				required : true
			},
			body : {
				required: true
			},
		},
		messages : {
//			body : {
//				required: 'Password do not match'
//			}
		},
		tooltip_options: {
//	        uid : { placement: 'top' },
//	        pwda : {placement: 'left'},
//	        pwdb :{ placement : 'bottom'} 
	    },
		// Make sure the form is submitted to the destination defined
		// in the "action" attribute of the form when valid
		submitHandler : function(form) {
			form.submit();
		}
	});
});
$(document).ready(function() {
	$("#otpform").validate({
		rules : {
			numotp : {
				equalTo: "#id_numotph"
			},
			strotp : {
				equalTo: "#id_strotph"
			},
			alnotp : {
				equalTo: "#id_alnotph"
			}
		},
		messages : {
			numotp : {
				equalTo: "OTP don't match"
			},
			strotp : {
				equalTo: "OTP don't match"
			},
			alnotp : {
				equalTo: "OTP don't match"
			}
		},
		// Make sure the form is submitted to the destination defined in the "action" attribute of the form when valid
		submitHandler : function(form) {
			form.submit();
		}
	});
});

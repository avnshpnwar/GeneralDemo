$(document).ready(function() {
	$("#id_transfer_date").prop('disabled', true);//make sure you enable it before submitting form
	
	//set datetpicker to use moment format
	$.datetimepicker.setDateFormatter({
	    parseDate: function (date, format) {
	        var d = moment(date, format);
	        return d.isValid() ? d.toDate() : false;
	    },
	    
	    formatDate: function (date, format) {
	        return moment(date).format(format);
	    }
	});
	
	//set format of datetimepicker
	jQuery('#id_transfer_date').datetimepicker({
		format:'YYYY-MM-DD HH:mm',
		formatTime:'HH:mm',
		formatDate:'YYYY-MM-DD',
		minDate:0,
		minTime:0
	});
	
	//make datetimepicker visible on clicking calendar button
	jQuery('#datetime').click(function(){
		console.log("i am clicked");
		jQuery('#id_transfer_date').datetimepicker('show'); //support hide,show and destroy command
	});
	
	
	$("#transfer").validate({
		rules : {
			from_account : {
				required : true
			},
			sender_text : {
				required: true,
				minlength: 5,
				maxlength: 30
			},
			transfer_date : {
				required: true
			},
			to_account : {
				required : true
			},
			receiver_text : {
				required : true,
				minlength : 5,
				maxlength : 30
			},
			agree : {
				required : true
			}
		},
		messages : {
			sender_text : {
				required: 'Please enter reason for transfer',
				minlength: 'Minimum 5 character',
				maxlength: 'Maximum 30 character'
			},
			receiver_text : {
				required: 'Please enter message for payee',
				minlength: 'Minimum 5 character',
				maxlength: 'Maximum 30 character'
			}, agree : {
				required: 'Please accept terms to proceed'
			}
		},
		tooltip_options: {
	        //name : { placement: 'top' },
	        agree : {placement: 'right'}
	    },
		// Make sure the form is submitted to the destination defined
		// in the "action" attribute of the form when valid
		submitHandler : function(form) {
			$("#id_transfer_date").prop('disabled', false);
			form.submit();
		}
	});
	
});// $( document ).ready(function()

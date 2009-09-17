$(document).ready(function() {
	var validator = $("#new-comment-form").validate({
		errorClass: 'invalid',
		rules: {
			name: {
				required: true,
				minlength: 2,
				maxlength: 40
			},
			body: {
				required: true,
				minlength: 4,
				maxlength: 15000
			}
		},
		messages: {
			name: {
				required: "Please enter your name.",
				minlength: jQuery.format("It has to be at least {0} letters."),
				maxlength: jQuery.format("It can't be more than {0} letters."),
			},
			body: {
				required: "Please enter a comment.",
				minlength: jQuery.format("It has to be at least {0} letters."),
				maxlength: jQuery.format("It can't be more than {0} letters."),
			},
		},
		errorPlacement: function(error, element) {
			error.appendTo( element.parent() );
		},
	});
});
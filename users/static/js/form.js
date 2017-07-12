$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			type : 'GET',
			url : '/process'
		})
		.done(function(data) {
            console.log(data);
			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});


	});

});
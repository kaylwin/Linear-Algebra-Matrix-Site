function drawMatrix() {

	//Get the value of the row input and column inputs
	var m = $('#row_input').val().trim();
	var n = $('#col_input').val().trim();

	//hide the form entry element
	if ($.isNumeric(m) && $.isNumeric(n)) {
		$('#matrix_dimension_entry').hide();

		// var $form = $("<form>").append('<input type="button" value="Hello" />')
		//can edit the css on this to put it in the middle of the page
		var $body = $('body');

		var $table = $('body').append("<table>");
		$table.css({
			'text-align' : 'center'
		});

		for (var row = 0; row < m; row++) {

			//note that the create element is capitalized
			var $tr = $table.append("<tr>");

			for (var col = 0; col < n; col++) {
				$("<textarea>", {
					WRAP : "off",
					class : "matrixEntryBox"
				}).appendTo($tr);

			}

		}

		//use the insert after to mess with this button

		var $button = $('<button>', {
			STYLE : "width: 30vw; height: 2.2em; text-align: center; font-size:1.5em"

		});

		$body.append("<br>");
		$body.append($button);
		$button.append("Enter Matrix");

		$button.on("click", function(event) {
			getMatrix(m, n);
		});

	} else {
		alert('Please enter real numbers');
	}

}

function getMatrix(m, n) {
	var next_page = new Boolean(true);
	var data = [];
	var length = 0;
	$('textarea').each(function(i, val) {
		value = $(val).val();
		if (value && $.isNumeric(value)) {
			if (value.toString().length > length) {
				length = value.toString().length;
			}
			data.push(value);

		} else {
			next_page = false;
			alert('Please check Box ' + (i + 1) + " for errors including a non-numeric value or an empty box");
			return false;
		}

	});

	if (next_page != false) {
		console.log(data);
		var matrixNo;
		//have to conver the matrix into a string
		var matricies = $.cookie("matricies");
		if (matricies == undefined) {
			//One seems like a better place to start
			matrixNo = 0;

		} else {
			matrixNo = parseInt(matricies);
		}
		
		data = JSON.stringify(data);
	    
		
		
		matrixNo += 1;
		//One cookie will keep track of how many matrices there are
		//the other will keep track of the matrix itself
		$.cookie("matricies", matrixNo);
		$.cookie("matrix:" + matrixNo, data);
		$.cookie("matrix_details:" + matrixNo, m + ':' + n);
		
		location = "/Matrix";
	}

}


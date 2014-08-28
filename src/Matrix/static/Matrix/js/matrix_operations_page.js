!(function() {

	//Get all the matricies and populate left div
	var no_matricies = $.cookie('matricies');
	no_matricies = parseInt(no_matricies);
	var $viewer = $("#MatrixViewer");
	for (var i = 1; i < no_matricies + 1; i++) {

		//Retreive dta from cookie
		var matrix_string = $.cookie("matrix:" + i);
		if (matrix_string != undefined) {

			var matrix_list = (JSON.parse(matrix_string));

			var matrix_details = $.cookie('matrix_details:' + i);
			var m = parseInt(matrix_details.split(':')[0]);
			var n = parseInt(matrix_details.split(':')[1]);

			//if 3x3 matrix then slice 3 long
			// 0 - 2,
			console.log(matrix_list + "matrix list");
			var counter = 0;
			var matrix = new Array();
			var minilist = new Array();
			while (counter < m * n) {
				for (var j = counter; j < counter + (n ); j++) {
					minilist.push(parseFloat(matrix_list[j]));
				}
				matrix.push(minilist);
				minilist = [];
				counter = counter + n;
			}

			matrix = new Matrix(m, n, matrix);

			//TODO style this div
			var $div = $('<div>', {
				class : "Matrix",
			});
			$div.data("matrix", matrix);
			//make it so they do the cool flashy thing

			$div.hover(function() {
				$(this).fadeOut(100);
				$(this).fadeIn(500);
			}, function() {
				//Make sure it doesn't do anything on leave
			});

			$div.click(function() {
				//var $clone = $(this).clone();

				var actual_matrix = $(this).data("matrix");
				$selection_div = $('#matrix_selection');
				$selection_div.empty();
				$table = $(this).find('table').clone();
				$table.attr("align", "center");
				$table.data("matrix", actual_matrix);
				$table.attr("id", "matrixchoice");
				$selection_div.append($table);
			});

			$viewer.append($div);
			var actual_matrix = matrix.matrix;

			var $table = $('<table>', {
				class : "matrix",
				align : "center"
			}).appendTo($div);

			for (var row = 0; row < actual_matrix.length; row++) {
				var $tr = $('<tr>');

				for (var col = 0; col < actual_matrix[0].length; col++) {
					var $td = $('<td>' + actual_matrix[row][col] + '</td>').appendTo($tr);

					//$td.append($element);
					//Create new div with new elements
					//have the div data be a matrix

				}
				$table.append($tr);
			}
		}
	}
})();

function addMatrix() {
	location = "/Matrix/Add";
}

function Orthagonalize() {
	//var csrftoken = $.cookie('csrftoken');

	var $matrixDiv = $('#matrixchoice');
	var matrix = $matrixDiv.data("matrix").matrix;
	console.log(matrix);
	$.ajax({
		type : "GET",
		url : "/Matrix/Orthagonalize/",
		data : {
			matrix_string : JSON.stringify(matrix)
		},
		success : function(data) {
			var actual_matrix = JSON.parse(data);
			//actual_matrix.m = actual_matrix.length;
			//acutal_matrix.n = actual_matrix[0].leng
			//matrix_answer
			var $ans_div = $('#matrix_answer');
			$ans_div.empty();

			var $mtx_div = $('<div>', {
				align : "center"
			}).appendTo($ans_div);

			$mtx_div.data("matrix", actual_matrix);

			var $table = $('<table>', {
				class : "matrix"
			}).appendTo($mtx_div);

			for (var row = 0; row < actual_matrix.length; row++) {
				var $tr = $('<tr>');

				for (var col = 0; col < actual_matrix[0].length; col++) {
					var $td = $('<td>' + Math.round(actual_matrix[row][col]*1000)/1000 + '</td>').appendTo($tr);

					//$td.append($element);
					//Create new div with new elements
					//have the div data be a matrix

				}
				$table.append($tr);
			}

		}
	});
}

//Works up to this point
function getEigens() {
	var $matrixDiv = $('#matrixchoice');
	var matrix = $matrixDiv.data("matrix").matrix;
	$.ajax({
		type : "GET",
		url : "/Matrix/getEigens/",
		data : {
			matrix_string : JSON.stringify(matrix)
		},
		success : function(data) {
			var actual_matrix = JSON.parse(data);
			//actual_matrix.m = actual_matrix.length;
			//acutal_matrix.n = actual_matrix[0].leng
			//matrix_answer
			var $ans_div = $('#matrix_answer');
			$ans_div.empty();

			$ans_div.data("matrix", actual_matrix);
			$element = $("<b>", {
				style : "font-size: 2em; margin: 20px",
			});
			for (var i = 0; i < actual_matrix.length; i++) {
				$element.append(actual_matrix[i] + ", ");
			}
			$ans_div.append($element);

		}
	});
}

function RREF() {
	var $matrixDiv = $('#matrixchoice');
	var matrix = $matrixDiv.data("matrix").matrix;
	console.log(matrix);
	$.ajax({
		type : "GET",
		url : "/Matrix/RREF/",
		data : {
			matrix_string : JSON.stringify(matrix)
		},
		success : function(data) {
			var actual_matrix = JSON.parse(data);
			//actual_matrix.m = actual_matrix.length;
			//acutal_matrix.n = actual_matrix[0].leng
			//matrix_answer
			var $ans_div = $('#matrix_answer');
			$ans_div.empty();

			var $mtx_div = $('<div>', {
				align : "center"
			}).appendTo($ans_div);

			$mtx_div.data("matrix", actual_matrix);

			var $table = $('<table>', {
				class : "matrix"
			}).appendTo($mtx_div);

			for (var row = 0; row < actual_matrix.length; row++) {
				var $tr = $('<tr>');

				for (var col = 0; col < actual_matrix[0].length; col++) {
					var $td = $('<td>' + actual_matrix[row][col] + '</td>').appendTo($tr);

					//$td.append($element);
					//Create new div with new elements
					//have the div data be a matrix

				}
				$table.append($tr);
			}

		}
	});
}

function Invert() {
	var $matrixDiv = $('#matrixchoice');
	var matrix = $matrixDiv.data("matrix").matrix;
	console.log(matrix);
	$.ajax({
		type : "GET",
		url : "/Matrix/Invert/",
		data : {
			matrix_string : JSON.stringify(matrix)
		},
		success : function(data) {
			var actual_matrix = JSON.parse(data);

			//actual_matrix.m = actual_matrix.length;
			//acutal_matrix.n = actual_matrix[0].leng
			//matrix_answer
			var $ans_div = $('#matrix_answer');
			$ans_div.empty();

			var $mtx_div = $('<div>', {
				align : "center"
			}).appendTo($ans_div);

			$mtx_div.data("matrix", actual_matrix);

			var $table = $('<table>', {
				class : "matrix"
			}).appendTo($mtx_div);

			for (var row = 0; row < actual_matrix.length; row++) {
				var $tr = $('<tr>');

				for (var col = 0; col < actual_matrix[0].length; col++) {
					var $td = $('<td>' + actual_matrix[row][col] + '</td>').appendTo($tr);

					//$td.append($element);
					//Create new div with new elements
					//have the div data be a matrix

				}
				$table.append($tr);
			}

		}
	});
}


function Matrix(m, n, matrix) {
	this.m = m;
	this.n = n;
	var ZERO = 0;
	this.matrix = matrix;

	//if the matrix entered length is zero then initialize the list
	if (this.matrix.length == 0) {
		for (var i = 0; i < this.m; i++) {
			var minilist = [];
			for (var j = 0; j < this.n; j++) {
				minilist.push(0);
			}
			this.matrix.push(minilist);

		}
	}
}

//Have the rest of the operations be written below

function vector_multiply(operant, vector) {
	var a = operant;
	var b = vector;
	if ( typeof a == 'object') {

		var sum_vec_mult = 0;

		//Execute vector * vector multiplication
		for (var i = 0; i < b.length; i++) {
			sum_vec_mult +=  Math.round((a[i] * b[i]) * 10000) / 10000;

		}
		return sum_vec_mult;

	} else if ( typeof (a) == "number") {
		//Perform scalar multiplication
		for (var i = 0; i < b.length; i++) {
			//b[i] = b[i] * a;
			b[i] = Math.round((b[i] * a) * 10000) / 10000;
		}
		return b;
	}
}

function add_vectors(vector1, vector2) {
	var a = vector1;
	var b = vector2;
	if (a.length != b.length) {
		console.log("ERROR ON ADD VECTORS!!!");
	}
	var c = [];
	for (var i = 0; i < a.length; i++) {
		c.push(a[i] + b[i]);

	}
	// Return the sum of the characters
	return c;
}

function magnitude_half(vector1) {
	var a = vector1;
	var sum_vector1 = 0;
	for (var i = 0; i < a.length; i++) {
		sum_vector1 += a[i] * a[i];
	}
	return Math.round(sum_vector1 * 10000) / 10000;
}

function magnitude(vector1) {
	var a = vector1;
	var sum = 0;
	for (var i = 0; i < a.length; i++) {
		sum +=   Math.round(a[i] * a[i] * 10000) / 10000;
	}
	return Math.sqrt(sum);
}

function projection(u, v) {

	// assuming both u & v are vectros

	var scalar = vector_multiply(u,v) / magnitude_half(v);
	scalar = Math.round(scalar * 10000) / 10000;
	return vector_multiply(scalar, v);
	

}

function gram_schmidt(matrix2breduced) {
	
	console.log("gram_schmidt matrix: " + matrix2breduced);
	var output_matrix = [];
	//add in the first row as the start of the algorithm
	//var m_zero = m[0];
	
	output_matrix.push(matrix2breduced[0]);
	
	for (var position = 1; position < matrix2breduced.length; position++) {
		var sum = [];
		
		for (var i = 0; i < position; i++) {

			//TODO this stuff is causing problems
			if (sum.length != 0) {
				vproj = projection(matrix2breduced[position], matrix2breduced[i]);
				sum = add_vectors(sum, vproj);
			} else {
				sum = projection(matrix2breduced[position], matrix2breduced[i]);
			}


		}
		console.log("Sum b4 vm " + sum);
		
		sum = vector_multiply(-1, sum);

		console.log("Sum aft vm " + sum);
		
		console.log(" added vector: " + add_vectors(sum, matrix2breduced[position]));
		var fvector = add_vectors(sum, matrix2breduced[position]);
		//output.push(fvector);
		// sum is a vector
	}
	console.log(output_matrix);
	return output_matrix;
}

function QR_F_to_Q(F) {
	Q = [];
	for (var i = 0; i < F.length; i++) {
		var scalar = 1 / magnitude(F);
		Q.push(vector_multiply(scalar, F));
	}
	return Q;
}

function transpose(matrix) {
	//This function assumes matrix is a list of lists, not an object
	C = [];
	for (var i = 0; i < matrix.length; i++) {
		C.push(new Array(matrix[0].length));
	}
	for (var i = 0; i < matrix.length; i++) {
		for (var j = 0; j < matrix[0].length; j++) {
			C[i][j] = matrix[j][i];
		}
	}
	return C;
}

function getColumn(matrix, column) {
	var m = matrix;
	var col = column;
	column = [];
	for (var i = 0; i < m.length; i++) {
		for (var j = 0; j < m[0].length; j++) {
			if (j == col) {
				column.push(m[i][j]);
			}
		}
	}
	return column;
}

function matrix_multiply(matrix1, matrix2) {
	var a = matrix1;
	var b = matrix2;

	var c = new Array();
	for (var i = 0; i < a.length; i++) {
		c.push(new Array(b[0].length));
	}

	for (var i = 0; i < a.length; i++) {
		for (var j = 0; j < b[0].length; j++) {
			var va = a[i];
			var vb = getColumn(j);
			var product = [];
			for (var x = 0; x < va.length; x++) {
				product.push(vector_multiply(va, vb));
				dot = 0;
				for (var item = 0; item < product.length; item++) {
					dot += product[item];
					c[i][j] = dot;
				}
			}
		}
	}
	return c;

}

function factor_QR(matrix) {
	var A = transpose(matrix);
	// transpose in order to work with columns

	console.log("A: " + A);

	var F = gram_schmidt(A);
	console.log("F: " + F);
	var Q = QR_F_to_Q(F);
	console.log("Q: " + Q);
	var Flen = F.length;

	R = [];
	// This is the R matrix
	for (var i = 0; i < Flen; i++) {
		//make a matrix of the appropriate dimensions
		R.push(new Array(Flen));
	}

	for (var i = 0; i < Flen; i++) {
		for (var j = 0; j < Flen; j++) {

			if (i == j) {
				R[i][j] = magnitude(F[i]);

			} else if (i < j) {
				//Set the matrix spaces to their appropriate values
				R[i][j] = vector_multiply(C[j], Q[i]);
			}
		}

		//Return the matrix R * Q
		return matrix_multiply(R, Q);

	}
}

function QR_algorithm(matrix) {
	console.log(matrix);
	var a = this.matrix;
	for (var i = 0; i < 1; i++) {
		a = factor_QR(matrix);
	}

	console.log("Completed Matrix: ", a);

}


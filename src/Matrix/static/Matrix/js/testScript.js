function Matrix(m,n, matrix){
	this.m = m;
	this.n = n;
	var ZERO = 0;
	this.matrix = matrix;

  //if the matrix entered length is zero then initialize the list
	if (this.matrix.length == 0){
		for(var i = 0; i<this.m; i++){
			var minilist = [];
			for(var j =0; j<this.n; j++){
				minilist.push(0);
			}
			this.matrix.push(minilist);

		}
	}

  this.getRow = function(row){
    var C = this.matrix;
    for(var i = 0; i< C.length; i++){
      for (var j = 0; j< C[i].length; j++){

        document.write("hello\n\n\n");
      }

    }
  };

  //Find the eigen values
  this.getEigenValues = function(){
    m = this.m;
    n = this.n;
    C = this.matrix;
    for( var i = 0; i<m; i++){
      row = matrix.getRow(i);



    }



  };
}




var m1 = [[1,2],[3,4]];
var C = new Matrix(2,2,m1);
C.getRow();







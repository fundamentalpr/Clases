square([2,2]);
translate([10,0])circle(2,$fn=15);
translate([20,0])polygon(points=[[0,0],[10,0],[10,10]], paths=[[0,1,2]]);
translate([40,0])text("ArrancaPR");
translate([0,-20])text("ArrancaPR", font = "Liberation Sans:style=Bold Italic");
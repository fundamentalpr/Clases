/*
linear_extrude(height = 10, center = false, convexity = 10, twist = 0)
{
text("arranca pr");
}*/


/*linear_extrude(height = 10, center = false, convexity = 10, twist = 180)
{
text("arranca pr");
}*/

/*linear_extrude(height = 10, center = false, convexity = 10, twist = 180)
{
translate([0,2])circle(2);
}*/


/*linear_extrude(height = 10, center = false, convexity = 10, twist = 180,slices=900)
{
translate([0,2])circle(2);
}*/


rotate_extrude(convexity = 10,$fn=20)
{
translate([2, 0, 0])
text("C"); 
}


module pill(height=5)
{
hull()
{
sphere(height);
translate([0,0,15])sphere(height);
}
}
pill();

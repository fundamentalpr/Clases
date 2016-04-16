module estrella(cantidad=6)
{
tsdist = rands(1,10,cantidad);
for ( i = [0 : cantidad-1] )
{
    rotate( i * 360 / cantidad, [1, 0, 0])
    
    hull()
    {
    sphere(r=1);
    translate([0, tsdist[i], 0])
    sphere(r = 1);
    }
}
}
estrella();
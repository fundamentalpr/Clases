//Alfredo Alvarez
// Escena de piso mesa y silla o posibles sillas
use <libreriamuebles.scad>;
module pisoexpandido()
{
scale([5,5,1])color("Lavender",1)piso();
}
module conjuntodemesas(cantidad = 3)
{
    for(z=[0:cantidad])
    {
    translate([150,-200+120*z,0])scale([1,2,1])color("Red",1)mesa();
    }
}

module sillasparalasmesas(cantidad = 3)
{
    for(z=[0:cantidad])
    {
    translate([150,-200+120*z,0]) mirror([1,0,0])silla();
    }
}

module filadesillas(cantidad =7)
{
    for(z=[0:cantidad])
    {
        translate([50,-160+40*z,0])color("Blue",1)silla();
    }
}
module sillasaudiencia(cantidad = 2)
{
    for(z=[0:cantidad])
    {
        translate([-50*z,0,0])filadesillas();
    }
}


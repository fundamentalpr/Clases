//Alfredo Alvarez
// Escena de piso mesa y silla o posibles sillas
use <libreriamuebles.scad>;

color("Lavender",1)piso();
color("Red",1)mesa();
color("Blue",1)silla();
mirror([1,0,0])silla();

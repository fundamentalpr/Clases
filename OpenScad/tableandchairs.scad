module piso()
{
    cube([100,100,3],center=true);
}

module table()
{
    //first leg
    translate([-20,-20,1.5])cylinder(h = 30, r=1.5); // normal height of a table
    //second leg
    translate([-20,20,1.5])cylinder(h = 30, r=1.5); // normal height of a table
    //third leg
    translate([20,-20,1.5])cylinder(h = 30, r=1.5); // normal height of a table
    //fourth leg
    translate([20,20,1.5])cylinder(h = 30, r=1.5); // normal height of a table
    translate([0,0,31.5])cube([45,45,3],center=true);    
}

module chairBase()
{
    //first leg
    translate([-40,-7.5,1.5])cylinder(h = 18, r=1.5); // normal height of a table
    //second leg
    translate([-40,7.5,1.5])cylinder(h = 18, r=1.5); // normal height of a table
    //third leg
    translate([-25,-7.5,1.5])cylinder(h = 18, r=1.5); // normal height of a table
    //fourth leg
    translate([-25,7.5,1.5])cylinder(h = 18, r=1.5); // normal height of a table
    translate([-32.5,0,19.5])cube([18,18,3],center=true);     
}

module chairTop()
{
    difference(){
    //chair back
    translate([-41.5,0,32.5])cube([2.5,18,23],center=true);
    //Some design
    translate([-41.5,0,35])sphere(5);     
    };    
}

module chair()
{
    chairBase();
    chairTop();
}



piso();
table();
chair();
mirror([1,0,0])chair();
module loquesea(parametro)
{
    if(parametro % 2 == 0) //es par
    {
        sphere(parametro);
    }
    else
    {
        cube(2*parametro, center =true);                      
    }
}

loquesea(10);
translate([0,0,20])loquesea(11);
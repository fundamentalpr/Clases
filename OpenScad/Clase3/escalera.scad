module escalera(escalones=3)
{
    tamano = 4;
  
    for(i =[0:escalones])
    {       
       translate([0,0,i*-4])cube([4,4+4*i,4]);   
    }
}
escalera();

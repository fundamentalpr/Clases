cantidad = 100;
direction = rands(0,4,cantidad);

//vamos a dibujar un camino

translate([0,0,0])cube(1);

function calcx(vector, pos) = pos == -1?0:
    vector[pos] >3? calcx(vector,pos-1)+1:vector[pos] >2?calcx(vector,pos-1)-1:calcx(vector,pos-1);
 
 function calcy(vector, pos) = pos == -1?0:
    vector[pos] <2? calcy(vector,pos-1)+1:vector[pos] <1?calcy(vector,pos-1)-1:calcy(vector,pos-1);



for  (i = [0:cantidad-1])
{ 
        echo("i:");
        echo(i);
        echo("direccion");
        echo(direction[i]);
        echo("x:");
        echo(calcx(direction,i));
        echo("y:");
        echo(calcy(direction,i));
        echo("-----");
        translate([calcx(direction,i),calcy(direction,i),0])cube(1);    
}
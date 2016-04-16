function fibo(x) =
x == 1 ? 1:x == 0?1: fibo(x-1) + fibo(x-2);


echo(fibo(5));

for(z =([0:115]))
{
    translate([fibo(z)*2,y,0])sphere(fibo(z));
}
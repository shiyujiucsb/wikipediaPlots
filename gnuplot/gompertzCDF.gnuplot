set term svg size 800,600 enhanced font 'Arial, 24'
set output 'gompertzCDF.svg'

set samples 500
set xrange [0:5]
set yrange [0:1]
set xtics 1
set ytics 0.2
set xzeroaxis lt -1 lc rgb "black" lw 1
set yzeroaxis lt -1 lc rgb "black" lw 1

# Draw the Gompertz distribution's pdf
set key right bottom

f(x, eta, b) = 1-exp(-eta*(exp(b*x)-1))

plot f(x, 0.1, 1.0) t "eta=0.1, b=1" lc rgb "red" lw 5,\
   f(x, 1.0, 1.0) t "eta=2.0, b=1" lc rgb "black" lw 5,\
   f(x, 2.0, 1.0) t "eta=3.0, b=1" lc rgb "blue" lw 5,\
   f(x,1.0, 2) t "eta=1.0, b=2" lc rgb "green" lw 5,\
   f(x,1.0, 3) t "eta=1.0, b=3" lc rgb "grey" lw 5

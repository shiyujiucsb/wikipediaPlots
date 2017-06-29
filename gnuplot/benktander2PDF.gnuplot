set term svg size 800,600 enhanced font 'Arial, 24'
set output 'benktander2PDF.svg'

set samples 500
set xrange [1:5]
set yrange [0:3]
set xtics 1
set ytics 0.2
set xzeroaxis lt -1 lc rgb "black" lw 1
set yzeroaxis lt -1 lc rgb "black" lw 1

# Draw the Benktander type-II distribution's pdf
set key default

f(x, a, b) = exp(a/b*(1-x**b))*x**(b-2)*(a*x**b-b+1)

plot f(x, 1.0, 1.0) t "a=1, b=1" lc rgb "red" lw 5,\
   f(x, 2.0, 1.0) t "a=2, b=1" lc rgb "black" lw 5,\
   f(x, 3.0, 1.0) t "a=3, b=1" lc rgb "blue" lw 5,\
   f(x,1.0, 0.5) t "a=1, b=0.5" lc rgb "green" lw 5,\
   f(x,1.0, 0.2) t "a=1, b=0.2" lc rgb "grey" lw 5

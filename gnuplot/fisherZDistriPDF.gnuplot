set term svg size 800,600 enhanced font 'Arial, 24'
set output 'fisherZDistriPDF.svg'

set samples 500
set xrange [-5:5]
set yrange [0:1]
set xtics 1
set ytics 0.2
set xzeroaxis lt -1 lc rgb "black" lw 1
set yzeroaxis lt -1 lc rgb "black" lw 1

# Draw the Fisher z distribution's pdf
set key default

beta(x, y) = gamma(x) * gamma(y) / gamma(x+y)

f(x,d1,d2) = 2*d1**(0.5*d1) * d2**(0.5*d2) * exp(d1*x) \
	/ ((d1*exp(2*x) + d2)**(0.5*(d1+d2))) \
	/ beta(0.5*d1, 0.5*d2)

plot f(x, 1.0, 1.0) t "d1=1, d2=1" lc rgb "red" lw 5,\
   f(x, 2.0, 1.0) t "d1=2, d2=1" lc rgb "black" lw 5,\
   f(x, 5.0, 2.0) t "d1=5, d2=2" lc rgb "blue" lw 5,\
   f(x,10.0, 1.0) t "d1=10, d2=1" lc rgb "green" lw 5,\
   f(x,1.0, 100.0) t "d1=1, d2=100" lc rgb "grey" lw 5

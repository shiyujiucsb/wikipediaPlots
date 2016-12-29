set term svg 
set output 'param_j3k3.svg'

set samples 10000

unset label
unset tic
unset border

set key off
set multiplot layout 5, 4

fx(t) = cos(a*t)-cos(b*t)*cos(b*t)*cos(b*t)
fy(t) = sin(c*t)-sin(d*t)*sin(d*t)*sin(d*t)

set parametric
set size square

a = 1
b = 2
c = 1
d = 2
x(t) = fx(t)
y(t) = fy(t)
set title "1, 2, 1, 2"
plot [-pi:pi] x(t), y(t) lc "red" lw 0.2

a = 2
b = 1
c = 2
d = 1
x(t) = fx(t)
y(t) = fy(t)
set title "2, 1, 2, 1"
plot [-pi:pi] x(t), y(t) lc "red" lw 0.2

a = 1
b = 3
c = 1
d = 3
x(t) = fx(t)
y(t) = fy(t)
set title "1, 3, 1, 3"
plot [-pi:pi] x(t), y(t) lc "red" lw 0.2

a = 3
b = 1
c = 3
d = 1
x(t) = fx(t)
y(t) = fy(t)
set title "3, 1, 3, 1"
plot [-pi:pi] x(t), y(t) lc "red" lw 0.2

a = 1
b = 80
c = 1
d = 80
x(t) = fx(t)
y(t) = fy(t)
set title "1, 80, 1, 80"
plot [-pi:pi] x(t), y(t) lc "red" lw 0.2

a = 80
b = 1
c = 1
d = 80
x(t) = fx(t)
y(t) = fy(t)
set title "80, 1, 1, 80"
plot [-pi:pi] x(t), y(t) lc "red" lw 0.2

a = 80
b = 1
c = 80
d = 1
x(t) = fx(t)
y(t) = fy(t)
set title "80, 1, 80, 1"
plot [-pi:pi] x(t), y(t) lc "red" lw 0.2

a = 1
b = 100
c = 1
d = 50
x(t) = fx(t)
y(t) = fy(t)
set title "1, 100, 1, 50"
plot [-pi:pi] x(t), y(t) lc "red" lw 0.2

unset multiplot
set term windows
set output
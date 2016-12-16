set term svg font 'Times, 24'
set output 'param33_1_80_1_80.svg'

set samples 10000

unset label
unset tic
unset border

set key off

set parametric
a = 1
b = 80
c = 1
d = 80
x(t) = cos(a*t)-cos(b*t)*cos(b*t)*cos(b*t)
y(t) = sin(c*t)-sin(d*t)*sin(d*t)*sin(d*t)
plot [-pi:pi] x(t), y(t) lc "red"

set term windows
set output
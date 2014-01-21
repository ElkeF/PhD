set terminal pdf enhanced color solid font "Helvetica, 24"
set output 'ArXeXe12_12_surf.pdf'


# Paletten
set palette defined (-1 '#1E90FF',0 'white',2 '#1E90FF',4 '#1E90FF')
#set palette defined (0 '#1E90FF',1 '#1E90FF',2 '#191970', 3 '#191970')
#set palette defined (0 '#1E90FF',1 '#1E90FF')
#set palette defined (-2 'red',-1 'black',0 'white',1 'black',2 'red')
#set palette defined (-2 'red',0 'white',2 'red')
#set palette defined (-1 'blue',-1 'grey',0 'white',1 'grey',2 'red')
#set palette defined (-1 'red',0 'white',1 'blue')
#set palette defined (-2 'violet',-1 'blue',0 'green',1 'yellow',2 'red')
#set palette defined (0 'magenta',1 '#3366ff',2 '#99ffcc',3 '#339900',4 '#66ff33',5 '#996633', 6 '#ff9900',7 '#ffff33',8 'red')

set view 80,30
set view 45,45

set nokey
unset colorbox

set samples 300

set hidden3d
set style line 3  linetype -1 linewidth 0.5
#set pm3d depthorder hidden3d 3
set style fill  transparent solid 0.65 border

set xlabel 'R in Angstrom' offset -1,-2.,1
set ylabel 'theta in radians' offset 3,-1,0
set zlabel 'E in eV'
set ztics 5

d(x,y) = 12.13 + 12.13 + 14.39964 / sqrt(4.04**2 - 2*4.04*x*cos(y) + x**2)
e(x,y) = 13.44 + 12.13 + 14.39964 / sqrt(4.04**2 - 2*4.04*x*cos(y) + x**2)
f(x,y) = (13.44 + 13.44 + 14.39964 / sqrt(4.04**2 - 2*4.04*x*cos(y) + x**2))
g(x,y) = 29.2
#splot [4:12][0.34906:3.14159] f(x,y) with pm3d, \
#                              d(x,y) with pm3d, \
#                              e(x,y) with pm3d, \
#                              g(x,y) lt rgb '#191970'

splot [4:12][0.34906:3.14159] f(x,y) with pm3d, \
                              g(x,y) lt rgb '#191970'

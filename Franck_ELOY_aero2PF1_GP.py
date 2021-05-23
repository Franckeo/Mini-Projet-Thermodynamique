import matplotlib.pyplot as plt
import math
from numpy import *

#                       --- GRAPHIQUES Lennard-Jones 1 ---

r_r0 = linspace(0,2.5,1000)
r = linspace(0,2.5,1000)

Ep1 = (r_r0)**(-12) - 2*((r_r0)**(-6))
Ep2 = -2*(1/r**6)
Ep3 = (1/r)**12

#plt.style.use('dark_background')
plt.xlim(0.5, 2.5)
plt.ylim(-1.5, 1.5)
plt.grid(color='grey', linewidth=1)
plt.plot(r_r0, Ep1, color='green', label = "Energie d'intéraction réduite totale")
plt.plot(r, Ep2, color='blue', label = "Energie réduite d'attraction")
plt.plot(r, Ep3, color='red', label = 'Energie réduite de répulsion')
plt.axvspan(2, 2.5, facecolor='palegreen', alpha=0.5, label='zone sans interaction')
plt.axvspan(1, 2, facecolor='steelblue', alpha=0.5, label="zone attractive")
plt.axvspan(0.5, 1, facecolor='indianred', alpha=0.5, label='zone répulsive')
plt.xlabel('r/r0')
plt.ylabel('E0/epsilon')
plt.legend(loc='upper right')
plt.title("Potentiel de Lennard Jones 1")
plt.show()

#                       --- GRAPHIQUES Lennard-Jones 2 ---

r = linspace(0.5,2.5,1000)

Ep1 = ((12*(r**11))/(r**24)-2*((6*(r**5))/(r**12)))
Ep2 = (12*(r**11))/(r**24)
Ep3 = -2*(6*(r**5))/(r**12)

#plt.style.use('dark_background')
plt.xlim(0.5, 2.5)
plt.ylim(-6, 6)
plt.grid(color='grey', linewidth=1)
plt.plot(r, Ep1, color='green', label = "Energie d'intéraction réduite totale")
plt.plot(r, Ep2, color='blue', label = "Energie réduite d'attraction")
plt.plot(r, Ep3, color='red', label = 'Energie réduite de répulsion')
plt.xlabel('r/r0')
plt.ylabel('E0/epsilon')
plt.legend(loc='upper right')
plt.title("Potentiel de Lennard Jones 2")
plt.show()

#                       --- GRAPHIQUES GP ---

R = 8.314 

T1 = 10
T2 = 20
T3 = 30

v = linspace(-10,10,1000)
P1 = (R*T1)/v
P2 = (R*T2)/v
P3 = (R*T3)/v

#plt.style.use('dark_background')
plt.xlim(-10, 10)
plt.ylim(-200, 200)
plt.grid(color='grey', linewidth=1)
plt.plot(v, P1, color='red', label = 'Température 1')
plt.plot(v, P2, color='green', label = 'Température 2')
plt.plot(v, P3, color='blue', label = 'Température 3')
plt.xlabel('Volume (m^3)')
plt.ylabel('Pression (Pa)')
plt.legend(loc='upper left')
plt.title("Représentation graphique mathématique de l'équation des gaz parfaits")
plt.show()

#                       --- GRAPHIQUES VDW ---


a = 1.0
b = 4.0
k1 = 10
k2 = 20
k3 = 30

v = linspace(-10,10,100)
P1 = (k1/(v-b))-(a/(v**2))
P2 = (k2/(v-b))-(a/(v**2))
P3 = (k3/(v-b))-(a/(v**2))

#plt.style.use('dark_background')
plt.xlim(-10, 10)
plt.ylim(-100, 100)
plt.grid(color='grey', linewidth=1)
plt.plot(v, P1, color='red', label = 'k=10')
plt.plot(v, P2, color='green', label = 'k=20')
plt.plot(v, P3, color='blue', label = 'k=30')
plt.xlabel('Volume (m^3/mol)')
plt.ylabel('Pression (Pa)')
plt.legend(loc='upper left')
plt.title("Courbe representative de l'equation de Van Der Waals")
plt.show()

#                       --- GRAPHIQUES Clapeyron (P en fonction de V) ---

R = 8.314
a = 363.7*10**(-3)
b = 0.0427*10**(-3)
Pc = (363.7*10**(-3))/(27*(0.0427*10**(-3))**2)
Tc = (8*(363.7*10**(-3)))/(27*(0.0427*10**(-3))*8.314)
Vc = 3*(0.0427*10**(-3))
num = 0 

V = linspace(5*10**-5, 1*10**(-3),1000)

plt.xlim(0, 1.20*10**-3)
plt.ylim(0, 6*10**7)
plt.grid(color='grey', linewidth=1)

for T in range(300, 1301, 200):
    P1 = (R*T)/V #GP
    P2 = ((T*R)/(V-b)) - a/(V**2) #VDW

    if num == 0:
        label0 = 'Equation Gaz Parfaits'
        label1 = 'Equation de Van Der Waals'
    else:
        label0=''
        label1=''
    num += 1
    plt.plot(V, P1, color='blue', label = label0)
    plt.plot(V, P2, color='red', label = label1)
    
plt.xlabel('Volume (m^3/mol)')
plt.ylabel('Pression (Pa)')
plt.legend(loc='upper right')
plt.title("      Isotherme d'un gaz parfait et d'un gaz de Van Der Waals")
plt.show()

#                       --- GRAPHIQUES P en fonction de T ---

R = 8.314
a = 363.7*10**(-3)
b = 0.0427*10**(-3)
Pc = (363.7*10**(-3))/(27*(0.0427*10**(-3))**2)
num = 0 

T = linspace(300, 1300, 1000)

plt.xlim(100, 1500)
plt.ylim(0, 8*10**7)
plt.grid(color='grey', linewidth=1)

for V in [2*10**(-4), 4*10**(-4), 6*10**(-4), 8*10**(-4), 10**(-3)]:
    P1 = (R*T)/V #GP
    P2 = ((T*R)/(V-b)) - a/(V**2) #VDW
    if num == 0:
        label0 = 'Equation Gaz Parfaits'
        label1 = 'Equation de Van Der Waals'
    else:
        label0=''
        label1=''
    num += 1
    plt.plot(T, P1, color='blue', label = label0)
    plt.plot(T, P2, color='red', label = label1)
    
plt.xlabel('Température (K)')
plt.ylabel('Pression (Pa)')
plt.legend(loc='upper right')
plt.title("      Isotherme d'un gaz parfait et d'un gaz de Van Der Waals")
plt.show()

#                       --- G GRAPHIQUES Amagat ---

Tm = (363.7*10**(-3))/(8.314*(0.0427*10**(-3)))
r = 8.314
p_vdwl =[]
p_gpl = []
p_vdwl2 = []
p_gpl2 = []

for t in range(200, 1700, 100):
    for v in range(1, 1001):
        p_vdw =  (r*t)/(v*10**(-4.3)-(0.0427*10**(-3))) - (363.7*10**(-3))/(v*10**(-4.3))**2
        p_vdw2 = ((r*t)/(v*10**(-4.3)-(0.0427*10**(-3))) - (363.7*10**(-3))/(v*10**(-4.3))**2)*v*10**(-4.3)
        p = (r*t)/v*10**(-3)
        pv_1 = (r*t)

        p_vdwl.append(p_vdw)
        p_vdwl2.append(p_vdw2)
        p_gpl.append(p)
        p_gpl2.append(pv_1)

#    plt.plot(p_gpl, p_gpl2, color = 'red')

    plt.plot(p_vdwl, p_vdwl2, color = 'blue')
    plt.xlim(0, 10**(7.5))
    plt.ylim(0, 9000)
    p_vdwl =[]
    p_vdwl2 = [] 
    p_gpl =[]
    p_gpl2 =[]

pv_1 = linspace(0, 9000, 256)
p = - (pv_1**2)/(2*(363.7*10**(-3))) + pv_1 /(2*(0.0427*10**(-3)))

#plt.plot(p,pv_1, color='red')

plt.ylabel("PV (Pa.m^3)")
plt.xlabel("Pression (pa)")
plt.grid()
plt.title("Coordonnées d'Amagat : PV en fonction de P Gaz et d'un Van Der Waals")
plt.legend()
plt.show()

#                       --- H GRAPHIQUES Mariotte ---

plt.xlim(0, 10**(7.5))
plt.ylim(0, 9000)
pv_1 = linspace(0, 9000, 256)
p = - (pv_1**2)/(2*(363.7*10**(-3))) + pv_1 /(2*(0.0427*10**(-3)))

plt.plot(p,pv_1, color='red')

plt.ylabel("PV (Pa.m^3)")
plt.xlabel("Pression (Pa)")
plt.grid()
plt.title("Parabole de Mariotte")
plt.legend()
plt.show()

#                       --- Equation réduite de Van Der Waals ---

x = linspace(0.4,2,10000)
plt.xlim(0.4, 2)
plt.ylim(0.8, 1.4)

y1 = ((8*1.03)/((3*x)-1))-(3/x**2)
plt.plot(x, y1, color='maroon',label="Tr = 1.03")

y2 = ((8*1.02)/((3*x)-1))-(3/x**2)
plt.plot(x, y2, color='maroon',label="Tr = 1.02")

y3 = ((8*1.01)/((3*x)-1))-(3/x**2)
plt.plot(x, y3, color='maroon',label="Tr = 1.01")

y4 = ((8*1.00)/((3*x)-1))-(3/x**2)
plt.plot(x, y4, color='red',label="Tr = 1.00")

y5 = ((8*0.99)/((3*x)-1))-(3/x**2)
plt.plot(x, y5, color='slateblue',label="Tr = 0.99")

y6 = ((8*0.98)/((3*x)-1))-(3/x**2)
plt.plot(x, y6, color='slateblue',label="Tr = 0.98")

y7 = ((8*0.97)/((3*x)-1))-(3/x**2)
plt.plot(x, y7, color='slateblue',label="Tr = 0.97")

plt.plot(1,1 , marker = "o", color='black', label='Point Critique')

plt.ylabel("Pression réduite Pr")
plt.xlabel("Volume réduit Vr")
plt.grid()
plt.title("Equation de Van der Waals en coordonée réduite dans le diagramme de Clapeyron")
plt.legend()
plt.show()
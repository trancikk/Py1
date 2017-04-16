import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import formlayout as fml

import xlwt



def g_jm_r(c_r, alf_r, a_kpsi0r, z_kr, z_0kr, ds, kk, ll):
    gjm1 = (c_r[kk, ll] * a_kpsi0r[ll] / (z_kr[ll] - z_0kr[ll]) -
            np.conj(c_r[kk, 0] * a_kpsi0r[0]) * alf_r[0, ll] /
            (z_kr[ll] - np.conj(z_0kr[0])) -
            np.conj(c_r[kk, 1] * a_kpsi0r[1]) * alf_r[1, ll] /
            (z_kr[ll] - np.conj(z_0kr[1])) -
            np.conj(c_r[kk, 2] * a_kpsi0r[2]) * alf_r[2, ll] /
            (z_kr[ll] - np.conj(z_0kr[2])) -
            np.conj(c_r[kk, 3] * a_kpsi0r[3]) * alf_r[3, ll] /
            (z_kr[ll] - np.conj(z_0kr[3])))#*ds
    return gjm1



def Nk_r(field1, field2, e_ipsi):
    Nkr = -field1 * np.real(e_ipsi) - field2 * np.imag(e_ipsi)
    return Nkr


# main program
# initial part
# Materials and cracks forms
datalist1 = [(None, '<b>Materials<b>'),
             ('Material 1', 1),
             (None, '<b>Geometric<b>'),
             ('the number of partition for cracs:n', 17),
             (None, 'parameters for cracs '),
             ('p1_1', 1.), ('p2_1', 1.),('h1',1.),('alf1',0)]
mat, n, p1_1, p2_1,h1,alf1 = fml.fedit(datalist1, title="Cracs form")
alf1=float(alf1)*pi
# n=int(raw_input('Enter the number of partition for cracs: n\n'))
# p1_1,p2_1,h1=raw_input('Enter the parameters for cracs 1\
# (use Space buttom to split): p1, p2,h\n').split(' ')
# p1_1=float(p1_1);p2_1=float(p2_1);h1=float(h1)
# p1_2,p2_2,h2=raw_input('Enter the parameters for cracs 2\
# p1_2=float(p1_2);
# p2_2=float(p2_2);h2=float(h2)


# dictionary mater_const['key'] contains list of const for material 'key'
# s11=s33=[0], s22=[1], s44=s66=[2], s55=[3], s12=s23=[4],s13=[5]
# g16=g34=[6],g21=g23=[7],g22=[8],p16=p34=[9],p21=p23=[10],p22=[11]
# bet11=bet33=[12],bet22=[13],nu11=nu33=[14],nu22=[15],hi11=hi33=[16],hi22=[17]
# mu1=[18],mu2=[19],mu3=[20],mu4=[21]

s0 = 1.e-6
g0 = 1.e-2
p0 = 1.e-5
bt0 = 1.e3
nu0 = 1.e-1
hi0 = 1.e-1
mater_const = dict.fromkeys(['M1', 'M2', 'M3'])
mater_const['M1'] = [22.260 * s0, 14.984 * s0, 47.481 * s0, 69.204 * s0, -6.437 * s0, \
                     -11.942 * s0, 109.22 * g0, -4.333 * g0, 8.016 * g0, 268.318 * p0, \
                     17.778 * p0, 31.206 * p0, 19.612 * bt0, 10.612 * bt0, 213.404 * nu0, \
                     -5.534 * nu0, 0.590 * hi0, 0.575 * hi0, 2.89987007j, 1.25351156j, \
                     -1.67633363e-01 + 0.44518972j, 1.67633363e-01 + 0.44518972j]
mater_const['M2'] = [10.745 * s0, 7.398 * s0, 7.637 * s0, 32.680 * s0, -2.542 * s0, \
                     -5.595 * s0, 2.054 * g0, -1.159 * g0, 2.458 * g0, 98.843 * p0, \
                     12.102 * p0, 22.268 * p0, 0.106 * bt0, 0.09 * bt0, -14.931 * nu0, \
                     -3.74 * nu0, 0.805 * hi0, 0.704 * hi0, 1.7671015j, 0.99501903j, \
                     -3.93881996e-01 + 0.72471621j, 3.93881996e-01 + 0.72471621j]
mater_const['M3'] = [7.165 * s0, 6.797 * s0, 19.912 * s0, 19.802 * s0, -2.337 * s0, \
                     -2.736 * s0, 2.028 * g0, -0.496 * g0, 1.157 * g0, 1.85 * p0, \
                     0.576 * p0, 1.186 * p0, 0.156 * bt0, 0.137 * bt0, -0.190 * nu0, \
                     -0.185 * nu0, 0.336 * hi0, 0.119 * hi0, 1.3066352j, 0.92818319j, \
                     0.80544586j, 0.59523266j]
mater_correspond = {1: 'M1', 2: 'M2', 3: 'M3'}
# mat=raw_input('Enter number of material 1 (upper)  from 1 to 3\n')
print 'You choose the material upper ', mater_correspond[mat]
# '\n You choose the material lower halfplane ', mater_correspond[mat_]
# initial part
# parameters of materials save in m_p1, mp2 and correspond vectors mu1 and mu2
m_p1 = mater_const[mater_correspond[mat]]
mu1 = m_p1[18:]

datalist2 = [(None, '<b> fields at infinity <b>'),
             ('sig11_1i', 0), ('sig12i', 0), ('sig22i', 0),
             ('D1_1i', 0), ('D2i', 0), ('B1_1i', 0),
             ('B2ip1_2', 0)]
fields = fml.fedit(datalist2, title="Initial condition at infinity")
f_inf = list()
for f_i in fields:
    f_inf.append(float(f_i))
print 'solution given for \n sig11_1i=', f_inf[0], '  sig12i=', f_inf[1], \
    ' sig22i=', f_inf[2], ' \n D1_1i=', f_inf[3], ' D2i=', f_inf[4], \
    ' B1_1i=', f_inf[5], ' B2i=', f_inf[6]

datalist3 = [(None, '<b> pressure on the banks of the cracs press_r<b>'),
             ('pres_1', 1.)]
press_r = fml.fedit(datalist3, title="Pressure")
press = list()
for p_i in press_r:
    press.append(float(p_i))
print 'solution given for \n press_1=', press[0]

# construct the polynoms L_ij(1,mu) as function of mu
L11 = lambda x: np.poly1d([x[0], 0., 2 * x[4] + x[2], 0., x[1]])
L12 = lambda x: np.poly1d([-(x[7] + x[6]), 0., -x[8]])
L13 = lambda x: np.poly1d([-(x[10] + x[9]), 0., -x[11]])
L22 = lambda x: np.poly1d([-x[12], 0., -x[13]])
L23 = lambda x: np.poly1d([-x[14], 0., -x[15]])
L33 = lambda x: np.poly1d([-x[16], 0., -x[17]])
# construct the polynoms A_ij(1,mu)-cofactors of matrix L as function of mu
A11 = lambda x: np.polyadd(np.polymul(L22(x), L33(x)), -np.polymul(L23(x), L23(x)))
A12 = lambda x: np.polyadd(np.polymul(L23(x), L13(x)), -np.polymul(L12(x), L33(x)))
A13 = lambda x: np.polyadd(np.polymul(L12(x), L23(x)), -np.polymul(L22(x), L13(x)))
A22 = lambda x: np.polyadd(np.polymul(L11(x), L33(x)), -np.polymul(L13(x), L13(x)))
A23 = lambda x: np.polyadd(np.polymul(L12(x), L13(x)), -np.polymul(L11(x), L23(x)))
A33 = lambda x: np.polyadd(np.polymul(L11(x), L22(x)), -np.polymul(L12(x), L12(x)))
# construct the matrices of constants c_1,c_2- for upper and lower halfspaces
c_1 = np.mat([[-mu1[k] * A11(m_p1)(mu1[k]) for k in xrange(4)], \
              [A11(m_p1)(mu1[k]) for k in xrange(4)], \
              [-A12(m_p1)(mu1[k]) for k in xrange(4)], \
              [-A13(m_p1)(mu1[k]) for k in xrange(4)]])
# construct the matrices of constants m_1,m_2- for upper and lower halfspaces
r_1 = np.mat([[(m_p1[0] * (mu1[k] ** 2) + m_p1[4]) * A11(m_p1)(mu1[k]) - \
               m_p1[7] * A12(m_p1)(mu1[k]) - \
               m_p1[10] * A13(m_p1)(mu1[k]) for k in xrange(4)], \
              [(m_p1[4] * mu1[k] + m_p1[1] / mu1[k]) * A11(m_p1)(mu1[k]) - \
               m_p1[8] / mu1[k] * A12(m_p1)(mu1[k]) - \
               m_p1[11] / mu1[k] * A13(m_p1)(mu1[k]) for k in xrange(4)], \
              [mu1[k] * (m_p1[6] * A11(m_p1)(mu1[k]) + m_p1[12] * A12(m_p1)(mu1[k]) + \
                         m_p1[14] * A13(m_p1)(mu1[k])) for k in xrange(4)], \
              [mu1[k] * (m_p1[9] * A11(m_p1)(mu1[k]) + m_p1[14] * A12(m_p1)(mu1[k]) + \
                         m_p1[16] * A13(m_p1)(mu1[k])) for k in xrange(4)]])

#ckm_1 = np.array([[A11(m_p1)(mu1[k]) for k in xrange(4)], \
 #                 [-mu1[k] * A11(m_p1)(mu1[k]) for k in xrange(4)], \
  #                [(m_p1[0] * (mu1[k] ** 2) + m_p1[4]) * A11(m_p1)(mu1[k]) - \
   #                m_p1[7] * A12(m_p1)(mu1[k]) - \
    #               m_p1[10] * A13(m_p1)(mu1[k]) for k in xrange(4)], \
     #             [(m_p1[4] * mu1[k] + m_p1[1] / mu1[k]) * A11(m_p1)(mu1[k]) - \
      #             m_p1[8] / mu1[k] * A12(m_p1)(mu1[k]) - \
       #            m_p1[11] / mu1[k] * A13(m_p1)(mu1[k]) for k in xrange(4)], \
        #          [-A13(m_p1)(mu1[k]) for k in xrange(4)], \
         #         [mu1[k] * (m_p1[9] * A11(m_p1)(mu1[k]) + m_p1[14] * A12(m_p1)(mu1[k]) + \
          #                   m_p1[16] * A13(m_p1)(mu1[k])) for k in xrange(4)], \
           #       [-A12(m_p1)(mu1[k]) for k in xrange(4)], \
            #      [mu1[k] * (m_p1[6] * A11(m_p1)(mu1[k]) + m_p1[12] * A12(m_p1)(mu1[k]) + \
             #                m_p1[14] * A13(m_p1)(mu1[k])) for k in xrange(4)]])

Ckm_ = np.mat(c_1)
Bkm = np.mat(np.conj(c_1))
alf_1 = Ckm_.I * Bkm
alf_1 = np.conj(alf_1)


field_11 = np.array([[press[0]], [0], [0], [0]])
field_21 = np.array([[0], [press[0]], [0], [0]])

for alf1 in np.linspace(0*pi,1*pi/2,15): #h1:
    # interpolation points T_n(bt)=0
    bet = [np.cos((2 * (k + 1) - 1) * pi / 2 / n) for k in xrange(n)]
    # colocation points U_(n-1)(bt0)=0
    bet0 = [np.cos(pi * (l + 1) / n) for l in xrange(n - 1)]

    for bt0 in bet0:
        z_10 = (p2_1*bt0+1.j*p1_1*bt0*bt0)*np.exp(1.j*alf1)+1.j*h1
        dz10 = (p2_1+2*1.j*p1_1*bt0)*np.exp(1.j*alf1)
        ds10 = np.sqrt(dz10.real ** 2 + dz10.imag ** 2)
        eipsi10 = -1.j * dz10 / ds10
        z_10k = list([z_10.real + mu * z_10.imag for mu in mu1])
        a_kpsi01 = list([mu * eipsi10.real - eipsi10.imag for mu in mu1])
        for bt in bet:
            z_1 = (p2_1*bt+1.j*p1_1*bt*bt)*np.exp(1.j*alf1)+1.j*h1
            dz1 = (p2_1+2*1.j*p1_1*bt)*np.exp(1.j*alf1)
            ds1 = np.sqrt(dz1.real ** 2 + dz1.imag ** 2)
            z_1k = list([z_1.real + mu * z_1.imag for mu in mu1])
            g_11 = np.zeros((4, 4), 'complex')
            for jj in xrange(4):
                for mm in xrange(4):
                    g_11[jj, mm] = g_jm_r(-c_1, alf_1, a_kpsi01, z_1k, z_10k, ds1, jj, mm)
            if bt == bet[0]:
                GG = np.hstack((g_11, np.conj(g_11)))
            else:
                GG1 = np.hstack((g_11, np.conj(g_11)))
                GG = np.hstack((GG, GG1))
        N_1 = Nk_r(field_11, field_21, eipsi10)
        if bt0 == bet0[0]:
            AA = GG.copy()
            BB = N_1.copy()
        else:
            AA = np.vstack((AA, GG))
            BB = np.vstack((BB, N_1))

    # conditions (161) and algebraic equations

    for bt in bet:
        z_1 = (p2_1 * bt + 1.j * p1_1 * bt * bt) * np.exp(1.j * alf1) + 1.j * h1
        dz1 = (p2_1+2*1.j*p1_1*bt)*np.exp(1.j*alf1)
        ds1 = np.sqrt(dz1.real ** 2 + dz1.imag ** 2)
        g_11 = r_1# * ds1
        if bt == bet[0]:
            GG = np.hstack((g_11, -np.conj(g_11)))
        else:
            GG1 = np.hstack((g_11, -np.conj(g_11)))
            GG = np.hstack((GG, GG1))
    AA = np.vstack((AA, GG))
    for k in xrange(n):
        g_11 = np.hstack((np.zeros((4, 8 * k), 'complex'), -c_1, \
                            -np.conj(-c_1), np.zeros((4, 8 * (n - k - 1)), 'complex')))
        if k == 0:
            GG = g_11.copy()
        else:
            GG = np.vstack((GG, g_11))
    AA = np.mat(np.vstack((AA, GG)))
    BB = np.mat((np.vstack((BB, np.zeros((4 * n + 4, 1), 'complex')))) * 2 * n)

    W = AA.I * BB
    omeg = np.array(W).reshape(n, 8)
    print omeg[0,:]
    print omeg[n-1,:]

    ctan1 = np.array([((-1) ** (k + 2)) / np.tan((2 * (k + 1) - 1) * pi / 4 / n) / n for k in xrange(n)])
    tan_1 = np.array([((-1) ** (k + 1 + n)) * np.tan((2 * (k + 1) - 1) * pi / 4 / n) / n for k in xrange(n)])
    omeg1 = np.dot(ctan1, omeg)
    omeg_1 = np.dot(tan_1, omeg)
    #omeg11-line 0 -
    omeg1 = np.array(omeg1).reshape(2, -1)
    omeg11=omeg1[0, :]

    omeg_1 = np.array(omeg_1).reshape(2, -1)
    omeg_11=omeg_1[0, :]



    bet = np.array(bet).reshape(n, 1)
    zet = (p2_1*bet+1.j*p1_1*bet*bet)*np.exp(1.j*alf1)+1.j*h1
    plt.plot(np.around(zet.real,5),np.around(zet.imag,5))

    bt0=1
    z_10 = (p2_1*bt0+1.j*p1_1*bt0*bt0)*np.exp(1.j*alf1)+1.j*h1
    dz10 = (p2_1+2*1.j*p1_1*bt0)*np.exp(1.j*alf1)
    ds10 = np.sqrt(dz10.real ** 2 + dz10.imag ** 2)
    eipsi10 = -1.j * dz10 / ds10
    a_kpsi01 = list([mu * eipsi10.real - eipsi10.imag for mu in mu1])
    bk=list([-mu * eipsi10.imag - eipsi10.real for mu in mu1])
    d_1 = np.sqrt(pi/ds10)*np.mat([[a_kpsi01[k] * A11(m_p1)(mu1[k]) for k in xrange(4)], \
                    [bk[k]*A11(m_p1)(mu1[k]) for k in xrange(4)], \
                    [A12(m_p1)(mu1[k]) for k in xrange(4)], \
                    [A13(m_p1)(mu1[k]) for k in xrange(4)]])
    d_1=np.real(d_1*np.mat(omeg11).T)

    print 'd_1',d_1

    bt0=-1
    z_10 = (p2_1*bt0+1.j*p1_1*bt0*bt0)*np.exp(1.j*alf1)+1.j*h1
    dz10 = (p2_1+2*1.j*p1_1*bt0)*np.exp(1.j*alf1)
    ds10 = np.sqrt(dz10.real ** 2 + dz10.imag ** 2)
    eipsi10 = -1.j * dz10 / ds10
    a_kpsi01 = list([mu * eipsi10.real - eipsi10.imag for mu in mu1])
    bk=list([-mu * eipsi10.imag - eipsi10.real for mu in mu1])
    d_1_ = np.sqrt(pi/ds10)*np.mat([[a_kpsi01[k] * A11(m_p1)(mu1[k]) for k in xrange(4)], \
                    [bk[k]*A11(m_p1)(mu1[k]) for k in xrange(4)], \
                    [A12(m_p1)(mu1[k]) for k in xrange(4)], \
                    [A13(m_p1)(mu1[k]) for k in xrange(4)]])
    d_1_=np.real(d_1_*np.mat(omeg_11).T)

    Ked = np.sqrt(pi/ds10)*np.real(r_1[2:]*(-c_1.I)*np.mat(omeg_11).T)


    d_1_=np.vstack((alf1,d_1_,Ked))
    if alf1==0*pi:
        k_int=d_1_
    else:
        k_int=np.hstack((k_int,d_1_))
        
    print 'd_1_',d_1_
    print 'alf1',alf1
print 'k_int',k_int
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Sheet_1')
#for i in range(6):
    #print 'THis is i: \n'
    #print i
print 'hehe \n'
print k_int[5]
print k_int[4]
for i in range(6):
    alist=k_int[i]
    blist=alist.tolist()
    sheet.row(i).write(i,blist) 
#sheet.write(k_int,(k_int[i] for i in k_int))
#sheet.
workbook.save('my_file.xls')
plt.show()
plt.xlabel('Alpha')
plt.ylabel('KI')
plt.show(plt.plot(k_int[0],k_int[1],'go'))
plt.xlabel('Alpha')
plt.ylabel('KII')
plt.show(plt.plot(k_int[0],k_int[2],'go'))
plt.xlabel('Alpha')
plt.ylabel('KD')
plt.show(plt.plot(k_int[0],k_int[3],'go'))
plt.xlabel('Alpha')
plt.ylabel('KB')
plt.show(plt.plot(k_int[0],k_int[4],'go'))
plt.xlabel('Alpha')
plt.ylabel('KE')
plt.show(plt.plot(k_int[0],k_int[5],'go'))
plt.xlabel('Alpha')
plt.ylabel('KH')
plt.show(plt.plot(k_int[0],k_int[6],'go'))
#print 'len(k_int[0])',len(k_int[0])
    



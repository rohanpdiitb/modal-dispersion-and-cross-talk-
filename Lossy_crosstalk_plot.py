import numpy
import pickle
import math, sys
from pylab import *
from math import *
import ConfigParser
from math import factorial,log10
from numpy import linalg as LA
import matplotlib.pyplot as plt
from scipy.linalg import expm
from scipy import signal
from tempfile import TemporaryFile
from matplotlib import rc
rc('text', usetex=True)
rc('xtick', labelsize=20)
rc('ytick', labelsize=20)
rc('legend', fontsize=32)
rc('xtick', labelsize=15)
rc('ytick', labelsize=15)
t = numpy.arange(0, 1.01e10, 1e8)
A = numpy.zeros(len(t))
B = numpy.zeros(len(t))
C = numpy.zeros(len(t))
D = numpy.zeros(len(t))
E = numpy.zeros(len(t))
F = numpy.zeros(len(t))
G = numpy.zeros(len(t))
H = numpy.zeros(len(t))
data1 = numpy.zeros(len(t))
data2 = numpy.zeros(len(t))
data3 = numpy.zeros(len(t))
data4 = numpy.zeros(len(t))
data5 = numpy.zeros(len(t))
data6 = numpy.zeros(len(t))
data7 = numpy.zeros(len(t))
data8 = numpy.zeros(len(t))
for q in range(3):
    print q+3
    filename1 = 'lossy_crosstalk_First_response multi mode_offset2 1km'+str(q+3)+str(0)
    filename2 = 'lossy_crosstalk_First_response multi mode_offset2 1km'+str(q+3)+str(1)
    filename3 = 'lossy_crosstalk_First_response multi mode_offset2 1km'+str(q+3)+str(2)
    filename4 = 'lossy_crosstalk_First_response multi mode_offset2 1km'+str(q+3)+str(3)
    filename5 = 'lossy_crosstalk_Higher_response multi mode_offset2 1km'+str(q+3)+str(0)
    filename6 = 'lossy_crosstalk_Higher_response multi mode_offset2 1km'+str(q+3)+str(1)
    filename7 = 'lossy_crosstalk_Higher_response multi mode_offset2 1km'+str(q+3)+str(2)
    filename8 = 'lossy_crosstalk_Higher_response multi mode_offset2 1km'+str(q+3)+str(3)
    f1 = open(filename1,'r')
    f2 = open(filename2,'r')
    f3 = open(filename3,'r')
    f4 = open(filename4,'r')
    f5 = open(filename5,'r')
    f6 = open(filename6,'r')
    f7 = open(filename7,'r')
    f8 = open(filename8,'r')
    
    A = pickle.load(f1)
    B = pickle.load(f2)
    C = pickle.load(f3)
    D = pickle.load(f4)
    E = pickle.load(f5)
    F = pickle.load(f6)
    G = pickle.load(f7)
    H = pickle.load(f8)
    data1 = numpy.array(A)+numpy.array(data1)
    data2 = numpy.array(B)+numpy.array(data2)
    data3 = numpy.array(C)+numpy.array(data3)
    data4 = numpy.array(D)+numpy.array(data4)
    data5 = numpy.array(E)+numpy.array(data5)
    data6 = numpy.array(F)+numpy.array(data6)
    data7 = numpy.array(G)+numpy.array(data7)
    data8 = numpy.array(H)+numpy.array(data8)
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
ms = 20.0
markevery =10
lw = 5
plt.plot([i / 1e9 for i in t],((data5/3)), 'g-^', lw=lw,ms=40,markevery=markevery,label='Higher order response at $\sigma_\kappa$ = 1 m$^{-1}$',markeredgecolor='black',markeredgewidth=1)
plt.plot([i / 1e9 for i in t],((data6/3)), 'r-s', lw=lw,ms=30,markevery=markevery,label='Higher order response at $\sigma_\kappa$ = 3 m$^{-1}$',markeredgecolor='black',markeredgewidth=1)
plt.plot([i / 1e9 for i in t],((data7/3)), 'y-*', lw=lw,ms=15,markevery=markevery,label='Higher order response at $\sigma_\kappa$ = 7 m$^{-1}$',markeredgecolor='black',markeredgewidth=1)
plt.plot([i / 1e9 for i in t],((data8/3)), 'b-v', lw=lw,ms=ms,markevery=markevery,label='Higher order response at $\sigma_\kappa$ = 10 m$^{-1}$',markeredgecolor='black',markeredgewidth=1)
plt.xlabel(r'\text{Modulation bandwidth} (GHz)',fontsize=30)
plt.ylabel(r'\text{Cross-talk} (dB)',fontsize=30)
plt.grid(True)
plt.legend(loc = 'lower right',numpoints=1)
plt.show()

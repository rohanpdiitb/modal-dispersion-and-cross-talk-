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
rc('xtick', labelsize=30)
rc('ytick', labelsize=30)
t = numpy.arange(0, 1.01e11, 1e9)
A = numpy.zeros(len(t))
B = numpy.zeros(len(t))
C = numpy.zeros(len(t))
D = numpy.zeros(len(t))
E = numpy.zeros(len(t))
data1 = numpy.zeros(len(t))
data2 = numpy.zeros(len(t))
data3 = numpy.zeros(len(t))
data4 = numpy.zeros(len(t))
data5 = numpy.zeros(len(t))
for q in range(15):
    filename1='First_frequency response100G few mode 10km00'
    filename2 = 'Higher_frequency response100G few mode 10km'+str(q)+str(0)
    filename3 = 'Higher_frequency response100G few mode 10km'+str(q)+str(1)
    filename4 = 'Higher_frequency response100G few mode 10km'+str(q)+str(2)
    filename5 = 'Higher_frequency response100G few mode 10km'+str(q)+str(3)
    f1 = f1=open(filename1,'r')
    f2 = open(filename2,'r')
    f3 = open(filename3,'r')
    f4 = open(filename4,'r')
    f5 = open(filename5,'r')
    A = pickle.load(f1)
    
    B = pickle.load(f2)
    C = pickle.load(f3)
    D = pickle.load(f4)
    E = pickle.load(f5)
    data1 =numpy.array(A)+numpy.array(data1)
    data2 = numpy.array(B)+numpy.array(data2)
    data3 = numpy.array(C)+numpy.array(data3)
    data4 = numpy.array(D)+numpy.array(data4)
    data5 = numpy.array(E)+numpy.array(data5)
    f1.close()
    f2.close()
    f3.close()
    f4.close()
plt.figure(figsize=(20, 16))
matplotlib.rc('xtick', labelsize=40) 
matplotlib.rc('ytick', labelsize=40) 
plt.axis([0,70, -5, 1])
ms = 20.0
markevery =10
lw = 5
plt.plot([i / 1e9 for i in t],data1/15,'m-o', lw=lw,ms=40,markevery=markevery,label='First order response',markeredgecolor='black',markeredgewidth=1)
plt.plot([i / 1e9 for i in t],data2/15, 'g-^', lw=lw,ms=30,markevery=markevery,label='Higher order response at $\sigma_{\kappa}$ = 1 m$^{-1}$',markeredgecolor='black',markeredgewidth=1)
plt.plot([i / 1e9 for i in t],data3/15, 'r-s', lw=lw,ms=15,markevery=markevery,label='Higher order response at $\sigma_{\kappa}$ = 3 m$^{-1} $',markeredgecolor='black',markeredgewidth=1)
plt.plot([i / 1e9 for i in t],data4/15, 'y-*', lw=lw,ms=ms,markevery=markevery,label='Higher order response at $\sigma_{\kappa}$ = 5 m$^{-1} $',markeredgecolor='black',markeredgewidth=1)
plt.plot([i / 1e9 for i in t],data5/15, 'b-v', lw=lw,ms=ms,markevery=markevery,label='Higher order response at $\sigma_{\kappa}$ = 7 m$^{-1}$',markeredgecolor='black',markeredgewidth=1)
plt.xlabel(r'\text{Modulation bandwidth} (GHz)',fontsize=30)
plt.ylabel(r'\text{Frequency response} (dB)',fontsize=30)
plt.grid(True)
plt.legend(loc = 'lower left', numpoints=1)
plt.show()

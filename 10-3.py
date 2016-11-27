import matplotlib.pyplot as plt
import numpy as np
import math
alfa=[0.0003,0.0005,0.0008,0.0015,0.0035]
xp=[[],[],[],[],[]]
yp=[[],[],[],[],[]]
tp=[[],[],[],[],[]]
theta=[[],[],[],[],[]]
xy=[[],[],[],[],[]]
x2=[[],[],[],[],[]]
x_mean=[]
y_mean=[]
xy_mean=[]
x2_mean=[]
xy1=[]
x21=[]
xf=np.linspace(0,2,200)
yf=[]
class elliptical:
    def __init__(self,GMs=4*math.pi**2,dt=0.0001,time=2):
        self.GMs=GMs
        self.x=[[0.47],[0.47],[0.47],[0.47],[0.47]]
        self.y=[[0],[0],[0],[0],[0]]
        self.vx=[[0],[0],[0],[0],[0]]
        self.vy=[[8.2],[8.2],[8.2],[8.2],[8.2]]
        self.dt=dt
        self.time=time
        self.r=[[math.sqrt(self.x[0][0]**2+self.y[0][0]**2)],[math.sqrt(self.x[0][0]**2+self.y[0][0]**2)],[math.sqrt(self.x[0][0]**2+self.y[0][0]**2)],[math.sqrt(self.x[0][0]**2+self.y[0][0]**2)],[math.sqrt(self.x[0][0]**2+self.y[0][0]**2)]]
        self.t=[[0],[0],[0],[0],[0]]
        self.a=[]
        self.b=[]
    def calculate(self):
        for n in range(len(alfa)):
            for i in range(int(self.time//self.dt)):
                self.vx[n].append(self.vx[n][i]-self.GMs*self.x[n][i]*self.dt/self.r[n][i]**3-alfa[n]*self.GMs*self.x[n][i]*self.dt/self.r[n][i]**5)
                self.vy[n].append(self.vy[n][i]-self.GMs*self.y[n][i]*self.dt/self.r[n][i]**3-alfa[n]*self.GMs*self.y[n][i]*self.dt/self.r[n][i]**5)
                self.x[n].append(self.x[n][i]+self.vx[n][i+1]*self.dt)
                self.y[n].append(self.y[n][i]+self.vy[n][i+1]*self.dt)
                self.t[n].append(self.t[n][i]+self.dt)
                self.r[n].append(math.sqrt(self.x[n][i+1]**2+self.y[n][i+1]**2))
            for j in range(len(self.r[n])-2):
                if (self.r[n][j+1]**2-self.r[n][j]**2>0 and self.r[n][j+1]**2-self.r[n][j+2]**2>0):
                    xp[n].append(self.x[n][j+1])
                    yp[n].append(self.y[n][j+1])
                    tp[n].append(self.t[n][j+1])
                    if self.x[n][j+1]>=0 and self.y[n][j+1]/self.x[n][j+1]>=0:
                        theta[n].append(math.atan(self.y[n][j+1]/self.x[n][j+1])*180/math.pi)
                    if self.x[n][j+1]>=0 and self.y[n][j+1]/self.x[n][j+1]<0:
                        theta[n].append(math.atan(self.y[n][j+1]/self.x[n][j+1])*180/math.pi+360)
                    if self.x[n][j+1]<0 and self.y[n][j+1]/self.x[n][j+1]>=0:
                        theta[n].append(math.atan(self.y[n][j+1]/self.x[n][j+1])*180/math.pi+180)
                    if self.x[n][j+1]<0 and self.y[n][j+1]/self.x[n][j+1]<0:
                        theta[n].append(math.atan(self.y[n][j+1]/self.x[n][j+1])*180/math.pi+180)
            for k in range(len(theta[n])):
                xy[n].append(tp[n][k]*theta[n][k])
                x2[n].append(tp[n][k]**2)
            x_mean.append(float(sum(tp[n]))/len(tp[n]))
            y_mean.append(float(sum(theta[n]))/len(theta[n]))
            xy_mean.append(float(sum(xy[n]))/len(xy[n]))
            x2_mean.append(float(sum(x2[n]))/len(x2[n]))
            self.a.append(float((xy_mean[n]-x_mean[n]*y_mean[n]))/float((x2_mean[n]-x_mean[n]**2)))
            self.b.append(float((x2_mean[n]*y_mean[n]-x_mean[n]*xy_mean[n]))/float((x2_mean[n]-x_mean[n]**2)))
    def fit(self):
        for k in range(len(alfa)):
            xy1.append(alfa[k]*self.a[k])
            x21.append(alfa[k]**2)
        x_mean1=float(sum(alfa))/len(alfa)
        y_mean1=float(sum(self.a))/len(self.a)
        xy_mean1=float(sum(xy1))/len(xy1)
        x2_mean1=float(sum(x21))/len(x21)
        a=float((xy_mean1-x_mean1*y_mean1))/float((x2_mean1-x_mean1**2))
        b=float((x2_mean1*y_mean1-x_mean1*xy_mean1))/float((x2_mean1-x_mean1**2))
        print a,b
        for m in range(len(xf)):
            yf.append(a*xf[m]+b)
    def show_results(self):
        plt.plot(xf,yf,'g',label='least-squares line')
        plt.scatter(alfa,self.a,label='scatter')
        plt.title(u'Simulation of the precession of Mercury',fontsize=14)
        plt.xlabel(u'alpha',fontsize=14)
        plt.ylabel(u'$d\Theta/dt$(degrees/yr)',fontsize=14)
        plt.xlim(0,0.005)
        plt.ylim(0,60)
        plt.legend(fontsize=14,loc='best')
        
a=elliptical()
a.calculate()
a.fit()
a.show_results()
plt.show()

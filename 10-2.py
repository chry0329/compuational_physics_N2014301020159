import matplotlib.pyplot as plt
import numpy as np
import math
alfa=0.0008
x0=0
y0=0
xp=[]
yp=[]
tp=[]
theta=[]
class elliptical:
    def __init__(self,GMs=4*math.pi**2,dt=0.0001,time=2):
        self.GMs=GMs
        self.x=[0.47]
        self.y=[0]
        self.vx=[0]
        self.vy=[8.2]
        self.dt=dt
        self.time=time
        self.r=[math.sqrt(self.x[0]**2+self.y[0]**2)]
        self.t=[0]
    def calculate(self):
        for i in range(int(self.time//self.dt)):
            self.vx.append(self.vx[i]-self.GMs*self.x[i]*self.dt/self.r[i]**3-alfa*self.GMs*self.x[i]*self.dt/self.r[i]**5)
            self.vy.append(self.vy[i]-self.GMs*self.y[i]*self.dt/self.r[i]**3-alfa*self.GMs*self.y[i]*self.dt/self.r[i]**5)
            self.x.append(self.x[i]+self.vx[i+1]*self.dt)
            self.y.append(self.y[i]+self.vy[i+1]*self.dt)
            self.t.append(self.t[i]+self.dt)
            self.r.append(math.sqrt(self.x[i+1]**2+self.y[i+1]**2))
    def precession(self):
        for j in range(len(self.r)-2):
            if (self.r[j+1]**2-self.r[j]**2>0 and self.r[j+1]**2-self.r[j+2]**2>0):
                xp.append(self.x[j+1])
                yp.append(self.y[j+1])
                tp.append(self.t[j+1])
                if self.x[j+1]>=0 and self.y[j+1]/self.x[j+1]>=0:
                    theta.append(math.atan(self.y[j+1]/self.x[j+1])*180/math.pi)
                if self.x[j+1]>=0 and self.y[j+1]/self.x[j+1]<0:
                    theta.append(math.atan(self.y[j+1]/self.x[j+1])*180/math.pi+360)
                if self.x[j+1]<0 and self.y[j+1]/self.x[j+1]>=0:
                    theta.append(math.atan(self.y[j+1]/self.x[j+1])*180/math.pi+180)
                if self.x[j+1]<0 and self.y[j+1]/self.x[j+1]<0:
                    theta.append(math.atan(self.y[j+1]/self.x[j+1])*180/math.pi+180)
    def show_results(self):
        for j in range(len(xp)):
            plt.plot([0,xp[j]],[0,yp[j]])
        plt.plot(self.x,self.y,'g',label=r'$\alpha$=0.0008'+' trajectory')
        plt.scatter(x0,y0)
        #plt.scatter(tp,theta,label='trajectory')
        plt.title(r'$\alpha$=0.0008'+'  Simulation of the precession of Mercury ',fontsize=14)
        plt.xlabel(u'x(AU)',fontsize=14)
        plt.ylabel(u'y(AU)',fontsize=14)
        #plt.xlabel(u'time(yr)')
        #plt.ylabel(u'$\Theta$(degrees)',fontsize=14)
        #plt.xlim(-1,1)
        #plt.ylim(-1,1)
        plt.legend(fontsize=14,loc='best')
        
a=elliptical()
a.calculate()
a.precession()
a.show_results()
plt.show()

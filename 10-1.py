import matplotlib.pyplot as plt
import numpy as np
import math
beta=[2.01,2.10,2.50,3.00]
x0=0
y0=0
class elliptical:
    def __init__(self,e=0.2,GMs=4*math.pi**2,dt=0.0001,time=4):
        self.e=e
        self.GMs=GMs
        self.x1=[1]
        self.y1=[0]
        self.vx1=[0]
        self.vy1=[2*math.pi*math.sqrt(1-self.e)]
        self.x2=[1]
        self.y2=[0]
        self.vx2=[0]
        self.vy2=[2*math.pi*math.sqrt(1-self.e)]
        self.x3=[1]
        self.y3=[0]
        self.vx3=[0]
        self.vy3=[2*math.pi*math.sqrt(1-self.e)]
        self.x4=[1]
        self.y4=[0]
        self.vx4=[0]
        self.vy4=[2*math.pi*math.sqrt(1-self.e)]
        self.dt=dt
        self.time=time
        self.r1=[math.sqrt(self.x1[0]**2+self.y1[0]**2)]
        self.r2=[math.sqrt(self.x2[0]**2+self.y2[0]**2)]
        self.r3=[math.sqrt(self.x3[0]**2+self.y3[0]**2)]
        self.r4=[math.sqrt(self.x4[0]**2+self.y4[0]**2)]
    def calculate(self):
        for i in range(int(self.time//self.dt)):
            self.vx1.append(self.vx1[i]-self.GMs*self.x1[i]*self.dt/self.r1[i]**(beta[0]+1))
            self.vy1.append(self.vy1[i]-self.GMs*self.y1[i]*self.dt/self.r1[i]**(beta[0]+1))
            self.x1.append(self.x1[i]+self.vx1[i+1]*self.dt)
            self.y1.append(self.y1[i]+self.vy1[i+1]*self.dt)
            self.r1.append(math.sqrt(self.x1[i+1]**2+self.y1[i+1]**2))
        for j in range(int(self.time//self.dt)):
            self.vx2.append(self.vx2[j]-self.GMs*self.x2[j]*self.dt/self.r2[j]**(beta[1]+1))
            self.vy2.append(self.vy2[j]-self.GMs*self.y2[j]*self.dt/self.r2[j]**(beta[1]+1))
            self.x2.append(self.x2[j]+self.vx2[j+1]*self.dt)
            self.y2.append(self.y2[j]+self.vy2[j+1]*self.dt)
            self.r2.append(math.sqrt(self.x2[j+1]**2+self.y2[j+1]**2))
        for i in range(int(self.time//self.dt)):
            self.vx3.append(self.vx3[i]-self.GMs*self.x3[i]*self.dt/self.r3[i]**(beta[2]+1))
            self.vy3.append(self.vy3[i]-self.GMs*self.y3[i]*self.dt/self.r3[i]**(beta[2]+1))
            self.x3.append(self.x3[i]+self.vx3[i+1]*self.dt)
            self.y3.append(self.y3[i]+self.vy3[i+1]*self.dt)
            self.r3.append(math.sqrt(self.x3[i+1]**2+self.y3[i+1]**2))
        for j in range(int(self.time//self.dt)):
            self.vx4.append(self.vx4[j]-self.GMs*self.x4[j]*self.dt/self.r4[j]**(beta[3]+1))
            self.vy4.append(self.vy4[j]-self.GMs*self.y4[j]*self.dt/self.r4[j]**(beta[3]+1))
            self.x4.append(self.x4[j]+self.vx4[j+1]*self.dt)
            self.y4.append(self.y4[j]+self.vy4[j+1]*self.dt)
            self.r4.append(math.sqrt(self.x4[j+1]**2+self.y4[j+1]**2))
    def show_results(self):
        ax1=plt.subplot(221)
        ax2=plt.subplot(222)
        ax3=plt.subplot(223)
        ax4=plt.subplot(224)
        plt.sca(ax1)
        plt.plot(self.x1,self.y1,label='trajectory')
        plt.scatter(x0,y0)
        plt.title(r'$\beta=2.01$'+ 'Simulation of elliptical orbit',fontsize=10)
        plt.xlabel(u'x(AU)',fontsize=10)
        plt.ylabel(u'y(AU)',fontsize=10)
        plt.sca(ax2)
        plt.plot(self.x2,self.y2,label='trajectory')
        plt.scatter(x0,y0)    
        plt.title(r'$\beta=2.10$'+ 'Simulation of elliptical orbit',fontsize=10)
        plt.xlabel(u'x(AU)',fontsize=10)
        plt.ylabel(u'y(AU)',fontsize=10)
        plt.sca(ax3)
        plt.plot(self.x3,self.y3,label='trajectory')
        plt.scatter(x0,y0)
        plt.title(r'$\beta=2.50$'+ 'Simulation of elliptical orbit',fontsize=10)
        plt.xlabel(u'x(AU)',fontsize=10)
        plt.ylabel(u'y(AU)',fontsize=10)
        plt.sca(ax4)
        plt.plot(self.x4,self.y4,label='trajectory')
        plt.scatter(x0,y0)    
        plt.title(r'$\beta=3.00$'+ 'Simulation of elliptical orbit',fontsize=10)
        plt.xlabel(u'x(AU)',fontsize=10)
        plt.ylabel(u'y(AU)',fontsize=10)
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.legend(fontsize=10,loc='best')
a=elliptical()
a.calculate()
a.show_results()
plt.show()

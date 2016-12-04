import math
import pylab as pl
class Hyperion:
    def __init__(self,theta1,theta2): 
        self.theta1 = [theta1]
        self.theta2 = [theta2]
        self.dt = 0.0001
        self.t = [0]
        self.x = [1]
        self.y = [0]
        self.v_x = [0]
        self.v_y = [2.0*math.pi]
        #self.v_y = [5]
        self.r = [1]
        self.beta = 2
        self.avelo1 = [0]
        self.avelo2 = [0]
        self.dthe = [math.log(abs(0.01))]
    def calculate(self):
        while (self.t[-1]<=10):
            self.r[-1] = math.sqrt((self.x[-1]**2) + (self.y[-1]**2))
            self.v_x.append(self.v_x[-1] - \
            4*(math.pi)**2*self.x[-1]*self.dt/((self.r[-1])**(self.beta + 1)))
            self.v_y.append(self.v_y[-1] - \
            4*(math.pi)**2*self.y[-1]*self.dt/((self.r[-1])**(self.beta + 1)))
            self.avelo1.append(self.avelo1[-1]-12*(math.pi**2)*\
            (self.x[-1]*math.sin(self.theta1[-1]) - self.y[-1]*math.cos(self.theta1[-1]))*\
            (self.x[-1]*math.cos(self.theta1[-1]) + self.y[-1]*math.sin(self.theta1[-1]))*\
            self.dt/(self.r[-1])**5)
            self.theta1.append(self.theta1[-1]+self.avelo1[-1]*self.dt)
            self.avelo2.append(self.avelo2[-1]-12*(math.pi**2)*\
            (self.x[-1]*math.sin(self.theta2[-1]) - self.y[-1]*math.cos(self.theta2[-1]))*\
            (self.x[-1]*math.cos(self.theta2[-1]) + self.y[-1]*math.sin(self.theta2[-1]))*\
            self.dt/(self.r[-1])**5)
            self.theta2.append(self.theta2[-1]+self.avelo2[-1]*self.dt)
            if self.theta1[-1] < -math.pi:
                self.theta1[-1] = self.theta1[-1] + 2*math.pi
            if self.theta1[-1] > math.pi:
                self.theta1[-1] = self.theta1[-1] - 2*math.pi
            else:
                pass
            if self.theta2[-1] < -math.pi:
                self.theta2[-1] = self.theta2[-1] + 2*math.pi
            if self.theta2[-1] > math.pi:
                self.theta2[-1] = self.theta2[-1] - 2*math.pi
            else:
                pass
            self.x.append(self.x[-1] + self.v_x[-1]*self.dt)
            self.y.append(self.y[-1] + self.v_y[-1]*self.dt)
            self.t.append(self.t[-1] + self.dt)
            self.dthe.append(abs(self.theta2[-1] - self.theta1[-1]))
    def show_results(self):
        #font = {'family': 'serif',
               #'color':  'darkred',
                #'weight': 'normal',
                #'size': 16,
                #}
        #plot,= pl.plot(self.t, self.theta1)
        #plot, = pl.plot(self.t,self.avelo1)
        plot,= pl.plot(self.t, self.dthe)
        pl.semilogy(self.t,self.dthe)
        pl.xlim(0,10)
        #pl.ylabel('$\Theta$(radians)')
        #pl.ylabel('$\omega$(radians/yr)')
        pl.ylabel('$\Delta$ $\Theta$(radians)')
        pl.xlabel('time(yr)')
        #pl.title('Hyperion $\Theta$ versus time 096')
        #pl.title('Hyperion $\omega$ versus time 096')
        pl.title('Hyperion $\Delta$ $\Theta$ versus time 096')
        pl.legend([plot,],['Circular orbit',],loc = "best")
        #pl.legend([plot,],['Elliptical orbit',],loc = "best")
        #pl.text(self.t[600], self.theta1[600],'Circular orbit', fontdict = font) 
        pl.show()
a = Hyperion(0,0.01)
a.calculate()
a.show_results()

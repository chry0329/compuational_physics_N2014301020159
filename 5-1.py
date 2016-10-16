import pylab as pl
import math
class projectile():
    def __init__(self,time_step=0.1,total_time=10,intial_velocity_x=50,\
    intial_velocity_y=50, intial_x=0,intial_y=0,mass=10,B2=0.001,B1=0.001):
        self.v_x=[intial_velocity_x]
        self.v_y=[intial_velocity_y]
        self.v=[math.sqrt(pow(intial_velocity_x,2)+pow(intial_velocity_y,2))]
        self.x=[intial_x]
        self.y=[intial_y]
        self.dt=time_step
        self.time=total_time
        self.m=mass
        self.B2=B2
        self.B1=B1
        self.intial_velocity_x=intial_velocity_x
        self.intial_velocity_y=intial_velocity_y
    def run(self):
        _time=0
        while(_time<self.time):
            self.v.append(math.sqrt(pow(self.v_x[-1],2)+pow(self.v_y[-1],2)))
            self.v_x.append(self.v_x[-1]-(self.B2/self.m)*self.v[-1]*self.dt*self.v_x[-1])
            self.x.append(self.v_x[-1]*self.dt+self.x[-1])
            self.v_y.append(self.v_y[-1]-10*self.dt-(self.B1/self.m)*self.v[-1]*self.dt*self.v_y[-1])
            self.y.append(self.v_y[-1]*self.dt+self.y[-1])
            _time+=self.dt
    def show_results(self):
        pl.plot(self.x,self.y,label='angle is %f'%(math.atan(self.intial_velocity_y/self.intial_velocity_x)*180/math.pi))
        pl.ylim(0,)
        pl.title('With resistance')
        pl.show
        pl.legend()
a=projectile()
a.run()
a.show_results()

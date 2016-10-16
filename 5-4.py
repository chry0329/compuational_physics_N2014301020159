#For the calculation of graviety we use the formula:g(h)=\frac{GM}{(h+re)^{2}} to
#calculate,G means the gravational constant,M means the mass of sun,re is the raius of earth#
#For convenience,GM=4.03^10^13,re=6.371*10^6#
#Replace g=10 with g=(4.03*pow(10,14)/pow((self.y[-1]+6.371*pow(10,6)),2))#
import pylab as pl
import math
class projectile():
    def __init__(self,time_step=0.1,total_time=10,intial_velocity_x=50,\
    intial_velocity_y=50, intial_x=0,intial_y=1,mass=10,B2=0.001,B1=0.001,F_0=5,alpha=2.5,a=0.0025,T_0=273):
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
        self.F_0=F_0
        self.alpha=alpha
        self.a=a
        self.T_0=T_0
        self.intial_velocity_x=intial_velocity_x
        self.intial_velocity_y=intial_velocity_y
    def run(self):
        _time=0
        while(_time<self.time):
            self.v.append(math.sqrt(pow(self.v_x[-1],2)+pow(self.v_y[-1],2)))
            self.v_x.append(self.v_x[-1]-\
            (self.B2/self.m)*self.v[-1]*self.dt*self.v_x[-1]-\
            self.F_0*pow(1-self.a*self.y[-1]/self.T_0,self.alpha)*self.dt*self.v_x[-1]/(self.m*self.v[-1]))
            self.x.append(self.v_x[-1]*self.dt+self.x[-1])
            self.v_y.append(self.v_y[-1]-(4.03*pow(10,14)/pow((self.y[-1]+6.371*pow(10,6)),2))*self.dt-\
            (self.B1/self.m)*self.v[-1]*self.dt*self.v_y[-1]-\
             self.F_0*pow(1-self.a*self.y[-1]/self.T_0,self.alpha)*self.dt*self.v_y[-1]/(self.m*self.v[-1]))#isothermal term#
            self.y.append(self.v_y[-1]*self.dt+self.y[-1])
            _time+=self.dt
    def show_results(self):
        pl.plot(self.x,self.y,label='angle is %f'%(math.atan(self.intial_velocity_y/self.intial_velocity_x)*180/math.pi))
        pl.ylim(0,)
        pl.title('With resistance,gravity and adiabatic altitude effect. ')
        pl.legend()
        pl.show
a=projectile()
a.run()
a.show_results()

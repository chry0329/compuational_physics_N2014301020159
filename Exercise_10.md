# Abstract
  From the prsent chapter we will consider several problems that arises in the study of plantery motion.We firstly begin with the simplest situation where a sun and a single planet get moved with interaction.We investigate a few of the properities of this model solar system.The very firts thing that we would like to investigate is the Kepler' laws of motion.Additionally,the inverse-square law and the stability of plantery orbits will be discussed.In the end,we will study the precession of the perihelion of Mercury. 

# Background

  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-1.jpg)

  万有引力定律是伟大科学家牛顿致力二十多年研究的结果，他从苹果落地开始思考，直到星际间的运动，总结出物体之间的作用规律，最后发表于1687年。他是在开普勒、第谷研究得出了行星运动规律的基础上，总结并推广到任何物体之间存在相互作用的引力，宣告天上和地下的万物都遵循同一条规律，彻底否定了宗教势力的天上地下不同的思想。这是人类认识史上的一次飞跃，牛顿应用万有引力成功地解释了潮汐现象，接着海王星、冥王星的发现进一步证实了万有引力定律的正确性、万有引力定律的创立，使天上的运动和地面上的运动统一在一起，揭开了神秘宇宙的第一层面纱，为人类认识宇宙、了解自然迈开了第一步。

  关于两定律中距离平方是否可靠的问题。平方反比定律是否会出现偏差？即r的指数是否一定等于2，这是目前科学家关心的问题。如果万有引力的指数有偏差，则会引起力场的高斯定理不成立等一系列问题，是与我们所学的知识背道而弛的，这些基本物理规律被破坏当然不可能想象。譬如说，现在如果有人宣布r的指数比2略大或者略小，哪怕只是一丁点儿，物理学则可能重新被修改。
# Main body & Conclusion
  [一.Simulation of elliptical orbit]()
  
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-1.py)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-2.png)
  
  1.For β=2.00, this is a normal elliptical with the Sun in one point. 
  
  2.Ghange β, observe the difference between different β.
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-3.png)
  
  When β is close to 2,the trajectory nears the elliptical,However,with β increasing gradually,the difference between its orbit and elliptical amplifies.To a degree,the trajectory is much different from the elliptical 
  
  [二.Simulation of the precession of Mercury]()
  
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-2.py)
  
  α=0.01 and 0.0008
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-4.png)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-5.png)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-6.png)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-7.png)
  
  The lines drawn from the Sun to the orbit show the orientation of the long axis of the ellipse. 
  
  [三.Orbit orientation versus time]() 
  
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-3.py)
  
  α=0.01 and 0.0008
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-8.png)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-9.png)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-10.png)
  
  From the figure,we can see that the precession angle θ varies linearly with time.This means that theprecession rate is a constant.
 
  Next,we calculate dθ/dt,is the slope of the line.
  
  We would like to choose a line that comes as close as possible to all of the points
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-11.png)
  
  obtain the slope:k=11296.7052527 and intercept a=-0.5
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/10-12.png)
  
  alope 11338.3567789 intercept -0.545998755352

# Acknowledgement
  Thanks to ZZT & LJJ！

# 摘要
  3.12 3.13 3.14题
# 背景介绍
  混沌是指确定性动力学系统因对初值敏感而表现出的不可预测的、类似随机性的运动，动力学系统的确定性是一个数学概念，指系统在任一时刻的状态被初始状态所决定。虽然根据运动的初始状态数据和运动规律能推算出任一未来时刻的运动状态，但由于初始数据的测定不可能完全精确，预测的结果必然出现误差，甚至不可预测。运动的可预测性是一个物理概念。一个运动即使是确定性的，也仍可为不可预测的，二者并不矛盾。牛顿力学的成功，特别是它在预言海王星上的成功，在一定程度上产生误解，把确定性和可预测性等同起来，以为确定性运动一定是可预测的。20世纪70年代后的研究表明，大量非线性系统中尽管系统是确定性的，却普遍存在着对运动状态初始值极为敏感、貌似随机的不可预测的运动状态——混沌运动
# 正文
  将能量耗散、外力驱动和非线性同时纳入考虑范围，物理摆的运动方程如下
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-1.png)
  
  [代码1](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-1.py)
  
  选择一个初始角度差为0.001的混沌摆，考察它在F=1.2与F=0.5的情况下角度之差的变化规律，利用python进行相关运算
 
  F=1.2时：
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-2.png)
  
  F=0.5时：
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-3.png)
  
  [代码2](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-2.py)
  
  F=1.2，且相位差为π/2时：
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-4.png)
  
  F=1.2，且相位差为π/4时：
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-5.png)
  
  则有：
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-6.png)

  [代码3](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-3.py)
 
  阻尼系数轻微变化(q=0.51)
  
  F=1.2时：
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-7.png)
  
  F=0.5时：
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/7-8.png)
  
# 结论
  F=1.2时：混沌现象较为明显，系统对阻尼，初始相位等条件比较敏感，初始条件的细微变化即能使结果完全不同
 
  F=0.5时：混沌现象却不这么明显
# 致谢
  感谢段俊磊同学提供的帮助！

# 摘要
  同时考虑空气阻力和密度的影响，计算不同角度下的炮弹运动轨迹，并找到能使炮弹飞得最远的初始角度。
# 背景介绍
  忽略空气阻力时，炮弹的运动方程由牛顿第二定律给出：

 　　　　 

 若考虑空气阻力，炮弹受到阻力：



使用欧勒法，有

 　　　　　　　　 

 　　　　 

 其中，

 　  　　　 

 由于炮弹通常在高空中运行，从地面到高空空气密度的变化较大，需考虑此项影响。此时，空气阻力变为：



 空气密度随高度的变化公式：

 
# 正文
  代码：[Decay Problem](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/Decay%20Problem.py)
  
  1.当Na=100，Nb=0时
    ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/result%200-100.png)
    
  2.当Na=100，Nb=20时
    ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/result%2020-100.png)
    
  3.当Na=80，Nb=20时
    ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/result%2020-80.png)
# 结论
  由图可知，不管Na与Nb取何值，其衰变终将稳定在(Na+Nb)/2附近
# 致谢
  感谢段俊磊同学提供的帮助！

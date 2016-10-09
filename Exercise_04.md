# 摘要
  Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are
  ![1](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/problem.png)
  where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equation for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc, and take tau=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.
# 背景介绍
  应用matplotlib实现decay problem的进行过程以得到结论
# 正文
  [代码](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/Decay%20Problem.py)
  1.当Na=100，Nb=0时
    ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/result%200-100.png)
  2.当Na=100，Nb=20时
    ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/result%2020-100.png)
  3.当Na=80，Nb=20时
    ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/result%2020-80.png)
# 结论
  由图可知，不管Na与Nb取何值，其最终将稳定在(Na+Nb)/2附近
# 致谢
  感谢胡塾绪同学提供的帮助！

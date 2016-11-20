# Abstract
  Question 3.30
  Investigate the Lyapunov exponent of the stadium billiard for several values of α. You can do this qualitatively by examining the behavior for only one set of initial conditions for each value of α you consider, or more quantitatively by averaging over a range of initial conditions for each value of α.
# Background
  Lorentz was studying the basic equations of fluid mechanics, which are known as the Navier-Stokes equations and which can be regarded as Newton’s law written in a form appropriate to a fluid. The specific situation he considered was the Rayleigh-Benard problem, which concerns a fluid in a container whose top and bottom surfaces are held at different temperatures. Indeed, he grossly simplified the problem as he reached to the so-called Lorentz equations, or equivalently, the Lorentz model, which provided a major contribution to the modern field of physics.
# Main body
  [The Lorenz model]
  we have a variable in Lorentz model, projection of the trajectory can be considered.
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-1.png)
  
  Though we can predict something from the phase-space plot, we would like to have more than hints. Hence, while the time-dependent behavior is unpredictable, we can predict with certainty that the system will be found somewhere on the attractor surface in phase space.
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-1.py)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-2.jpg)
  
  [Question 3.30]
  First, we consider a quite simple model-the motion of a billiard on a square table. The billiard started at point (0.2, 0). Specific parameters are shown in my code.
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-2.py)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-3.jpg)
  
  But, when we consider another table, what will change? For example, If the table is circular table, the result will be beautiful and amazing!
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-3.py)

  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-4.png)
  
  However, if we cut the table along the x axis, and pull the two semicircular halves apart (along y), a distance 2α r, the trajectory will be definitely not symmetric.
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-4.py)

  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-5.png)
  
  Phase-space plots for the trajectories of α=0, 0.001, 0.01, 0.1 shown in the figure below.
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-5.py)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-6.png)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-7.png)
  
  Now, we have enough knowdgeable to finish the first question-3.30. Here, the initial separation of the billiards was 0.00001.
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-6.py)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/9-8.png)

# Conclusion
  When we plot it in phase space, The figure 1 gives some hints of an underlying regularity.
  We see from the figure that even though the behavior is strongly chaotic, there is a very high degree of regularity in the phase-space trajectory.
  From figure 3., we can predict this kind of motion easily.
  The trajectories are always highly symmetric,
  This motion is quite regular.
  In fact, figure 5 reminds us of chaotic motion.
  When α=0, it is a nonchaotic system. However, for the α is not equal to 0, it is indeed chaotic.
# Acknowledgement
  Thanks to TS！

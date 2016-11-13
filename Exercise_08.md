# Abstract
  We have seen that at low driving forces the damped, nonlinear pendulum exhibits simple oscillatory motion, while at high drive it can be chaotic. However, when we consider this question again, the question must come out, that is, exactly how does the transition from simple to chaotic behavior take place? This is the main problem that we will deal with in the following content.
# Background
  Calculate Poincare section for the pendulum as it undergoes the period-doubling route to chaos. Plot ω versus θ, with one point plotted for each drive cycle, as in Figure 3.9. Do this FD=1.4,1.44,1.465, using the other parameters as given in connection with Figure 3.10. You should find that after removing the points corresponding to the initial transient the attractor in the period-1 regime will contain only a single point. Likewise, if the behavior is period n, the attractor will contain n discrete points.
# Main body
  We are going to introduce examples of Poincare section. 
  Bifurcation diagram is very helpful to analyze the transition to chaos. It can show us lines for θ as a function of drive amplitude, which was constructed in the following manner. For each value of FD we have calculated θ as a function of time. After waiting for 300 driving periods so that the initial transients have decayed away, we plotted θ at times that were in phase with the driving force as a function of FD. Here we plotted points up to the 428th driving period.
  After that, we can calculate the Feigenbaum δ parameter through following formula:

  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/8-1.png)
  
  In theory, whencmd-markdown-logo levels off to infinity, δ=4.669.
  
  [code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/Exercise_08.py)
  
  FD=1.4:
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/8-2.jpg)
  
  FD=1.465:
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/8-3.png)
  
# Conclusion
  Conclusion: from figure, it quite easy find that after removing the points corresponding to the initial transient the attractor in the period-1 regime will contain only a single point. Likewise, if the behavior is period , the attractor will contain discrete points.
# Acknowledgement
  Thanks to ZYF！

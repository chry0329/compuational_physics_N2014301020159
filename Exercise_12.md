# Abstract
  This article will solve the electric potential and electric field of figure 5.7 and compare 3 different methods to solve this problem.
# Background
  In regions of space that don't contain any electric charges,the electric potential obeys Laplace's equation
  
  ΔV=0
  
  or![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-1.jpg)

  This is partial differential equation (PDE).To solve this equation, we will use relaxation method.
# Main body
  When boundary condition is given as shown in following figure: 
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-2.png)
  
  We can solve the distribution of electric potential by numerical method:
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-3.png)
  
  For two dimensional problem, Laplace's equation can be written as
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-4.png)
  
  Different method:
  
  Jacobi method[code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-1.py):
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-5.png)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-6.png)
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-7.png)
  
  Gauss-Seidel method:
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-8.png)
  
  Simultaneous over-relaxation method (SOR method)[code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-2.py):
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-9.png)
  
  The best choice for α is：![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-10.png)
  
  Comparison：
  
  Next, I use this porgram to obtain the data which describes the relationship between numbers of iterations and L.[code](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-3.py)
  
  The comparison of 3 different methods at the same accuracy: 
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-11.png)
  
  We can see that under the same L, the convergent speeds of SOR method is faster than SOR method, which is faster than that of Jacobi method. (The smaller number of iterations is, the faster convergent speed is.) 
  
  Jacobi method
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-12.png)
  
  Fit equation:
  
  N=a*L^2
  
  a=0.2849
  
  R^2=0.9834
  
  The number of iterations N is about proportional to L^2
  
  SOR method
  
  ![](https://github.com/chry0329/compuational_physics_N2014301020159/blob/master/12-13.png)
  
  Fit equation:
  
  N=a*L
  
  a=1.531
  
  R^2=0.9949
  
  The number of iterations N is approximately proportional to L
# Conclusion
  I solved the electric potential and field of exercise 5.7.
  
  Comparing 3 different methods, the convergent speeds:SOR method > GS method > Jacobi method.
  
  At the same accuracy, using Jacobi method, the number of iterations N is about proportional to L^2;while using SOR method, the number of iterations N is about proportional to L.
# Acknowledgement
  Thanks to GX！

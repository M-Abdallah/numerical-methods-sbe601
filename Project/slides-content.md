class: center, middle

# Numerical solution for Schrodinger equation

---

# Agenda

1. Introduction to Schrodinger Equation
--

2. Biomedical applications for S.E
--

3. Different approaches to solve the S.E
--

---

# Introduction to Schrodinger Equation

Erwin Schrodinger derived the equation in 1925, he was trying to come up with an equation to explain the motion of particles in the Quantum Realm.
--

$$
\imath \hbar \frac{\partial}{\partial t} \vert \psi (r,t)\rangle = [ \frac{-\hbar}{2\mu} \nabla^2+ V(r,t) ]\vert \psi(r,t)\rangle 
$$
--

This describes the quantum state of a particle bounded by specific potential field.
---

An example for the S.E solution is at potential = 0, simply the free-particle equation 
--

$$
\imath \hbar \frac{\partial}{\partial t} \vert \psi (r,t)\rangle = \frac{-\hbar}{2\mu} \nabla^2 \vert \psi(r,t)\rangle 
$$
--

![S.E at V=0](../images/wave-v0.gif)
---

# Biomedical applications for S.E

The scientists who work in nanotechnology  use S.E in various applications
1. The motion of electrons in nanotubes
2. Quantum dots and its light frequencies 

---
# Different approaches to solve it

We will study differnet approaches to solve it

1. Crank-Nicolson Method
2. Finite difference
--

We are planning to implement the solution using Python  
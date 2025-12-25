# Damped Simple Pendulum Simulation (Python + Tkinter)

This project is a physics-based simulation of a **damped simple pendulum**, built using **Python and Tkinter**.  
It demonstrates how analytical models of mechanical systems can be translated into animated, observable motion.

The goal is not visual flair, but **clarity of modelling, computation, and system behaviour**.

---

## 📐 Physical Model

The pendulum is modelled using the **small-angle approximation** with linear damping:

\[
\ddot{\theta} + 2\beta \dot{\theta} + \frac{g}{L}\theta = 0
\]

Where:
- \( \theta \) = angular displacement (rad)
- \( L \) = pendulum length (m)
- \( g \) = gravitational acceleration (9.81 m/s²)
- \( \beta \) = damping coefficient (s⁻¹)

For the underdamped case, the analytical solution is:

\[
\theta(t) = \theta_0 e^{-\beta t}\cos(\omega_d t)
\]

with damped angular frequency:

\[
\omega_d = \sqrt{\frac{g}{L} - \beta^2}
\]

---

## 🎛 User Inputs

The simulation allows the user to specify:
- **Pendulum length (L)** in metres  
- **Initial angular displacement (θ₀)** in degrees  
- **Damping coefficient (β)** in s⁻¹  

From these inputs, the program computes:
- Natural frequency  
- Damped frequency  
- Time-varying angular motion  

---

## 🖥 Simulation Features

- Real-time Tkinter animation  
- Physics-driven motion (not scripted animation)  
- Exponential decay of oscillation amplitude  
- Clear separation between model, computation, and rendering  

---

## 🛠 Tools Used

- **Python**
- **Tkinter** (GUI & animation)
- **Math / analytical modelling**

No external libraries are required.

---

## 🚀 How to Run

1. Clone the repository
2. Ensure Python 3 is installed
3. Run:

```bash
python pendulum.py

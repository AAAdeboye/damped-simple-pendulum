import tkinter as tk
import math
import time

# ------------------ Constants ------------------
g = 9.81  # gravity (m/s^2)
PIXELS_PER_METER = 150


class PendulumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Damped Simple Pendulum Simulation")

        # Canvas
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.grid(row=0, column=0, rowspan=7)

        # Inputs
        tk.Label(root, text="Length L (m):").grid(row=0, column=1, sticky="w")
        self.length_entry = tk.Entry(root)
        self.length_entry.insert(0, "1.0")
        self.length_entry.grid(row=0, column=2)

        tk.Label(root, text="Initial Angle θ₀ (deg):").grid(row=1, column=1, sticky="w")
        self.angle_entry = tk.Entry(root)
        self.angle_entry.insert(0, "20")
        self.angle_entry.grid(row=1, column=2)

        tk.Label(root, text="Damping β (1/s):").grid(row=2, column=1, sticky="w")
        self.damping_entry = tk.Entry(root)
        self.damping_entry.insert(0, "0.2")
        self.damping_entry.grid(row=2, column=2)

        # Outputs
        self.freq_label = tk.Label(root, text="Natural Frequency: -- Hz")
        self.freq_label.grid(row=3, column=1, columnspan=2)

        self.damped_label = tk.Label(root, text="Damped Frequency: -- Hz")
        self.damped_label.grid(row=4, column=1, columnspan=2)

        # Button
        tk.Button(root, text="Start Simulation",
                  command=self.start_simulation).grid(row=5, column=1, columnspan=2)

        # Geometry
        self.pivot = (200, 50)
        self.running = False

    # ------------------ Simulation ------------------
    def start_simulation(self):
        try:
            self.L = float(self.length_entry.get())
            theta0_deg = float(self.angle_entry.get())
            self.beta = float(self.damping_entry.get())
        except ValueError:
            return

        self.theta0 = math.radians(theta0_deg)

        self.omega_n = math.sqrt(g / self.L)
        self.omega_d = math.sqrt(max(0, self.omega_n**2 - self.beta**2))

        self.freq_label.config(
            text=f"Natural Frequency: {self.omega_n / (2*math.pi):.3f} Hz")
        self.damped_label.config(
            text=f"Damped Frequency: {self.omega_d / (2*math.pi):.3f} Hz")

        self.start_time = time.time()
        self.running = True
        self.animate()

    def animate(self):
        if not self.running:
            return

        t = time.time() - self.start_time

        theta = self.theta0 * math.exp(-self.beta * t) * math.cos(self.omega_d * t)

        x = self.pivot[0] + self.L * PIXELS_PER_METER * math.sin(theta)
        y = self.pivot[1] + self.L * PIXELS_PER_METER * math.cos(theta)

        self.canvas.delete("pendulum")

        # Rod
        self.canvas.create_line(
            self.pivot[0], self.pivot[1], x, y,
            width=2, tags="pendulum")

        # Bob
        r = 10
        self.canvas.create_oval(
            x - r, y - r, x + r, y + r,
            fill="blue", tags="pendulum")

        self.root.after(16, self.animate)


# ------------------ Run ------------------
root = tk.Tk()
app = PendulumApp(root)
root.mainloop()

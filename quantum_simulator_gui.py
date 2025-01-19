import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# Initialize the quantum state |0⟩
def init_state():
    return np.array([1, 0])  # |0⟩ state

# Apply a quantum gate to a quantum state
def apply_gate(state, gate):
    return np.dot(gate, state)

# Define some common quantum gates (Hadamard, Pauli-X)
H = 1/np.sqrt(2) * np.array([[1, 1], [1, -1]])  # Hadamard gate
X = np.array([[0, 1], [1, 0]])  # Pauli-X gate

# Measurement function (collapse the state)
def measure(state):
    probabilities = np.abs(state) ** 2  # Square of the amplitudes gives probabilities
    result = np.random.choice([0, 1], p=probabilities)
    return result

# Visualize the quantum state (simple 2D plot)
def plot_state(state):
    angles = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)
    plt.plot(x, y, label="Quantum State Evolution")
    plt.scatter(np.real(state[0]), np.imag(state[0]), color='red', label="|0⟩")
    plt.scatter(np.real(state[1]), np.imag(state[1]), color='blue', label="|1⟩")
    plt.legend()
    plt.title("Quantum State Visualization")
    plt.show()

# UI Functionality
class QuantumSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum Computing Simulator")
        
        self.state = init_state()  # Start with |0⟩ state
        
        # Create buttons and labels for the UI
        self.state_label = tk.Label(root, text="Quantum State: |0⟩", font=("Helvetica", 14))
        self.state_label.pack(pady=10)
        
        self.hadamard_button = tk.Button(root, text="Apply Hadamard Gate", command=self.apply_hadamard, font=("Helvetica", 12))
        self.hadamard_button.pack(pady=10)
        
        self.pauli_x_button = tk.Button(root, text="Apply Pauli-X Gate", command=self.apply_pauli_x, font=("Helvetica", 12))
        self.pauli_x_button.pack(pady=10)
        
        self.measure_button = tk.Button(root, text="Measure Qubit", command=self.measure_qubit, font=("Helvetica", 12))
        self.measure_button.pack(pady=10)
        
        self.visualize_button = tk.Button(root, text="Visualize Quantum State", command=self.visualize_state, font=("Helvetica", 12))
        self.visualize_button.pack(pady=10)

    def update_state_label(self):
        # Update the state label in the UI
        state_text = f"Quantum State: |{'0' if np.real(self.state[0]) > np.real(self.state[1]) else '1'}⟩"
        self.state_label.config(text=state_text)

    def apply_hadamard(self):
        self.state = apply_gate(self.state, H)
        self.update_state_label()

    def apply_pauli_x(self):
        self.state = apply_gate(self.state, X)
        self.update_state_label()

    def measure_qubit(self):
        result = measure(self.state)
        messagebox.showinfo("Measurement Result", f"Measurement outcome: |{result}⟩")
    
    def visualize_state(self):
        plot_state(self.state)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumSimulatorApp(root)
    root.mainloop()

"""
A simple 2Q model of the effect of filtering on an entangled pair of qubits affected by amplitude damping.

Task: implement 1Q case with and without the filtering on amp damp channel (applied to |+> state?) → entropy? extend to higher nQ?

Existing implementation: https://github.com/Sjd-Hz/Weak-measurement-in-IBM-Qiskit/
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import (amplitude_damping_error, NoiseModel, QuantumError, ReadoutError, pauli_error, depolarizing_error, thermal_relaxation_error)

# #Noise model: amplitude damping channel
# noise_model = NoiseModel()
# p_AD = 0.1
# error_AD = amplitude_damping_error(p_AD)
# noise_model.add_all_qubit_quantum_error(error_AD, ['id'])

# qc = QuantumCircuit(2)
# qc.h(0)
# qc.cx(0, 1)
# qc.id(0)
# qc.id(1)
# qc.measure_all()
# print(qc)

# sim = AerSimulator()
# result = sim.run(qc, noise_model=noise_model, shots=1000).result()
# counts = result.get_counts()
# print(counts)

# V2
from qiskit.quantum_info import DensityMatrix, Kraus
import numpy as np

# Entangling unitary
qc_ent = QuantumCircuit(2)
qc_ent.h(0)
qc_ent.cx(0, 1)
U_ent = Kraus(qc_ent)

# Weak measurement (filtering) operators
p1 = 0.1
p2 = 0.1
M1 = [[1, 0], [0, np.sqrt(1 - p1)]]
M2 = [[1, 0], [0, np.sqrt(1 - p2)]]


rho = DensityMatrix.from_label('00')
rho.evolve(U_ent)



# Provenance notice:
# Portions of this file are adapted from Qiskit Nature's "Ground state solvers" tutorial:
# https://github.com/qiskit-community/qiskit-nature/blob/ff222f77f78928a701268732bd1013fa9affc4cd/docs/tutorials/03_ground_state_solvers.ipynb
# Upstream copyright: Copyright 2017 IBM and its contributors
# Upstream license: Apache License 2.0
# Project-specific modifications are licensed under this repository's Apache License 2.0.
# See THIRD_PARTY_NOTICES.md for details.

from qiskit import Aer
from qiskit_nature.drivers import UnitsType, Molecule
from qiskit_nature.drivers.second_quantization import (
    ElectronicStructureDriverType,
    ElectronicStructureMoleculeDriver,
)
from qiskit_nature.problems.second_quantization import ElectronicStructureProblem
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit_nature.mappers.second_quantization import JordanWignerMapper,BravyiKitaevMapper
from qiskit.algorithms.optimizers import SLSQP
from qiskit.opflow import X, Z, I


slsqp = SLSQP(maxiter=1000)
H2 = [['H', [0., 0, 0]],['H', [0, 0, -1.5]]]
qubit_converter = QubitConverter(JordanWignerMapper())

molecule = Molecule(
    geometry=[["H", [0.0, 0.0, 0.0]], ["H", [0.0, 0.0, 0.735]]], charge=0, multiplicity=1
)
driver = ElectronicStructureMoleculeDriver(
    molecule, basis="sto3g", driver_type=ElectronicStructureDriverType.PYSCF
)

es_problem = ElectronicStructureProblem(driver)


from qiskit.providers.aer import StatevectorSimulator
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit_nature.algorithms import VQEUCCFactory

quantum_instance = QuantumInstance(backend=Aer.get_backend("aer_simulator_statevector"))
vqe_solver = VQEUCCFactory(quantum_instance)

from qiskit.algorithms import VQE
from qiskit.circuit.library import TwoLocal
from qiskit_nature.algorithms import GroundStateEigensolver

tl_circuit = TwoLocal(
    rotation_blocks='ry', entanglement_blocks='cz'
)

vqe_solver = VQE(
    ansatz=tl_circuit,
    optimizer=slsqp,
    quantum_instance=QuantumInstance(Aer.get_backend("aer_simulator_statevector")),
)

calc = GroundStateEigensolver(qubit_converter, vqe_solver)
res = calc.solve(es_problem)

print(res.groundenergy)
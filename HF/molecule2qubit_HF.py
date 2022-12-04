from openfermion.chem import MolecularData
from openfermion.transforms import get_fermion_operator, jordan_wigner
from openfermion.linalg import get_ground_state, get_sparse_operator
import numpy
import scipy
import scipy.linalg
import re

# assign numbers of bond to calculate
num = 12
# initialize bond length
diatomic_bond_length = 0
# set location of export folder
folder = ''

# generate molecule at different bond lengths.
for i in range(num):
    diatomic_bond_length = round(diatomic_bond_length+0.2 ,2)
    geometry = [('H', (0., 0., 0.)), ('F', (0., 0., diatomic_bond_length))]
    basis = 'sto-3g'
    multiplicity = 1

    # Load data. ( Notice that your data should have been stored in '\...\openfermion\testing\data' already if you had
    # previously computed this molecule using an electronic structure package, if it's not, you should compute the molecule first
    # using electronic structure packages like Psi4 (https://github.com/quantumlib/OpenFermion-Psi4) or PySCF (https://github.com/quantumlib/OpenFermion-PySCF) )
    molecule = MolecularData(geometry, basis, multiplicity, description=str(diatomic_bond_length) )
    molecule.load()

    # get the Hamiltonian in an active space.
    molecular_hamiltonian = molecule.get_molecular_hamiltonian(
        occupied_indices=range(1),
        active_indices=range(1,5))

    # map operator to fermions and qubits.
    fermion_hamiltonian = get_fermion_operator(molecular_hamiltonian)
    qubit_hamiltonian = jordan_wigner(fermion_hamiltonian)
    qubit_hamiltonian.compress()
    # print('The Jordan-Wigner Hamiltonian in canonical basis follows:\n{}'.format(qubit_hamiltonian))

    # get sparse operator and ground state energy.
    sparse_hamiltonian = get_sparse_operator(qubit_hamiltonian)
    energy, state = get_ground_state(sparse_hamiltonian)
    # print('Ground state energy before rotation is {} Hartree.\n'.format(energy))

    # export calculated ground state energy and qubit-encoded hamiltonian to txt files
    filepath = folder + "HF_bond" + str(diatomic_bond_length) + '.txt'
    file = open(filepath, 'w')
    file.write('Ground state energy is {} Hartree.\t'.format(energy))
    file.write('\n') 
    file.write(str(qubit_hamiltonian))
    file.close()

    # set the regex of coefficients and gates
    filecontent = str(qubit_hamiltonian)
    coeffRegex = re.compile(r'\d.*\d\d|-\d.*\d\d')
    gateRegex = re.compile(r'\[.*\d\]')

    # store the collected coefficients and gates
    coefficient = coeffRegex.findall(filecontent)
    gate = gateRegex.findall(filecontent)

    # export collected coefficients and gates to txt files
    save_coeffient = open('coefficient_'+filepath, 'w')
    save_coeffient.write('\n'.join(coefficient))
    save_coeffient.close()
    save_gate = open('gate_'+filepath, 'w')
    save_gate.write('\n'.join(gate))
    save_gate.close()
   
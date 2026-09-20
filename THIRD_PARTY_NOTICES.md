# Third-Party Notices

This repository contains both project-original code and third-party or derived material. The top-level Apache License 2.0 applies to project-original material unless otherwise noted. Third-party material retains its upstream copyright and license terms.

## Paulihedral-derived benchmark material

Parts of `Benchmarks/benchmark/` and `Benchmarks/data/` originate from the artifact accompanying:

Gushu Li et al., **"Paulihedral: A Generalized Block-Wise Compiler Optimization Framework For Quantum Simulation Kernels,"** ASPLOS 2022.

- Paper: https://arxiv.org/abs/2109.03371
- Artifact DOI: https://doi.org/10.5281/zenodo.5780204
- Upstream license: **Apache License 2.0**

Confirmed examples include:

- `Benchmarks/benchmark/mypauli.py`
- multiple files under `Benchmarks/data/`

These files retain the upstream Paulihedral copyright and Apache-2.0 terms.

## OpenFermion-derived examples

The molecular Hamiltonian-generation scripts below contain code adapted from or based on OpenFermion examples:

- `H2/molecule2qubit_H2.py`
- `HF/molecule2qubit_HF.py`
- `LiH/molecule2qubit_LiH.py`

OpenFermion is distributed under the **Apache License 2.0**:

- Upstream repository: https://github.com/quantumlib/OpenFermion
- License: https://github.com/quantumlib/OpenFermion/blob/main/LICENSE

Adapted portions remain subject to the upstream Apache-2.0 terms and attribution requirements.


## Qiskit Nature-derived VQE example

`demovqe.py` contains code adapted from the Qiskit Nature ground-state solver tutorial, including the H2 molecular setup, `ElectronicStructureMoleculeDriver` workflow, `VQEUCCFactory` example, and `GroundStateEigensolver` usage.

A historical upstream version predating this repository's copy is:

- Upstream project: **Qiskit Nature**
- Upstream file: `docs/tutorials/03_ground_state_solvers.ipynb`
- Historical revision: `ff222f77f78928a701268732bd1013fa9affc4cd`
- Source: https://github.com/qiskit-community/qiskit-nature/blob/ff222f77f78928a701268732bd1013fa9affc4cd/docs/tutorials/03_ground_state_solvers.ipynb
- Upstream copyright: Copyright 2017 IBM and its contributors
- Upstream license: **Apache License 2.0**
- License source: https://github.com/qiskit-community/qiskit-nature/blob/ff222f77f78928a701268732bd1013fa9affc4cd/LICENSE.txt

The adapted upstream portions of `demovqe.py` remain subject to the Qiskit Nature Apache-2.0 terms. Project-specific modifications in this repository are also made available under Apache License 2.0.

## Project-original material

Other project-specific benchmark-generation, processing, and organization code authored for this repository is licensed under the repository's Apache License 2.0 unless otherwise noted.

Generated numerical scientific results should retain provenance where known; their presence in this repository should not be interpreted as changing the copyright or license of upstream software used to generate them.

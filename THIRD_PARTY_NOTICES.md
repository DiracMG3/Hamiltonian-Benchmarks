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

## Project-original material

Other project-specific benchmark-generation, processing, and organization code authored for this repository is licensed under the repository's Apache License 2.0 unless otherwise noted.

Generated numerical scientific results should retain provenance where known; their presence in this repository should not be interpreted as changing the copyright or license of upstream software used to generate them.

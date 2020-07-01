# Basic Ocean Programs

This folder contains examples of basic Ocean programs written for problems
formulated as either a QUBO or Ising model.

## Basic QUBO Program

The file `general_program_qubo.py` provides a basic Ocean program that runs a
QUBO problem on the D-Wave QPU. In this example we use Ocean's
`EmbeddingComposite` to determine the best placement of our problem onto the
physical hardware.

Program Characteristics:

- Model: QUBO
- Sampler: `DWaveSampler` with `EmbeddingComposite`

Optimal Solutions:

- A = 1, B = 0, C = 0, K = 1; Energy: -1.0
- A = 0, B = 1, C = 1, K = 0; Energy: -1.0

## Basic Ising Program

The file `general_program_ising.py` provides a basic Ocean program that runs an
Ising version of the QUBO problem on the D-Wave QPU. In this example we use
Ocean's `EmbeddingComposite` to determine the best placement of our problem
onto the physical hardware.

Program Characteristics:

- Model: Ising
- Sampler: `DWaveSampler` with `EmbeddingComposite`

Optimal Solutions:

- A = +1, B = -1, C = -1, K = +1; Energy: -1.5
- A = -1, B = +1, C = +1, K = -1; Energy: -1.5

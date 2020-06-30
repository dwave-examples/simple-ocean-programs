# Exploring BQM Functionality

## Basic BQM Program

The file `general_program_bqm.py` provides a basic Ocean program that creates a BQM from the QUBO problem and runs it on the D-Wave QPU. In this example we use Ocean's `EmbeddingComposite` to determine the best placement of our problem onto the physical hardware.

Program Characteristics:

- Model: BQM (from QUBO)
- Sampler: `DWaveSampler` with `EmbeddingComposite`

Optimal Solutions:

- A = 1, B = 0, C = 0, K = 1; Energy: -1.0
- A = 0, B = 1, C = 1, K = 0; Energy: -1.0

Note that we could use a similar BQM functionality to create a BQM model in Ocean from the Ising model for our problem.

## Converting a BQM

The file `bqm_conversion.py` provides a basic Ocean program that takes our BQM created in `general_program_bqm.py`, converts the problem to an Ising model, and then runs the Ising problem on the D-Wave QPU.

Program Characteristics:

- Model:  Ising (from BQM from QUBO)
- Sampler: `DWaveSampler` with `EmbeddingComposite`

Optimal Solutions:

- A = +1, B = -1, C = -1, K = +1; Energy: -1.5
- A = -1, B = +1, C = +1, K = -1; Energy: -1.5

# Exploring BQM Functionality

## Basic BQM Program

The file `general_program_bqm.py` provides a basic Ocean program that creates a BQM from the QUBO problem and runs it on the D-Wave QPU. In this example we use Ocean's `EmbeddingComposite` to determine the best placement of our problem onto the physical hardware.

Program Characteristics:

- Model: BQM (from QUBO)
- Sampler: `DWaveSampler` with `EmbeddingComposite`

Optimal Solutions:

- A = 1, B = 0, C = 0, K = 1; Energy: -1.0
- A = 0, B = 1, C = 1, K = 0; Energy: -1.0

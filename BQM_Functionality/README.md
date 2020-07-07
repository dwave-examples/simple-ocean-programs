# Exploring BQM Functionality

The Ocean SDK provides a [binary quadratic model](https://docs.ocean.dwavesys.com/projects/dimod/en/stable/reference/bqm/) (BQM) structure for storing and
submitting problems to the quantum processing unit (QPU).

## Basic BQM Program

The file `general_program_bqm.py` provides a basic Ocean program that creates
a BQM from the QUBO problem and runs it on the D-Wave QPU. In this example we
use Ocean's `EmbeddingComposite` to determine the best placement of our problem
onto the physical hardware.

Program Characteristics:

- Model: BQM (from QUBO)
- Sampler: `DWaveSampler` with `EmbeddingComposite`

Optimal Solutions:

- A = 1, B = 0, C = 0, K = 1; Energy: -1.0
- A = 0, B = 1, C = 1, K = 0; Energy: -1.0

Note that we could use a similar BQM functionality to create a BQM model in
Ocean from the Ising model for our problem.

## Converting a BQM

The file `bqm_conversion.py` provides a basic Ocean program that takes our BQM
created in `general_program_bqm.py`, converts the problem to an Ising model,
and then runs the Ising problem on the D-Wave QPU.

Program Characteristics:

- Model:  Ising (from BQM from QUBO)
- Sampler: `DWaveSampler` with `EmbeddingComposite`

Optimal Solutions:

- A = +1, B = -1, C = -1, K = +1; Energy: -1.5
- A = -1, B = +1, C = +1, K = -1; Energy: -1.5

## Using Offsets in a BQM

The Ising and QUBO problems that we ran earlier provide the same partition of
variables in both programs.  The optimal solutions in both programs partition
our variables into the sets {A, K} and {B, C}.  However, the minimum energy
value differs between QUBO and Ising due to constants in the problem
formulations.  Within a BQM model in Ocean we can use the offset feature to add
in this constant to see consistent energy values for optimal solutions between
the two models.

Program Characteristics:

- Models: BQM (QUBO) and BQM (Ising)
- Sampler: `DWaveSampler` with `EmbeddingComposite`

Optimal QUBO Solutions:

- A = 1, B = 0, C = 0, K = 1; Energy: 0.0
- A = 0, B = 1, C = 1, K = 0; Energy: 0.0

Optimal Ising Solutions:

- A = +1, B = -1, C = -1, K = +1; Energy: 0.0
- A = -1, B = +1, C = +1, K = -1; Energy: 0.0

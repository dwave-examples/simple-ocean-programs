# intro-to-ocean

This repository provides examples of introductory Ocean programs and concepts.  Many of the problems that these examples are created from in this repository are explored in our guide, ["Learning to Formulate Problems"](https://docs.dwavesys.com/docs/latest/c_pf_3.html#social-networks-friends-and-enemies).

## Basic QUBO Program

The file `general_program_qubo.py` provides a basic Ocean program that runs a QUBO problem on the D-Wave QPU. In this example we use Ocean's `EmbeddingComposite` to determine the best placement of our problem onto the physical hardware.

Program Characteristics:

- Model: QUBO
- Sampler: `DWaveSampler` with `EmbeddingComposite`

Optimal Solutions:

- A = 1, B = 0, C = 0, K = 1; Energy: -1.0
- A = 0, B = 1, C = 1, K = 0; Energy: -1.0
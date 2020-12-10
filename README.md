[![Linux/Mac/Windows build status](
  https://circleci.com/gh/dwave-examples/simple-ocean-programs.svg?style=svg)](
  https://circleci.com/gh/dwave-examples/simple-ocean-programs)

# Simple Ocean Examples

This repository provides examples of introductory Ocean programs and concepts.
Many of the problems that these examples are created from in this repository
are explored in our guide, ["Learning to Formulate Problems"](https://docs.dwavesys.com/docs/latest/c_pf_3.html#social-networks-friends-and-enemies).  This guide
discusses how to formulate problems as a binary quadratic model, or BQM, as
required by the Ocean SDK.

## Basic Programs

In the `Basic_Programs` folder are programs to demonstrate the basic usage of
the Ocean SDK to run QUBO and Ising problems on the D-Wave quantum processing
unit (QPU).

## BQM Functionality

In the `BQM_Functionality` folder are programs that demonstrate the
functionality of the binary quadratic model (BQM) structure within Ocean.
Using BQMs we can translate seamlessly between QUBO and Ising models, and
provide offsets for any constants in our models.

## Exploring Pegasus

In the `Exploring_Pegasus` folder are programs which explore the 
Pegasus topology and the Advantage QPU.

## Pegasus Embedding Video

In the `Pegasus_Embedding_Video` folder are programs that were used in creating
our YouTube video showcasing the pegasus topology.  The video can be viewed at
[https://youtu.be/aAhvyxzJyQE](https://youtu.be/aAhvyxzJyQE).

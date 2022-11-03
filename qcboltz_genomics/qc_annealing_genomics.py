from dwave.system import EmbeddingComposite, FixedEmbeddingComposite, DWaveSampler
import random
import numpy as np
import os
import math as math
import statistics as stat
import dimod
import pandas
from minorminer import find_embedding

d = 8
N = 100
T = 5

for cMod in range(3):
    for cTrial in range(5):

      if cMod==1:
        fname = "/workspace/simple-ocean-programs/qcboltz_genomics/params/params_qboltz_" + str(cTrial) + ".csv"
      if cMod==2:
        fname = "/workspace/simple-ocean-programs/qcboltz_genomics/params/params_hqboltz_" + str(cTrial) + ".csv"
      if cMod==3:
        fname = "/workspace/simple-ocean-programs/qcboltz_genomics/params/params_hqboltz_aux_" + str(cTrial) + ".csv"

      params = np.loadtxt(open(fname, "rb"), delimiter=",", skiprows=0)

      for n in range(N):   

        s_star = params[0,n]
        h = {}
        for i in range(d):
            h[i] = params[1+i,n]*T/2
            h[i] = params[1+i,n]
        gamma = {}
        for i in range(d):
            gamma[i] = T*(math.exp((params[1+d+i,n]**2)))
        J = {}
        c = 0
        for i in range(d):
            for j in range(i+1,d):
                J[(i,j)] = params[1+(d*2)+c,n]*T
                J[(i,j)] = params[1+(d*2)+c,n]*2
                c = c + 1

        #print(h)
        #print(J)

        anneal_sched = [[0.0, 0.0], [50, s_star], [190, s_star], [200, 1.0]]

        qpu_chimera = DWaveSampler(solver={'topology__type': 'chimera'})

        max_units = 16*16
        reads = 5000
        nodes = {s: sorted(list(set(list(range(s, s + max_units*8, 8))) &
                           set(qpu_chimera.nodelist))) for s in h.keys()}

        embedding = find_embedding(J.keys(),
                               qpu_chimera.edgelist)                           
        sampler = FixedEmbeddingComposite(qpu_chimera, embedding)

        offset = [0]*qpu_chimera.properties['num_qubits']
        for i in range(d):
            for j in range(len(embedding[i])):
                idx = embedding[i][j]
                val = gamma[i]
                rng = qpu_chimera.properties['anneal_offset_ranges'][idx]
                if val < rng[0]:
                    offset[embedding[i][j]] = rng[0]
                elif val > rng[1]:
                    offset[embedding[i][j]] = rng[1]
                else:
                    offset[embedding[i][j]] = val


        sampleset = sampler.sample_ising(h, J, num_reads=1000)

        mat = dimod.as_samples(sampleset)
        mat = mat[0]

        df = sampleset.to_pandas_dataframe()
        #print(df)
        fout = "/workspace/simple-ocean-programs/qcboltz_genomics/samples/samples_qboltz_" + str(cTrial) + "_" + str(n) + ".csv"
        df.to_csv(fout)


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
N = 1 #10
T = 1 #5
nMod = 1 #3

for cMod in range(nMod):
    for cTrial in range(T):

      if cMod==0:
        fname = "/workspace/simple-ocean-programs/Basic_Programs/params_qboltz_" + str(cTrial+1) + ".csv"
      if cMod==1:
        fname = "/workspace/simple-ocean-programs/Basic_Programs/params_hqboltz_" + str(cTrial+1) + ".csv"
      if cMod==2:
        fname = "/workspace/simple-ocean-programs/Basic_Programs/params_hqboltz_aux_" + str(cTrial+1) + ".csv"

      params = np.loadtxt(open(fname, "rb"), delimiter=",", skiprows=0)

      for n in range(N):   

        h = {}
        for i in range(d):
            h[i] = params[i,n]*T/2
            h[i] = params[i,n]
        gamma = {}
        for i in range(d):
            gamma[i] = T*(math.exp((params[d+i,n]**2)))
        J = {}
        c = 0
        for i in range(d):
            for j in range(i+1,d):
                J[(i,j)] = params[d*2+c,n]*T
                J[(i,j)] = params[d*2+c,n]*2
                c = c + 1

        #print(h)
        #print(J)

        gamma_mu = sum(gamma.values()) / len(gamma)
        gamma_off = gamma
        gamma_off = {key: gamma[key] - gamma_mu for key in gamma.keys()}

        #print(gamma_mu)
        #print(gamma_off)
        ## for gamma_mu = 5.14, use s=0.189	A=5.13821200	B=0.73652400
        s_star = 0.189
        A = 5.13821200
        B = 0.73652400

        # rescale J and h + get anneal_sched
        h2 = {}
        for i in range(d):
            h2[i] = h[i] / (B-gamma_off[i])
        J2 = {}
        c = 0
        for i in range(d):
            for j in range(i+1,d):
                J2[(i,j)] = J[(i,j)] / (math.sqrt((B-gamma_off[i])*(B-gamma_off[j])))
                c = c + 1
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
                val = gamma_off[i]
                rng = qpu_chimera.properties['anneal_offset_ranges'][idx]
                if val < rng[0]:
                    offset[embedding[i][j]] = rng[0]
                elif val > rng[1]:
                    offset[embedding[i][j]] = rng[1]
                else:
                    offset[embedding[i][j]] = val


        sampleset = sampler.sample_ising(h, J, num_reads=1000, postprocess='sampling', beta=0.001)

        mat = dimod.as_samples(sampleset)
        mat = mat[0]

        df = sampleset.to_pandas_dataframe()
        #print(df)
        fout = "/workspace/simple-ocean-programs/Basic_Programs/samples_qboltz_" + str(cTrial+1) + "_" + str(n+1) + ".csv"
        df.to_csv(fout)



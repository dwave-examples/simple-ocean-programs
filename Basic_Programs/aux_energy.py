from dwave.system import EmbeddingComposite, FixedEmbeddingComposite, DWaveSampler
import random
import numpy as np
import os
import math as math
import statistics as stat
import dimod
import pandas
from minorminer import find_embedding

Dx = 2; # N spin
Ntrial = 500;
Ntime = 250;

delta_b = 0.4;
delta_gamma = 3;
delta_w = 0.2;

T = 4; 
K = 50;
c_off = 1; 

U = np.array([1, -0.5]) * delta_b;
V = np.array([1, 1]) * delta_w;
G = np.array([1, 1]) * delta_gamma;

Ny = 2**Dx;
Dy = Ny;
Y = np.array([[0, 0], [1, 0], [0, 1], [1, 1]]);

b_u = np.zeros([Ny,Dx]);
w_1 = np.zeros([Ny,Dx]);
w_2 = np.zeros([Ny,Dx]);
for j in range(Ny):
    b_u[j,:] = U * (1-2*Y[j,:]);
    w_1[j,:] = V * np.equal(Y[j,:],[Y[j,1], Y[j,0]]);
    w_2[j,:] = V * (1-np.equal(Y[j,:],[Y[j,1], Y[j,0]]));

B = 2;
Nbit = ((2*B) + 3) * Dx;
Nbit1 = ((2*B) + 3);
a1 = (2*B);
a2 = (2*B) + 1;
a3 = (2*B) + 2;

hs = [];
Js = [];
for i in range(Ny):
        h = np.zeros([1,Nbit]);
        J = np.zeros([Nbit,Nbit]);
        c = -np.min([b_u[i,0],b_u[i,1],0]) + c_off;
        for alpha in range(B):
            for ii in range(Dx):
                val = (2**(B-alpha-1)) * np.max([(b_u[i,ii]+c),0]);
                J[a1+Nbit1*ii,alpha+B+Nbit1*ii] = val; J[alpha+B+Nbit1*ii,a1+Nbit1*ii] = val; 
                J[a1+Nbit1*ii,alpha+Nbit1*ii] = -val; J[alpha+Nbit1*ii,a1+Nbit1*ii] = -val;
		##
                h[0,a1+Nbit1*ii] = 2*G[ii]/B; h[0,alpha+B+Nbit1*ii] += -K; h[0,alpha+Nbit1*ii] += -K;
                J[a1+Nbit1*ii,alpha+B+Nbit1*ii] = K; J[alpha+B+Nbit1*ii,a1+Nbit1*ii] = K; 
                J[a1+Nbit1*ii,alpha+Nbit1*ii] = K; J[alpha+Nbit1*ii,a1+Nbit1*ii] = K; 
		##
                val = np.max([w_2[i,ii]-w_1[i,ii],0])*(2**(B-alpha-1));
                J[a2+Nbit1*ii,alpha+Nbit1*ii] = val; J[alpha+Nbit1*ii,a2+Nbit1*ii] = val; 
                J[a2+Nbit1*ii,alpha+Nbit1*np.mod(ii+1,Dx)] = -val; J[alpha+Nbit1*np.mod(ii+1,Dx),a2+Nbit1*ii] = -val; 
		##
                J[a2+Nbit1*ii,alpha+Nbit1*np.mod(ii+1,Dx)] =-val; J[alpha+Nbit1*np.mod(ii+1,Dx),a2+Nbit1*ii] = -val; 
                J[a2+Nbit1*ii,alpha+Nbit1*ii] = val; J[alpha+Nbit1*ii,a2+Nbit1*ii] = val; 
                h[0,alpha+Nbit1*np.mod(ii+1,Dx)] +=val; 
                h[0,alpha+Nbit1*ii] += -val; 
		##
                val = np.max([w_2[i,ii]-w_1[i,ii],0])*(2**(B-alpha-1));
                J[a3+Nbit1*ii,alpha+B+Nbit1*np.mod(ii+1,Dx)] = val; J[alpha+B+Nbit1*np.mod(ii+1,Dx),a3+Nbit1*ii] = val; 
                J[a3+Nbit1*ii,alpha+B+Nbit1*ii] = -val; J[alpha+B+Nbit1*ii,a3+Nbit1*ii] = -val; 
		##
                J[a3+Nbit1*ii,alpha+B+Nbit1*ii] =-val; J[alpha+B+Nbit1*ii,a3+Nbit1*ii] = -val; 
                J[a3+Nbit1*ii,alpha+B+Nbit1*np.mod(ii+1,Dx)] = val; J[alpha+B+Nbit1*ii,a3+Nbit1*np.mod(ii+1,Dx)] = val; 
                h[0,alpha+B+Nbit1*np.mod(ii+1,Dx)] +=val; 
                h[0,alpha+B+Nbit1*ii] += -val; 
		##
                val = np.max([w_1[i,ii]-w_2[i,ii],0])*(2**(B-alpha-1));
                J[a2+Nbit1*ii,alpha+Nbit1*ii] += val; J[alpha+Nbit1*ii,a2+Nbit1*ii] += val; 
                J[a2+Nbit1*ii,alpha+B+Nbit1*np.mod(ii+1,Dx)] += -val; J[alpha+B+Nbit1*np.mod(ii+1,Dx),a2+Nbit1*ii] += -val; 
		##
                val = np.max([w_1[i,ii]-w_2[i,ii],0])*(2**(B-alpha-1));
                J[a3+Nbit1*ii,alpha+Nbit1*np.mod(ii+1,Dx)] += val; J[alpha+Nbit1*np.mod(ii+1,Dx),a3+Nbit1*ii] += val; 
                J[a3+Nbit1*ii,alpha+B+Nbit1*ii] += -val; J[alpha+B+Nbit1*ii,a3+Nbit1*ii] += -val;
		##
        hs.append(h);
        Js.append(J);


####

for i in range(Ny):
    #sampler = DWaveSampler(solver={'topology__type': 'chimera'})
    sampler = EmbeddingComposite(DWaveSampler())

    sampleset = sampler.sample_ising(hs[i][0], Js[i],
        	                         num_reads = 10) #,
                	                 #postprocess='sampling', beta=0.001)


    mat = dimod.as_samples(sampleset)
    mat = mat[0]

    df = sampleset.to_pandas_dataframe()
    print(df)
    df.to_csv("/workspace/simple-ocean-programs/Basic_Programs/aux_samples_" + str(i) + ".csv")


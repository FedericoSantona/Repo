# Config
output_filename = "../data/vmc_playground.csv"

nparticles = 4
dim = 3
nsamples =  int(2**12) #  2**18 = 262144
scale = 1 + (dim-1)*0.1
nchains = 1#4# number of Markov chains. When you parallelize, you can set this to the number of cores. Note you will have to implement this yourself.
eta = 0 #0.001
training_cycles = 0 #500 # this is cycles for the ansatz
mcmc_alg = "mh" # eiteer "mh" or "m"
backend = "numpy" # or "numpy" but jax should go faster because of the jit
optimizer = "gd"
hamiltonian = "eo" # either ho or eo 
interaction = "Coulomb" # either Coulomb or None
radius =  0.0043
batch_size = 0 # 200
detailed = True
wf_type = "vmc" 
seed = 142
alpha = 0.2
beta = 1 #2.82843


#only important for Metropolis hastings:

time_step = 0.05
diffusion_coeff = 0.5


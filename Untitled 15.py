#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
def return_matrix(arr, factor):
    x, y = factor
    mat = np.zeros((x,y), dtype=np.int64)
    for i in range(x*y):
        mat[i%x, i%y] = arr[i]
    return mat

def sequence(prime_num):
    m = np.arange(1,prime_num)
    n = np.zeros(prime_num-1, dtype=np.int64)
    for i in range(1, prime_num):
        n[i-1] = (2 ** i) % prime_num
    return n

def get_well_depth(matrix, _lambda, p):
    return matrix * (_lambda / (2 * p))

def phase_change(matrix, _lambda):
    return (2 * matrix) * ((2 * np.pi) / _lambda)

def get_lambda(fg):
    return 343/fg

def get_periods(fg, amount):
    return (1/fg) * amount

def pure_sine_wave(frequency, duration, sampling_rate, initial, periods=None):
    if periods is not None:
        duration = get_periods(frequency, periods)
    phase_change = np.arange((1/frequency) * sampling_rate, dtype=int)
    time = np.roll(np.linspace(0, duration, int(duration * sampling_rate)), -phase_change[int((phase_change.shape[0]/360)*initial)])
    sinewave = np.sin(2 * np.pi * frequency * time)
    return sinewave

def _time_delay(depth): # in sec
    return (2 * depth) / 343 # c (velocity sound) = 343

prime_num = 307
fg = 3500
_lambda = get_lambda(fg)
factor = (18,17)
seq = sequence(prime_num)
mat = matrix(seq, factor)
dep = get_well_depth(mat, _lambda, prime_num)
pac = phase_change(dep, _lambda)


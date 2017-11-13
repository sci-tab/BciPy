import numpy as np
from eeg_model.mach_learning.trial_reshaper import trial_reshaper
from helpers.load import load_txt_data


# A 3 channel dummy input
inp = np.array([range(4000)] * 3)
# Sampling frequency
fs = 256
# Downsampling ratio
k = 2

# Load trigger file
trigger_loc = load_txt_data()

# reshape function is applied to dummy data with given trigger file
arg = trial_reshaper(trigger_loc=trigger_loc, filtered_eeg=inp, fs=256, k=2)

# Print results.
print 'Reshaped trials:'
print arg[0]
print
print 'Labels:'
print arg[1]

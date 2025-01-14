import numpy as np
import pandas as pd 
import mne

path = '../EEG/EMOTIV/'
data = pd.read_csv(path + 'odball.csv', 
                   skiprows=0, usecols=[*range(0, 14)]) 
data = data.transpose()
#print(data)
ch_names = ['EEG.AF3','EEG.F7',',EEG.F3','EEG.FC5',
            'EEG.T7','EEG.P7','EEG.O1','EEG.O2','EEG.P8','EEG.T8',
                'EEG.FC6','EEG.F4','EEG.F8','EEG.AF4']

sfreq = 128 
info = mne.create_info(ch_names = ch_names, sfreq = sfreq)
raw = mne.io.RawArray(data, info)
raw.plot(block=True)

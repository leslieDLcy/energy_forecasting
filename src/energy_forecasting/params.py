"""Hyperparameters for Karl models."""

from dataclasses import dataclass

'''
    notes:

'''

@dataclass(frozen=True)  # Instances of this class are immutable.
class Params:

    num_samples = 200

    figsize = (10, 3)
    lowest_q, low_q, high_q, highest_q = 0.01, 0.1, 0.9, 0.99
    label_q_outer = f"{int(lowest_q * 100)}-{int(highest_q * 100)}th percentiles"
    label_q_inner = f"{int(low_q * 100)}-{int(high_q * 100)}th percentiles"


    # define train/validation cutoff time
    forecast_horizon = 48
    input_chunk_length = 144


    @property
    # template for property
    def sth(self):
        """ template for property"""
        return int(round(self.patch_window_seconds / self.stft_hop_seconds))
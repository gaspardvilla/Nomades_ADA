import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def downsample_mean(signal_df, target_fs):
    """
    Downsample the signal using mean
    signal_df: input DataFrame with 'time' and 'signal' columns
    target_fs: target sampling frequency (Hz)
    """
    # Calculate the downsampling factor
    original_fs = 1 / (signal_df['time'][1] - signal_df['time'][0])
    factor = int(original_fs / target_fs)
    
    # Group by time bins and take mean
    downsampled = signal_df.groupby(
        signal_df['time'] // (1/target_fs)
    ).agg({
        'time': 'first',
        'signal': 'mean'
    }).reset_index(drop=True)
    return downsampled

def add_noise_and_desync(signal_df, delay=1, noise_std=1):
    """
    Add noise and desynchronize the signal
    signal_df: input DataFrame with 'time' and 'signal' columns
    delay: delay in seconds
    noise_std: standard deviation of the noise
    """
    # Create a copy of the original signal
    noisy_signal = signal_df.copy()
    
    # Add delay
    noisy_signal['time'] += delay
    
    # Add noise
    noisy_signal['signal'] += noise_std * np.random.randn(len(noisy_signal))
    
    return noisy_signal

def generate_brownian_motion(seed, path, fs=250, duration=10):
    """
    Generate a Brownian motion time series
    fs: sampling frequency (Hz)
    duration: duration in seconds
    """
    np.random.seed(seed)
    t = np.arange(0, duration, 1/fs)
    n_samples = len(t)
    dt = 1/fs
    
    # Generate Brownian motion
    dB = np.sqrt(dt) * np.random.randn(n_samples)
    B = np.cumsum(dB)
    df = pd.DataFrame({
        'time': t,
        'signal': B
    })
    df.to_csv(f'{path}/bm.csv', index=False)

    # Add noise and desynchronize
    noisy_signal = add_noise_and_desync(df, noise_std=0.3)
    noisy_signal.to_csv(f'{path}/bm_noisy.csv', index=False)

    # Downsample both signals to 15 Hz
    original_downsampled = downsample_mean(df, 15)
    original_downsampled.to_csv(f'{path}/bm_downsampled.csv', index=False)
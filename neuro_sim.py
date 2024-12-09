import argparse
import json
import numpy as np
import matplotlib.pyplot as plt

def parse_arguments():
    parser = argparse.ArgumentParser(description='Simulate a single LIF neuron model and alpha synapse model.')
    parser.add_argument('mode', choices=['current', 'spike'], help='Simulation mode: "current" or "spike"')
    parser.add_argument('sim_time', type=float, help='Simulation time in seconds')
    parser.add_argument('--current', type=float, help='Input current in nA (only for "current" mode)')
    parser.add_argument('--spike_rate', type=float, help='Spike rate (only for "spike" mode)')
    return parser.parse_args()


def H(t, t_r, t_s):
    if t > t_s + t_r:
        return v_spike * 1
    else:
        return 0

def I(v, t, t0, mode):
    if mode == "current":
        return current
    else:
        return w * g_bar * (v_rev - v) * (t - t0) / tao_syn * np.exp(-(t - t0) / tao_syn)

def dvdt(v, t, t_s, t0, mode):
    derivative = (-((v - v_r) / tao_m) + (I(v, t, t0, mode) / c_m)) * H(t, t_r, t_s)
    return derivative

def v_t(v, t, t_s, t0, mode):
    return v + dt * dvdt(v, t, t_s, t0, mode)

def load_config():
    with open("config.json", "r") as file:
       return json.load(file)

if __name__ == "__main__":
    args = parse_arguments()
    config = load_config()
    mode = args.mode
    sim_time = args.sim_time
    spike_rate = args.spike_rate
    current = args.current
    current = args.current if args.current is not None else 0
    
    # Constants
    v_r = config['v_r']
    v_thr = config['v_thr']
    v_spike = config['v_spike']
    v_rev = config['v_rev']
    tao_m = config['tao_m']
    tao_syn = config['tao_syn']
    c_m = config['c_m']
    g_bar = config['g_bar']
    t_r = config['t_r']
    w = config['w']
    dt = config['dt']

    # Starting conditions
    v0 = v_spike
    t_stop = 0.5
    t_start = 0

    # Time and voltage arrays
    times = [t_start]
    voltages = [v0]

    # Simulation loop
    while times[-1] < t_stop:
        times.append(times[-1] + dt)
        t0 = (1 / spike_rate) * (times[-1] // (1 / spike_rate))
        t_s = t0 - (1 / spike_rate)
        voltages.append(v_t(voltages[-1], times[-1], t_s, t0, mode))
    v = v_r
    for t in np.arange(t_start, t_stop, dt):
        if v >= v_thr:
            voltages.append(v_spike)
            v = v_r  # reset voltage after spike
        else:
            # Update voltage based on current input and decay
            v += dt * dvdt(v, t, t_s, t0, mode)
        times.append(t)
        voltages.append(v)

    # Plotting
    plt.plot(times, voltages, color='k')
    plt.xlabel("Time (ms)")
    plt.ylabel("Membrane Potential (Volts)")
    plt.show()
LIF Neuron Model Simulation

This repository contains a Python script to simulate a single Leaky Integrate-and-Fire (LIF) neuron model with an alpha synapse model. The script allows for two modes of simulation: using a constant input current or input spike rate. The simulation parameters are customizable through a configuration file (config.json).

Features
Simulate a LIF neuron with an alpha synapse model.
Two modes of operation:
Current Mode: Use a constant input current (current) for the simulation.
Spike Mode: Use an input spike rate (spike_rate) to generate synaptic currents.
Customizable neuron and simulation parameters via a config.json file.
Visualize the simulation results with a membrane potential vs. time graph.

Requirements
Python 3.8+
Libraries:
argparse
json
numpy
matplotlib
Usage

Command-Line Arguments

python lif_simulation.py <mode> <sim_time> [--current <current>] [--spike_rate <spike_rate>]
<mode>: Simulation mode, either current or spike.

<sim_time>: Total simulation time in seconds.
--current: Input current in nA (applicable for current mode only).
--spike_rate: Spike rate in Hz (applicable for spike mode only).

Example Commands

Simulate in current mode with a constant input current of 10 nA:

python lif_simulation.py current 0.5 --current 10

Simulate in spike mode with a spike rate of 50 Hz:

python lif_simulation.py spike 0.5 --spike_rate 50

Installation

Clone the repository:

git clone https://github.com/your-username/lif-simulation.git
cd lif-simulation

Install the required Python libraries:

pip install numpy matplotlib
Contributions
Contributions are welcome! Please fork this repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

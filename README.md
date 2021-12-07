# Knapsack problem and committee selection

## Problem formulation

There is a committee with ![alt text](latex_eqs/N.svg) seats. 
An attacker wants to select certain seats at a minimum cost in order to stop/overtake the committee.

Let ![alt text](latex_eqs/Ci.svg) denote the cost of selecting seat ![alt text](latex_eqs/i.svg), 
and ![alt text](latex_eqs/Wi.svg) denote the weight (voting power) of seat ![alt text](latex_eqs/i.svg). 
Define ![alt text](latex_eqs/ui.svg) to be a binary variable (i.e. ![alt text](latex_eqs/uiin.svg) 
representing whether seat ![alt text](latex_eqs/i.svg) is going to be selected or not. That is, 
![alt text](latex_eqs/ui.svg) are our decision variables: if ![alt text](latex_eqs/ui0.svg), seat 
![alt text](latex_eqs/i.svg) shall not be selected, and if ![alt text](latex_eqs/ui1.svg), seat 
![alt text](latex_eqs/i.svg) shall be selected.

The total voting power of the committee with ![alt text](latex_eqs/N.svg) seats is:
<p align="center">
<img src="latex_eqs/sumWi.svg" />
</p>

The obtained voting power by the attacker is defined as follows:
<p align="center">
<img src="latex_eqs/sumWiui.svg" />
</p>
and the cost of this is
<p align="center">
<img src="latex_eqs/sumCiui.svg" />
</p>

We are interested in two scenarios:
1. In order to **stop** the committee, the attacker needs to obtain 1/3 or more of the total 
voting power.
2. In order to **overtake** the committee, the attacker needs to obtain more than 2/3 of the total 
voting power.

Define $\alpha \in \{1/3, 2/3\}$.
We now formulate the following optimization problem
\begin{equation}
    \text{Minimize} \sum_{i=1}^{N}C_iu_i\\
    \text{subject to} \sum_{i=1}^{N}W_iu_i \geq \alpha\sum_{i=1}^{N}W_i,\\
    u_i \in \{0, 1\}. 
\end{equation}

In the relevant literature, this problem is known as a **minimization knapsack problem**.

## Implementation

The coding language of this project is ```Python 3.9```. [Pyomo](http://www.pyomo.org/) and [GLPK](https://www.gnu.org/software/glpk/) are used to solve the optimzation problem.

## Getting Started
Please follow these instructions to install all the requirements and use the package correctly.

### Requirements and Installation
**Make sure you have installed:**
1. [Python 3.9](https://www.python.org/downloads/release/python-390/)
2. [GLPK](https://www.gnu.org/software/glpk/)

**Download the code:**
```bash
git clone https://github.com/roman1e2f5p8s/kp_committee
```

**Create a virtual environment ```venv```:**
```bash
python3.9 -m venv venv
```

**Activate the virtual environment:**
- On Unix or MacOS:
```bash
source venv/bin/activate
```
- On Windows:
```bash
venv\Scripts\activate.bat
```

**Install the dependencies:**
```bash
pip3.9 install -r requirements.txt
```

### Usage

See help files for more details:

```bash
python main.py --help
```

```
usage: main.py --n_nodes {4,5,...} --n_seats {4,5,...} --mode {stop,overtake} [-h]
               [--seed {1,2,...}] [--max_weight {1,2,...,20}] [--solver SOLVER] [--latex]
               [--hide_plots]

Solves Knapsack problem for committee selection

required arguments:
  --n_nodes {4,5,...}        number of nodes in the network
  --n_seats {4,5,...}        number of seats in the committee
  --mode {stop,overtake}     mode to simulate: either stop or overtake the committee

optional arguments:
  -h, --help                 show this help message and exit
  --seed {1,2,...}           seed for random generator, defaults to 2021
  --max_weight {1,2,...,20}  maximum value of voting power, defaults to 20
  --solver SOLVER            solver name, defaults to glpk
  --latex                    use LaTeX in plots, defaults to False
  --hide_plots               do not show plots, defaults to False
```


```python

```

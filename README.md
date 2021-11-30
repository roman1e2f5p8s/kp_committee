# Knapsack problem and committee selection

## Problem formulation

There is a committee with $N$ seats. An adversary wants to select certain seats at a minimum cost in order to stop/overtake the committee.

Let $C_i$ denote the cost of selecting seat $i$, and $W_i$ denote the weight (voting power) of seat $i, i \in \{1,2,...,N\}$. Define $u_i$ to be a binary variable (i.e. $u_i \in \{0, 1\}$) representing whether seat $i$ is going to be selected or not. That is, $u_i$ are our decision variables: if $u_i=0$, seat $i$ shall not be selected, and if $u_i=1$, seat $i$ shall be selected.

The total voting power of the committee with $N$ seats is:
\begin{equation}
    \sum_{i=1}^{N}W_i
\end{equation}

The obtained voting power by adversary is defined as follows:
\begin{equation}
    \sum_{i=1}^{N}W_iu_i,
\end{equation}
and the cost of this is
\begin{equation}
    \sum_{i=1}^{N}C_iu_i,
\end{equation}

We are interested in two scenarios:
1. In order to **stop** the committee, the adversary needs to obtain at least 1/3 of the total voting power.
2. In order to **overtake** the committee, the adversary needs to obtain at least 2/3 of the total voting power.

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

[//]: # (
Then run
```bash
python3.9 setup.py install
```
)


```python

```

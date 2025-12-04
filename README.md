# ILBAI Final Project
Cam Eich and Satyam Patel

## Overview
This is our final project for Professor Selmer Brinsjord's Intro to Logic-Based AI course in the Fall '25 semester. Our goal is to develop a logical model that represents the rules and constraints of Rush Hour puzzles in first-order logic, then use ShadowProver to automatically solve given puzzles.

## Installation 

Install Conda: https://anaconda.org/anaconda/conda

### Python dependencies 
```
conda init 
conda env create -f environment.yml
conda activate spectra_env
```

### Install EProver

```
cd eprover
./configure --enable-ho
make rebuild
```

Run the examples in the notebooks
# ILBAI Final Project
Cam Eich and Satyam Patel

## Overview
This is our final project for Professor Selmer Brinsjord's Intro to Logic-Based AI course in the Fall '25 semester. Our goal is to develop a logical model that represents the rules and constraints of Rush Hour puzzles in first-order logic, then use Spectra to automatically solve given puzzles.

## Architecture

This project uses:
- **ShadowProver**: Automated reasoning engine for first-order logic
- **Spectra**: AI planner that uses ShadowProver for planning problems
- **EProver**: Theorem prover backend used by ShadowProver

We use the Python implementation of Spectra.

## Installation

### Prerequisites

- **Conda**: (Anaconda or Miniconda)
- **GCC/Make**: For building EProver (if not already built)

### Setup Environment

1. Create the Conda environment from the provided `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   ```

2. Activate the environment:
   ```bash
   conda activate spectra_env
   ```

3. Build eprover:
   ```bash
   cd eprover
   ./configure --enable-ho
   make rebuild
   cd ..
   ```

## Running Puzzles

To run the Rush Hour solver:

```bash
python rush_hour.py
```

This script defines the puzzle domain, background knowledge, and actions directly in Python and uses the Spectra planner to find a solution.
# ILBAI Final Project
Cam Eich and Satyam Patel

## Project Overview
This is our final project for Professor Selmer Brinsjord's Intro to Logic-Based AI course in the Fall '25 semester. Our goal is to develop a logical model that represents the rules and constraints of Rush Hour puzzles in first-order logic, then use Spectra to automatically solve given puzzles.

## Architecture

This project uses:
- **ShadowProver**: Automated reasoning engine for first-order logic
- **Spectra**: AI planner that uses ShadowProver for planning problems
- **EProver**: Theorem prover backend used by ShadowProver

We use the Python implementation of Spectra.

## Game Overview

Rush Hour is a sliding-block puzzle played on a grid. Vehicles occupy one or more contiguous tiles and can move only along their orientation (horizontal cars move left/right; vertical cars move up/down). The objective is to move the red car to the exit, which in our visualization is the rightmost side of the middle row. A legal move slides a vehicle into adjacent empty tiles without rotating or jumping. The puzzle is solved when the red car reaches the exit.

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

### Option 1: Visual Mode (Recommended)

To see the puzzle grid displayed before and after the solution:

```bash
python run_visual.py problems/<puzzle_name>.py
```

To print the board after each action step, add `--steps`:

```bash
python run_visual.py problems/<puzzle_name>.py --steps
```

This will:
1. Load the puzzle from the specified file
2. Display the starting board configuration
3. Run the Spectra planner to solve the puzzle
4. Print each action and show the updated board (with `--steps`)
5. Show the final solved board with the goal marker (`<-- Goal`)

### Option 2: Standard Mode

To run the Rush Hour solver without visualization:

```bash
python <puzzle_name>.py
```

This script defines the puzzle domain, background knowledge, and actions directly in Python and uses the Spectra planner to find a solution.

## Resources

- **EProver**: https://github.com/eprover/eprover
- **ShadowProver**: https://github.com/RAIRLab/ShadowProver
- **Spectra**: https://github.com/RAIRLab/Spectra
- **Spectra Examples (starter repo)**: https://github.com/naveensundarg/spectra-examples
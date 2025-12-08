# ILBAI Final Project
Cam Eich and Satyam Patel

## Overview
This is our final project for Professor Selmer Brinsjord's Intro to Logic-Based AI course in the Fall '25 semester. Our goal is to develop a logical model that represents the rules and constraints of Rush Hour puzzles in first-order logic, then use ShadowProver and Spectra to automatically solve given puzzles.

## Architecture

This project uses:
- **ShadowProver**: Automated reasoning engine for first-order logic
- **Spectra**: AI planner that uses ShadowProver for planning problems
- **EProver**: Theorem prover backend used by ShadowProver

We use the native Java/Clojure implementation of Spectra rather than the Python wrapper for better performance with the large state spaces in Rush Hour puzzles.

## Installation

### Prerequisites

- **Java 17 or higher**: Required for ShadowProver and Spectra
- **Apache Maven**: For building Java projects
- **GCC/Make**: For building EProver

#### Install Java 17
```bash
sudo apt update
sudo apt install openjdk-17-jdk
java -version  # Verify installation
```

#### Install Maven (if not already installed)
```bash
sudo apt install maven
mvn -version  # Verify installation
```

### Build Instructions

#### 1. Build ShadowProver
```bash
cd ShadowProver
mvn package
mvn install  # Install to local Maven repository
cd ..
```

#### 2. Build Spectra
```bash
cd Spectra
mvn package
mvn install  # Install to local Maven repository
cd ..
```

#### 3. Build EProver
```bash
cd eprover
./configure --enable-ho
make rebuild
cd ..
```

### Verify Installation

```bash
# Verify EProver
./eprover/PROVER/eprover-ho --version

# Should output: E 3.0.1-ho Countess Grey
```

## Running Puzzles

Use the provided Python runner script to solve Rush Hour puzzles:

```bash
python run_puzzle.py problems/rush_hour_beginner_1.clj
```

The runner script automatically:
- Sets the `EPROVER_HOME` environment variable
- Validates all required paths
- Runs Spectra with the specified puzzle file
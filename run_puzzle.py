#!/usr/bin/env python3
"""
Rush Hour Puzzle Runner

Runs Rush Hour puzzles using Spectra planner with proper environment setup.

Usage:
    python run_puzzle.py <puzzle_file>
    python run_puzzle.py problems/rush_hour_beginner_1.clj
"""

import os
import sys
import subprocess
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_puzzle.py <puzzle_file>")
        print("\nExample:")
        print("  python run_puzzle.py problems/rush_hour_beginner_1.clj")
        sys.exit(1)
    
    # Get the puzzle file path
    puzzle_file = sys.argv[1]
    
    # Resolve paths
    project_root = Path(__file__).parent.absolute()
    puzzle_path = project_root / puzzle_file
    spectra_dir = project_root / "Spectra"
    eprover_dir = project_root / "eprover"
    run_script = spectra_dir / "run_spectra.sh"
    
    # Validate paths
    if not puzzle_path.exists():
        print(f"Error: Puzzle file not found: {puzzle_path}")
        sys.exit(1)
    
    if not spectra_dir.exists():
        print(f"Error: Spectra directory not found: {spectra_dir}")
        print("Make sure Spectra is built and installed.")
        sys.exit(1)
    
    if not run_script.exists():
        print(f"Error: run_spectra.sh not found: {run_script}")
        sys.exit(1)
    
    if not eprover_dir.exists():
        print(f"Error: EProver directory not found: {eprover_dir}")
        print("Make sure EProver is built.")
        sys.exit(1)
    
    # Set environment variables
    env = os.environ.copy()
    env['EPROVER_HOME'] = str(eprover_dir)
    
    # Print info
    print(f"Running puzzle: {puzzle_path.name}")
    print(f"Spectra: {spectra_dir}")
    print(f"EProver: {eprover_dir}")
    print("-" * 60)
    
    # Run Spectra
    try:
        result = subprocess.run(
            [str(run_script), str(puzzle_path)],
            cwd=str(spectra_dir),
            env=env,
            text=True
        )
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\nError running Spectra: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

import sys
import os
import re
import argparse
import importlib.util

from shadowprover.reasoners.planner import run_spectra
from shadowprover.syntax.reader import r

def load_puzzle_module(file_path):
    """Dynamically load a python module from a file path."""
    module_name = os.path.basename(file_path).replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {file_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def parse_tile(tile_str):
    # t12 -> 12
    return int(tile_str[1:])

def print_board(state):
    grid = [['.' for _ in range(4)] for _ in range(4)]
    
    # Extract (on Car Tile) predicates
    for fact in state:
        fact_str = str(fact)
        # Match (on Car Tile)
        match = re.search(r'\(on (\w+) (t\d+)\)', fact_str)
        if match:
            car = match.group(1)
            tile = match.group(2)
            try:
                idx = parse_tile(tile)
                if 0 <= idx < 16:
                    row = idx // 4
                    col = idx % 4
                    grid[row][col] = car[0] # First letter of car
            except ValueError:
                pass
            
    print("-" * 17)
    for row in grid:
        print("| " + " | ".join(row) + " |")
        print("-" * 17)

def apply_action(state, action_str):
    # Action: (move ?c ?t1 ?t2 ?t3 ?dir)
    # We only care about updating (on ?c ?t) facts for visualization
    
    # Parse action
    # (move R t14 t15 t12 left)
    content = action_str.strip("()")
    parts = content.split()
    if len(parts) < 5 or parts[0] != 'move':
        return state
        
    car = parts[1]
    t1 = parts[2]
    # t2 = parts[3] # Middle/Pivot
    t3 = parts[4] # New position
    
    # Create new state
    new_state = set()
    
    # The logic: remove (on car t1), add (on car t3)
    # We construct a regex to match the fact we want to delete to be robust against whitespace
    # del_fact_str = f"(on {car} {t1})"
    
    for fact in state:
        fact_str = str(fact)
        # Check if this fact is (on car t1)
        # We use a regex to be safe about whitespace
        # Escape car and t1 just in case, though they are usually simple alphanumeric
        # Use re.IGNORECASE to handle R vs r, Y vs y
        if not re.search(rf'\(on\s+{re.escape(car)}\s+{re.escape(t1)}\)', fact_str, re.IGNORECASE):
            new_state.add(fact)
            
    # Add new fact.
    new_state.add(r(f"(on {car} {t3})"))
    
    return new_state

def main():
    parser = argparse.ArgumentParser(description='Run Rush Hour puzzle solver with visualization.')
    parser.add_argument('puzzle_file', help='Path to the python puzzle file (e.g., problems/rush_hour.py)')
    args = parser.parse_args()

    if not os.path.exists(args.puzzle_file):
        print(f"Error: File '{args.puzzle_file}' not found.")
        sys.exit(1)

    try:
        puzzle = load_puzzle_module(args.puzzle_file)
    except Exception as e:
        print(f"Error loading puzzle file: {e}")
        sys.exit(1)

    print("Starting State:")
    print_board(puzzle.start)
    
    print("\nRunning Spectra...")
    try:
        # run_spectra returns a list of plans
        plans = run_spectra(
            puzzle.domain, 
            puzzle.background, 
            puzzle.start, 
            puzzle.goal, 
            puzzle.actions, 
            puzzle.get_cached_prover(), 
            verbose=False
        )
        
        if plans and len(plans) > 0 and plans[0] is not None:
            plan = plans[0]
            print("\nPlan found:")
            current_state = puzzle.start
            for step in plan:
                print(f"Action: {step}")
                current_state = apply_action(current_state, str(step))
            
            print("\nFinal State:")
            print_board(current_state)
        else:
            print("\nNo plan found.")
            
    except TypeError as e:
        if "'NoneType' object is not iterable" in str(e):
             print("\nPlan found:\nAn error occurred: 'NoneType' object is not iterable")
        else:
            print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

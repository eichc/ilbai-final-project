import os
# Set EPROVER_HOME if not already set. Adjust path as necessary.
os.environ['EPROVER_HOME'] = os.environ.get('EPROVER_HOME', './eprover/')

from shadowprover.syntax import *
from shadowprover.reasoners.planner import Action, run_spectra
from shadowprover.syntax.reader import r
from shadowprover.fol.fol_prover import fol_prove
from functools import cache

# 1. Domain Definition
domain = {
    r("t0"), r("t1"), r("t2"), r("t3"), r("t4"), r("t5"), r("t6"), r("t7"),
    r("t8"), r("t9"), r("t10"), r("t11"), r("t12"), r("t13"), r("t14"), r("t15"),
    r("right"), r("down"), r("left"), r("up"), r("r"), r("y"), r("b")
}

# 2. Background Knowledge
background = set(
    list(
        map(
            r,
            [
                # Grid adjacency relations
                "(adjacent t0 t1 right)", "(adjacent t1 t2 right)", "(adjacent t2 t3 right)",
                "(adjacent t4 t5 right)", "(adjacent t5 t6 right)", "(adjacent t6 t7 right)",
                "(adjacent t8 t9 right)", "(adjacent t9 t10 right)", "(adjacent t10 t11 right)",
                "(adjacent t12 t13 right)", "(adjacent t13 t14 right)", "(adjacent t14 t15 right)",

                "(adjacent t1 t0 left)", "(adjacent t2 t1 left)", "(adjacent t3 t2 left)",
                "(adjacent t5 t4 left)", "(adjacent t6 t5 left)", "(adjacent t7 t6 left)",
                "(adjacent t9 t8 left)", "(adjacent t10 t9 left)", "(adjacent t11 t10 left)",
                "(adjacent t13 t12 left)", "(adjacent t14 t13 left)", "(adjacent t15 t14 left)",

                "(adjacent t0 t4 down)", "(adjacent t1 t5 down)", "(adjacent t2 t6 down)", "(adjacent t3 t7 down)",
                "(adjacent t4 t8 down)", "(adjacent t5 t9 down)", "(adjacent t6 t10 down)", "(adjacent t7 t11 down)",
                "(adjacent t8 t12 down)", "(adjacent t9 t13 down)", "(adjacent t10 t14 down)", "(adjacent t11 t15 down)",

                "(adjacent t4 t0 up)", "(adjacent t5 t1 up)", "(adjacent t6 t2 up)", "(adjacent t7 t3 up)",
                "(adjacent t8 t4 up)", "(adjacent t9 t5 up)", "(adjacent t10 t6 up)", "(adjacent t11 t7 up)",
                "(adjacent t12 t8 up)", "(adjacent t13 t9 up)", "(adjacent t14 t10 up)", "(adjacent t15 t11 up)",

                # Distinct coordinates
                "(not (= t0 t1))", "(not (= t0 t2))", "(not (= t0 t3))", "(not (= t0 t4))", "(not (= t0 t5))", "(not (= t0 t6))", "(not (= t0 t7))",
                "(not (= t0 t8))", "(not (= t0 t9))", "(not (= t0 t10))", "(not (= t0 t11))", "(not (= t0 t12))", "(not (= t0 t13))", "(not (= t0 t14))", "(not (= t0 t15))",

                "(not (= t1 t2))", "(not (= t1 t3))", "(not (= t1 t4))", "(not (= t1 t5))", "(not (= t1 t6))", "(not (= t1 t7))", "(not (= t1 t8))",
                "(not (= t1 t9))", "(not (= t1 t10))", "(not (= t1 t11))", "(not (= t1 t12))", "(not (= t1 t13))", "(not (= t1 t14))", "(not (= t1 t15))",

                "(not (= t2 t3))", "(not (= t2 t4))", "(not (= t2 t5))", "(not (= t2 t6))", "(not (= t2 t7))", "(not (= t2 t8))", "(not (= t2 t9))",
                "(not (= t2 t10))", "(not (= t2 t11))", "(not (= t2 t12))", "(not (= t2 t13))", "(not (= t2 t14))", "(not (= t2 t15))",

                "(not (= t3 t4))", "(not (= t3 t5))", "(not (= t3 t6))", "(not (= t3 t7))", "(not (= t3 t8))", "(not (= t3 t9))", "(not (= t3 t10))",
                "(not (= t3 t11))", "(not (= t3 t12))", "(not (= t3 t13))", "(not (= t3 t14))", "(not (= t3 t15))",

                "(not (= t4 t5))", "(not (= t4 t6))", "(not (= t4 t7))", "(not (= t4 t8))", "(not (= t4 t9))", "(not (= t4 t10))", "(not (= t4 t11))",
                "(not (= t4 t12))", "(not (= t4 t13))", "(not (= t4 t14))", "(not (= t4 t15))",

                "(not (= t5 t6))", "(not (= t5 t7))", "(not (= t5 t8))", "(not (= t5 t9))", "(not (= t5 t10))", "(not (= t5 t11))", "(not (= t5 t12))",
                "(not (= t5 t13))", "(not (= t5 t14))", "(not (= t5 t15))",

                "(not (= t6 t7))", "(not (= t6 t8))", "(not (= t6 t9))", "(not (= t6 t10))", "(not (= t6 t11))", "(not (= t6 t12))", "(not (= t6 t13))",
                "(not (= t6 t14))", "(not (= t6 t15))",

                "(not (= t7 t8))", "(not (= t7 t9))", "(not (= t7 t10))", "(not (= t7 t11))", "(not (= t7 t12))", "(not (= t7 t13))", "(not (= t7 t14))",
                "(not (= t7 t15))",

                "(not (= t8 t9))", "(not (= t8 t10))", "(not (= t8 t11))", "(not (= t8 t12))", "(not (= t8 t13))", "(not (= t8 t14))", "(not (= t8 t15))",

                "(not (= t9 t10))", "(not (= t9 t11))", "(not (= t9 t12))", "(not (= t9 t13))", "(not (= t9 t14))", "(not (= t9 t15))",

                "(not (= t10 t11))", "(not (= t10 t12))", "(not (= t10 t13))", "(not (= t10 t14))", "(not (= t10 t15))",

                "(not (= t11 t12))", "(not (= t11 t13))", "(not (= t11 t14))", "(not (= t11 t15))",

                "(not (= t12 t13))", "(not (= t12 t14))", "(not (= t12 t15))",

                "(not (= t13 t14))", "(not (= t13 t15))",

                "(not (= t14 t15))",
            ],
        )
    )
)

# 3. Actions
actions = [
    Action(
        r("(move ?c ?t1 ?t2 ?t3 ?dir)"),
        precondition=r(
            """(and 
                (on ?c ?t1)
                (on ?c ?t2)
                (not (= ?t1 ?t2))
                (not (= ?t1 ?t3))
                (not (= ?t2 ?t3))
                (adjacent ?t1 ?t2 ?dir)
                (adjacent ?t2 ?t3 ?dir)
                (notOccupied ?t3)
            )"""
        ),
        additions={
            r("(on ?c ?t3)"),
            r("(on ?c ?t2)"),
            r("(notOccupied ?t1)")
        },
        deletions={
            r("(on ?c ?t1)"),
            r("(notOccupied ?t3)")
        },
    ),
]

# 4. Start State
start = set(
    map(
        r,
        [
            "(on r t4)",
            "(on r t5)",
            "(on y t2)",
            "(on y t6)",
            "(on b t7)",
            "(on b t11)",
            "(notOccupied t0)",
            "(notOccupied t1)",
            # "(notOccupied t2)",
            "(notOccupied t3)",
            # "(notOccupied t4)",
            # "(notOccupied t5)",
            # "(notOccupied t6)",
            # "(notOccupied t7)",
            "(notOccupied t8)",
            "(notOccupied t9)",
            "(notOccupied t10)",
            # "(notOccupied t11)",
            "(notOccupied t12)",
            "(notOccupied t13)",
            "(notOccupied t14)",
            "(notOccupied t15)",
        ],
    )
)

# 5. Goal State
goal = r(
    """
    (and (on r t6) (on r t7))
    """
)

# 6. Prover Setup
def get_cached_prover(find_answer=True, max_answers=5):
    @cache
    def cached_prover(inputs, output, find_answer=find_answer, max_answers=max_answers):
        return fol_prove(inputs, output, find_answer=find_answer, max_answers=max_answers)
    
    def _prover_(inputs, output, find_answer=find_answer, max_answers=max_answers):
        return cached_prover(frozenset(inputs), output, find_answer, max_answers=max_answers)
    
    return _prover_

# 7. Execution
if __name__ == "__main__":
    print("Starting Rush Hour Planner...")
    try:
        # run_spectra returns a list of plans, we take the first one
        plans = run_spectra(domain, background, start, goal, actions, get_cached_prover(), verbose=True)
        
        if plans:
            print("\nPlan found:")
            for step in plans[0]:
                print(step)
        else:
            print("\nNo plan found.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

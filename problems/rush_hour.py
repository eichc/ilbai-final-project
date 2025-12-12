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
    r("t16"), r("t17"), r("t18"), r("t19"), r("t20"), r("t21"), r("t22"), r("t23"), r("t24"),
    r("right"), r("down"), r("left"), r("up"), r("r"), r("y"), r("b"), r("g")
}

# 2. Background Knowledge
background = set(
    list(
        map(
            r,
            [
                # Grid adjacency relations (5x5 grid)
                # Horizontal adjacencies (right)
                "(adjacent t0 t1 right)", "(adjacent t1 t2 right)", "(adjacent t2 t3 right)", "(adjacent t3 t4 right)",
                "(adjacent t5 t6 right)", "(adjacent t6 t7 right)", "(adjacent t7 t8 right)", "(adjacent t8 t9 right)",
                "(adjacent t10 t11 right)", "(adjacent t11 t12 right)", "(adjacent t12 t13 right)", "(adjacent t13 t14 right)",
                "(adjacent t15 t16 right)", "(adjacent t16 t17 right)", "(adjacent t17 t18 right)", "(adjacent t18 t19 right)",
                "(adjacent t20 t21 right)", "(adjacent t21 t22 right)", "(adjacent t22 t23 right)", "(adjacent t23 t24 right)",

                # Horizontal adjacencies (left)
                "(adjacent t1 t0 left)", "(adjacent t2 t1 left)", "(adjacent t3 t2 left)", "(adjacent t4 t3 left)",
                "(adjacent t6 t5 left)", "(adjacent t7 t6 left)", "(adjacent t8 t7 left)", "(adjacent t9 t8 left)",
                "(adjacent t11 t10 left)", "(adjacent t12 t11 left)", "(adjacent t13 t12 left)", "(adjacent t14 t13 left)",
                "(adjacent t16 t15 left)", "(adjacent t17 t16 left)", "(adjacent t18 t17 left)", "(adjacent t19 t18 left)",
                "(adjacent t21 t20 left)", "(adjacent t22 t21 left)", "(adjacent t23 t22 left)", "(adjacent t24 t23 left)",

                # Vertical adjacencies (down)
                "(adjacent t0 t5 down)", "(adjacent t5 t10 down)", "(adjacent t10 t15 down)", "(adjacent t15 t20 down)",
                "(adjacent t1 t6 down)", "(adjacent t6 t11 down)", "(adjacent t11 t16 down)", "(adjacent t16 t21 down)",
                "(adjacent t2 t7 down)", "(adjacent t7 t12 down)", "(adjacent t12 t17 down)", "(adjacent t17 t22 down)",
                "(adjacent t3 t8 down)", "(adjacent t8 t13 down)", "(adjacent t13 t18 down)", "(adjacent t18 t23 down)",
                "(adjacent t4 t9 down)", "(adjacent t9 t14 down)", "(adjacent t14 t19 down)", "(adjacent t19 t24 down)",

                # Vertical adjacencies (up)
                "(adjacent t5 t0 up)", "(adjacent t10 t5 up)", "(adjacent t15 t10 up)", "(adjacent t20 t15 up)",
                "(adjacent t6 t1 up)", "(adjacent t11 t6 up)", "(adjacent t16 t11 up)", "(adjacent t21 t16 up)",
                "(adjacent t7 t2 up)", "(adjacent t12 t7 up)", "(adjacent t17 t12 up)", "(adjacent t22 t17 up)",
                "(adjacent t8 t3 up)", "(adjacent t13 t8 up)", "(adjacent t18 t13 up)", "(adjacent t23 t18 up)",
                "(adjacent t9 t4 up)", "(adjacent t14 t9 up)", "(adjacent t19 t14 up)", "(adjacent t24 t19 up)",

                # Distinct coordinates (all pairwise inequalities for 5x5 grid)
                "(not (= t0 t1))", "(not (= t0 t2))", "(not (= t0 t3))", "(not (= t0 t4))", "(not (= t0 t5))",
                "(not (= t0 t6))", "(not (= t0 t7))", "(not (= t0 t8))", "(not (= t0 t9))", "(not (= t0 t10))",
                "(not (= t0 t11))", "(not (= t0 t12))", "(not (= t0 t13))", "(not (= t0 t14))", "(not (= t0 t15))",
                "(not (= t0 t16))", "(not (= t0 t17))", "(not (= t0 t18))", "(not (= t0 t19))", "(not (= t0 t20))",
                "(not (= t0 t21))", "(not (= t0 t22))", "(not (= t0 t23))", "(not (= t0 t24))",

                "(not (= t1 t2))", "(not (= t1 t3))", "(not (= t1 t4))", "(not (= t1 t5))", "(not (= t1 t6))",
                "(not (= t1 t7))", "(not (= t1 t8))", "(not (= t1 t9))", "(not (= t1 t10))", "(not (= t1 t11))",
                "(not (= t1 t12))", "(not (= t1 t13))", "(not (= t1 t14))", "(not (= t1 t15))", "(not (= t1 t16))",
                "(not (= t1 t17))", "(not (= t1 t18))", "(not (= t1 t19))", "(not (= t1 t20))", "(not (= t1 t21))",
                "(not (= t1 t22))", "(not (= t1 t23))", "(not (= t1 t24))",

                "(not (= t2 t3))", "(not (= t2 t4))", "(not (= t2 t5))", "(not (= t2 t6))", "(not (= t2 t7))",
                "(not (= t2 t8))", "(not (= t2 t9))", "(not (= t2 t10))", "(not (= t2 t11))", "(not (= t2 t12))",
                "(not (= t2 t13))", "(not (= t2 t14))", "(not (= t2 t15))", "(not (= t2 t16))", "(not (= t2 t17))",
                "(not (= t2 t18))", "(not (= t2 t19))", "(not (= t2 t20))", "(not (= t2 t21))", "(not (= t2 t22))",
                "(not (= t2 t23))", "(not (= t2 t24))",

                "(not (= t3 t4))", "(not (= t3 t5))", "(not (= t3 t6))", "(not (= t3 t7))", "(not (= t3 t8))",
                "(not (= t3 t9))", "(not (= t3 t10))", "(not (= t3 t11))", "(not (= t3 t12))", "(not (= t3 t13))",
                "(not (= t3 t14))", "(not (= t3 t15))", "(not (= t3 t16))", "(not (= t3 t17))", "(not (= t3 t18))",
                "(not (= t3 t19))", "(not (= t3 t20))", "(not (= t3 t21))", "(not (= t3 t22))", "(not (= t3 t23))",
                "(not (= t3 t24))",

                "(not (= t4 t5))", "(not (= t4 t6))", "(not (= t4 t7))", "(not (= t4 t8))", "(not (= t4 t9))",
                "(not (= t4 t10))", "(not (= t4 t11))", "(not (= t4 t12))", "(not (= t4 t13))", "(not (= t4 t14))",
                "(not (= t4 t15))", "(not (= t4 t16))", "(not (= t4 t17))", "(not (= t4 t18))", "(not (= t4 t19))",
                "(not (= t4 t20))", "(not (= t4 t21))", "(not (= t4 t22))", "(not (= t4 t23))", "(not (= t4 t24))",

                "(not (= t5 t6))", "(not (= t5 t7))", "(not (= t5 t8))", "(not (= t5 t9))", "(not (= t5 t10))",
                "(not (= t5 t11))", "(not (= t5 t12))", "(not (= t5 t13))", "(not (= t5 t14))", "(not (= t5 t15))",
                "(not (= t5 t16))", "(not (= t5 t17))", "(not (= t5 t18))", "(not (= t5 t19))", "(not (= t5 t20))",
                "(not (= t5 t21))", "(not (= t5 t22))", "(not (= t5 t23))", "(not (= t5 t24))",

                "(not (= t6 t7))", "(not (= t6 t8))", "(not (= t6 t9))", "(not (= t6 t10))", "(not (= t6 t11))",
                "(not (= t6 t12))", "(not (= t6 t13))", "(not (= t6 t14))", "(not (= t6 t15))", "(not (= t6 t16))",
                "(not (= t6 t17))", "(not (= t6 t18))", "(not (= t6 t19))", "(not (= t6 t20))", "(not (= t6 t21))",
                "(not (= t6 t22))", "(not (= t6 t23))", "(not (= t6 t24))",

                "(not (= t7 t8))", "(not (= t7 t9))", "(not (= t7 t10))", "(not (= t7 t11))", "(not (= t7 t12))",
                "(not (= t7 t13))", "(not (= t7 t14))", "(not (= t7 t15))", "(not (= t7 t16))", "(not (= t7 t17))",
                "(not (= t7 t18))", "(not (= t7 t19))", "(not (= t7 t20))", "(not (= t7 t21))", "(not (= t7 t22))",
                "(not (= t7 t23))", "(not (= t7 t24))",

                "(not (= t8 t9))", "(not (= t8 t10))", "(not (= t8 t11))", "(not (= t8 t12))", "(not (= t8 t13))",
                "(not (= t8 t14))", "(not (= t8 t15))", "(not (= t8 t16))", "(not (= t8 t17))", "(not (= t8 t18))",
                "(not (= t8 t19))", "(not (= t8 t20))", "(not (= t8 t21))", "(not (= t8 t22))", "(not (= t8 t23))",
                "(not (= t8 t24))",

                "(not (= t9 t10))", "(not (= t9 t11))", "(not (= t9 t12))", "(not (= t9 t13))", "(not (= t9 t14))",
                "(not (= t9 t15))", "(not (= t9 t16))", "(not (= t9 t17))", "(not (= t9 t18))", "(not (= t9 t19))",
                "(not (= t9 t20))", "(not (= t9 t21))", "(not (= t9 t22))", "(not (= t9 t23))", "(not (= t9 t24))",

                "(not (= t10 t11))", "(not (= t10 t12))", "(not (= t10 t13))", "(not (= t10 t14))", "(not (= t10 t15))",
                "(not (= t10 t16))", "(not (= t10 t17))", "(not (= t10 t18))", "(not (= t10 t19))", "(not (= t10 t20))",
                "(not (= t10 t21))", "(not (= t10 t22))", "(not (= t10 t23))", "(not (= t10 t24))",

                "(not (= t11 t12))", "(not (= t11 t13))", "(not (= t11 t14))", "(not (= t11 t15))", "(not (= t11 t16))",
                "(not (= t11 t17))", "(not (= t11 t18))", "(not (= t11 t19))", "(not (= t11 t20))", "(not (= t11 t21))",
                "(not (= t11 t22))", "(not (= t11 t23))", "(not (= t11 t24))",

                "(not (= t12 t13))", "(not (= t12 t14))", "(not (= t12 t15))", "(not (= t12 t16))", "(not (= t12 t17))",
                "(not (= t12 t18))", "(not (= t12 t19))", "(not (= t12 t20))", "(not (= t12 t21))", "(not (= t12 t22))",
                "(not (= t12 t23))", "(not (= t12 t24))",

                "(not (= t13 t14))", "(not (= t13 t15))", "(not (= t13 t16))", "(not (= t13 t17))", "(not (= t13 t18))",
                "(not (= t13 t19))", "(not (= t13 t20))", "(not (= t13 t21))", "(not (= t13 t22))", "(not (= t13 t23))",
                "(not (= t13 t24))",

                "(not (= t14 t15))", "(not (= t14 t16))", "(not (= t14 t17))", "(not (= t14 t18))", "(not (= t14 t19))",
                "(not (= t14 t20))", "(not (= t14 t21))", "(not (= t14 t22))", "(not (= t14 t23))", "(not (= t14 t24))",

                "(not (= t15 t16))", "(not (= t15 t17))", "(not (= t15 t18))", "(not (= t15 t19))", "(not (= t15 t20))",
                "(not (= t15 t21))", "(not (= t15 t22))", "(not (= t15 t23))", "(not (= t15 t24))",

                "(not (= t16 t17))", "(not (= t16 t18))", "(not (= t16 t19))", "(not (= t16 t20))", "(not (= t16 t21))",
                "(not (= t16 t22))", "(not (= t16 t23))", "(not (= t16 t24))",

                "(not (= t17 t18))", "(not (= t17 t19))", "(not (= t17 t20))", "(not (= t17 t21))", "(not (= t17 t22))",
                "(not (= t17 t23))", "(not (= t17 t24))",

                "(not (= t18 t19))", "(not (= t18 t20))", "(not (= t18 t21))", "(not (= t18 t22))", "(not (= t18 t23))",
                "(not (= t18 t24))",

                "(not (= t19 t20))", "(not (= t19 t21))", "(not (= t19 t22))", "(not (= t19 t23))", "(not (= t19 t24))",

                "(not (= t20 t21))", "(not (= t20 t22))", "(not (= t20 t23))", "(not (= t20 t24))",

                "(not (= t21 t22))", "(not (= t21 t23))", "(not (= t21 t24))",

                "(not (= t22 t23))", "(not (= t22 t24))",

                "(not (= t23 t24))",
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
            "(on r t10)",
            "(on r t11)",
            "(on y t7)",
            "(on y t12)",
            "(on b t17)",
            "(on b t22)",
            "(on g t1)",
            "(on g t2)",
            "(notOccupied t0)",
            # "(notOccupied t1)",
            # "(notOccupied t2)",
            "(notOccupied t3)",
            "(notOccupied t4)",
            "(notOccupied t5)",
            "(notOccupied t6)",
            # "(notOccupied t7)",
            "(notOccupied t8)",
            "(notOccupied t9)",
            # "(notOccupied t10)",
            # "(notOccupied t11)",
            # "(notOccupied t12)",
            "(notOccupied t13)",
            "(notOccupied t14)",
            "(notOccupied t15)",
            "(notOccupied t16)",
            # "(notOccupied t17)",
            "(notOccupied t18)",
            "(notOccupied t19)",
            "(notOccupied t20)",
            "(notOccupied t21)",
            # "(notOccupied t22)",
            "(notOccupied t23)",
            "(notOccupied t24)",
        ],
    )
)

# 5. Goal State
goal = r(
    """
    (and (on r t13) (on r t14))
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

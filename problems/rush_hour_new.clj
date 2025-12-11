{:name "Rush Hour - James' Model"

    :background [;; Grid adjacency relations
        (adjacent t0 t1 horizontal) (adjacent t1 t2 horizontal) (adjacent t2 t3 horizontal)
        (adjacent t4 t5 horizontal) (adjacent t5 t6 horizontal) (adjacent t6 t7 horizontal)
        (adjacent t8 t9 horizontal) (adjacent t9 t10 horizontal) (adjacent t10 t11 horizontal)

        (adjacent t0 t4 vertical) (adjacent t4 t8 vertical)
        (adjacent t1 t5 vertical) (adjacent t5 t9 vertical)
        (adjacent t2 t6 vertical) (adjacent t6 t10 vertical)
        (adjacent t3 t7 vertical) (adjacent t7 t11 vertical)

        (forall [?x ?x1 ?dir] (if (adjacent ?x ?x1 ?dir) (adjacent ?x1 ?x ?dir)))

        ;; Distinct coordinates
        ;; (not (= t0 t1)) (not (= t0 t2)) (not (= t0 t3)) (not (= t0 t4)) (not (= t0 t5)) (not (= t0 t6)) (not (= t0 t7)) (not (= t0 t8)) (not (= t0 t9)) (not (= t0 t10)) (not (= t0 t11))
        ;; (not (= t1 t2)) (not (= t1 t3)) (not (= t1 t4)) (not (= t1 t5)) (not (= t1 t6)) (not (= t1 t7)) (not (= t1 t8)) (not (= t1 t9)) (not (= t1 t10)) (not (= t1 t11))
        ;; (not (= t2 t3)) (not (= t2 t4)) (not (= t2 t5)) (not (= t2 t6)) (not (= t2 t7)) (not (= t2 t8)) (not (= t2 t9)) (not (= t2 t10)) (not (= t2 t11))
        ;; (not (= t3 t4)) (not (= t3 t5)) (not (= t3 t6)) (not (= t3 t7)) (not (= t3 t8)) (not (= t3 t9)) (not (= t3 t10)) (not (= t3 t11))
        ;; (not (= t4 t5)) (not (= t4 t6)) (not (= t4 t7)) (not (= t4 t8)) (not (= t4 t9)) (not (= t4 t10)) (not (= t4 t11))
        ;; (not (= t5 t6)) (not (= t5 t7)) (not (= t5 t8)) (not (= t5 t9)) (not (= t5 t10)) (not (= t5 t11))
        ;; (not (= t6 t7)) (not (= t6 t8)) (not (= t6 t9)) (not (= t6 t10)) (not (= t6 t11))
        ;; (not (= t7 t8)) (not (= t7 t9)) (not (= t7 t10)) (not (= t7 t11))
        ;; (not (= t8 t9)) (not (= t8 t10)) (not (= t8 t11))
        ;; (not (= t9 t10)) (not (= t9 t11))
        ;; (not (= t10 t11))
    ]

    :actions [
        (define-action move [?c ?t1 ?t2 ?t3 ?dir] {
            :preconditions [
                (on ?c ?t1)
                (on ?c ?t2)
                (not (= ?t1 ?t2))
                (not (= ?t1 ?t3))
                (not (= ?t2 ?t3))
                (adjacent ?t2 ?t3 ?dir)
                ;; (not (exists [?c2] (on ?c2 ?t3)))
            ]
            :additions [
                (not (on ?c ?t1))
                (on ?c ?t3)
            ]
            :deletions [
                (on ?c ?t1)
                (not (on ?c ?t3))
            ]
        })
    ]

    :start [
        (on R t0)
        (on R t1)
        (not (on R t2))
    ]

    :goal [
        (on R t2)
    ]
                           
}
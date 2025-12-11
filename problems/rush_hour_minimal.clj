{:name "Rush Hour - Minimal Test"

    :background [;; Grid successor relations
        (NextX x0 x1) (NextX x1 x2) (NextX x2 x3) (NextX x3 x4) (NextX x4 x5)
        (NextY y0 y1) (NextY y1 y2) (NextY y2 y3) (NextY y3 y4) (NextY y4 y5)

        ;; Distinct coordinates
        (not (= x0 x1)) (not (= x0 x2)) (not (= x0 x3)) (not (= x0 x4)) (not (= x0 x5))
        (not (= x1 x2)) (not (= x1 x3)) (not (= x1 x4)) (not (= x1 x5))
        (not (= x2 x3)) (not (= x2 x4)) (not (= x2 x5))
        (not (= x3 x4)) (not (= x3 x5))
        (not (= x4 x5))

        (not (= y0 y1)) (not (= y0 y2)) (not (= y0 y3)) (not (= y0 y4)) (not (= y0 y5))
        (not (= y1 y2)) (not (= y1 y3)) (not (= y1 y4)) (not (= y1 y5))
        (not (= y2 y3)) (not (= y2 y4)) (not (= y2 y5))
        (not (= y3 y4)) (not (= y3 y5))
        (not (= y4 y5))
    ]

    :actions [
        (define-action moveRight [?v ?x ?newx ?y] {
            :preconditions [
                (At ?v ?x ?y)
                (NextX ?x ?newx)
            ]
            :additions [
                (At ?v ?newx ?y)
            ]
            :deletions [
                (At ?v ?x ?y)
            ]
        })
    ]

    :start [
        (At R x0 y0)
    ]

    :goal [
        (At R x1 y0)
    ]
                           
}
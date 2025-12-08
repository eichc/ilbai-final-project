{:name "Rush Hour - Beginner Puzzle 1"

 :background [;; A vehicle at position blocks that position
              (forall [?v ?x ?y]
                      (if (At ?v ?x ?y)
                        (Blocked ?x ?y)))

              ;; Horizontal cars (size 2) block one space to the right
              (forall [?v ?x ?y]
                      (if (and (At ?v ?x ?y)
                               (Horizontal ?v)
                               (not (Truck ?v)))
                        (Blocked (+ ?x 1) ?y)))

              ;; Horizontal trucks (size 3) block two spaces to the right
              (forall [?v ?x ?y]
                      (if (and (At ?v ?x ?y)
                               (Horizontal ?v)
                               (Truck ?v))
                        (and (Blocked (+ ?x 1) ?y)
                             (Blocked (+ ?x 2) ?y))))

              ;; Vertical cars (size 2) block one space below
              (forall [?v ?x ?y]
                      (if (and (At ?v ?x ?y)
                               (not (Horizontal ?v))
                               (not (Truck ?v)))
                        (Blocked ?x (+ ?y 1))))

              ;; Vertical trucks (size 3) block two spaces below
              (forall [?v ?x ?y]
                      (if (and (At ?v ?x ?y)
                               (not (Horizontal ?v))
                               (Truck ?v))
                        (and (Blocked ?x (+ ?y 1))
                             (Blocked ?x (+ ?y 2)))))]

 :start [;; Red car (goal piece) - horizontal car at row 2
         (At R 0 2)
         (Horizontal R)
         (IsGoal R)

         ;; Orange car - vertical car (not horizontal, not truck)
         (At O 0 0)

         ;; Yellow car - horizontal car
         (At Y 2 0)
         (Horizontal Y)

         ;; Green car - vertical car
         (At G 3 1)

         ;; Blue car - horizontal car
         (At B 4 3)
         (Horizontal B)

         ;; Purple truck - vertical truck
         (At P 5 0)
         (Truck P)]

 :goal [(At R 4 2)]

 :actions [(define-action moveRightCar [?v ?x ?y]
                          {:preconditions [(At ?v ?x ?y)
                                           (Horizontal ?v)
                                           (not (Truck ?v))
                                           (not (Blocked (+ ?x 2) ?y))
                                           (< (+ ?x 2) 6)]
                           :additions     [(At ?v (+ ?x 1) ?y)
                                           (Blocked (+ ?x 2) ?y)]
                           :deletions     [(At ?v ?x ?y)
                                           (Blocked ?x ?y)]})

           (define-action moveRightTruck [?v ?x ?y]
                          {:preconditions [(At ?v ?x ?y)
                                           (Horizontal ?v)
                                           (Truck ?v)
                                           (not (Blocked (+ ?x 3) ?y))
                                           (< (+ ?x 3) 6)]
                           :additions     [(At ?v (+ ?x 1) ?y)
                                           (Blocked (+ ?x 3) ?y)]
                           :deletions     [(At ?v ?x ?y)
                                           (Blocked ?x ?y)]})

           (define-action moveLeftCar [?v ?x ?y]
                          {:preconditions [(At ?v ?x ?y)
                                           (Horizontal ?v)
                                           (not (Truck ?v))
                                           (not (Blocked (- ?x 1) ?y))
                                           (> ?x 0)]
                           :additions     [(At ?v (- ?x 1) ?y)
                                           (Blocked (- ?x 1) ?y)]
                           :deletions     [(At ?v ?x ?y)
                                           (Blocked (+ ?x 1) ?y)]})

           (define-action moveLeftTruck [?v ?x ?y]
                          {:preconditions [(At ?v ?x ?y)
                                           (Horizontal ?v)
                                           (Truck ?v)
                                           (not (Blocked (- ?x 1) ?y))
                                           (> ?x 0)]
                           :additions     [(At ?v (- ?x 1) ?y)
                                           (Blocked (- ?x 1) ?y)]
                           :deletions     [(At ?v ?x ?y)
                                           (Blocked (+ ?x 2) ?y)]})

           (define-action moveDownCar [?v ?x ?y]
                          {:preconditions [(At ?v ?x ?y)
                                           (not (Horizontal ?v))
                                           (not (Truck ?v))
                                           (not (Blocked ?x (+ ?y 2)))
                                           (< (+ ?y 2) 6)]
                           :additions     [(At ?v ?x (+ ?y 1))
                                           (Blocked ?x (+ ?y 2))]
                           :deletions     [(At ?v ?x ?y)
                                           (Blocked ?x ?y)]})

           (define-action moveDownTruck [?v ?x ?y]
                          {:preconditions [(At ?v ?x ?y)
                                           (not (Horizontal ?v))
                                           (Truck ?v)
                                           (not (Blocked ?x (+ ?y 3)))
                                           (< (+ ?y 3) 6)]
                           :additions     [(At ?v ?x (+ ?y 1))
                                           (Blocked ?x (+ ?y 3))]
                           :deletions     [(At ?v ?x ?y)
                                           (Blocked ?x ?y)]})

           (define-action moveUpCar [?v ?x ?y]
                          {:preconditions [(At ?v ?x ?y)
                                           (not (Horizontal ?v))
                                           (not (Truck ?v))
                                           (not (Blocked ?x (- ?y 1)))
                                           (> ?y 0)]
                           :additions     [(At ?v ?x (- ?y 1))
                                           (Blocked ?x (- ?y 1))]
                           :deletions     [(At ?v ?x ?y)
                                           (Blocked ?x (+ ?y 1))]})

           (define-action moveUpTruck [?v ?x ?y]
                          {:preconditions [(At ?v ?x ?y)
                                           (not (Horizontal ?v))
                                           (Truck ?v)
                                           (not (Blocked ?x (- ?y 1)))
                                           (> ?y 0)]
                           :additions     [(At ?v ?x (- ?y 1))
                                           (Blocked ?x (- ?y 1))]
                           :deletions     [(At ?v ?x ?y)
                                           (Blocked ?x (+ ?y 2))]})]
}

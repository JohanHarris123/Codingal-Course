def circuit_q(A: int, B: int, C: int) -> int:

    A = 1 if A else 0
    B = 1 if B else 0
    C = 1 if C else 0


    t1 = A & B
    t2 = B | C

    t3 = (~C) & 1
    t4 = (A & t2)

    Q = t1 | t4

    return Q & 1

def truth_table():
    print("A B C | Q")
    for A in (0,1):
        for B in (0,1):
            for C in (0,1):
                print(f"{A} {B} {C} | {circuit_q(A,B,C)}")


truth_table()
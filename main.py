from math import pi, fabs
from sympy import diff, symbols, pi as pii, Matrix

def f_value(f,x):
    x_1, x_2, x_3 = symbols('x_1, x_2, x_3')
    return f.evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]})

def df_value(df,x):
    x_1, x_2, x_3 = symbols('x_1, x_2, x_3')
    return [
        df[0].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]}),
        df[1].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]}),
        df[2].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]})
    ]

def ddf_value(ddf,x):
    x_1, x_2, x_3 = symbols('x_1, x_2, x_3')
    result = [
        [
            ddf[0][0].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]}),
            ddf[0][1].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]}),
            ddf[0][2].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]})
        ],
        [
            ddf[1][0].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]}),
            ddf[1][1].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]}),
            ddf[1][2].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]})
        ],
        [
            ddf[2][0].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]}),
            ddf[2][1].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]}),
            ddf[2][2].evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]})
        ]
    ]
    return result

def grad_value(grad_f, x):
    x_1, x_2, x_3 = symbols('x_1, x_2, x_3')
    return grad_f.evalf(subs={x_1: x[0], x_2: x[1], x_3: x[2]})

def get_alpha(m, a, b, epsilon, f):
    x_one = []
    x_two = []
    for i in range(m):
        x_one.append((a[i] + b[i]) / 2 - epsilon / 2)
        x_two.append((a[i] + b[i]) / 2 + epsilon / 2)
    if f_value(f,x_one)<=f_value(f,x_two):
        for i in range(m):
            b[i] = x_two[i]
    else:
        for i in range(m):
            a[i] = x_one[i]
    return [a,b]


def first_step(x_now, x_back, m, f, epsilon):
    for i in range(m):





def first_crit(x_now, x_back, m, epsilon):
    flag = True
    for i in range(m):
        if abs(x_now[i]-x_back[i])>epsilon:
            flag = False
            break
    return flag

def second_crit(f, x_now, x_back, m, epsilon):
    flag = True
    x_1, x_2, x_3 = symbols('x_1, x_2, x_3')
    for i in range(m):
        if abs(f.evalf(subs={x_1: x_now[0], x_2: x_now[1], x_3: x_now[2]})
               -f.evalf(subs={x_1: x_back[0], x_2: x_back[1], x_3: x_back[2]})
               )>epsilon:
            flag = False
            break
    return flag

def third_crit(grad_f,x_now, x_back, epsilon):
    flag = True
    x_1, x_2, x_3 = symbols('x_1, x_2, x_3')
    if abs(grad_value(grad_f,x_now) - grad_value(grad_f, x_back))>epsilon:
        flag = False
    return flag

def first_method():
    pass

def second_method():
    pass


def main():
    x_0 = [0,0,0]
   # x_start =
    x_1, x_2, x_3 = symbols('x_1, x_2, x_3')
    f = (x_1 - x_2) ** 3 + 0.1 * ((x_2 - 2*x_1) ** 3) + 10 * ((x_3 - 3) ** 3)
    df = [diff(f,x_1), diff(f,x_2), diff(f,x_3)]
    ddf = [
        [diff(df[0], x_1), diff(df[0], x_2), diff(df[0], x_3)],
        [diff(df[1], x_1), diff(df[1], x_2), diff(df[1], x_3)],
        [diff(df[2], x_1), diff(df[2], x_2), diff(df[2], x_3)]
    ]
    grad_f = df[0] + df[1] + df[2]
    #print("f:\t", f)
    #print("df:\t", df)
    #print("ddf:\t", ddf)
    #print(ddf_value(ddf, [0,0,0]))
    #print(first_crit([0,0,0], [1,1,1], 3, 0.5))
    #print(second_crit(f, [0,0,0], [1,2,3], 3, 1))
    #print(grad_f)
    #print(grad_value(grad_f,[1,0,0]))
    #print(third_crit(grad_f, [0,0,0], [1,1,1], 150.3))
    #print(get_alpha(3, [0,0,0], [5,5,5], 1, f))

    #print(f.evalf(subs={x_1: 1, x_2: 2, x_3: 3}))
    x_now = [0,0,0]
    x_back = [1,1,1]
    m=3
    epsilon = 0.1

    while (not first_crit(x_now, x_back, m, epsilon)) and (not second_crit(f, x_now, x_back, m, epsilon)) and (not third_crit(grad_f, x_now, x_back, epsilon)):
        #first_step
        break

main()

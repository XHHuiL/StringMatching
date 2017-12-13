# coding: utf-8
# created by liu hui

#############################
# naive string matching
# running time is
# O((n-m+1)*m) average case
#############################


def naive(t, p):
    n = len(t)
    m = len(p)
    s = []
    if n >= m:
        for i in range(n-m+1):
            if p == t[i:i+m]:
                s.append(i)
    return s


##############################################
# rabin karp string matching
# running time is
# O((n-m+1)*m) worst case
# 进行取模操作而不是乘法操作主要是如果字符集的基数
# 太大的话，那么预处理就不能在O(m)的时间内完成，此时
# 乘法操作不再是常数时间内完成
##############################################


def rabin_karp(t, p, d=128, q=127):
    n = len(t)
    m = len(p)
    h = pow(d, m-1) % q
    T = 0
    P = 0
    dif = n-m
    s = []

    # Preprocessing
    for i in range(m):
        P = (d*P+ord(p[i])) % q
        T = (d*T+ord(t[i])) % q

    # matching
    for i in range(n-m+1):
        if P == T:
            if p == t[i:i+m]:
                s.append(i)
        if i < dif:
            T = (d*(T - ord(t[i])*h) + ord(t[i+m])) % q
            if T < 0:
                 T = T + q
    return s


###################################
# finite automaton
# running time is
# O(m^3*|at|+n)
###################################


def finite_automaton(T, P, at):
    ta = compute_transition_function(P, at)
    n = len(T)
    m = len(P)
    q = 0
    s = []
    for i in range(n):
        q = ta[str(q)+T[i]]
        if q == m:
            s.append(i-m+1)
    return s


def compute_transition_function(p, at):
    m = len(p)
    ta = {}
    for q in range(m+1):
        for a in at:
            k = min(m, q+2)
            while not is_suffix(p[:k], p[:q]+a):
                k -= 1
            ta[str(q)+a] = k
    return ta


def is_suffix(s, t):
    m = len(s)
    n = len(t)
    if s == t[n-m:]:
        return True
    return False

#############################################
# Knuth-Morris-Pratt algorithm
# running time is
# O(m+n)
# all above algorithms , KMP is the best one
#############################################


def compute_prefix_function(P):
    m = len(P)
    pre = []
    pre.append(-1)
    k = -1
    for i in range(1, m):
        while k > -1 and P[k+1] != P[i]:
            k = pre[k]
        if P[k+1] == P[i]:
            k = k+1
        pre.append(k)
    return pre


def KMP(T, P):
    s =[]
    n = len(T)
    m = len(P)
    pre = compute_prefix_function(P)
    print(pre)
    q = -1
    for i in range(n):
        while q > -1 and P[q+1] != T[i]:
            q = pre[q]
        if P[q+1] == T[i]:
             q = q+1
        if q+1 == m:
            q = pre[q]
            s.append(i-m+1)
    return s


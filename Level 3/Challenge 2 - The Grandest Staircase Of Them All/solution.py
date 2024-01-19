def solution(n):
    # Represent polynomial as a list of coefficients from x^0 to x^n.
    # G_0 = 1
    G = [int(g_pow == 0) for g_pow in range(n + 1)]
    for k in range(1, n):
        # G_k = G_{k-1} * (1 + x^k)
        # This is equivalent to adding G shifted to the right by k to G
        # Ignore powers greater than n since we don't need them.
        G = [G[g_pow] if g_pow - k < 0 else G[g_pow] + G[g_pow - k] for g_pow in range(n + 1)]
    return G[n]

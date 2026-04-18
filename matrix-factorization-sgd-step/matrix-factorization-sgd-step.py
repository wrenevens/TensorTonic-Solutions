def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here
    dot = 0.0
    for i in range(len(U)):
        dot += U[i] * V[i]

    e = r - dot

    U_new = [U[i] + lr * (e * V[i] - reg * U[i]) for i in range(len(U))]
    V_new = [V[i] + lr * (e * U[i] - reg * V[i]) for i in range(len(V))]

    return U_new, V_new
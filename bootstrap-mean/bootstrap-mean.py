import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    x = np.array(x)
    N = len(x)
    if not rng:
        rng = np.random.default_rng()

    rng_indices = rng.integers(0, N, size=(n_bootstrap, N))
    boot_x = x[rng_indices]

    alpha = 1 - ci
    boot_mean = np.mean(boot_x, axis=-1)
    lower, upper = np.percentile(boot_mean, [
        alpha/2 * 100,
        (1-alpha/2) * 100
    ])

    return boot_mean, float(lower), float(upper)
    
    
    
    


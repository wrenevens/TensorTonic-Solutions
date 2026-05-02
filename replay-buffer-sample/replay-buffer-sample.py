import numpy as np
def replay_buffer_sample(buffer, batch_size, seed):
    """
    Sample a batch of transitions from the replay buffer.
    """
    # Write code here
    sampler = np.random.RandomState(seed)
    buffer = np.array(buffer)

    indices = np.arange(len(buffer))
    picked = sampler.choice(indices, size=batch_size, replace=False)

    return buffer[picked]
    
    
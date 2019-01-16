import flom

import trainer

def train(motion, output, robot, timestep=0.0165/4, frame_skip=4, chunk_length=3, num_iteration=1000, num_chunk=50, weight_factor=0.01):
    m = flom.load(motion)
    trained = trainer.train(m, robot, timestep, frame_skip, chunk_length, num_iteration, num_chunk, weight_factor)
    trained.dump(output)

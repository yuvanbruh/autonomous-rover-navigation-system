import matplotlib.pyplot as plt

def render_world(world):

    # plt.figure(figsize=(8,8))

    plt.imshow(world, cmap='tab20')

    plt.title("Mars Environment")

    plt.colorbar()

    # plt.show()

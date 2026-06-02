import matplotlib.pyplot as plt

def render_world(world,
                 current_state,
                 battery):

    plt.imshow(
        world,
        cmap="gray",
        origin="upper"
    )
    

    plt.title(
    f"State: {current_state} | Battery: {battery:.1f}",
    fontsize=14,
    fontweight="bold"
)

    plt.xlabel("Y Position")
    plt.ylabel("X Position")
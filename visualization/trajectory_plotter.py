import matplotlib.pyplot as plt


def plot_trajectory(

    true_x,
    true_y,

    gps_x,
    gps_y,

    ekf_x,
    ekf_y

):

    # separate localization window

    plt.figure(2)

    # clear previous frame

    plt.clf()


    # true rover trajectory

    plt.plot(

        true_y,
        true_x,

        'b-',

        linewidth=2,

        label='True Path'

    )


    # noisy GPS trajectory

    plt.plot(

        gps_y,
        gps_x,

        'r.',

        markersize=4,

        label='GPS Measurements'

    )


    # EKF filtered trajectory

    plt.plot(

        ekf_y,
        ekf_x,

        'g-',

        linewidth=2,

        label='EKF Estimate'

    )


    # fixed visualization bounds

    plt.xlim(0, 100)

    plt.ylim(0, 100)


    # title

    plt.title("Localization")


    # grid

    plt.grid(True)


    # legend

    plt.legend()


    # live update pause

    plt.pause(0.001)
import matplotlib.pyplot as plt 

def render_rover(state):
    plt.plot(state.y, state.x ,  'ko', markersize=8)
    
    
    
def render_lidar(obstacle):
        for obstacle in obstacle:
          x,y = obstacle
          plt.plot(y,x, "bo", markersize=4)    
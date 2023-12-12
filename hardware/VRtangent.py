import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def find_tangent(circle_center, circle_radius, ellipse_center, a, b):
    def equations(p):
        x, y, u, v = p
        circle_eq = (x - circle_center[0])**2 + (y - circle_center[1])**2 - circle_radius**2
        ellipse_eq = ((u - ellipse_center[0])/a)**2 + ((v - ellipse_center[1])/b)**2 - 1
        tangent_line_eq1 = (x - circle_center[0])*(u - x) + (y - circle_center[1])*(v - y)
        tangent_line_eq2 = (b**2)*(u - ellipse_center[0])*(u - x) + (a**2)*(v - ellipse_center[1])*(v - y)
        return (circle_eq, ellipse_eq, tangent_line_eq1, tangent_line_eq2)
    
    # Initial guess
    x0, y0 = circle_center[0] + circle_radius, circle_center[1]
    u0, v0 = ellipse_center[0] + a, ellipse_center[1]
    
    solution = fsolve(equations, (x0, y0, u0, v0))
    
    x, y, u, v = solution
    distance = np.sqrt((u - x)**2 + (v - y)**2)
    
    print("Point of tangency on the circle:", (x, y))
    print("Point of tangency on the ellipse:", (u, v))
    print("Distance between points of tangency:", distance)
    
    return (x, y), (u, v)

def plot_shapes(circle_center, circle_radius, ellipse_center, a, b, tangent_points):
    fig, ax = plt.subplots()
    
    # Plot the circle
    circle = plt.Circle(circle_center, circle_radius, fill=False, edgecolor='r', linewidth=0.5)
    ax.add_patch(circle)
    
    # Plot the ellipse
    ellipse = plt.matplotlib.patches.Ellipse(ellipse_center, 2*a, 2*b, fill=False, edgecolor='b', linewidth=0.5)
    ax.add_patch(ellipse)
    
    if tangent_points is not None:
        # Plot the tangent line between the tangency points
        point_circle, point_ellipse = tangent_points
        plt.plot([point_circle[0], point_ellipse[0]], [point_circle[1], point_ellipse[1]], 'g--')
        
        # Plot the line from the center of the circle to the tangent point on the circle
        plt.plot([circle_center[0], point_circle[0]], [circle_center[1], point_circle[1]], 'm--')
    
    # Set the aspect of the plot to be equal
    ax.set_aspect('equal', 'box')
    
    # Set limits
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    
    plt.grid(True)
    plt.show()


# Example usage:
circle_center = (0, 0)
circle_radius = 10
ellipse_center = (0, -8)
a = 4
b = 3
#tangent_points = find_tangent(circle_center, circle_radius, ellipse_center, a, b)
#plot_shapes(circle_center, circle_radius, ellipse_center, a, b, tangent_points)

# After finding the tangent points
tangent_points = find_tangent(circle_center, circle_radius, ellipse_center, a, b)
# Pass them to the updated plot_shapes function
plot_shapes(circle_center, circle_radius, ellipse_center, a, b, tangent_points)
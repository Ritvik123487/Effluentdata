import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_plot(input1, input2):
    def x(input1):
         #BOD
        input1 = input1*(100-60)/100*0.4
        return input1

    def y(input2):
        #COD
        input2 = input2*(100-60)/100*0.4
        return input2

    # Calculate the values of x and y for the original data point
    x_orig = x(input1)
    y_orig = y(input2)
    # Create empty lists to store the values of x and y
    x_values = [x_orig]
    y_values = [y_orig]

    ct=0
    while ct < 5:
        input1 = input1*1.25
        input2 = input2*1.25
        ct+=1
        x_val = x(input1)
        y_val = y(input2)
        x_values.append(x_val)
        y_values.append(y_val)

    # Create the line graph using matplotlib
    x_vals = x_values
    y_vals = y_values

    # Create a line plot
    plt.plot(x_vals, y_vals, marker='o', markersize=8, linestyle='-', linewidth=2)
    plt.axvline(x=1200, color='red')

    # Draw a red line on y axis at a value of 4500
    plt.axhline(y=4500, color='red')
    # Add axis labels and a title
    plt.xlabel('BOD')
    plt.ylabel('COD')
    plt.title('BOD and COD Output Levels')

    # Add labels to the data points
    for i, (x_val, y_val) in enumerate(zip(x_values, y_values)):
        plt.annotate(f"({x_val:.2f}, {y_val:.2f})", xy=(x_val, y_val), xytext=(10,-10),
                    textcoords='offset points', ha='left', va='top', fontsize=8)
    plt.legend()

    # Save the plot to a BytesIO object and encode it as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return plot_data
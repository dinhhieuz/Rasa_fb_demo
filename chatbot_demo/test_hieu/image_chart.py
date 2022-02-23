# from matplotlib import colors, pyplot as plt
# import pandas as pd
# import numpy as np

# speed = [0.1, 17.5, 40, 48, 52, 69, 88]
# lifespan = [2, 8, 70, 1.5, 25, 12, 28]
# index = ['snail', 'pig', 'elephant',
#         'rabbit', 'giraffe', 'coyote', 'horse']
# df = pd.DataFrame({'speed': speed,
#               'lifespan': lifespan}, index=index)

# trend_df_hours = pd.Series(np.random.rand(10))
# trend_df_qty = pd.Series(np.random.rand(10))

# fig0, ax0 = plt.subplots()
# ax1 = ax0.twinx()
# trend_df_hours.plot(kind='bar', stacked=True, ax=ax0, title="hihihi", legend = True)
# trend_df_qty.plot(kind='line', secondary_y=True, ax=ax1)
# plt.show()
# plt.close()
#!--------------------------
# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

def line_chart(data = None, x_label = None, y_bar = [], y_line = [], color_bar = ['blue', 'yellow'], color_line = 'green', width =  .40):

    data[y_bar].plot(kind='bar', width = width, color = color_bar, title = "Chi tiết doanh thu")
    data[y_line].plot(kind='line', color = color_line, legend='Reverse')
    #---secondary_y: chỉ lấy đoạn dữ liệu đầu và cuối để vẽ line: df['normal'].plot(secondary_y=True)
    plt.xticks(rotation = 80)

    ax = plt.gca()
    #--- Gạch mức ở biểu đồ: ax.axhline(.75, color='k', ls='--')
    for l in range (len(y_bar)):
        ax.bar_label(ax.containers[l], labels=[f'{p.get_height():,.0f}' for p in ax.containers[l]], rotation=90, padding=3)
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    # plt.xlim([-width, len(data[y_line])-width])
    ax.set_xticklabels(data[x_label])
    # figure = plt.gcf()  # get current figure
    # figure.set_size_inches(32, 18) # set figure's size manually to your full screen (32x18)
    # plt.savefig(f'../{name_img}', format='png', bbox_inches='tight',dpi = 300)
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(18.5, 10.5, forward=True) # set figure's size manually to your full screen (32x18)
    
    plt.show()
    #bbox_inches: remove white space
    #dpi: resource inch of image
data = pd.DataFrame({
    'loi_nhuan' : [90,40,30,30,31,25,25],
    'chi_phi' : [100,70,65,70,11,60,50],
    'doanh_thu' : [200,160,170,111,190,200,210],
    'thoi_gian' : ['2021-01-03','2021-06-13','2021-05-13','2021-11-03','2021-11-03','2021-01-13','2021-01-04']})
bar = ['doanh_thu','chi_phi']
line = 'loi_nhuan'
x = 'thoi_gian'
line_chart(data = data, x_label = x, y_bar = bar, y_line = line, color_bar = ['#02b4f0', '#cf4f25' ], color_line='#045220', width =  .40)

# plt.bar([0,1,2,3], [100,200,300,400])
# ax = plt.gca()
# plt.bar_label(ax.containers[0])
# for container in ax.containers:
#     plt.bar_label(container)

# plt.show()
# %%
import matplotlib.pyplot as plt
import numpy as np

errorRateListOfFast = ['9.09', '9.09', '9.38', '9.40', '7.89', '8.02', '10.00']
errorRateListOfSlow = [10, '13.04', '14.29', '12.50', '14.29', '14.53', '11.11']

# Convert to floats
errorRateListOfFast = [float(x) for x in errorRateListOfFast]
errorRateListOfSlow = [float(x) for x in errorRateListOfSlow]

opacity = 0.4
bar_width = 0.35

plt.xlabel('Tasks')
plt.ylabel('Error Rate')
plt.title('Add text for each bar with matplotlib')

plt.xticks(range(len(errorRateListOfFast)),('[10-20)', '[20-30)', '[30-50)', '[50-70)','[70-90)', '[90-120)', ' [120 < )'), rotation=30)
bar1 = plt.bar(np.arange(len(errorRateListOfFast)) + bar_width, errorRateListOfFast, bar_width, align='center', alpha=opacity, color='b', label='Fast <= 6 sec.')
bar2 = plt.bar(range(len(errorRateListOfSlow)), errorRateListOfSlow, bar_width, align='center', alpha=opacity, color='r', label='Slower > 6 sec.')
errorRateListOfSlow.plt.line()
# Add counts above the two bar graphs
for rect in bar1 + bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.0f}', ha='center', va='bottom')

plt.legend()
plt.tight_layout()
plt.show()

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bring some raw data.
frequencies = [6, -16, 75, 160, 244, 260, 145, 73, 16, 4, 1]

# In my original code I create a series and run on that,
# so for consistency I create a series from the list.
freq_series = pd.Series.from_array(frequencies)

x_labels = [108300.0, 110540.0, 112780.0, 115020.0, 117260.0, 119500.0,
            121740.0, 123980.0, 126220.0, 128460.0, 130700.0]

# Plot the figure.
plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind='bar')
ax.set_title('Amount Frequency')
ax.set_xlabel('Amount ($)')
ax.set_ylabel('Frequency')
ax.set_xticklabels(x_labels)


def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.


# Call the function above. All the magic happens there.
add_value_labels(ax)

# %%

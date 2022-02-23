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
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

def bar_chart(data = None, x_label = None, y_bar = [], color_bar = ['blue', 'yellow'], width =  .40):

    data[y_bar].plot(kind='bar', width = width, color = color_bar, title = "Chi tiết doanh thu")
    # data[y_line].plot(kind='line', color = color_line, legend='Reverse')
    #---secondary_y: chỉ lấy đoạn dữ liệu đầu và cuối để vẽ line: df['normal'].plot(secondary_y=True)

    ax = plt.gca()
    #--- Gạch mức ở biểu đồ: ax.axhline(.75, color='k', ls='--')
    #- show label on head columns
    for l in range (len(y_bar)):
        ax.bar_label(ax.containers[l], labels=[f'{p.get_height():,}' for p in ax.containers[l]])
    # convert formart number yaxis to VNĐ
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    # for container in ax.containers:
        # plt.bar_label(container,)
    plt.xlim()
    ax.set_xticklabels(data[x_label])
    # ax.axis('tight')
    # plt.show()
    # plt.close()
    fig = plt.gcf()  # get current figure
    # figure.set_size_inches(32, 18) # set figure's size manually to your full screen (32x18)
    fig.set_size_inches(18.5, 10.5, forward=True)
    
    # plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]
    # fig.savefig('test2png.png', dpi=100)
    plt.savefig('filename.png', bbox_inches='tight',dpi = 70)
    # plt.show()
    #bbox_inches: remove white space
    #dpi: resource inch of image
data = pd.DataFrame({
    'loi_nhuan' : [90,40,30,30,31,25,25],
    'chi_phi' : [100,70,65,70,11,60,50],
    'doanh_thu' : [200,160,170,111,190,200,210],
    'thoi_gian' : ['2021-01-03','2021-06-13','2021-05-13','2021-11-03','2021-11-03','2021-01-13','2021-01-04']})
dataa = pd.DataFrame({
    'doanh_thu' : [200, 160],
    'cua_hang' : ['CH1', 'CH2']
})
bar = ['doanh_thu']
line = 'loi_nhuan'
x = 'cua_hang'
bar_chart(data = dataa, x_label = x, y_bar = bar, color_bar = ['#cf4f25', '#02b4f0'], width =  .40)

# plt.bar([0,1,2,3], [100,200,300,400])
# ax = plt.gca()
# plt.bar_label(ax.containers[0])
# for container in ax.containers:
#     plt.bar_label(container)

# plt.show()
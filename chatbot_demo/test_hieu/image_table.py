from numpy.core.fromnumeric import shape
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import six

# df['date'] = ['2016-04-01', '2016-04-02', '2016-04-03', '2016-04-04']
# df['calories'] = [2200, 2100, 1500, 1800]
# df['sleep hours'] = [2200, 2100, 1500, 1500]
# df['gym'] = [True, False, False, True]

#---Param: df


def table (df = None, title = ""):
    df = pd.DataFrame(df)
    #----- Set column STT from Index
    df.index = np.arange(1, len(df) + 1)
    df = df.rename_axis('STT').reset_index()

    def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                        header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                        bbox=[0, 0, 1, 1], header_columns=0,
                        ax=None, **kwargs):
        if ax is None:
            size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
            fig, ax = plt.subplots(figsize=size)
            #Title of table
            ax.set_title(title, fontdict={'fontsize':13, 'fontweight':23,'verticalalignment': 'baseline'})
            ax.axis('off')
        ax.axis([0,1,data.shape[0],-1]) ## <---------- Change here
        #---Param: Title table
        mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
        mpl_table.auto_set_font_size(False)
        mpl_table.set_fontsize(font_size)
        mpl_table.auto_set_column_width(col=list(range(len(df.columns))))
        for k, cell in six.iteritems(mpl_table._cells):
            cell.set_edgecolor(edge_color)
            if k[0] == 0 or k[1] < header_columns:
                cell.set_text_props(weight='bold', color='w')
                cell.set_facecolor(header_color)
            else:
                cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
        return ax


    def set_row_edge_color(ax, row, column, color):
        #--Grid Row in the table
        # (có viền ngoài)
        for x in range(-1, row+1): ax.axhline(x, color=color)
        # (có viền không viền)
        # for x in range(row): ax.axhline(x, color=color)
        #--Grib Column in the table
        for y in range(column): ax.axvline(y, color=color)
        # print(column)
        # ax.axvline(0, color=color)
        # ax.axvline(2, color=color)
        # ax.axvline(-1, color=color)
        # ax.axvline(column+1, color=color)

    ax = render_mpl_table(df, header_columns=0, col_width=3.0)
    set_row_edge_color(ax, df.shape[0], df.shape[1], 'k')
    plt.show()
    # plt.savefig('foo.png')

df = {
        'Hàng hó3a': ['kệ kễ kề kệkệkệkệkệkệkệkệ', 'ghế', 'tủ', 'hoa',None],
        'Hàng hóa': ['kệ kễ kề kệkệkệkệkệkệkệkệkệkệkệkệ', 'ghế', 'tủ', 'hoa',None],
        'Số lượng': [5.001, 0.4354, 243324, 65.234, ''],
        'Hàng bán': ['kệ kễ kề kệ', 'ghế', 'tủ', 'hoa','hóa'],
        'Hàng b3n': ['kệ kễ kề kệ', 'ghế', 'tủ', 'hoa','hóa']
      }
table(df,"Top 10 Fields of Research by Aggregated Funding Amount")
#!--------------------------------------------
# from matplotlib import pyplot as plt
# import pandas as pd
# # Create some example data
# data = [{"Movie": "Happy Gilmore", "Lead Actor": "Adam Sandler" , "Year": "1996", 
#               "Plot": "An ice hockey star takes up golfing.", 
#               "Quotes": "\"Just give it a little tappy. Tap tap taparoo.\""}]
# dff = pd.DataFrame(data)
# fig, ax = plt.subplots(3,1, figsize=(10,4))

# tab0 = ax[0].table(cellText=dff.values, colLabels=dff.columns, loc='center', cellLoc='center')
# ax[0].set_title("Default")
# tab1 = ax[1].table(cellText=dff.values, colLabels=dff.columns, loc='center', cellLoc='center')
# ax[1].set_title("Font AutoSize off")
# tab2 = ax[2].table(cellText=dff.values, colLabels=dff.columns, loc='center', cellLoc='center')
# ax[2].set_title("Column Width Auto Set, Font AutoSize off")
# [a.axis("off") for a in ax]
# [t.auto_set_font_size(False) for t in [tab1, tab2]]
# [t.set_fontsize(8) for t in [tab1, tab2]]

# tab2.auto_set_column_width(col=list(range(len(dff.columns)))) # Provide integer list of columns to adjust
# plt.show()
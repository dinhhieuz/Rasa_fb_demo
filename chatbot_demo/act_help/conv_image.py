from os import error
import matplotlib.pyplot as plt
import dataframe_image as dfi
import numpy as np
import datetime
import pandas as pd
from numpy.core.fromnumeric import shape
import matplotlib as mpl
import six
from sqlalchemy import column, false
class conv_image:

    def bar_chart(data = None, x_label = None, y_bar = [], color_bar = ['blue', 'yellow'], width =  .40, name_img = '', title= ''):
        try:
            data[y_bar].plot(kind='bar', width = width, color = color_bar, title = title)
            ax = plt.gca()
            for l in range (len(y_bar)):
                ax.bar_label(ax.containers[l], labels=[f'{p.get_height():,}' for p in ax.containers[l]])
            # convert formart number yaxis to VNĐ
            ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
            plt.xlim()
            ax.set_xticklabels(data[x_label])
            figure = plt.gcf()  # get current figure
            figure.set_size_inches(18.5, 10.5, forward=True) # set figure's size manually to your full screen (32x18)
            plt.savefig(f'../{name_img}', format='png', bbox_inches='tight',dpi = 80)
        except Exception as error:
            print('[convert_bar_chart]->' + error)
            return 0

    def bar_line_chart(data = None, x_label = None, y_bar = [], y_line = [], color_bar = ['blue', 'yellow'], color_line = 'green', title = "", name_img = None, width =  .44):
        try:
            data = (data.reset_index()).drop("index", axis=1)
            data[y_bar].plot(kind='bar', width = width, color = color_bar, title = title, xlabel=x_label, legend=False)
            data[y_line].plot(kind='line', color = color_line, legend='Reverse', fontsize = 10)
            #---secondary_y: chỉ lấy đoạn dữ liệu đầu và cuối để vẽ line: df['normal'].plot(secondary_y=True)
            #--Nhãn ở dưới trục x
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
            plt.savefig(f'../{name_img}', format='png', bbox_inches='tight',dpi = 80)

            return 1
        except Exception as error:
            print('[convert_chart]->' + error)
            return 0

    def table(df = None, name_img = None, title = ""):
        
        try:
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
                    ax.set_title(title, fontdict={'fontsize':18, 'fontweight':28,'verticalalignment': 'baseline'})
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
                for x in range(-1, row+1): ax.axhline(x, color=color)
                #--Grib Column in the table
                # for y in range(column+1): ax.axvline(y/column, color=color)
                for y in range(column): ax.axvline(y, color=color)

            ax = render_mpl_table(df, header_columns=0, col_width=2.0)
            set_row_edge_color(ax, df.shape[0], df.shape[1], 'k')
            # Export Styled Table to PNG
            #---File đang đứng ở chatbot_demo
            plt.savefig(f'../{name_img}', format='png', bbox_inches='tight',dpi = 80)
            
            return 1
        except Exception as error:
            print('[convert_table]->' + error)
            return 0
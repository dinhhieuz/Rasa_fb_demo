# #------ Code: Create Image Chart
# import matplotlib.pyplot as plt
# import numpy as np
# import datetime
# fig = plt.figure()

# x = np.arange(0, 10, 0.1)
# y = np.sin(x)
# name_chart = "{:%Y-%m-%d_%Hh-%Mm-%Ss}".format(datetime.datetime.now())
# plt.plot(x, y)
# fig.savefig(f'../../assets/{name_chart}.png')
# plt.close()

# # -------- Code: Commit File to Github
import base64
from github import Github
from github import InputGitTreeElement

token = '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'
g = Github(token)
repo = g.get_user().get_repo('Rasa_fb_demo')
file_list = [
    '../../assets/mytable.png'
]
commit_message = 'Add simple regression analysis'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)
element_list = list()
for entry in file_list:
    with open(entry, 'rb') as input_file:
        data = input_file.read()
    if entry.endswith('.png'):
        data = base64.b64encode(data).decode('utf-8')
    element = InputGitTreeElement(entry, '100644', 'blob', data)
    element_list.append(element)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)
""" An egregious hack to change the PNG contents after the commit """
for entry in file_list:
    with open(entry, 'rb') as input_file:
        data = input_file.read()
    if entry.endswith('.png'):
        old_file = repo.get_contents(entry)
        commit = repo.update_file('assets/'+old_file.path, 'Update PNG content', data, old_file.sha)

# ------------- Code: Create Image Table
# #!-
# import dataframe_image as dfi
# import numpy as np
# import pandas as pd

# df = pd.DataFrame({
#     'Fruits': ['Apple', 'Apple', 'Apple', 'Orange', 'Banana', 'Orange'],
#     'BuyPrice': [1000, 3000, 2400, 3000, 800, 1500],
#     'SellPrice': [1200, 2800, 2500, 2500, 700, 1750]
# })

# # Add Profit percentage column
# df['Profit'] = (df['SellPrice'] - df['BuyPrice']) / df['BuyPrice']

# # Rename column titles
# df = df.rename({'BuyPrice': 'Buy Price', 'SellPrice': 'Sell Price'}, axis=1)
# # Highlight positive and negative profits
# def highlight_cols(s):
#     return np.where(s < 0, 'color: red', 'color:green')


# # CSS for col_headings
# headers = {
#     'selector': 'th.col_heading',
#     'props': 'background-color: orange; color: white;'
# }

# # CSS for rows
# rows = [
#     {
#         'selector': 'tbody tr:nth-child(even)',
#         'props': 'background-color: lightgray'
#     },
#     {
#         'selector': 'tbody tr:nth-child(odd)',
#         'props': 'background-color: white'
#     }
# ]

# styler = (
#     df.reset_index()  # make current index a column
#     .style  # Create Styler
#     .hide_index()  # Hide new index (since old index is a column
#     .apply(
#         # apply highlighter function to Profit Column
#         highlight_cols, axis=0, subset=['Profit']
#     )
#     .format(
#         # apply percentage formatting to Profit Column
#         formatter='{:.2%}', subset=['Profit']
#     )
#     .set_table_styles([headers, *rows])  # add CSS
# )
# # Export Styled Table to PNG
# dfi.export(styler, 'table_f3ruits.png')


# -----------------------------------------------------------------------------------

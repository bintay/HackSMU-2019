import numpy as np
import pandas as pd
import csv
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.layouts import layout,widgetbox
from bokeh.models import Toggle, BoxAnnotation, CustomJS, Circle, HoverTool, ColumnDataSource, NumeralTickFormatter, OpenURL, TapTool
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn, Panel, Tabs, DateFormatter,TextInput, Button, Toggle
from datetime import date





output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")

# x = master_sheet['soft_index']
# y = master_sheet['tech_index']
# appending values from local csv
df = pd.read_csv("lel.csv")
sample = df.sample(50)
source = ColumnDataSource(sample)

# # output to static HTML file (with CDN resources)

TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select, tap"

# create a new plot with the tools above, and explicit ranges


p = figure(tools=TOOLS, title="Applicant Pool",x_range=(0, 12), y_range=(0, 12))
p.xaxis.axis_label = "Tech Compotency Index"
p.xaxis.axis_label_text_color = "#aa6666"

p.yaxis.axis_label = "Soft Skill Index"
p.yaxis.axis_label_text_color = "blue"

hover = HoverTool()
hover.tooltips=[
    ('Name', '@first_name'),
    ('Soft Skill Index', '@soft_index'),
    ('Tech Compotency Index', '@tech_index'),
    ('Code Duration', '@code_time'),
    ('Code Attempts','@code_attempts'),
    ('Date of Submission','@date'),
    ('Email','@email')
]

p.add_tools(hover) 

p.circle(x = 'tech_index', y = 'soft_index', source = source,  size=20,

                       # set visual properties for selected glyphs
                       selection_color="firebrick",

                       # set visual properties for non-selected glyphs
                       nonselection_fill_alpha=0.2,
                       nonselection_fill_color="blue",
                       nonselection_line_color="firebrick",
                       nonselection_line_alpha=1.0)





box = BoxAnnotation(bottom =0, top = 5, left=0, right=5, fill_color='#F01716', fill_alpha=0.1)
p.add_layout(box)



tab1 = Panel(child=p, title="Applicant Comparison Graph")




columns = [
        TableColumn(field="first_name", title="Applicant Name"),
        TableColumn(field="email", title="Email"),
        TableColumn(field="date", title="Date of Submission", formatter=DateFormatter()),
        TableColumn(field="code_time", title="Duration of Code"),
        TableColumn(field="code_attempts", title="Attempts"),
        TableColumn(field="soft_index", title="Soft Skills Index"),
        TableColumn(field="tech_index", title="Tech Skills Index")
    ]

data_table = DataTable(source=source, columns=columns, width=1300, height=1000)

tab2 = Panel(child = data_table, title= "Table")


text_input = TextInput(title="Search for Applicant:")
taptool = p.select(type = TapTool)
url = "http://www.colors.commutercreative.com/@color/"
taptool.callback = OpenURL(url=url)




# def search(strin):
#     text_value = text_input.value

#     if df['first_name'].match(text_value) == True:
#         return df.loc[df['first_name'] == text_value]
#     else:
#         return False
    

tabs = Tabs(tabs=[ tab1, tab2 ])
# show the results
# search(text_input)
show (tabs)




import numpy as np
import pandas as pd
import csv
from bokeh.themes import built_in_themes
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.layouts import layout,widgetbox
from bokeh.models import Toggle, BoxAnnotation, CustomJS, Circle, HoverTool, ColumnDataSource, NumeralTickFormatter, OpenURL, TapTool, Selection
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn, Panel, Tabs, DateFormatter,TextInput, Button, Toggle
from datetime import date

curdoc().theme = 'dark_minimal'
output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")


df = pd.read_csv("lel.csv")
sample = df.sample(50)
source = ColumnDataSource(sample)


TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select, tap"



p = figure(tools=TOOLS, title="Applicant Pool",x_range=(0, 1.1), y_range=(0, 1.1))
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


box = BoxAnnotation(bottom =0, top = 0.5, left=0, right=0.5, fill_color='#F01716', fill_alpha=0.1)
p.add_layout(box)



tab1 = Panel(child=p, title="Applicant Comparison Graph")




columns = [
        TableColumn(field="first_name", title="Applicant Name"),
        TableColumn(field="email", title="Email"),
        TableColumn(field="date", title="Date of Submission", formatter=DateFormatter()),
        TableColumn(field="code_time", title="Duration of Code"),
        TableColumn(field="soft_index", title="Soft Skills Index"),
        TableColumn(field="tech_index", title="Tech Skills Index")
    ]

data_table = DataTable(source=source, columns=columns, width=1300, height=1000)
text_input = TextInput(title="Search for Applicant:")
# def selectdata():
#     highlight = text_input.value
#     selected = df
   
#     selected = selected[selected.first_name.str.contains(highlight)==True]
    
#     return selected


l = layout([text_input],[data_table])
tab2 = Panel(child = l, title= "Table")


taptool = p.select(type = TapTool)
url = "http://www.colors.commutercreative.com/@color/"
taptool.callback = OpenURL(url=url)


tabs = Tabs(tabs=[ tab1, tab2 ])

# selectdata()

show (tabs)




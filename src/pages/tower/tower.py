# package imports
import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

# local imports
from utils.utils import id_factory
id = id_factory('tower')
from .functions import *
from data.tower_data import *

# page registration
dash.register_page(
    __name__,
    path='/tower',
    title='Monitoring data of the Leaning Tower of Pisa'
)


#==============
#    LAYOUT
#==============
# The layout is divided into Tabs. To make everything
# as clear as possible, the tabs are defined first,
# then recalled into the outer lebel.

#------------
#    TABS
#------------
# TOWER PLAN Tab
#----In this tab you can plot the displacements of benchmarks
#----in the Tower and in the Catino, choosing from a plan view

# standalone figures
## FIX: these two functions are practically the same: unify them
t_fig_bench_sel = figureBenchSelection(T_CAPRARO_BENCHMARKS)
t_fig_stabil_bench_sel = figureBenchStabilSelection(T_STABIL_COORDS)

# tab itself
t_tab_plan= dbc.Tab([
    html.Div([
        html.Br(),
        html.P("This tab contains plots of levelling measurement of the tower",
          style=dict(color='grey', fontSize='small'))
    ]),
    html.Div([
        html.H2('Plan view of the benchmarks'),
        dcc.Markdown(
            """
            Select, using the pictures, the prisms for which you would like to produce displacement plots.
            Selection can be done:
            - by clicking (hold Shift or Ctrl for multiple selection);
            - using the Lasso- or Box-selection tools (on the toolbar).
            """
        ),
        html.Br(),
        dcc.Markdown("Circle benchmarks are also part of the altimetric monitoring of the square, unlike the diamond-shaped ones."),
    ]),
    html.Div([
            dbc.Row([
                dbc.Col([
                    dcc.Markdown('**Levelling during 2002-2022:**',),
                    dcc.Graph(id=id('fig_bench_displacement_selection'), figure=t_fig_bench_sel),
                ],
                    width=6, align='left'
                ),
                dbc.Col([
                    dcc.Markdown('**Levelling during soil freezing and application of lead weights (1995-1999):**'),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    dcc.Graph(id=id('fig_stabil_bench_displacement_selection'), 
                    figure=t_fig_stabil_bench_sel),
                ],
                    width=6, align='right'
                ),
            ]),
    ]),
    html.Br(),
    html.Div(id=id('div_bench_displacement_plots')),
    html.Br(),
    html.Div(id=id('div_stabil_bench_displacement_plots')),
],
    label='LEVELLING PLAN'
)


# TOWER SECTION Tab
#----In this tab you can plot the displacements of benchmarks
#----in the Tower and in the Catino, as seen in section view

# standalone figures
t_rot_tower = rot_tower(T_CAPRARO_DATA)

# the tab itself
t_tab_section = dbc.Tab([
    html.Div([
        html.Br(),
        html.P(
            "This tab contains plots of benchmarks in section view.",
            style=dict(color='grey', fontSize='small')
        )
    ]),
    html.Div([
        html.H2("Section view of the benchmarks"),
        dcc.Markdown(
            """
            Select, using the slider on the side, the section whose displacements you want to see. \n
            A resampling of the data can be done with the slider immediately below.
            """
        ),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id=id('fig_bench_section')),
            ],
                width=9, align='center'
            ),
            dbc.Col([
                dcc.Markdown('**Select a section**'),
                dcc.Slider(
                    id=id('slider_bench_section_selection'),
                    min=1, max=4, step=1,
                    value=1,
                    updatemode='drag'
                ),
                dcc.Graph(
                    id=id('fig_bench_section_selection'),
                    config=dict(
                        displayModeBar=False,
                    )
                ),
                html.Br(),
                dcc.Markdown("**Resampling of data**"),
                dcc.Slider(
                    id=id('slider_bench_section_resample'),
                    min=0, max=6, step=1,
                    value=6,
                    marks={
                        0: 'M',
                        1: '2M',
                        2: '4M',
                        3: '6M',
                        4: '8M',
                        5: '10M',
                        6: '12M'
                    },
       
                    updatemode='drag'
                ),
                dcc.Markdown(id=id('text_bench_section_resample')),
            ], 
                width=3, align='top'
            )
        ])
    ]),
    html.Div(id=id('div_rot'))
],
    label='LEVELLING SECTIONS'
)


# TOWER STATIC MONITORING Tab
#----In this tab you can plot and export data from static
#----monitoring of the Tower

# accordion for sensor selection
from data.tower.static_sensor_list import t_sensor_dict

t_accordion_static_sensors = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                dbc.Checklist(
                    options=[
                        {
                            'label': sensor,
                            'value': sensor
                        }
                        for sensor in t_sensor_dict[sensor_group]
                    ],
                    id=id('static_selection_'+sensor_group)
                ),
                title=sensor_group
            )
            for sensor_group in t_sensor_dict.keys()
        ],
        start_collapsed=True,
    ),
)

# t_accordion_static_sensors = html.Div(
#     [
#         dbc.Checklist(
#             options=[
#                 {
#                     'label': sensor,
#                     'value': sensor
#                 }
#                 for sensor in t_sensor_dict['others']
#             ],
#             id='cicciopasticcio'
#         )
#     ],
#     style={'height': '100px'}
# )

# the tab itself
t_tab_static= dbc.Tab([
    html.Div([
        html.Br(),
        html.P("This tab is for plotting and exporting static monitoring data of the Tower.",
          style=dict(color='grey', fontSize='small'))
    ]),
    html.Div([
        html.H2('Static monitoring data'),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        t_accordion_static_sensors,
                    ],
                    style={ "overflow-y":"scroll", "height": "300px"},
                ),
                dbc.Col(
                    [
                        dbc.Button(
                            "Select all",
                            color="primary",
                            id=id('button_select_all_static')
                        ),
                        html.Br(),
                        dbc.Button(
                            "Deselect all",
                            color="danger",
                            id=id('button_deselect_all_static')
                        )
                    ],
                ),
                dbc.Col(
                    [
                        dbc.Textarea(placeholder="Sensor codes separated by a comma"),
                    ]
                )
            ],
            align='start',
        ),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Markdown('Superimpose the plots of all sensors?'),
                dbc.Checklist(
                    options=[
                        {"label": 'Together', 'value':1}
                    ],
                    switch=True,
                    value=[0],
                    id=id('switch_static_together')
                )
            ]),
            dbc.Col([
                dcc.Markdown('Date range:'),
                dcc.DatePickerRange(
                    clearable=True,
                    start_date = '1993-01-01',
                    end_date = '2023-12-31',
                    min_date_allowed = '1993-01-01',
                    max_date_allowed = '2023-12-31', ## FIX: how to set dates appropriately
                    id=id('datepicker_static')
                )
            ]),
            dbc.Col([
                dcc.Markdown('Resample:'),
                dcc.Slider(
                    0, 3,
                    step = None,
                    value = 0,
                    marks = {
                        0: {'label': 'None'},
                        1: {'label': '1D'},
                        2: {'label': '1W'},
                        3: {'label': '1M'}
                    },
                    id=id('slider_static_resample')
                )
            ])
        ],
            justify='center'
        ),
    ]),
    html.Div(id=id('div_static_plots')),
],
    label='STATIC MONITORING'
)


#-------------------
#    OUTER LEVEL
#-------------------
layout = dbc.Row([
    dbc.Col([
        html.Div([
            html.Br(),
            html.H1('Leaning Tower of Pisa'),
            html.H4('Monitoring data analysis and visualization'),
            html.Br(),
            dbc.Tabs([
                t_tab_plan,
                t_tab_section,
                t_tab_static
            ])
        ]),
    ], lg=dict(width=10, offset=0)
    ), #dbc.Col(width=1)
])

#=================
#    CALLBACKS
#=================
#----------------------
#    TOWER PLAN tab
#----------------------
#---Select Capraro benchmarks and plot their displacement
@callback(Output(id('div_bench_displacement_plots'), 'children'),
             Input(id('fig_bench_displacement_selection'), 'selectedData'))
def callDivBenchDisplacement(selectedData):
    try:
        bench = [el['customdata'] for el in selectedData['points']]
        children=[]
        children += [dcc.Graph(figure=figureBenchDisplacement(b, T_CAPRARO_DATA)) for b in bench]
    except:
        children = dcc.Markdown('Select at least one benchmark.')
        
    return children

#---Select stabilization benchmarks and plot their displacement
@callback(Output(id('div_stabil_bench_displacement_plots'), 'children'),
             Input(id('fig_stabil_bench_displacement_selection'), 'selectedData'))
def callDivDFBenchDisplacement(selectedData):
    try:
        bench = [el['customdata'] for el in selectedData['points']]
        children=[]
        children += [dcc.Graph(figure=figureStabilBenchDisplacement(b, T_STABIL_DISP)) for b in bench]
    except:
        children = dcc.Markdown('')
        
    return children
    
    
#-------------------------
#    TOWER SECTION tab
#-------------------------
#----Update section selection plot
@callback(Output(id('fig_bench_section_selection'), 'figure'),
             Input(id('slider_bench_section_selection'), 'value'))
def callFigureBenchSectionSelection(selection):
    b = str(selection)
    if len(b) == 1:
        b = '0' + b    
    selected_bench = selectBenchSection(b)
    return figureSectionSel(selected_bench, T_CAPRARO_BENCHMARKS)

#----Update resample text in settings pane
@callback(Output(id('text_bench_section_resample'), 'children'),
             Input(id('slider_bench_section_resample'), 'value'))
def callTextBenchSectionresample(resample):
    reslisttext=['', '2', '4', '6', '8', '10', '12']
    reslist=list(enumerate(reslisttext))
    if resample==0:
        text= "Data isn't resampled"
    else:
        text = "Resampling with data every " + reslist[resample][1]+ "  months. \n **Pay attention**: when resampling, the days (and also months, for strong resampling) of measurement are not the real ones."        
    return text

#----Update bench section plot
@callback(Output(id('fig_bench_section'), 'figure'),
             Input(id('slider_bench_section_selection'), 'value'),
             Input(id('slider_bench_section_resample'), 'value'))        
def callFigureBenchSection(selection, resample):
    b = str(selection)
    if len(b) == 1:
        b = '0' + b
    selected_bench = selectBenchSection(b)
    return figureBenchSection(selected_bench, resample, T_CAPRARO_DATA, T_CAPRARO_BENCHMARKS)

#----Plot angle between benchmarks 904-911
@callback(Output(id('div_rot'), 'children'),
             Input(id('slider_bench_section_selection'), 'value'))
def callFigureRot(selection):
    b = str(selection)
    if b=='1' or b=='01':
        children = dbc.Row(dcc.Graph(figure=t_rot_tower))
        return children


#-----------------------------------
#    TOWER STATIC MONITORING tab
#-----------------------------------
#----Write checklist value in input form
# @callback(Output(id(

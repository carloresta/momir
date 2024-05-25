# imports
import pandas as pd
import plotly.graph_objects as go
from colour import Color
from datetime import datetime as dt


# local imports
from utils.styles import *


#==============================
#    TAB-SPECIFIC FUNCTIONS
#==============================
#----------------------
#    TOWER PLAN TAB
#----------------------
def figureBenchSelection(pos_tower):
    '''
    Generates a figure with the location of the benchmarks
    used for levelling in the Tower between 2002 and now. It's
    a plan view and the benchmarks can be selected.
    '''
    fig = go.Figure(layout_template='plotly_white')

    fig.update_layout(
        width=500,
        margin=dict(l=0,r=0,b=0,t=0)
    )

    #Add benchmarks
    x=[xi for xi in pos_tower['x']]
    y=[yi for yi in pos_tower['y']]
    name=[str(n) for n in pos_tower.index]
    types=[t for t in pos_tower['type']]
    marker_symbol=[]
    text_position=[]
    for i in range(0,len(pos_tower)):
        if pos_tower['type'].iloc[i]=='Square levelling':
            marker_symbol.append('circle')
            text_position.append('middle right')
        else:
            marker_symbol.append('diamond')
            text_position.append('middle left')
    marker_symbol=[m for m in marker_symbol]
    text_position=[t for t in text_position]

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            text=name,
            customdata=name,
            mode="markers+text",
            textposition= text_position,
            textfont_size=10,
            marker_color='#009988',
            hoverinfo='text',
            marker_symbol=marker_symbol,
            selected_marker_color='#332288'
        )
    )


    # Add the shape of the Catino
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-12.33, y0=-12.33, x1=12.33, y1=12.33,
        line_color="lightgrey"
    )
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-9.05, y0=-9.05, x1=9.05, y1=9.05,
        line_color="lightgrey",

    )

    # Add the shape of the Wall
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-12.8, y0=-12.8, x1=12.8, y1=12.8,
        line_color="lightgrey",
    )


    # Add the shape of the Tower
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-3.55, y0=-3.55, x1=3.55, y1=3.55,
        line_color="lightgrey"
    )
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-7.9, y0=-7.9, x1=7.9, y1=7.9,
        line_color="lightgrey",
    )


    #Add trace of plan of maximum inclination
    fig.add_shape(
        type="line",
        x0=0.54, y0=-14, x1=-0.54, y1=13.4,
        line=dict(
            color="lightgrey",
            dash="dashdot",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[0.54], y=[-15.5],
            text="Trace of plan of <br> maximum inclination",
            mode="text",
        )
    )

    # Format plot
    fig.update_xaxes(
        range = (pos_tower['x'].min()-3, pos_tower['x'].max()+3),
        showgrid = False,
        visible = False,
    )
    fig.update_yaxes(
        range = (pos_tower['y'].min()-5, pos_tower['y'].max()+3),
        showgrid = False,
        visible = False,
    )
    fig.update_layout(
        yaxis1=dict(
            scaleanchor = "x1",
            scaleratio = 1,
        )
    )

    fig.update(layout_showlegend=False)
    fig.update_layout(clickmode='event+select')

    #Re-order the order of visualization
    fig.data = (fig.data[1], fig.data[0])

    return fig


def figureBenchStabilSelection(DF_coord):
    ''' 
    Generates a figure with the location of the benchmarks
    used for levelling in the Tower during stabilization. 
    It's a plan view and the benchmarks can be selected.
    '''
    fig = go.Figure(layout_template='plotly_white')
    
    fig.update_layout(
        width=250,
        margin=dict(l=0,r=0,b=0,t=0)
    )
    
    # Add benchmarks
    x = [xi for xi in DF_coord['x']]
    y = [yi for yi in DF_coord['y']]
    name = [str(n) for n in DF_coord.index]
   
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            text=name,
            customdata=name,
            mode="markers+text",
            textfont_size=10,
            marker_color='#EE7733',
            hoverinfo='text',
            selected_marker_color='#CC3311',
            textposition='top center'
        )
    )
        
    
    # Add the shape of the Catino
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-12.33, y0=-12.33, x1=12.33, y1=12.33,
        line_color="lightgrey"
    )                
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-9.05, y0=-9.05, x1=9.05, y1=9.05,
        line_color="lightgrey",
    )
    
    # Add the shape of the Wall
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-12.8, y0=-12.8, x1=12.8, y1=12.8,
        line_color="lightgrey",
    )
        
    
    # Add the shape of the Tower
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-3.55, y0=-3.55, x1=3.55, y1=3.55,
        line_color="#DDDDDD"
    )                
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-7.9, y0=-7.9, x1=7.9, y1=7.9,
        line_color="#DDDDDD",
    )
    
                
    #Add trace of plan of maximum inclination
    fig.add_shape(
        type="line",
        x0=0.54, y0=-14, x1=-0.54, y1=13.4,
        line=dict(
            color="lightgrey",
            dash="dashdot",
        )
    )     
    
    fig.add_trace(
        go.Scatter(
            x=[0.54], y=[-15.5],
            text="Trace of plan of <br> maximum inclination",
            mode="text",
        )
    )
    
    # Format plot
    fig.update_xaxes(
        range = (DF_coord['x'].min()-3, DF_coord['x'].max()+3),
        showgrid = False,
        visible = False,
    )
    fig.update_yaxes(
        range = (DF_coord['y'].min()-5, DF_coord['y'].max()+3),
        showgrid = False,
        visible = False,
    )
    fig.update_layout(
        yaxis1=dict(
        scaleanchor = "x1",
        scaleratio = 1,
        )
    )
    
    fig.update(layout_showlegend=False)
    fig.update_layout(clickmode='event+select')
    
    #Re-order the order of visualization
    fig.data = (fig.data[1], fig.data[0])
    
    return fig
    
    
## FIX: this function and the following
#-------are practically the same: unify them!
def figureBenchDisplacement(b, lev_tower):
    ''' 
    A figure of displacement of the benchmarks in time.
    '''
    fig = go.Figure(layout_template='plotly_white')
    
    fig.update_layout(height=500, width=1000,
                         margin=dict(l=0,r=0,b=0,t=0))
    
    dz=lev_tower[b]-lev_tower[b].iloc[0]
    
    fig.add_trace(
        go.Scatter(
            x=lev_tower.index,
            y=dz,
            mode='markers+lines',
            marker_color = '#332288',
            line_color = '#332288',
        )
    )
    
   
    list_date=[]
    for n,date in list(enumerate(lev_tower.index)):
        if n%4==0:
            list_date.append(date)
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals =[d for d in list_date],
            tickformat="%b-%Y",
            tickangle=270
        ),
        yaxis_title="Displacement [cm]",
        title='Displacement of benchmarks'+str('b')
        
    )
    
    fig.add_annotation(
        xref="x domain",
        yref="y domain",
        x=0.95,
        y=0.9,
        text='<b>'+'benchmark n°'+'<b>'+'<b>'+ b+'</b>',
        #font_family='Roboto',
        font_color='black',
        font_size=14,
        borderpad=4,
        bordercolor='black',
        borderwidth=1.5,
        showarrow=False
    )
        
    return fig
    
    
## FIX: this function and the previous
#-------are practically the same: unify them!
def figureStabilBenchDisplacement(b, DF_disp):
    ''' 
    A figure of displacement of the benchmarks in time.
    '''
    fig = go.Figure(layout_template='plotly_white')
    
    fig.update_layout(height=500, width=1000,
                         margin=dict(l=0,r=0,b=0,t=0))
    
    dz=(DF_disp[b]-DF_disp[b].iloc[0])/10
    
    fig.add_trace(
        go.Scatter(
            x=DF_disp.index,
            y=dz,
            mode='markers+lines',
            marker_color = '#CC3311',
            line_color = '#CC3311',
        )
    )
    
   
    list_date=[]
    for n,date in list(enumerate(DF_disp.loc['1995'].index)):
        if n%14==0:
            list_date.append(date)
    for n,date in list(enumerate(DF_disp.loc['1996':'1999'].index)):
        if n%4==0:
            list_date.append(date)
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals =[d for d in list_date],
            tickformat="%Y-%m-%d",
            tickangle=270
        ),
        yaxis_title="Displacement [cm]",        
    )
    
    fig.add_annotation(
        xref="x domain",
        yref="y domain",
        x=0.95,
        y=0.9,
        text='<b>'+'benchmark n°'+'<b>'+'<b>'+ b+'</b>',
        #font_family='Roboto',
        font_color='black',
        font_size=14,
        borderpad=4,
        bordercolor='black',
        borderwidth=1.5,
        showarrow=False
    )
        
    return fig
    

#-------------------------
#    TOWER SECTION TAB
#-------------------------
def selectBenchSection(n):
    full_section = {
        '01':['E2','I2','904','102','106','911','I6','E6'],
        '02':['E3','I3','906','103','107','913','I7','E7'],
        '03':['E4','I4','908','104','108','915','I8','E8'],
        '04':['E5','I5','910','105','101','902','I1','E1'],
    }
    section = full_section[n]
    
    return section
    
    
def figureSectionSel(selected_bench, pos_tower):
    """
    A small figure showing which section was selected.
    """
    fig = go.Figure(layout_template='plotly_white')
    fig.update_layout(
        height=250, width=250,
        margin=dict(l=0,r=0,b=0,t=0)
    )
    
    unselected_bench = [el for el in pos_tower.index if el not in selected_bench]
    
    ub_x = [pos_tower['x'].loc[i] for i in unselected_bench]
    ub_y = [pos_tower['y'].loc[i] for i in unselected_bench]
    sb_x = [pos_tower['x'].loc[i] for i in selected_bench]
    sb_y = [pos_tower['y'].loc[i] for i in selected_bench]
    
   # Add the shape of the Catino 
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-12.33, y0=-12.33, x1=12.33, y1=12.33,
        line_color="lightgrey"
    )                
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-9.05, y0=-9.05, x1=9.05, y1=9.05,
        line_color="lightgrey",
    )
    
    # Add the shape of the Tower
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-3.55, y0=-3.55, x1=3.55, y1=3.55,
        line_color="#DDDDDD"
    )                
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-7.9, y0=-7.9, x1=7.9, y1=7.9,
        line_color="#DDDDDD",
    )
    
                
    #Add trace of plan of maximum inclination
    fig.add_shape(
        type="line",
        x0=0.54, y0=-14, x1=-0.54, y1=13.4,
        line=dict(
            color="lightgrey",
            dash="dashdot",
        )
    )     
    fig.add_trace(
        go.Scatter(
            x=[0.54], y=[-15.5],
            #text="Trace of plan of <br> maximum inclination",
            mode="text",
        )
    )
    
    # Add unselected benchmarks
    fig.add_trace(
        go.Scatter(
            x=ub_x, y=ub_y,
            mode='markers',
            marker_color='#009988',
            hovertext=[
                'Benchmark n. {}'.format(i) 
                for i in unselected_bench
            ],
            hoverinfo='text',
            marker_size=5
        )
    )
    
    # Add selected benchmarks
    fig.add_trace(
        go.Scatter(
            x=sb_x, y=sb_y,
            mode='markers',
            marker_color='#CC3311',
            hovertext=[
                'Benchmark n. {}'.format(i) 
                for i in selected_bench
            ],
            hoverinfo='text',
            marker_size=5
        )
    )
    
    # Disable the legend
    fig.update(layout_showlegend=False)
    
    # Format plot
    fig.update_xaxes(
        range = (-18, 18),
        showgrid = False,
        visible = False,
    )
    fig.update_yaxes(
        range = (-18, 18),
        showgrid = False,
        visible = False,
    )
    fig.update_layout(
        yaxis1=dict(
        scaleanchor = "x1",
        scaleratio = 1,
        )
    )
    return fig
    
    
def figureBenchSection(section, resample, lev_tower, pos_tower):
    '''
    A figure that shows displacements of the section of interest. 
    '''
    res = ['','2M','4M','6M','8M','10M','12M']
    
    df = lev_tower.copy()
    df1 = [df[str(section[i])] - df[str(section[i])].iloc[0] for i in range(0,len(section))]
    df2 = pd.DataFrame()
    for d in df1:
        df2 = pd.concat([df2,d],axis=1)
        df2.index = pd.to_datetime(df2.index)
    if resample != 0:
        df2 = df2.resample(res[resample]).last()
    else:
        df2 = df2
    df2.dropna(axis = 0, how = 'all', inplace = True)
    df2.index = pd.to_datetime(df2.index, format='%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    dist = [pos_tower['radius'].loc[el] for el in section]
    height = [df2[str(s)] for s in section]
    
    fig = go.Figure(layout_template='plotly_white')
    fig.update_layout(
        height=1000, width=900,
        margin=dict(l=0,r=0,b=0,t=0)
    )
    
    ## FIX(?): use standard colors
    #lista di colori
    n = len(df2.index)
    sand = Color("#DDCC77")
    colors = list(sand.range_to(Color("#117733"), n))
    df2['colors'] = colors
    
    # Add benchmarks
    for date in df2.index:
        height = [df2[str(s)].loc[date] for s in section] 
        fig.add_trace(
            go.Scatter(
                x=dist, y=height,
                mode='markers+lines',
                hovertext=[
                    'Benchmark n. {}'.format(i) 
                    for i in section
                ],
                #hoverinfo='name',
                marker_size=5,
                name=str(date),
                marker_color=str(df2['colors'].loc[date])
            )                   
        )
        
    # Format plot
    fig.update_yaxes(
        #range = (-18, 18),
        showgrid = True,
        visible = True,
        zeroline = True, zerolinewidth = 3, zerolinecolor = 'grey',
        title = 'Displacement[cm]',
    )
    fig.update_xaxes(
        range = (-15, 15),
        #title = 'Distance[m]',
        gridwidth = 2
    )
    
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = dist,
            ticktext = [el for el in section],
            tickangle = 270
        )
    )
    return fig
    
    
def rot_tower(lev_tower):
    rot_tower = (abs(lev_tower['904']) - abs(lev_tower['911']))/1685*3600
    fig = go.Figure(layout_template='plotly_white')
    
    fig.update_layout(
        height=500, width=1000,
        margin=dict(l=0,r=0,b=0,t=0)
    )
    
    fig.add_trace(
        go.Scatter(
            x=lev_tower.index,
            y=rot_tower,
            mode='markers+lines',
            marker_color = '#44AA99',
            line_color = '#44AA99',
        )
    )
    
    list_date=[]
    for n,date in list(enumerate(lev_tower.index)):
        if n%4==0:
            list_date.append(date)
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals =[d for d in list_date],
            tickformat="%b-%Y",
            tickangle=270
        ),
        yaxis_title="Angle [arcsec]",
    )
    
    fig.add_annotation(
        xref="x domain",
        yref="y domain",
        x=0.95,
        y=0.9,
        text='Angle between benchmarks 904-911',
        #font_family='Roboto',
        font_color='black',
        font_size=14,
        borderpad=4,
        bordercolor='black',
        borderwidth=1.5,
        showarrow=False
    )
    
    return fig

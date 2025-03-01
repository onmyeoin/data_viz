import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Import and process the CSV files
group_df = pd.read_csv('data_files/group.csv', index_col=0)
smithfield_df = pd.read_csv('data_files/smithfield.csv', index_col=0)
rathmines_df = pd.read_csv('data_files/rathmines.csv', index_col=0)


# Convert values for all dataframes
for col in group_df.columns:
    group_df[col] = group_df[col].apply(lambda x: float(str(x).replace(',', '')) 
                                       if isinstance(x, str) 
                                       else x)
    smithfield_df[col] = smithfield_df[col].apply(lambda x: float(str(x).replace(',', '')) 
                                                 if isinstance(x, str) 
                                                 else x)
    rathmines_df[col] = rathmines_df[col].apply(lambda x: float(str(x).replace(',', '')) 
                                               if isinstance(x, str) 
                                               else x)

# Transpose and reverse order for all dataframes
group_df = group_df.transpose()
group_df = group_df.iloc[::-1]

smithfield_df = smithfield_df.transpose()
smithfield_df = smithfield_df.iloc[::-1]

rathmines_df = rathmines_df.transpose()
rathmines_df = rathmines_df.iloc[::-1]

# Create figure with three subplots stacked vertically
fig = make_subplots(
    rows=3, cols=1,
    subplot_titles=("Group Revenue Breakdown with Net Profit",
                   "Smithfield Revenue Breakdown with Net Profit",
                   "Rathmines Revenue Breakdown with Net Profit"),
    shared_xaxes=True,
    vertical_spacing=0.1
)

# Function to add traces to subplot
def add_traces_to_subplot(df, row):
    # Get the correct wage cost column name
    wage_cost_col = 'Wage Cost % of revenue' if 'Wage Cost % of revenue' in df.columns else 'Wage cost %'

    # Calculate the wage amount for each period
    wage_amounts = df['Turnover'] * df[wage_cost_col]
    remaining_amounts = df['Turnover'] - wage_amounts

    # Add wage cost bar (bottom portion)
    fig.add_trace(
        go.Bar(
            name="Wage Cost",
            x=df.index,
            y=wage_amounts,
            marker_color='rgb(255,127,14)',
            hovertemplate="Wage Cost: €%{y:,.0f}<br>" +
                         "Wage Cost %: %{customdata:.1%}<br>" +
                         "<extra></extra>",
            customdata=df[wage_cost_col],
            showlegend=(row == 1)  # Only show legend for first subplot
        ),
        row=row, col=1
    )

    # Add remaining revenue bar (top portion)
    fig.add_trace(
        go.Bar(
            name="Remaining Revenue",
            x=df.index,
            y=remaining_amounts,
            marker_color='rgb(158,202,225)',
            hovertemplate="Revenue: €%{customdata:,.0f}<br>" +
                         "<extra></extra>",
            customdata=df['Turnover'],
            showlegend=(row == 1)  # Only show legend for first subplot
        ),
        row=row, col=1
    )

    # Add net profit line
    fig.add_trace(
        go.Scatter(
            name="Net Profit/(Loss)",
            x=df.index,
            y=df['Net Profit/(Loss)'],
            line=dict(color='rgb(44,160,44)', width=3),
            mode='lines+markers',
            hovertemplate="Net Profit/(Loss): €%{y:,.0f}<br>" +
                        "<extra></extra>",
            showlegend=(row == 1)  # Only show legend for first subplot
        ),
        row=row, col=1
    )

# Add traces for each dataset
add_traces_to_subplot(group_df, 1)
add_traces_to_subplot(smithfield_df, 2)
add_traces_to_subplot(rathmines_df, 3)

# Update layout
fig.update_layout(
    height=1800,  # Triple the height since we have three subplots
    width=1000,
    template='plotly_white',
    barmode='stack',
    hovermode='x unified',
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.98,
        xanchor="left",
        x=0.01
    )
)

# Update all y-axes
for i in range(1, 4):
    fig.update_yaxes(
        title_text="Revenue & Net Profit/(Loss) (€)",
        rangemode='tozero',
        tickformat=",d",
        row=i, col=1
    )

# Update x-axis (only shown for bottom subplot)
fig.update_xaxes(
    title_text="Weeks",
    type='category',
    row=3, col=1
)

# Show the figure
fig.show()





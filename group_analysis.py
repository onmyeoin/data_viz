import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Import and process the CSV files
group_df = pd.read_csv('data_files/group.csv', index_col=0)
rathmines_df = pd.read_csv('data_files/rathmines.csv', index_col=0)
smithfield_df = pd.read_csv('data_files/smithfield.csv', index_col=0)

def create_dual_axis_chart(df, title):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add turnover bars
    fig.add_trace(
        go.Bar(
            name="Turnover",
            x=df.index,
            y=df['Turnover'],
            marker_color='rgb(158,202,225)'
        ),
        secondary_y=False
    )

    # Add net profit/(loss) line
    fig.add_trace(
        go.Scatter(
            name="Net Profit/(Loss)",
            x=df.index,
            y=df['Net Profit/(Loss)'],
            line=dict(color='rgb(255,127,14)', width=3),
            mode='lines+markers'
        ),
        secondary_y=False
    )

    # Add wages cost % line on secondary axis
    fig.add_trace(
        go.Scatter(
            name="Wage Cost % of revenue",
            x=df.index,
            y=df['Wage Cost % of revenue'],
            line=dict(color='rgb(44,160,44)', width=3),
            mode='lines+markers'
        ),
        secondary_y=True
    )

    # Update layout
    fig.update_layout(
        title=title,
        template='plotly_white',
        hovermode='x unified',
        barmode='relative',
        height=600,
        width=1000,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    # Format y-axis for percentages on right side
    fig.update_yaxes(
        title_text="Turnover & Net Profit/(Loss) (€)", 
        secondary_y=False, 
        rangemode='tozero'
    )
    fig.update_yaxes(
        title_text="Wage Cost % of revenue",
        tickformat='.0%',  # Format as percentage
        secondary_y=True
    )
    fig.update_xaxes(title_text="Weeks")

    return fig

# Create and show charts
group_fig = create_dual_axis_chart(group_df, "Group Performance Metrics")
rathmines_fig = create_dual_axis_chart(rathmines_df, "Rathmines Performance Metrics")
smithfield_fig = create_dual_axis_chart(smithfield_df, "Smithfield Performance Metrics")

# Display all charts
group_fig.show()
rathmines_fig.show()
smithfield_fig.show()



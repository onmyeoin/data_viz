import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("Revenue_and_Net_Profit_Data.csv")

# Extracting weeks
weeks = df.columns[1:]

# Extracting data for plotting
revenue_smithfield = df.loc[df["Group"] == "Revenue Smithfield", weeks].values.flatten()
revenue_rathmines = df.loc[df["Group"] == "Revenue Rathmines", weeks].values.flatten()
net_profit = df.loc[df["Group"] == "Net profit (%)", weeks].values.flatten()

# Create figure
fig = go.Figure()

# Stacked bar for Revenue Smithfield
fig.add_trace(go.Bar(
    name="Revenue Smithfield",
    x=weeks,
    y=revenue_smithfield
))

# Stacked bar for Revenue Rathmines
fig.add_trace(go.Bar(
    name="Revenue Rathmines",
    x=weeks,
    y=revenue_rathmines
))

# Line for Net Profit (%)
fig.add_trace(go.Scatter(
    name="Net Profit (%)",
    x=weeks,
    y=net_profit,
    mode="lines+markers",
    line=dict(color="red", width=2),
    marker=dict(size=6)
))

# Update layout for stacked bars with a **single Y-axis**
fig.update_layout(
    barmode="stack",
    title="Group Revenue and Net Profit Over Time",
    xaxis_title="Weeks",
    yaxis_title="Revenue & Net Profit (€)",
    template="plotly_white",
    legend=dict(x=0.01, y=0.01),
    height=600,
    width=1000
)

# Show figure
fig.show()

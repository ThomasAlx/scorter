import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Example data for 3 projects scored by 10 people
np.random.seed(42)  # For reproducibility
projects = ["Project A", "Project B", "Project C"]
scores_impact = {
    "Project A": np.array([*0 * [1], *4 * [2], *0 * [3], *4 * [4], *2 * [5]]),
    "Project B": np.array([*0 * [1], *4 * [2], *1 * [3], *1 * [4], *4 * [5]]),
    "Project C": np.array([*2 * [1], *4 * [2], *2 * [3], *2 * [4], *0 * [5]]),
}
scores_feasibility = {
    "Project A": np.array([*2 * [1], *0 * [2], *0 * [3], *2 * [4], *6 * [5]]),
    "Project B": np.array([*3 * [1], *0 * [2], *5 * [3], *1 * [4], *1 * [5]]),
    "Project C": np.array([*3 * [1], *6 * [2], *0 * [3], *0 * [4], *1 * [5]]),
}

# Create DataFrames for the scores
df_impact = pd.DataFrame(scores_impact)
df_feasibility = pd.DataFrame(scores_feasibility)

# Calculate average scores for each category
average_impact = df_impact.mean()
average_feasibility = df_feasibility.mean()

# Combine averages into a single DataFrame
average_scores = pd.DataFrame(
    {
        "Project": projects,
        "Impact": average_impact.values,
        "Feasibility": average_feasibility.values,
    }
)

# Define quadrant thresholds (middle at 3 for both axes)
x_threshold = 3
y_threshold = 3

# Create scatter plot with quadrants
fig = go.Figure()


# # Add vertical and horizontal reference lines to split quadrants
# fig.add_shape(
#     type="line",
#     x0=x_threshold,
#     x1=x_threshold,
#     y0=1,
#     y1=5,
#     line=dict(color="gray", dash="solid"),
# )
# fig.add_shape(
#     type="line",
#     x0=1,
#     x1=5,
#     y0=y_threshold,
#     y1=y_threshold,
#     line=dict(color="gray", dash="solid"),
# )

# Add shaded regions for quadrants
fig.add_shape(
    type="rect",
    x0=1,
    x1=x_threshold,
    y0=1,
    y1=y_threshold,
    layer="between",
    fillcolor="rgba(255, 99, 71, 0.5)",  # Red
    line=dict(width=0),
)
fig.add_shape(
    type="rect",
    x0=x_threshold,
    x1=5,
    y0=1,
    y1=y_threshold,
    layer="between",
    fillcolor="rgba(241, 225, 166, 0.2)",  # Light green
    line=dict(width=0),
)
fig.add_shape(
    type="rect",
    x0=1,
    x1=x_threshold,
    y0=y_threshold,
    y1=5,
    fillcolor="rgba(241, 225, 166, 0.2)",  # Light green
    layer="between",
    line=dict(width=0),
)
fig.add_shape(
    type="rect",
    x0=x_threshold,
    x1=5,
    y0=y_threshold,
    y1=5,
    layer="between",
    fillcolor="rgba(152, 251, 152, 0.5)",  # Green
    line=dict(width=0),
)

# Update layout for quadrant visualization
fig.update_layout(
    title="Project Quadrant Analysis",
    xaxis_title="Feasibility (Low to High)",
    yaxis_title="Impact (Low to High)",
    xaxis=dict(range=[1, 5]),
    yaxis=dict(range=[1, 5]),
    height=600,
    width=800,
    showlegend=False,
)

# Add data points for projects
fig.add_trace(
    go.Scatter(
        x=average_scores["Feasibility"],
        y=average_scores["Impact"],
        mode="markers+text",
        text=average_scores["Project"],
        textposition="top center",
        marker=dict(size=10, color="black"),
        name="Projects",
    )
)

# Show plot
fig.show()

# Save as app.py and run: python app.py
# Open http://127.0.0.1:8050 in your browser

import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

app = dash.Dash(__name__)
server = app.server
# -----------------------------
# AI Adoption Growth (Animated Line Chart)
# -----------------------------
years = list(range(2026, 2047))
ai_adoption = [5 + i*3 for i in range(len(years))]

fig_growth = px.line(
    x=years,
    y=ai_adoption,
    title="Projected AI Adoption in Corporations (2026–2046)",
    labels={"x":"Year", "y":"AI Adoption (%)"},
)
fig_growth.update_traces(line=dict(color="cyan", width=4))
fig_growth.update_layout(template="plotly_dark")

# -----------------------------
# Future Opportunities (Bubble Timeline)
# -----------------------------
opportunities = [
    "AI-powered M&A", "Intelligent Supply Chains", "Sustainable AI",
    "AI-as-CEO", "Decentralized Corporations", "Emotionally Intelligent AI",
    "Quantum Finance", "AI Climate Modeling", "AI Space Exploration"
]
impact = [80, 90, 70, 60, 85, 75, 95, 88, 72]
timeline = [2030, 2032, 2035, 2040, 2042, 2045, 2038, 2036, 2044]

fig_bubble = px.scatter(
    x=timeline,
    y=impact,
    size=impact,
    text=opportunities,
    title="Future AI Opportunities Timeline",
    labels={"x":"Year", "y":"Impact Score"},
    size_max=60,
)
fig_bubble.update_traces(textposition="top center")
fig_bubble.update_layout(template="plotly_dark")

# -----------------------------
# Deep Research Themes (Radar Chart)
# -----------------------------
themes = ["Quantum AI", "Neuromorphic Computing", "Synthetic Biology + AI", "Decentralized Corporations", "AI + Climate Modeling", "AI + Space Exploration"]
importance = [95, 85, 90, 80, 88, 70]

fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(
    r=importance,
    theta=themes,
    fill='toself',
    name='Research Importance'
))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0,100])),
    showlegend=False,
    template="plotly_dark",
    title="Emerging AI Research Themes (2046 Vision)"
)

# -----------------------------
# Sector Impact (Bar Chart)
# -----------------------------
sectors = ["Healthcare", "Finance", "Manufacturing", "Energy", "Agriculture", "Education", "Space"]
impact_scores = [95, 90, 85, 80, 88, 75, 70]

fig_bar = px.bar(
    x=sectors,
    y=impact_scores,
    title="Sectoral Impact of Advanced AI (2046)",
    labels={"x":"Sector", "y":"Impact Score"},
    color=impact_scores,
    color_continuous_scale="Viridis"
)
fig_bar.update_layout(template="plotly_dark")

# -----------------------------
# Timeline of Breakthroughs (Scatter Plot)
# -----------------------------
breakthroughs = [
    "Explainable AI", "Quantum AI Integration", "Neuromorphic Chips", 
    "Synthetic Biology-AI Fusion", "Decentralized AI Corporations", "Emotionally Intelligent AI"
]
years_breakthrough = [2028, 2035, 2032, 2038, 2042, 2045]
importance_breakthrough = [70, 95, 85, 90, 80, 75]

fig_timeline = px.scatter(
    x=years_breakthrough,
    y=importance_breakthrough,
    text=breakthroughs,
    size=importance_breakthrough,
    title="Timeline of AI Breakthroughs (2026–2046)",
    labels={"x":"Year", "y":"Importance"},
    size_max=50
)
fig_timeline.update_traces(textposition="top center")
fig_timeline.update_layout(template="plotly_dark")

# -----------------------------
# Investment Distribution (Animated Pie Chart)
# -----------------------------
investment_categories = ["Quantum AI", "Neuromorphic Computing", "Synthetic Biology", "Decentralized AI", "Climate Modeling", "Space AI"]
investment_values = [25, 20, 15, 15, 15, 10]

fig_pie = px.pie(
    names=investment_categories,
    values=investment_values,
    title="Projected AI R&D Investment Distribution (2046)"
)
fig_pie.update_traces(textinfo="label+percent")
fig_pie.update_layout(template="plotly_dark")

# -----------------------------
# Global AI Adoption Heatmap
# -----------------------------
countries = ["USA", "China", "Japan", "Germany", "India", "Brazil", "UK"]
adoption_index = [95, 92, 88, 85, 80, 70, 78]

fig_heatmap = px.choropleth(
    locations=countries,
    locationmode="country names",
    color=adoption_index,
    color_continuous_scale="Plasma",
    title="Global AI Adoption Intensity (2046)"
)
fig_heatmap.update_layout(template="plotly_dark")

# -----------------------------
# 3D AI Adoption Growth (Scatter3D)
# -----------------------------
z_values = np.linspace(0, 10, len(years))  # Corporate maturity index

fig_growth_3d = go.Figure(data=[go.Scatter3d(
    x=years,
    y=ai_adoption,
    z=z_values,
    mode='lines+markers',
    line=dict(color='cyan', width=6),
    marker=dict(size=6, color=ai_adoption, colorscale='Viridis')
)])
fig_growth_3d.update_layout(
    scene=dict(
        xaxis_title='Year',
        yaxis_title='AI Adoption (%)',
        zaxis_title='Corporate Maturity Index'
    ),
    template="plotly_dark",
    title="3D Projection of AI Adoption Growth"
)

# -----------------------------
# 3D Future Opportunities Bubble Cloud
# -----------------------------
z_opportunities = [i*5 for i in range(len(opportunities))]

fig_bubble_3d = go.Figure(data=[go.Scatter3d(
    x=timeline,
    y=impact,
    z=z_opportunities,
    text=opportunities,
    mode='markers+text',
    marker=dict(size=[i/2 for i in impact], color=impact, colorscale='Plasma'),
    textposition="top center"
)])
fig_bubble_3d.update_layout(
    scene=dict(
        xaxis_title='Year',
        yaxis_title='Impact Score',
        zaxis_title='Depth Dimension'
    ),
    template="plotly_dark",
    title="3D Future AI Opportunities Landscape"
)

# -----------------------------
# 3D Global AI Adoption Surface
# -----------------------------
X, Y = np.meshgrid(range(len(countries)), range(len(countries)))
Z = np.outer(adoption_index, adoption_index)

fig_surface = go.Figure(data=[go.Surface(
    z=Z,
    x=X,
    y=Y,
    colorscale="Plasma"
)])
fig_surface.update_layout(
    scene=dict(
        xaxis_title='Country Index',
        yaxis_title='Country Index',
        zaxis_title='Adoption Intensity'
    ),
    template="plotly_dark",
    title="3D Global AI Adoption Surface (2046)"
)

# -----------------------------
# Layout (Presentation Slides)
# -----------------------------
app.layout = html.Div(
    style={"backgroundColor":"#111", "color":"white", "fontFamily":"Arial"},
    children=[
        html.H1("Advanced AI for Corporate Growth (2046 Vision)", style={"textAlign":"center", "marginBottom":"40px"}),

        html.Div([
            html.H2("Executive Summary"),
            html.P("AI will evolve into autonomous ecosystems, drive human-AI collaboration, and reshape corporate models."),
        ], style={"marginBottom":"50px"}),

        html.Div([dcc.Graph(figure=fig_growth, animate=True)], style={"marginBottom":"50px"}),
        html.Div([dcc.Graph(figure=fig_bubble, animate=True)], style={"marginBottom":"50px"}),
        html.Div([dcc.Graph(figure=fig_radar, animate=True)], style={"marginBottom":"50px"}),
        html.Div([dcc.Graph(figure=fig_bar, animate=True)], style={"marginBottom":"50px"}),
        html.Div([dcc.Graph(figure=fig_timeline, animate=True)], style={"marginBottom":"50px"}),
        html.Div([dcc.Graph(figure=fig_pie, animate=True)], style={"marginBottom":"50px"}),
        html.Div([dcc.Graph(figure=fig_heatmap, animate=True)], style={"marginBottom":"50px"}),

        # New 3D Visualizations
        html.Div([dcc.Graph(figure=fig_growth_3d, animate=True)], style={"marginBottom":"50px"}),
        html.Div([dcc.Graph(figure=fig_bubble_3d, animate=True)], style={"marginBottom":"50px"}),
        html.Div([dcc.Graph(figure=fig_surface, animate=True)], style={"marginBottom":"50px"}),

        html.Div([
            html.H2("Conclusion & Next Steps"),
            html.P("AI is not just a tool—it’s the foundation of future enterprises."),
            html.Ul([
                html.Li("Establish dedicated AI R&D divisions"),
                html.Li("Invest in ethical AI governance"),
                html.Li("Pilot autonomous decision-making projects"),
                html.Li("Partner with AI research institutions"),
            ]),
        ]),
    ]
)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8050))   # Render provides PORT dynamically
    app.run_server(host="0.0.0.0", port=port, debug=False)

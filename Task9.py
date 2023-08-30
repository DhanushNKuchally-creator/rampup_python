import plotly.graph_objects as go
import plotly.io as pio
areas = [
    "python", "AI ML stack", "Django", "java", "Spring boost",
    "Anugular Js", "Node js", "PHP", "Mongo DB", "Influx DB",
    "MySql/Postgress Sql", "Warrior Famework", "Robot Framework",
    "AWS/Cloud", "Optical", "L2/L3", "QA-CLI Auromation", "TMF API",
    "Angular 14", "Java Full Stack Developer", "Mean Stack Developer",
    "IOS Developer", "Android Developer", "Go Developer", "IOT",
    "Dockers", "Kubernetes", "Jenkins"
]
team_members = [
    30, 24, 7, 26, 5, 27, 1, 21, 13, 0, 14, 9, 12, 5, 2, 4, 0, 1,
    29, 0, 0, 15, 25, 5, 25, 10, 3, 19
]
fig = go.Figure(go.Treemap(
    labels=areas,
    parents=[''] * len(areas),  
    values=team_members,
    hovertemplate='<b>%{label}</b><br>Team Members: %{value}<extra></extra>',
    marker_colors=["#006400", "#008000", "#90EE90", "#006400", "#90EE90",
                   "#006400", "#00FF00", "#008000", "#98FB98", "#00FF00",
                   "#00FF00", "#00FF00", "#FFFFFF", "#00FF00", "#00FF00",
                   "#00FF00", "#FFFFFF", "#00FF00", "#006400", "#FFFFFF",
                   "#FFFFFF", "#00A000", "#008000", "#90EE90", "#008000",
                   "#90EE90", "#00FF00", "#00A000"]
))
fig.update_layout(
    title='Team Expertise Treemap',
    margin=dict(l=0, r=0, b=0, t=40)
)
pio.write_html(fig, 'treemap1.html' ,auto_open=True)
#fig.show()


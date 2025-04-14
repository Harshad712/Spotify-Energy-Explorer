from preswald import connect, get_df, text, table, slider, plotly
import plotly.express as px

# Connect and load the dataset
connect()

df = get_df("topsongs_csv")
# Show title
text("# 🎵 Spotify Energy Explorer")
text("This app shows top Spotify songs (2010–2019) with high energy levels.")

# Add slider to control energy threshold
threshold = slider("Energy Threshold", min_val=0, max_val=100, default=70)

# Filter the dataset by 'nrgy' (energy column)
filtered_df = df[df["nrgy"] > threshold]

# Show filtered data in a table
table(filtered_df, title="🎶 Songs with High Energy")

# Add a scatter plot (e.g., Energy vs Danceability)
fig = px.scatter(filtered_df, 
                 x="dnce", 
                 y="nrgy", 
                 color="top genre", 
                 hover_data=["title", "artist", "year"],
                 title="Energy vs Danceability by Genre")

plotly(fig)

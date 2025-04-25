import random
import textwrap
from themes import themes
from kinks import kinks

def generate_animated_svg(username, theme):
    """Generate an animated SVG for the profile."""
    
    if theme.lower() in ["daddy", "dom", "dominant_master", "chad"]:
        colors = ["#0A0A0A", "#8B0000", "#FF4500"]
    elif theme.lower() in ["mommy", "bimbo", "good_girl"]:
        colors = ["#FF69B4", "#FF1493", "#C71585"]
    elif theme.lower() in ["goth_babe", "edge_lord"]:
        colors = ["#000000", "#4B0082", "#800080"]
    elif theme.lower() in ["switch", "brat"]:
        colors = ["#9932CC", "#FF4500", "#1E90FF"]
    else:
        colors = ["#4B0082", "#9370DB", "#8A2BE2"]
    
    svg = f"""<svg width="400" height="120" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes pulse {{
      0% {{ opacity: 0.4; }}
      50% {{ opacity: 1; }}
      100% {{ opacity: 0.4; }}
    }}
    .text-animate {{
      animation: pulse 2s infinite;
      font-family: 'Arial', sans-serif;
      font-weight: bold;
    }}
  </style>
  <rect width="400" height="120" fill="{colors[0]}" rx="10" ry="10"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="{colors[1]}" font-size="24" class="text-animate">{username}'s Coding Den</text>
  <text x="50%" y="75%" dominant-baseline="middle" text-anchor="middle" fill="{colors[2]}" font-size="16" class="text-animate">{theme.title()} Developer</text>
</svg>"""
    
    return svg


def generate_profile(username, theme1, theme2, kink, language):
    """Generate a NSFW GitHub profile with the given parameters."""
    
    theme1_data = themes.get(theme1.lower(), random.choice(list(themes.values())))
    theme2_data = themes.get(theme2.lower(), random.choice(list(themes.values())))
    kink_data = kinks.get(kink.lower(), random.choice(list(kinks.values())))
    
    bio1 = random.choice(theme1_data["bios"])
    bio2 = random.choice(theme2_data["bios"])
    
    # combined_bio = f"{bio1} {kink_data['bio_addon']} {bio2}"
    
    awards = []
    awards.append(random.choice(theme1_data["awards"]))
    awards.append(random.choice(theme2_data["awards"]))
    awards.append(kink_data["award"])
    
    github_trophies = [
        "🏆 GitHub Pro",
        "🔰 Open Source Contributor",
        "⭐ Star Gazer",
        "🚀 Fast Merger",
        "🔍 Code Detective",
        "🧩 Problem Solver"
    ]
    
    selected_trophies = random.sample(github_trophies, 3)
    all_awards = awards + selected_trophies
    
    random.shuffle(all_awards)
    
    awards_str = "\n".join([f"- {award}" for award in all_awards])

    svg_content = generate_animated_svg(username, theme1)
    svg_filename = f"{username}_animation.svg"
    with open(svg_filename, "w", encoding="utf-8") as svg_file:
        svg_file.write(svg_content)
    
    readme = f"""<div align="center">
  
<img src="{svg_filename}" alt="{username}'s Animated SVG" />

## About Me 💻🔥

- {bio1} 
- {kink_data['bio_addon']} 
- {bio2}

### My Kink: {kink.title()} 🔞
*{kink_data['description']} {kink_data['flavor_text']}*

## Programming Skills 🚀
- **Favorite Language:** {language}
- **Specialty:** Making {theme1.title()}-style code meet {theme2.title()}-level expectations
- **Best At:** {random.choice(["Debugging at 3 AM", "Writing code that makes you blush", "Creating functions with multiple outputs", "Handling exceptions roughly", "Deep recursion"])}

## Trophy Case 🏆
{awards_str}

## My Coding Mood 🎭
```
{random.choice([
    f"When I commit, I {random.choice(['moan', 'gasp', 'shiver', 'tremble'])}", 
    f"My {language} code is as {random.choice(['hot', 'dirty', 'clean', 'tight'])} as my {random.choice(['mind', 'style', 'secrets'])}",
    f"I debug with {random.choice(['passion', 'intensity', 'precision', 'dominance'])}",
    f"My repositories are {random.choice(['deep', 'wide open', 'tightly secured', 'well-maintained'])}"
])}
```

## GitHub Stats 📊

<div align="center">
  <img width=350 src="https://github-readme-stats.vercel.app/api?username={username}&theme=radical&count_private=true&show_icons=true&rank_icon=github&locale=en" alt="{username}'s GitHub Stats" />
  <img width=350 src="https://github-readme-streak-stats.herokuapp.com/?user={username}&theme=radical&count_private=true&border_radius=10&locale=en" alt="{username}'s Streak" />
  <img width=350 src="https://github-readme-stats.vercel.app/api/top-langs?username={username}&theme=radical&layout=donut&hide=css&langs_count=8&border_radius=10&show_icons=true&locale=en" alt="{username}'s Most Used Languages" />
</div>


<img src="https://komarev.com/ghpvc/?username={username}&label=Profile+Views" alt="{username}'s profile views" />

</div>

<!-- This README was generated with the NSFW GitHub Profile Generator -->
"""
    return readme


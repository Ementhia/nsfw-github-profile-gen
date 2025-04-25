import os
from themes import themes
from kinks import kinks
from profile_generator import generate_profile, generate_animated_svg

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_available_themes():
    """Display all available themes."""
    print("Available themes:")
    for i, theme in enumerate(themes.keys(), 1):
        print(f"{i}. {theme.replace('_', ' ').title()}")

def display_available_kinks():
    """Display all available kinks."""
    print("Available kinks:")
    for i, kink in enumerate(kinks.keys(), 1):
        print(f"{i}. {kink.replace('_', ' ').title()}")

def get_theme_choice():
    """Get user's theme choice."""
    display_available_themes()
    while True:
        choice = input("\nSelect a theme (number or name): ").strip().lower()
        if choice.isdigit() and 1 <= int(choice) <= len(themes):
            return list(themes.keys())[int(choice) - 1]
        elif choice in themes:
            return choice
        elif choice.replace(' ', '_') in themes:
            return choice.replace(' ', '_')
        else:
            print("Invalid theme choice. Please try again.")

def get_kink_choice():
    """Get user's kink choice."""
    display_available_kinks()
    while True:
        choice = input("\nSelect a kink (number or name): ").strip().lower()
        if choice.isdigit() and 1 <= int(choice) <= len(kinks):
            return list(kinks.keys())[int(choice) - 1]
        elif choice in kinks:
            return choice
        elif choice.replace(' ', '_') in kinks:
            return choice.replace(' ', '_')
        else:
            print("Invalid kink choice. Please try again.")

def main():
    """Main function for NSFW GitHub Profile Generator."""
    clear_screen()
    print("🔥💻 Welcome to NSFW GitHub Profile Generator 💻🔥")
    print("==============================================")
    print("\nLet's create your spicy developer profile!\n")
    
    username = input("👤 Enter your GitHub username: ").strip()
    
    print("\n✨ Let's select your first theme!")
    theme1 = get_theme_choice()
    
    print(f"\n✨ Great choice with {theme1.replace('_', ' ').title()}! Now select your second theme!")
    theme2 = get_theme_choice()
    
    print("\n🌶️ Now let's add some spice with a kink!")
    kink = get_kink_choice()
    
    language = input("\n💻 What's your favorite programming language? ").strip()
    
    print("\n⏳ Generating your NSFW GitHub profile...")
    readme = generate_profile(username, theme1, theme2, kink, language)
    
    svg = generate_animated_svg(username, theme1)
    
    with open("NSFW_PROFILE_README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    
    with open(f"{username}_animation.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    
    clear_screen()
    print("🎉 Your NSFW GitHub profile has been generated! 🎉")
    print("==================================================")
    print(f"📄 README saved as: NSFW_PROFILE_README.md")
    print(f"🎨 Animation saved as: {username}_animation.svg")
    print("\nTo use these files:")
    print("1. Create a repository named exactly '{username}'")
    print("2. Upload NSFW_PROFILE_README.md as 'README.md'")
    print("3. Upload the SVG to add it to your README")
    print("\nEnjoy your new spicy developer profile! 🔥")

if __name__ == "__main__":
    main()
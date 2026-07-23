# Animated GitHub Profile Header Generator

A Python script to generate a cool, animated, terminal-style SVG header for your GitHub Profile README.
It automatically converts a profile picture into ASCII art and adds typing animations for your details.

## Prerequisites

- Python 3.x
- `pip`

## Setup & Usage

1. **Install dependencies**:
   Run the following command to install the required `Pillow` library for image processing:
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your image**:
   Place an image of yourself in this folder and name it `profile.jpg`. (If no image is provided, a placeholder ASCII art will be used).

3. **Configure your details**:
   Open `generate_header.py` in your text editor. At the top of the file, you'll find the `CONFIG` dictionary. 
   Customize the text, links, and colors to your liking. The default color is Hacker Green (`#23d18b`).

4. **Generate the Header**:
   Run the script:
   ```bash
   python generate_header.py
   ```
   This will generate a `header.svg` file in the same directory.

5. **Add to your GitHub Profile**:
   Upload the `header.svg` to your GitHub profile repository and include it in your `README.md` like this:
   ```html
   <img src="header.svg" width="100%" alt="Profile Header" />
   ```

## Customization

- `theme_color`: Change the accent color (e.g., `#00ffff` for Cyan, `#ff00ff` for Magenta).
- `details`: Add or remove rows to display your tech stack, currently playing Spotify song, or anything else you'd like!

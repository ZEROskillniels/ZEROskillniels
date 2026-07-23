import os
import textwrap
from PIL import Image

# --- CONFIGURATION ---
CONFIG = {
    "image_path": "profile.png",
    "output_path": "header.svg",
    "theme_color": "#23d18b",  # Hacker green
    "text_color": "#c9d1d9",   # Standard text
    "bg_color": "#0d1117",     # Terminal background
    "border_color": "#23d18b",
    
    # Text Configuration
    "prompt": "user@github ~ % ./profile.sh --info",
    "details": [
        ("Subject", "Dein Name"),
        ("Role", "Software Developer"),
        ("Origin", "Germany"),
        ("Status", "Building, learning, coding"),
        ("Toolchain", "Python, VS Code, Git"),
        ("", ""),
        ("Core Lang", "Python, JavaScript, C++"),
        ("Frontend", "React, HTML, CSS"),
        ("Backend", "Node.js, Django, FastAPI"),
        ("Database", "PostgreSQL, MySQL"),
    ],
    
    # ASCII Art settings
    "ascii_width": 130,  # Characters wide
}

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image {image_path}: {e}")
        print("Using placeholder ASCII art...")
        return get_placeholder_ascii(new_width)

    # Convert to grayscale
    image = image.convert("L")
    
    # Resize
    width, height = image.size
    aspect_ratio = height / width
    # Fonts are usually twice as tall as they are wide, so we divide height by 2.2 for tighter vertical spacing
    new_height = int(aspect_ratio * new_width * 0.45)
    image = image.resize((new_width, new_height))
    
    # Convert pixels to chars
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value * len(ASCII_CHARS) // 256]
    
    # Split into lines
    ascii_img = ""
    for i in range(0, len(ascii_str), new_width):
        ascii_img += ascii_str[i:i+new_width] + "\n"
        
    return ascii_img

def get_placeholder_ascii(width):
    # A simple smiley face if no image is found
    face = """
       @@@@@@@@@@@@@@       
     @@@@@@@@@@@@@@@@@@     
    @@@@@@        @@@@@@    
   @@@@@@   @@@@   @@@@@@   
  @@@@@@    @@@@    @@@@@@  
  @@@@@@            @@@@@@  
  @@@@@@   @@@@@@   @@@@@@  
   @@@@@@   @@@@   @@@@@@   
    @@@@@@        @@@@@@    
     @@@@@@@@@@@@@@@@@@     
       @@@@@@@@@@@@@@       
"""
    return face.strip() + "\n"

def generate_svg(ascii_art):
    svg_width = 1200
    svg_height = 650
    text_x = 650
    
    # Escape special characters in text
    def escape_xml(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    # SVG Header
    svg = f"""<svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        .terminal-bg {{ fill: {CONFIG['bg_color']}; stroke: {CONFIG['border_color']}; stroke-width: 1; rx: 10; }}
        .header-bar {{ fill: #161b22; rx: 10; }}
        .ascii-text {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: 10px; font-weight: bold; fill: {CONFIG['theme_color']}; }}
        .cmd-text {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: 16px; fill: {CONFIG['text_color']}; font-weight: bold; }}
        .key-text {{ fill: {CONFIG['theme_color']}; font-weight: bold; }}
        .val-text {{ fill: {CONFIG['text_color']}; }}
        .cursor {{ fill: {CONFIG['theme_color']}; animation: blink 1s step-end infinite; }}
        
        @keyframes fadein {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        @keyframes blink {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0; }}
        }}
    </style>
    
    <!-- Background -->
    <rect x="1" y="1" width="{svg_width-2}" height="{svg_height-2}" class="terminal-bg" />
    <path d="M1 11 Q1 1 11 1 L{svg_width-11} 1 Q{svg_width-1} 1 {svg_width-1} 11 L{svg_width-1} 30 L1 30 Z" fill="#161b22" stroke="{CONFIG['border_color']}" stroke-width="1"/>
    
    <!-- Window controls -->
    <circle cx="20" cy="15" r="6" fill="#ff5f56" />
    <circle cx="40" cy="15" r="6" fill="#ffbd2e" />
    <circle cx="60" cy="15" r="6" fill="#27c93f" />
    
    <!-- Title -->
    <text x="{svg_width/2}" y="20" font-family="ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace" font-size="14" fill="#8b949e" text-anchor="middle">~/profile.sh</text>

    <!-- Clip Paths for Typing Animation -->
    <defs>
"""
    
    # Generate clip paths for each line
    start_delay = 0.5
    line_dur = 0.15
    y_offset = 80
    
    # Prompt line
    svg += f"""
        <clipPath id="clip-prompt">
            <rect x="{text_x}" y="{y_offset-15}" width="0" height="25">
                <animate attributeName="width" from="0" to="500" begin="{start_delay}s" dur="{line_dur*2}s" fill="freeze" />
            </rect>
        </clipPath>
"""
    start_delay += line_dur * 2 + 0.2
    
    # Details lines
    for i, (k, v) in enumerate(CONFIG["details"]):
        if k or v:
            svg += f"""
        <clipPath id="clip-line-{i}">
            <rect x="{text_x}" y="{y_offset + 35 + i*22 - 18}" width="0" height="25">
                <animate attributeName="width" from="0" to="400" begin="{start_delay}s" dur="{line_dur}s" fill="freeze" />
            </rect>
        </clipPath>
"""
            start_delay += line_dur
    
    svg += """
    </defs>
    
    <!-- ASCII Art (Left Side) -->
    <g transform="translate(20, 50)">
        <text xml:space="preserve" class="ascii-text">"""
    for i, line in enumerate(ascii_art.split('\n')):
        if line:
            delay = i * 0.04
            svg += f'<tspan x="0" dy="{11 if i>0 else 0}" style="opacity: 0; animation: fadein 0.5s {delay}s forwards">{escape_xml(line)}</tspan>'
    
    svg += """</text>
    </g>
    
    <!-- Text Content (Right Side) -->
"""
    
    # Prompt
    svg += f"""
        <text x="{text_x}" y="{y_offset}" class="cmd-text" clip-path="url(#clip-prompt)">{escape_xml(CONFIG['prompt'])}</text>
"""
    
    # Details
    for i, (k, v) in enumerate(CONFIG["details"]):
        if k or v:
            svg += f"""
        <text x="{text_x}" y="{y_offset + 35 + i*22}" class="cmd-text" clip-path="url(#clip-line-{i})">
            <tspan class="key-text" font-weight="bold">{escape_xml(k.ljust(12))}</tspan> 
            <tspan class="val-text">{escape_xml(v)}</tspan>
        </text>
"""
    
    # Cursor
    cursor_y = y_offset + 35 + len(CONFIG["details"])*22
    svg += f"""
        <rect x="{text_x}" y="{cursor_y-12}" width="10" height="15" class="cursor" opacity="0">
            <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;{min(1.0, start_delay/10)};{min(1.0, (start_delay+0.1)/10)};1" dur="10s" fill="freeze" />
        </rect>
</svg>
"""
    return svg

def main():
    print("Generating GitHub Profile Header...")
    
    # Generate ASCII art
    ascii_art = image_to_ascii(CONFIG["image_path"], new_width=CONFIG["ascii_width"])
    
    # Generate SVG
    svg_content = generate_svg(ascii_art)
    
    # Save SVG
    with open(CONFIG["output_path"], "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    print(f"Successfully saved to {CONFIG['output_path']}")

if __name__ == "__main__":
    main()

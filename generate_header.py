import os
import urllib.request
import base64

# ==========================================
# CONFIGURATION
# ==========================================
CONFIG = {
    "name": "Niels Duske",
    "role": "UI/UX Designer &amp; Frontend Dev",
    "description_lines": [
        "Creating thoughtful digital products through interaction design,",
        "user research, and frontend development."
    ],
    "avatar_url": "https://github.com/ZEROskillniels.png",
    
    "badges": ["FIGMA", "REACT", "NODE.JS", "ASTRO", "PYTHON", "ADOBE"],
    "status": "AVAILABLE",
    
    "width": 1000,
    "height": 450
}

def get_base64_image(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            image_data = response.read()
            b64_data = base64.b64encode(image_data).decode('utf-8')
            return f"data:image/png;base64,{b64_data}"
    except Exception as e:
        print(f"Failed to fetch image: {e}")
        return ""

def generate_svg():
    width = CONFIG["width"]
    height = CONFIG["height"]
    center_x = width / 2
    
    # Fetch avatar as base64
    avatar_b64 = get_base64_image(CONFIG["avatar_url"])
    
    # Calculate total badges width to center the group
    badge_widths = [len(b) * 8 + 30 for b in CONFIG["badges"]]
    total_badges_width = sum(badge_widths) + (len(badge_widths) - 1) * 12
    badges_start_x = center_x - (total_badges_width / 2)
    
    badges_svg = ""
    current_x = badges_start_x
    for i, badge in enumerate(CONFIG["badges"]):
        b_width = badge_widths[i]
        badges_svg += f'''
        <g transform="translate({current_x}, 0)">
            <rect x="0" y="0" width="{b_width}" height="26" rx="13" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.1)" />
            <text x="{b_width/2}" y="17" text-anchor="middle" class="badge-text">{badge}</text>
        </g>'''
        current_x += b_width + 12

    svg_content = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <filter id="blur-heavy" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="80" />
        </filter>
        <filter id="glass-blur" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="12" result="blur" />
            <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="glow" />
            <feMerge>
                <feMergeNode in="glow"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>

        <linearGradient id="glass-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(255, 255, 255, 0.08)"/>
            <stop offset="100%" stop-color="rgba(255, 255, 255, 0.01)"/>
        </linearGradient>
        <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#4ade80" />
            <stop offset="50%" stop-color="#22c55e" />
            <stop offset="100%" stop-color="#16a34a" />
        </linearGradient>
        
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/>
            <circle cx="40" cy="40" r="1" fill="rgba(255,255,255,0.1)"/>
        </pattern>
        
        <clipPath id="avatar-clip">
            <circle cx="{center_x}" cy="110" r="45" />
        </clipPath>
    </defs>

    <style>
        .title {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 38px; font-weight: 800; fill: #ffffff; letter-spacing: -0.5px; text-transform: uppercase; text-anchor: middle; }}
        .subtitle {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 16px; font-weight: 600; fill: url(#text-grad); text-transform: uppercase; letter-spacing: 3px; text-anchor: middle; }}
        .desc {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 15px; fill: #94a3b8; font-weight: 400; text-anchor: middle; }}
        .badge-text {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 11px; fill: #cbd5e1; font-weight: 600; letter-spacing: 1.5px; }}
        
        @keyframes float1 {{ 0%, 100% {{ transform: translate(0px, 0px) scale(1); }} 50% {{ transform: translate(40px, -50px) scale(1.1); }} }}
        @keyframes float2 {{ 0%, 100% {{ transform: translate(0px, 0px) scale(1); }} 50% {{ transform: translate(-50px, 30px) scale(1.15); }} }}
        @keyframes float3 {{ 0%, 100% {{ transform: translate(0px, 0px) scale(1); }} 50% {{ transform: translate(30px, 50px) scale(0.9); }} }}
        
        .nebula-1 {{ animation: float1 18s ease-in-out infinite; transform-origin: center; }}
        .nebula-2 {{ animation: float2 22s ease-in-out infinite; transform-origin: center; }}
        .nebula-3 {{ animation: float3 25s ease-in-out infinite; transform-origin: center; }}
        
        @keyframes pulse-star {{ 0%, 100% {{ opacity: 0.2; transform: scale(0.8); }} 50% {{ opacity: 1; transform: scale(1.3); }} }}
        .star {{ animation: pulse-star 4s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
        
        @keyframes dash {{ to {{ stroke-dashoffset: -400; }} }}
        .data-path {{ stroke-dasharray: 4 12; animation: dash 20s linear infinite; }}
        
        @keyframes glass-float {{ 0%, 100% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-5px); }} }}
        .glass-panel {{ animation: glass-float 8s ease-in-out infinite; }}
    </style>

    <rect width="100%" height="100%" fill="#050505" />
    <!-- Animated Nebulas (Green Shades) -->
    <circle cx="850" cy="100" r="220" fill="rgba(4, 120, 87, 0.45)" filter="url(#blur-heavy)" class="nebula-1" />
    <circle cx="150" cy="350" r="250" fill="rgba(16, 185, 129, 0.35)" filter="url(#blur-heavy)" class="nebula-2" />
    <circle cx="550" cy="-50" r="180" fill="rgba(52, 211, 153, 0.35)" filter="url(#blur-heavy)" class="nebula-3" />

    <path d="M -50 150 Q 200 100 350 250 T 700 350 T 1100 250" fill="none" stroke="rgba(52, 211, 153, 0.2)" stroke-width="1.5" class="data-path" />
    <path d="M -50 350 Q 300 450 550 200 T 900 100 T 1100 -50" fill="none" stroke="rgba(16, 185, 129, 0.2)" stroke-width="1" class="data-path" style="animation-duration: 25s;" />

    <circle cx="120" cy="80" r="2" fill="#fff" class="star" style="animation-delay: 0s;" />
    <circle cx="850" cy="350" r="3" fill="#10b981" class="star" style="animation-delay: 1.2s;" />
    <circle cx="450" cy="400" r="2" fill="#34d399" class="star" style="animation-delay: 2.5s;" />
    <circle cx="700" cy="120" r="1.5" fill="#fff" class="star" style="animation-delay: 0.5s;" />
    <circle cx="300" cy="200" r="2.5" fill="#fff" class="star" style="animation-delay: 1.8s;" />
    <circle cx="920" cy="180" r="1.5" fill="#047857" class="star" style="animation-delay: 0.8s;" />

    <g class="glass-panel" transform="translate(0, 0)">
        <rect x="50" y="30" width="900" height="390" rx="30" fill="url(#glass-grad)" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1.5" />
        
        <!-- Avatar -->
        <image href="{avatar_b64}" x="{center_x - 45}" y="65" width="90" height="90" clip-path="url(#avatar-clip)" />
        <circle cx="{center_x}" cy="110" r="46" fill="none" stroke="rgba(16, 185, 129, 0.5)" stroke-width="2" />
        
        <!-- Identity Text (Centered) -->
        <text x="{center_x}" y="195" class="title">{CONFIG['name']}</text>
        <text x="{center_x}" y="230" class="subtitle">{CONFIG['role']}</text>
        
        <text x="{center_x}" y="280" class="desc">{CONFIG['description_lines'][0]}</text>
        <text x="{center_x}" y="305" class="desc">{CONFIG['description_lines'][1]}</text>
        
        <!-- Badges -->
        <g transform="translate(0, 345)">
            {badges_svg}
        </g>
        
        <!-- Status Indicator (Top Right inside panel) -->
        <g transform="translate(780, 50)">
            <rect width="130" height="30" rx="15" fill="rgba(16, 185, 129, 0.05)" stroke="rgba(16, 185, 129, 0.3)" />
            <circle cx="20" cy="15" r="4" fill="#10b981" class="star" />
            <text x="35" y="19" class="badge-text" fill="#10b981">{CONFIG['status']}</text>
        </g>
    </g>

    </svg>'''
    
    with open("header.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print("Successfully generated centered space-like header.svg")

if __name__ == "__main__":
    generate_svg()

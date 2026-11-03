"""Build a self-contained, portfolio-inspired GitHub profile header."""

import base64
from html import escape
from pathlib import Path
from string import Template
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
CONFIG = {
    "name": "Niels Duske",
    "role": "UI/UX Designer & Frontend Dev",
    "description": (
        "Creating thoughtful digital products through interaction design,",
        "user research, and frontend development.",
    ),
    "badges": ("FIGMA", "REACT", "NODE.JS", "ASTRO", "PYTHON", "ADOBE"),
    "status": "WORKING FOR TENBYTE ATM",
}
SNAKE_URL = "https://raw.githubusercontent.com/ZEROskillniels/ZEROskillniels/output/github-snake.svg"


def snake_svg():
    generated = ROOT / "dist" / "github-snake.svg"
    if generated.exists():
        source = generated.read_text(encoding="utf-8")
    else:
        request = Request(SNAKE_URL, headers={"User-Agent": "github-profile-header"})
        with urlopen(request, timeout=20) as response:
            source = response.read().decode("utf-8")
    # Match the new palette even when the locally available snake is still green.
    for old, new in {
        "#16a34a": "#22d3ee",
        "#161b22": "#0b1730",
        "#064e3b": "#102e53",
        "#047857": "#155a95",
        "#10b981": "#238bd0",
        "#34d399": "#67d9f4",
    }.items():
        source = source.replace(old, new)
    return source


def badges_svg():
    output, x = [], 74
    for badge in CONFIG["badges"]:
        width = len(badge) * 8 + 28
        output.append(
            f'<g transform="translate({x} 0)"><rect width="{width}" height="28" rx="14" class="badge"/>'
            f'<text x="{width / 2}" y="18" class="badge-label">{escape(badge)}</text></g>'
        )
        x += width + 9
    return "".join(output)


SVG = Template("""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="720" viewBox="0 0 1000 720" role="img" aria-labelledby="title desc">
<title id="title">Niels Duske — UI/UX Designer und Frontend Developer</title>
<desc id="desc">Blauer Weltraum-Header mit Rakete, Profilbild und animierter GitHub-Commit-Schlange.</desc>
<defs>
  <linearGradient id="space" x2="1" y2="1"><stop stop-color="#010610"/><stop offset=".55" stop-color="#07182c"/><stop offset="1" stop-color="#0b2450"/></linearGradient>
  <radialGradient id="aura"><stop stop-color="#1686d2" stop-opacity=".48"/><stop offset="1" stop-color="#1686d2" stop-opacity="0"/></radialGradient>
  <linearGradient id="type"><stop stop-color="#a4efff"/><stop offset=".45" stop-color="#38c7ef"/><stop offset="1" stop-color="#398cf4"/></linearGradient>
  <linearGradient id="hull"><stop stop-color="#93b5d2"/><stop offset=".16" stop-color="#344a66"/><stop offset=".54" stop-color="#14283f"/><stop offset=".86" stop-color="#3c5976"/><stop offset="1" stop-color="#9ac4dc"/></linearGradient>
  <linearGradient id="fin" x2="1" y2="1"><stop stop-color="#669bc4"/><stop offset=".42" stop-color="#1e426a"/><stop offset="1" stop-color="#0c2549"/></linearGradient>
  <linearGradient id="plume" x2="0" y2="1"><stop stop-color="#e1fcff"/><stop offset=".15" stop-color="#50d8ff"/><stop offset=".55" stop-color="#167cd8" stop-opacity=".7"/><stop offset="1" stop-color="#1260a5" stop-opacity="0"/></linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#80b5e8" stroke-opacity=".055"/></pattern>
  <filter id="blur"><feGaussianBlur stdDeviation="28"/></filter>
  <filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <clipPath id="frame"><rect width="1000" height="720" rx="24"/></clipPath>
  <clipPath id="avatar"><circle cx="124" cy="191" r="47"/></clipPath>
</defs>
<style>
text{font-family:Inter,Arial,sans-serif}.eyebrow{fill:#a8c9df;font-size:12px;font-weight:700;letter-spacing:3px}
.name{fill:#fff;font-size:50px;font-weight:800;letter-spacing:-1.8px}.role{fill:url(#type);font-size:18px;font-weight:700;letter-spacing:1.4px}
.description{fill:#b3c5d9;font-size:16px}.badge{fill:#112744;fill-opacity:.8;stroke:#62b7e7;stroke-opacity:.33}
.badge-label{fill:#d0e9f5;font-size:11px;font-weight:700;letter-spacing:1px;text-anchor:middle}
.section-label{fill:#8ccde8;font-size:11px;font-weight:700;letter-spacing:2.5px}
.star{animation:twinkle 4s ease-in-out infinite}.rocket{animation:drift 7s ease-in-out infinite;transform-origin:760px 210px}
.plume{animation:flame 2s ease-in-out infinite;transform-origin:760px 370px}
@keyframes twinkle{50%{opacity:.25}}@keyframes drift{50%{transform:translateY(-6px) rotate(1deg)}}@keyframes flame{50%{transform:scaleY(.83);opacity:.72}}
@media(prefers-reduced-motion:reduce){.star,.rocket,.plume{animation:none}}
</style>
<g clip-path="url(#frame)">
  <rect width="1000" height="720" fill="url(#space)"/><rect width="1000" height="720" fill="url(#grid)"/>
  <ellipse cx="760" cy="195" rx="310" ry="260" fill="url(#aura)"/>
  <ellipse cx="97" cy="680" rx="250" ry="180" fill="#13529e" opacity=".25" filter="url(#blur)"/>
  <path d="M-80 390C240 330 540 460 1100 103" fill="none" stroke="#44bff5" stroke-opacity=".2" stroke-width="1.5" stroke-dasharray="4 12"/>
  <path d="M590-60C640 78 875 53 1070 340" fill="none" stroke="#6bd7f3" stroke-opacity=".13" stroke-width="1.5"/>
  <circle cx="760" cy="210" r="180" fill="none" stroke="#74c4ee" stroke-opacity=".12"/>
  <circle cx="760" cy="210" r="215" fill="none" stroke="#74c4ee" stroke-opacity=".08"/>
  <g fill="#bcefff">
    <circle class="star" cx="58" cy="71" r="1.5"/><circle class="star" cx="229" cy="95" r="1" style="animation-delay:1s"/>
    <circle class="star" cx="565" cy="58" r="2" style="animation-delay:2s"/><circle class="star" cx="913" cy="65" r="1.5"/>
    <circle class="star" cx="611" cy="352" r="1.5" style="animation-delay:1.5s"/><circle class="star" cx="945" cy="355" r="2"/>
    <circle class="star" cx="356" cy="389" r="1"/><circle class="star" cx="44" cy="405" r="2" style="animation-delay:2.8s"/>
    <circle class="star" cx="925" cy="559" r="1.5"/><circle class="star" cx="315" cy="641" r="1"/>
  </g>
  <path d="M42 46h510a30 30 0 0 1 30 30v327a30 30 0 0 1-30 30H42z" fill="#071426" fill-opacity=".65" stroke="#76c6ee" stroke-opacity=".16"/>
  <rect x="74" y="73" width="214" height="25" rx="12.5" fill="#103354" stroke="#4bbde9" stroke-opacity=".5"/>
  <circle cx="89" cy="85.5" r="4" fill="#59d8f3" filter="url(#glow)"/>
  <text x="101" y="90" fill="#a8e9f7" font-size="10" font-weight="700" letter-spacing="1">$status</text>
  <circle cx="124" cy="191" r="52" fill="#08213d" stroke="#52c8f1" stroke-width="2"/>
  <image href="$avatar" x="77" y="144" width="94" height="94" clip-path="url(#avatar)" preserveAspectRatio="xMidYMid slice"/>
  <text x="193" y="181" class="eyebrow">HELLO, I AM</text>
  <text x="192" y="230" class="name">$name</text>
  <text x="74" y="278" class="role">$role</text>
  <path d="M74 296h457" stroke="#5dbde6" stroke-opacity=".25"/>
  <text x="74" y="327" class="description">$description1</text>
  <text x="74" y="352" class="description">$description2</text>
  <g transform="translate(0 381)">$badges</g>
  <!-- A cylindrical metallic rocket with cyan circuitry, like the portfolio's 3D scene. -->
  <g class="rocket">
    <ellipse cx="765" cy="265" rx="107" ry="192" fill="#0b57a6" opacity=".27" filter="url(#blur)"/>
    <g class="plume">
      <path d="M738 350Q733 411 747 466Q763 490 776 466Q793 411 786 350Z" fill="url(#plume)" opacity=".55" filter="url(#glow)"/>
      <path d="M750 350Q745 402 760 441Q779 402 774 350Z" fill="url(#plume)"/>
      <path d="M760 359Q754 393 761 419Q769 393 766 359Z" fill="#d5faff" opacity=".9"/>
    </g>
    <path d="M719 308Q690 333 673 403Q707 392 746 363L744 298Z" fill="url(#fin)" stroke="#7fc5eb" stroke-opacity=".65" stroke-width="2"/>
    <path d="M800 308Q828 333 846 403Q809 392 774 363L777 298Z" fill="url(#fin)" stroke="#7fc5eb" stroke-opacity=".65" stroke-width="2"/>
    <path d="M724 351Q760 365 796 351L787 378Q760 387 733 378Z" fill="#0b203b" stroke="#8bdbf5" stroke-opacity=".62" stroke-width="2"/>
    <path d="M724 179Q733 123 760 80Q787 123 796 179L797 324Q796 350 782 360H738Q723 350 723 324Z" fill="url(#hull)" stroke="#a3c9e6" stroke-width="2.5"/>
    <path d="M735 169Q740 126 760 88Q780 126 786 169Z" fill="#18395c" stroke="#64bcec" stroke-opacity=".8" stroke-width="2"/>
    <path d="M760 92Q746 123 744 167" fill="none" stroke="#c8ecff" stroke-opacity=".65" stroke-width="2"/>
    <path d="M727 198H793M726 311H794" stroke="#61c9f3" stroke-opacity=".65" stroke-width="3" filter="url(#glow)"/>
    <path d="M740 206V299M781 206V299" stroke="#69cbee" stroke-opacity=".4" stroke-width="2" stroke-dasharray="9 8"/>
    <circle cx="760" cy="240" r="32" fill="#081b33" stroke="#a6e8f8" stroke-width="5"/>
    <circle cx="760" cy="240" r="25" fill="#0b5895" stroke="#61d9fa" stroke-width="2"/>
    <circle cx="760" cy="240" r="19" fill="#10334f"/>
    <path d="M747 235Q757 223 773 233" fill="none" stroke="#b8f5ff" stroke-opacity=".8" stroke-width="3" stroke-linecap="round"/>
    <path d="M750 332H770" stroke="#7adbf6" stroke-width="3" stroke-linecap="round" filter="url(#glow)"/>
  </g>
  <path d="M48 450H952" stroke="#73bee9" stroke-opacity=".25"/>
  <text x="64" y="478" class="section-label">GITHUB CONTRIBUTIONS</text>
  <text x="937" y="478" text-anchor="end" fill="#648fb1" font-size="10" letter-spacing="1.2">ANIMATED SNAKE</text>
  <rect x="48" y="491" width="904" height="199" rx="22" fill="#06152b" fill-opacity=".82" stroke="#76c6ee" stroke-opacity=".23"/>
  <g transform="translate(60 496)">$snake</g>
  <rect x="1" y="1" width="998" height="718" rx="23" fill="none" stroke="#89c8ee" stroke-opacity=".25" stroke-width="2"/>
</g>
</svg>""")


def generate_svg():
    avatar = base64.b64encode((ROOT / "profile.png").read_bytes()).decode("ascii")
    svg = SVG.substitute(
        avatar=f"data:image/png;base64,{avatar}",
        snake=snake_svg(),
        status=escape(CONFIG["status"]),
        name=escape(CONFIG["name"]),
        role=escape(CONFIG["role"]),
        description1=escape(CONFIG["description"][0]),
        description2=escape(CONFIG["description"][1]),
        badges=badges_svg(),
    )
    (ROOT / "header.svg").write_text(svg, encoding="utf-8")
    if (ROOT / "dist").exists():
        (ROOT / "dist" / "header.svg").write_text(svg, encoding="utf-8")
    print("Generated blue rocket header with animated contribution snake.")


if __name__ == "__main__":
    generate_svg()

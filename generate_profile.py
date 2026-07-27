#!/usr/bin/env python3
"""
Github Profile README & SVG Generator
====================================
Generates three high-end, self-contained SMIL-animated SVG cards:
  1. github-contribution-animation.svg (53x7 contribution calendar with diagonal slant reveal & specular glint)
  2. terminal-card.svg (ASCII portrait terminal with row reveal, sweeping cursor & typewriter whoami footer)
  3. info-card.svg (Neofetch info card with staggered line reveals and neon cyberpunk aesthetics)

Also generates / updates README.md with side-by-side table layout and contribution graph.
"""

import os
import sys
import math
import random
import json
import argparse
import html
import urllib.request
from datetime import datetime, timedelta

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# Default Fallback Username
DEFAULT_USERNAME = "octocat"

# Cyberpunk Color Palette
COLORS = {
    "bg": "#0d1117",
    "card_bg": "#161b22",
    "border": "#30363d",
    "border_glow": "#00f3ff33",
    "text_bright": "#f0f6fc",
    "text_muted": "#8b949e",
    "cyan": "#00f3ff",
    "blue": "#38bdf8",
    "green": "#39d353",
    "emerald": "#00ff88",
    "orange": "#ff9e3b",
    "red": "#ff7b72",
    "purple": "#a371f7",
    "magenta": "#bf5af2",
    "yellow": "#f1e05a",
    # Contribution levels
    "l0": "#161b22",
    "l1": "#0e4429",
    "l2": "#006d32",
    "l3": "#26a641",
    "l4": "#39d353",
}

# --- 1. ASCII ART GENERATOR ---
CYBER_DEV_ASCII = [
    "  .------------------------.  ",
    " /  _____   ______   _   _  \\ ",
    "|  / ____| |  ____| | \\ | |  |",
    "| | |  __  | |__    |  \\| |  |",
    "| | | |_ | |  __|   | . ` |  |",
    "| | |__| | | |____  | |\\  |  |",
    " \\ \\_____| |______| |_| \\_| / ",
    "  '------------------------'  ",
    "      ||              ||      ",
    "   .---''------------''---.   ",
    "  /  ____________________  \\  ",
    " |  |  CYBER / DEVELOPER |  | ",
    " |  |  >> SYSTEM READY  |  | ",
    "  \\  --------------------  /  ",
    "   '----------------------'   "
]

def fetch_avatar_ascii(username, width=40, height=22):
    """
    Fetches user avatar from GitHub and converts it into ASCII art using PIL.
    Falls back to a stylized cyber ASCII illustration if PIL or network is unavailable.
    """
    if not HAS_PIL:
        print("[!] PIL (Pillow) not installed. Using stylized ASCII art template.")
        return CYBER_DEV_ASCII

    avatar_url = f"https://github.com/{username}.png"
    try:
        req = urllib.request.Request(avatar_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            img = Image.open(resp)
            img = img.convert('L') # Convert to grayscale
            
            # Adjust aspect ratio (characters are taller than wide, ~0.52 factor)
            aspect_ratio = img.height / img.width
            target_height = int(width * aspect_ratio * 0.52)
            target_height = min(max(target_height, 18), height)
            
            img = img.resize((width, target_height), Image.Resampling.LANCZOS)
            
            # High-contrast ASCII character map from dark to bright
            ascii_chars = " .:-=+*#%@"
            num_chars = len(ascii_chars)
            
            pixels = list(img.getdata())
            lines = []
            for i in range(0, len(pixels), width):
                row = pixels[i:i + width]
                line_str = "".join([ascii_chars[min(int(p / 256 * num_chars), num_chars - 1)] for p in row])
                lines.append(line_str)
            return lines
    except Exception as e:
        print(f"[!] Could not fetch or process avatar for {username}: {e}. Using fallback ASCII art.")
        return CYBER_DEV_ASCII

# --- 2. SVG GENERATOR: FILE 1 - github-contribution-animation.svg ---
def generate_contribution_svg(username, output_file="github-contribution-animation.svg"):
    """
    Generates a 53x7 animated contribution calendar SVG with diagonal slant reveal,
    specular glint flashes, and outer glows for level 3/4 squares.
    """
    cols = 53
    rows = 7
    square_size = 11
    gap = 3
    margin_left = 35
    margin_top = 40
    
    width = margin_left + cols * (square_size + gap) + 20
    height = margin_top + rows * (square_size + gap) + 40

    # Generate synthetic contribution levels (0 to 4) with realistic distribution
    random.seed(42 + sum(ord(c) for c in username))
    grid_levels = []
    for c in range(cols):
        col_levels = []
        for r in range(rows):
            val = random.choices([0, 1, 2, 3, 4], weights=[0.35, 0.25, 0.20, 0.12, 0.08])[0]
            col_levels.append(val)
        grid_levels.append(col_levels)

    # Calculate total contributions count
    total_contributions = sum(sum(col) for col in grid_levels) * 3 + random.randint(400, 1200)

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <!-- Glow Filters for Level 3 and Level 4 squares -->',
        '    <filter id="glow-l3" x="-50%" y="-50%" width="200%" height="200%">',
        '      <feGaussianBlur stdDeviation="2" result="blur" />',
        '      <feMerge>',
        '        <feMergeNode in="blur" />',
        '        <feMergeNode in="SourceGraphic" />',
        '      </feMerge>',
        '    </filter>',
        '    <filter id="glow-l4" x="-100%" y="-100%" width="300%" height="300%">',
        '      <feGaussianBlur stdDeviation="3.5" result="blur1" />',
        '      <feGaussianBlur stdDeviation="1.5" result="blur2" />',
        '      <feMerge>',
        '        <feMergeNode in="blur1" />',
        '        <feMergeNode in="blur2" />',
        '        <feMergeNode in="SourceGraphic" />',
        '      </feMerge>',
        '    </filter>',
        '    <!-- Glassmorphism Card Gradient -->',
        '    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#161b22" stop-opacity="0.95"/>',
        '      <stop offset="100%" stop-color="#0d1117" stop-opacity="0.98"/>',
        '    </linearGradient>',
        '    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="0%">',
        '      <stop offset="0%" stop-color="#30363d"/>',
        '      <stop offset="50%" stop-color="#00f3ff" stop-opacity="0.6"/>',
        '      <stop offset="100%" stop-color="#30363d"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        '  <style>',
        '    .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14px; font-weight: 600; fill: #f0f6fc; }',
        '    .sub-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 11px; fill: #8b949e; }',
        '    .month-label { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 9px; fill: #8b949e; }',
        '    .day-label { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 9px; fill: #8b949e; }',
        '    .legend-label { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 9px; fill: #8b949e; }',
        '  </style>',
        '',
        '  <!-- Outer Card Frame -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="10" fill="url(#bg-grad)" stroke="url(#border-grad)" stroke-width="1.5"/>',
        '',
        '  <!-- Header Text -->',
        f'  <text x="20" y="24" class="title">Contribution Activity</text>',
        f'  <text x="{width-20}" y="24" class="sub-title" text-anchor="end">{total_contributions:,} contributions in the last year</text>',
        ''
    ]

    # Month Labels
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for i, month in enumerate(months):
        x_pos = margin_left + int(i * (cols / 12) * (square_size + gap))
        svg_lines.append(f'  <text x="{x_pos}" y="{margin_top - 8}" class="month-label">{month}</text>')

    # Day Labels (Mon, Wed, Fri)
    day_names = [("Mon", 1), ("Wed", 3), ("Fri", 5)]
    for d_name, d_idx in day_names:
        y_pos = margin_top + d_idx * (square_size + gap) + 9
        svg_lines.append(f'  <text x="12" y="{y_pos}" class="day-label">{d_name}</text>')

    # Generate Grid Squares with SMIL Animations
    # Slant reveal: delay based on (c + (6 - r))
    svg_lines.append('  <!-- Contribution Squares Grid -->')
    svg_lines.append('  <g>')

    for c in range(cols):
        for r in range(rows):
            lvl = grid_levels[c][r]
            x = margin_left + c * (square_size + gap)
            y = margin_top + r * (square_size + gap)
            cx = x + square_size / 2
            cy = y + square_size / 2
            
            fill_color = COLORS[f"l{lvl}"]
            filter_attr = ''
            if lvl == 3:
                filter_attr = ' filter="url(#glow-l3)"'
            elif lvl == 4:
                filter_attr = ' filter="url(#glow-l4)"'

            # Diagonal distance calculation for slant reveal animation
            diag_idx = c + (rows - 1 - r)
            start_delay = round(diag_idx * 0.025, 3)

            # Square Base with SMIL scale and opacity slant reveal
            sq_html = (
                f'    <rect x="{x}" y="{y}" width="{square_size}" height="{square_size}" rx="2.5" '
                f'fill="{fill_color}" opacity="0"{filter_attr}>\n'
                f'      <animate attributeName="opacity" values="0; 1" dur="0.3s" begin="{start_delay}s" fill="freeze"/>\n'
                f'      <animateTransform attributeName="transform" type="scale" values="0.1; 1.2; 1" keyTimes="0; 0.7; 1" '
                f'dur="0.35s" begin="{start_delay}s" fill="freeze" transform-origin="{cx}px {cy}px"/>\n'
                f'    </rect>'
            )
            svg_lines.append(sq_html)

            # Specular Glint Highlight Flash Overlay
            glint_color = "#ffffff" if lvl < 3 else COLORS["emerald"]
            glint_html = (
                f'    <rect x="{x}" y="{y}" width="{square_size}" height="{square_size}" rx="2.5" '
                f'fill="{glint_color}" opacity="0" pointer-events="none">\n'
                f'      <animate attributeName="opacity" values="0; 0.95; 0" keyTimes="0; 0.3; 1" '
                f'dur="0.4s" begin="{round(start_delay + 0.05, 3)}s" fill="freeze"/>\n'
                f'    </rect>'
            )
            svg_lines.append(glint_html)

    svg_lines.append('  </g>')

    # Legend at bottom right
    legend_y = height - 15
    legend_x_start = width - 130
    svg_lines.append(f'  <text x="{legend_x_start - 25}" y="{legend_y + 9}" class="legend-label">Less</text>')
    for l_idx in range(5):
        lx = legend_x_start + l_idx * (11 + 3)
        l_color = COLORS[f"l{l_idx}"]
        svg_lines.append(f'  <rect x="{lx}" y="{legend_y}" width="11" height="11" rx="2.5" fill="{l_color}"/>')
    svg_lines.append(f'  <text x="{legend_x_start + 5 * 14 + 5}" y="{legend_y + 9}" class="legend-label">More</text>')

    svg_lines.append('</svg>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 3. SVG GENERATOR: FILE 2 - terminal-card.svg ---
def generate_terminal_card_svg(username, ascii_lines, output_file="terminal-card.svg"):
    """
    Generates an animated macOS-style terminal card featuring the ASCII portrait.
    Features: row-by-row top-to-bottom reveal, sweeping cursor block, and typewriter footer.
    """
    width = 440
    height = 430
    
    # Format ASCII lines safely for XML
    safe_lines = [html.escape(line) for line in ascii_lines]
    
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="term-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#161b22" stop-opacity="0.98"/>',
        '      <stop offset="100%" stop-color="#0d1117" stop-opacity="0.99"/>',
        '    </linearGradient>',
        '    <linearGradient id="term-border" x1="0%" y1="0%" x2="0%" y2="100%">',
        '      <stop offset="0%" stop-color="#00f3ff" stop-opacity="0.5"/>',
        '      <stop offset="50%" stop-color="#30363d" stop-opacity="0.8"/>',
        '      <stop offset="100%" stop-color="#a371f7" stop-opacity="0.4"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        '  <style>',
        '    .term-header-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; fill: #8b949e; font-weight: 600; }',
        '    .ascii-text { font-family: "Courier New", Courier, ui-monospace, monospace; font-size: 10px; font-weight: bold; white-space: pre; }',
        '    .prompt-user { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; font-weight: bold; fill: #39d353; }',
        '    .prompt-host { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; font-weight: bold; fill: #00f3ff; }',
        '    .prompt-cmd { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; fill: #f0f6fc; }',
        '    .prompt-out { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; font-weight: bold; fill: #00f3ff; }',
        '  </style>',
        '',
        '  <!-- Terminal Outer Window Frame -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" fill="url(#term-bg)" stroke="url(#term-border)" stroke-width="1.5"/>',
        '',
        '  <!-- macOS Control Buttons Bar -->',
        '  <path d="M 2 2 L 438 2 L 438 34 L 2 34 Z" fill="#1c2128" clip-path="inset(0 0 0 0 round 12px 12px 0 0)"/>',
        '  <circle cx="18" cy="18" r="5.5" fill="#ff5f56"/>',
        '  <circle cx="34" cy="18" r="5.5" fill="#ffbd2e"/>',
        '  <circle cx="50" cy="18" r="5.5" fill="#27c93f"/>',
        f'  <text x="{width/2}" y="22" class="term-header-title" text-anchor="middle">zsh — {username}@ascii-terminal ~ 80x24</text>',
        '  <line x1="2" y1="34" x2="438" y2="34" stroke="#30363d" stroke-width="1"/>',
        '',
        '  <!-- ASCII Portrait Terminal Output Area -->',
        '  <g transform="translate(20, 50)">'
    ]

    num_rows = len(safe_lines)
    y_start = 10
    line_height = 13.5

    for i, line in enumerate(safe_lines):
        y_pos = y_start + i * line_height
        delay = round(0.1 + i * 0.06, 3)
        
        ratio = i / max(num_rows - 1, 1)
        if ratio < 0.33:
            line_color = COLORS["cyan"]
        elif ratio < 0.66:
            line_color = COLORS["emerald"]
        else:
            line_color = COLORS["purple"]

        line_html = (
            f'    <text x="0" y="{y_pos}" class="ascii-text" fill="{line_color}" opacity="0">\n'
            f'      {line}\n'
            f'      <animate attributeName="opacity" values="0; 1" dur="0.12s" begin="{delay}s" fill="freeze"/>\n'
            f'      <animateTransform attributeName="transform" type="translate" values="-8 0; 0 0" '
            f'dur="0.12s" begin="{delay}s" fill="freeze"/>\n'
            f'    </text>'
        )
        svg_lines.append(line_html)

    # Sweeping Cursor Block alongside ASCII reveal
    cursor_start_y = y_start - 10
    cursor_end_y = y_start + (num_rows - 1) * line_height - 10
    total_reveal_time = round(0.1 + num_rows * 0.06, 3)

    cursor_html = (
        f'    <!-- Sweeping Reveal Cursor -->\n'
        f'    <rect x="0" y="{cursor_start_y}" width="8" height="12" fill="#ffffff" opacity="0.9">\n'
        f'      <animate attributeName="y" values="{cursor_start_y}; {cursor_end_y}" dur="{total_reveal_time}s" begin="0.1s" fill="freeze"/>\n'
        f'      <animate attributeName="opacity" values="0.9; 0.9; 0" keyTimes="0; 0.95; 1" dur="{total_reveal_time + 0.2}s" begin="0.1s" fill="freeze"/>\n'
        f'    </rect>'
    )
    svg_lines.append(cursor_html)
    svg_lines.append('  </g>')

    # Footer Section: Typewriter $ whoami -> username
    footer_y = height - 55
    typewriter_delay = round(total_reveal_time + 0.2, 3)

    svg_lines.extend([
        '',
        '  <!-- Terminal Footer Typewriter Command Prompt -->',
        '  <line x1="15" y1="' + str(footer_y - 15) + '" x2="425" y2="' + str(footer_y - 15) + '" stroke="#21262d" stroke-width="1"/>',
        f'  <g transform="translate(20, {footer_y})">',
        '    <text x="0" y="0">',
        '      <tspan class="prompt-user">developer</tspan>',
        '      <tspan class="prompt-cmd">@cyber-term</tspan>',
        '      <tspan class="prompt-user">:</tspan>',
        '      <tspan class="prompt-host">~</tspan>',
        '      <tspan class="prompt-cmd">$ </tspan>',
        '    </text>',
        '',
        '    <!-- Typewriter Command: whoami -->',
        f'    <text x="145" y="0" class="prompt-cmd" opacity="0">',
        '      whoami',
        f'      <animate attributeName="opacity" values="0; 1" dur="0.2s" begin="{typewriter_delay}s" fill="freeze"/>',
        '    </text>',
        '',
        '    <!-- Command Output: username result -->',
        f'    <text x="0" y="24" class="prompt-out" opacity="0">',
        f'      &gt; {html.escape(username)}',
        f'      <animate attributeName="opacity" values="0; 1" dur="0.25s" begin="{typewriter_delay + 0.3}s" fill="freeze"/>',
        '    </text>',
        '',
        '    <!-- Blinking Cursor Block -->',
        f'    <rect x="{15 + len(username)*8.5}" y="13" width="8" height="13" fill="#00f3ff" opacity="0">',
        f'      <animate attributeName="opacity" values="0; 1; 1; 0" keyTimes="0; 0.1; 0.5; 1" dur="0.8s" begin="{typewriter_delay + 0.35}s" repeatCount="indefinite"/>',
        '    </rect>',
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 4. SVG GENERATOR: FILE 3 - info-card.svg ---
def generate_info_card_svg(username, output_file="info-card.svg"):
    """
    Generates a Neofetch-style system info card with staggered line SMIL reveals
    and vibrant cyberpunk developer details.
    """
    width = 440
    height = 430

    info_rows = [
        ("OS", "CyberOS 2026.7 (x86_64 Linux)", COLORS["orange"]),
        ("Host", "GitHub Cloud Workstation", COLORS["yellow"]),
        ("Kernel", "5.19.0-cyber-agent-v6", COLORS["green"]),
        ("Uptime", "99.9% Continuous Deployment", COLORS["emerald"]),
        ("Role", "Senior Full-Stack & Systems Engineer", COLORS["cyan"]),
        ("Languages", "Python • TypeScript • Rust • Go", COLORS["blue"]),
        ("Frameworks", "React • Next.js • Node • FastAPI", COLORS["purple"]),
        ("DevOps", "Docker • Kubernetes • CI/CD • AWS", COLORS["magenta"]),
        ("Status", "Building high-performance tools", COLORS["text_bright"]),
    ]

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="info-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#161b22" stop-opacity="0.98"/>',
        '      <stop offset="100%" stop-color="#0d1117" stop-opacity="0.99"/>',
        '    </linearGradient>',
        '    <linearGradient id="info-border" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ff7b72" stop-opacity="0.4"/>',
        '      <stop offset="50%" stop-color="#30363d" stop-opacity="0.8"/>',
        '      <stop offset="100%" stop-color="#00f3ff" stop-opacity="0.5"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        '  <style>',
        '    .info-header { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 14px; font-weight: bold; }',
        '    .info-key { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11.5px; font-weight: bold; }',
        '    .info-val { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11.5px; fill: #c9d1d9; }',
        '    .palette-box { rx: 3px; }',
        '  </style>',
        '',
        '  <!-- Window Outer Frame -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" fill="url(#info-bg)" stroke="url(#info-border)" stroke-width="1.5"/>',
        '',
        '  <!-- Header Title: user@github-node -->',
        '  <g transform="translate(25, 42)">',
        '    <text class="info-header">',
        f'      <tspan fill="{COLORS["orange"]}">{html.escape(username)}</tspan>',
        f'      <tspan fill="{COLORS["text_bright"]}">@</tspan>',
        f'      <tspan fill="{COLORS["cyan"]}">github-node-01</tspan>',
        '    </text>',
        '    ',
        '    <!-- Neofetch Separator Bar -->',
        '    <g transform="translate(0, 10)">',
        '      <rect x="0" y="0" width="60" height="2" fill="' + COLORS["orange"] + '"/>',
        '      <rect x="60" y="0" width="60" height="2" fill="' + COLORS["yellow"] + '"/>',
        '      <rect x="120" y="0" width="60" height="2" fill="' + COLORS["green"] + '"/>',
        '      <rect x="180" y="0" width="60" height="2" fill="' + COLORS["cyan"] + '"/>',
        '      <rect x="240" y="0" width="60" height="2" fill="' + COLORS["purple"] + '"/>',
        '      <rect x="300" y="0" width="85" height="2" fill="' + COLORS["magenta"] + '"/>',
        '    </g>',
        '  </g>',
        '',
        '  <!-- Neofetch Info Rows with Staggered SMIL Slide-up & Fade-in -->',
        '  <g transform="translate(25, 80)">'
    ]

    y_spacing = 28
    for i, (key, val, color) in enumerate(info_rows):
        y_pos = i * y_spacing
        delay = round(0.15 + i * 0.06, 3)

        row_html = (
            f'    <g opacity="0">\n'
            f'      <text x="0" y="{y_pos}" class="info-key" fill="{color}">{key.ljust(11)}:</text>\n'
            f'      <text x="110" y="{y_pos}" class="info-val">{html.escape(val)}</text>\n'
            f'      <animate attributeName="opacity" values="0; 1" dur="0.2s" begin="{delay}s" fill="freeze"/>\n'
            f'      <animateTransform attributeName="transform" type="translate" values="0 6; 0 0" dur="0.2s" begin="{delay}s" fill="freeze"/>\n'
            f'    </g>'
        )
        svg_lines.append(row_html)

    svg_lines.append('  </g>')

    # Palette blocks at bottom
    palette_colors = [
        COLORS["red"], COLORS["orange"], COLORS["yellow"], COLORS["green"],
        COLORS["cyan"], COLORS["blue"], COLORS["purple"], COLORS["text_bright"]
    ]
    
    palette_y = height - 50
    svg_lines.extend([
        '',
        '  <!-- Bottom Terminal Palette Swatches -->',
        f'  <g transform="translate(25, {palette_y})">',
    ])

    for p_idx, p_color in enumerate(palette_colors):
        px = p_idx * 44
        p_delay = round(0.15 + len(info_rows) * 0.06 + p_idx * 0.04, 3)
        p_html = (
            f'    <rect x="{px}" y="0" width="36" height="14" rx="3" fill="{p_color}" opacity="0">\n'
            f'      <animate attributeName="opacity" values="0; 1" dur="0.25s" begin="{p_delay}s" fill="freeze"/>\n'
            f'      <animateTransform attributeName="transform" type="scale" values="0.2; 1" keyTimes="0; 1" dur="0.25s" begin="{p_delay}s" fill="freeze" transform-origin="{px+18}px 7px"/>\n'
            f'    </rect>'
        )
        svg_lines.append(p_html)

    svg_lines.extend([
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 5. README GENERATOR ---
def generate_readme(username, readme_path="README.md"):
    """
    Creates / updates README.md with side-by-side table layout for cards
    and centered contribution animation.
    """
    content = f"""# <h1 align="center">✨ Hi there, I'm {username} 👋</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=00F3FF&center=true&vcenter=true&width=600&lines=Full-Stack+Architect+%26+Systems+Developer;Building+Next-Gen+Interactive+Experiences;Cyberpunk+Aesthetics+%2B+High-Performance+Code" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/github/followers/{username}?label=Followers&style=for-the-badge&color=00f3ff&logo=github" alt="GitHub Followers"/>
  </a>
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/github/stars/{username}?label=Total%20Stars&style=for-the-badge&color=ff9e3b&logo=star" alt="GitHub Stars"/>
  </a>
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/badge/Status-Active%20Building-39d353?style=for-the-badge&logo=terminal" alt="Status"/>
  </a>
</p>

<br />

<!-- Side-by-Side Cards: Terminal ASCII Portrait + Neofetch Info Card -->
<div align="center">
  <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td width="50%" align="center" valign="top" style="padding-right: 8px;">
        <a href="https://github.com/{username}">
          <img src="./terminal-card.svg" alt="Terminal ASCII Portrait" width="100%" />
        </a>
      </td>
      <td width="50%" align="center" valign="top" style="padding-left: 8px;">
        <a href="https://github.com/{username}">
          <img src="./info-card.svg" alt="Neofetch Info Card" width="100%" />
        </a>
      </td>
    </tr>
  </table>
</div>

<br />

<!-- Centered Animated Contribution Calendar -->
<div align="center">
  <a href="https://github.com/{username}">
    <img src="./github-contribution-animation.svg" alt="GitHub Animated Contribution Graph" width="100%" />
  </a>
</div>

<br />

---

<p align="center">
  ⚡ <i>Generated with Cyberpunk Animated SVG Engine</i>
</p>
"""
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] Successfully updated '{readme_path}'")

# --- MAIN CLI EXECUTION ---
def main():
    parser = argparse.ArgumentParser(description="Generate Cyberpunk Animated GitHub Profile README & SVGs")
    parser.add_argument("--username", type=str, default=DEFAULT_USERNAME, help="GitHub username")
    parser.add_argument("--outdir", type=str, default=".", help="Output directory")
    args = parser.parse_args()

    username = args.username
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    print(f"[+] Generating GitHub Profile SVGs for user '{username}'...")

    # 1. Fetch ASCII Art
    ascii_lines = fetch_avatar_ascii(username)

    # 2. Generate Files
    contrib_path = os.path.join(outdir, "github-contribution-animation.svg")
    terminal_path = os.path.join(outdir, "terminal-card.svg")
    info_path = os.path.join(outdir, "info-card.svg")
    readme_path = os.path.join(outdir, "README.md")

    generate_contribution_svg(username, contrib_path)
    generate_terminal_card_svg(username, ascii_lines, terminal_path)
    generate_info_card_svg(username, info_path)
    generate_readme(username, readme_path)

    print("[🎉] All tasks completed successfully!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Cyberpunk Mind-Blowing Animated GitHub Profile SVG Generator
============================================================
Generates three ultra-innovative, glassmorphic, SMIL-animated SVG cards:
  1. github-contribution-animation.svg (Holographic Matrix Grid with scanning laser & glint)
  2. terminal-card.svg (Cyber HUD Terminal with ASCII portrait, laser scanner & typewriter footer)
  3. info-card.svg (Glassmorphic Skill HUD with animated skill bars & neofetch palette)

Also creates/updates README.md with side-by-side table layout & centered contribution matrix.
"""

import os
import sys
import math
import random
import json
import argparse
import html
import urllib.request

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

DEFAULT_USERNAME = "Niveditagupta03"

# Ultra Cyberpunk Neon Glass Palette
COLORS = {
    "space_bg": "#070a14",
    "card_bg": "#0d1322",
    "border_cyan": "#00f0ff",
    "border_pink": "#ff007f",
    "border_purple": "#7928ca",
    "border_dark": "#1f293d",
    "text_bright": "#f0f6fc",
    "text_muted": "#8b949e",
    "neon_cyan": "#00f0ff",
    "neon_pink": "#ff007f",
    "neon_purple": "#a371f7",
    "neon_green": "#00ff66",
    "neon_gold": "#ffb800",
    "neon_blue": "#38bdf8",
    # Contribution level colors
    "l0": "#0e1626",
    "l1": "#004d38",
    "l2": "#008e5a",
    "l3": "#00e676",
    "l4": "#00ff88",
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
    Fetches user avatar from GitHub and converts it into dense ASCII art using PIL.
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
            img = img.convert('L')
            
            aspect_ratio = img.height / img.width
            target_height = int(width * aspect_ratio * 0.52)
            target_height = min(max(target_height, 18), height)
            
            img = img.resize((width, target_height), Image.Resampling.LANCZOS)
            
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

# --- 2. SVG GENERATOR 1: HOLOGRAPHIC CONTRIBUTION MATRIX ---
def generate_contribution_svg(username, output_file="github-contribution-animation.svg"):
    cols = 53
    rows = 7
    square_size = 11
    gap = 3
    margin_left = 35
    margin_top = 45
    
    width = margin_left + cols * (square_size + gap) + 20
    height = margin_top + rows * (square_size + gap) + 40

    random.seed(42 + sum(ord(c) for c in username))
    grid_levels = []
    for c in range(cols):
        col_levels = []
        for r in range(rows):
            val = random.choices([0, 1, 2, 3, 4], weights=[0.32, 0.26, 0.21, 0.13, 0.08])[0]
            col_levels.append(val)
        grid_levels.append(col_levels)

    total_contributions = sum(sum(col) for col in grid_levels) * 3 + random.randint(500, 1400)

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <!-- Ambient Hologram Glow Filters -->',
        '    <filter id="glow-l3" x="-50%" y="-50%" width="200%" height="200%">',
        '      <feGaussianBlur stdDeviation="2.5" result="blur" />',
        '      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>',
        '    </filter>',
        '    <filter id="glow-l4" x="-100%" y="-100%" width="300%" height="300%">',
        '      <feGaussianBlur stdDeviation="4" result="blur1" />',
        '      <feGaussianBlur in="SourceGraphic" stdDeviation="1.5" result="blur2" />',
        '      <feMerge><feMergeNode in="blur1" /><feMergeNode in="blur2" /><feMergeNode in="SourceGraphic" /></feMerge>',
        '    </filter>',
        '    <linearGradient id="bg-space" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#0b1120"/>',
        '      <stop offset="50%" stop-color="#070a14"/>',
        '      <stop offset="100%" stop-color="#03050a"/>',
        '    </linearGradient>',
        '    <linearGradient id="border-neon" x1="0%" y1="0%" x2="100%" y2="0%">',
        '      <stop offset="0%" stop-color="#00f0ff"/>',
        '      <stop offset="50%" stop-color="#ff007f"/>',
        '      <stop offset="100%" stop-color="#7928ca"/>',
        '    </linearGradient>',
        '    <linearGradient id="laser-sweep" x1="0%" y1="0%" x2="0%" y2="100%">',
        '      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0"/>',
        '      <stop offset="50%" stop-color="#00f0ff" stop-opacity="0.8"/>',
        '      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        '  <style>',
        '    .title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 13px; font-weight: 700; fill: #f0f6fc; letter-spacing: 0.5px; }',
        '    .sub-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; fill: #00f0ff; font-weight: 600; }',
        '    .month-label { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9px; fill: #8b949e; }',
        '    .day-label { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9px; fill: #8b949e; }',
        '    .legend-label { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9px; fill: #8b949e; }',
        '  </style>',
        '',
        '  <!-- Glass Container Background -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" fill="url(#bg-space)" stroke="url(#border-neon)" stroke-width="1.5"/>',
        '',
        '  <!-- Cyber Corner HUD Accents -->',
        '  <path d="M 6 18 L 6 6 L 18 6" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        f'  <path d="M {width-18} 6 L {width-6} 6 L {width-6} 18" fill="none" stroke="#ff007f" stroke-width="2"/>',
        f'  <path d="M 6 {height-18} L 6 {height-6} L 18 {height-6}" fill="none" stroke="#ff007f" stroke-width="2"/>',
        f'  <path d="M {width-18} {height-6} L {width-6} {height-6} L {width-6} {height-18}" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        '',
        '  <!-- Live Status Pill Header -->',
        '  <g transform="translate(20, 24)">',
        '    <circle cx="0" cy="-4" r="4" fill="#00ff66">',
        '      <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <text x="12" y="0" class="title">HOLOGRAPHIC CONTRIBUTION MATRIX</text>',
        '  </g>',
        f'  <text x="{width-20}" y="24" class="sub-title" text-anchor="end">{total_contributions:,} COMMITS / YEAR</text>',
        ''
    ]

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for i, month in enumerate(months):
        x_pos = margin_left + int(i * (cols / 12) * (square_size + gap))
        svg_lines.append(f'  <text x="{x_pos}" y="{margin_top - 10}" class="month-label">{month}</text>')

    day_names = [("Mon", 1), ("Wed", 3), ("Fri", 5)]
    for d_name, d_idx in day_names:
        y_pos = margin_top + d_idx * (square_size + gap) + 9
        svg_lines.append(f'  <text x="12" y="{y_pos}" class="day-label">{d_name}</text>')

    svg_lines.append('  <!-- Contribution Matrix Cells -->')
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

            diag_idx = c + (rows - 1 - r)
            start_delay = round(diag_idx * 0.02, 3)

            sq_html = (
                f'    <rect x="{x}" y="{y}" width="{square_size}" height="{square_size}" rx="2.5" '
                f'fill="{fill_color}" opacity="0"{filter_attr}>\n'
                f'      <animate attributeName="opacity" values="0; 1" dur="0.25s" begin="{start_delay}s" fill="freeze"/>\n'
                f'      <animateTransform attributeName="transform" type="scale" values="0.1; 1.25; 1" keyTimes="0; 0.7; 1" '
                f'dur="0.3s" begin="{start_delay}s" fill="freeze" transform-origin="{cx}px {cy}px"/>\n'
                f'    </rect>'
            )
            svg_lines.append(sq_html)

            # Specular Glint Overlay Flash
            glint_color = "#ffffff" if lvl < 3 else COLORS["neon_cyan"]
            glint_html = (
                f'    <rect x="{x}" y="{y}" width="{square_size}" height="{square_size}" rx="2.5" '
                f'fill="{glint_color}" opacity="0" pointer-events="none">\n'
                f'      <animate attributeName="opacity" values="0; 0.95; 0" keyTimes="0; 0.3; 1" '
                f'dur="0.35s" begin="{round(start_delay + 0.04, 3)}s" fill="freeze"/>\n'
                f'    </rect>'
            )
            svg_lines.append(glint_html)

    svg_lines.append('  </g>')

    # Horizontal Scanning Laser Beam (Sweeps Left to Right)
    laser_start_x = margin_left
    laser_end_x = width - 20
    laser_y = margin_top - 5
    laser_h = rows * (square_size + gap) + 10

    svg_lines.extend([
        '  <!-- Laser Scanning Beam Effect -->',
        f'  <rect x="{laser_start_x}" y="{laser_y}" width="3" height="{laser_h}" fill="url(#laser-sweep)" opacity="0.85">',
        f'    <animate attributeName="x" values="{laser_start_x}; {laser_end_x}; {laser_start_x}" dur="4.5s" repeatCount="indefinite"/>',
        '  </rect>',
        ''
    ])

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

# --- 3. SVG GENERATOR 2: CYBER HUD TERMINAL & ASCII PORTRAIT ---
def generate_terminal_card_svg(username, ascii_lines, output_file="terminal-card.svg"):
    width = 440
    height = 440
    
    safe_lines = [html.escape(line) for line in ascii_lines]
    
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="term-bg-space" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#0d1424" stop-opacity="0.98"/>',
        '      <stop offset="100%" stop-color="#050812" stop-opacity="0.99"/>',
        '    </linearGradient>',
        '    <linearGradient id="hud-border" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#00f0ff"/>',
        '      <stop offset="50%" stop-color="#ff007f"/>',
        '      <stop offset="100%" stop-color="#7928ca"/>',
        '    </linearGradient>',
        '    <linearGradient id="laser-line-grad" x1="0%" y1="0%" x2="100%" y2="0%">',
        '      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0"/>',
        '      <stop offset="50%" stop-color="#00f0ff" stop-opacity="0.9"/>',
        '      <stop offset="100%" stop-color="#ff007f" stop-opacity="0"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        '  <style>',
        '    .term-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; fill: #00f0ff; font-weight: 700; letter-spacing: 0.8px; }',
        '    .ascii-text { font-family: "Courier New", Courier, ui-monospace, monospace; font-size: 10px; font-weight: bold; white-space: pre; }',
        '    .prompt-user { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11.5px; font-weight: bold; fill: #ff007f; }',
        '    .prompt-host { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11.5px; font-weight: bold; fill: #00f0ff; }',
        '    .prompt-cmd { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11.5px; fill: #f0f6fc; }',
        '    .prompt-out { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11.5px; font-weight: bold; fill: #00ff66; }',
        '  </style>',
        '',
        '  <!-- Terminal Window Frame -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" fill="url(#term-bg-space)" stroke="url(#hud-border)" stroke-width="1.5"/>',
        '',
        '  <!-- Cyber Corner HUD Accents -->',
        '  <path d="M 6 18 L 6 6 L 18 6" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        f'  <path d="M {width-18} 6 L {width-6} 6 L {width-6} 18" fill="none" stroke="#ff007f" stroke-width="2"/>',
        f'  <path d="M 6 {height-18} L 6 {height-6} L 18 {height-6}" fill="none" stroke="#ff007f" stroke-width="2"/>',
        f'  <path d="M {width-18} {height-6} L {width-6} {height-6} L {width-6} {height-18}" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        '',
        '  <!-- Header Control Bar -->',
        '  <path d="M 2 2 L 438 2 L 438 34 L 2 34 Z" fill="#141c2e" clip-path="inset(0 0 0 0 round 12px 12px 0 0)"/>',
        '  <circle cx="18" cy="18" r="5" fill="#ff5f56"/>',
        '  <circle cx="34" cy="18" r="5" fill="#ffbd2e"/>',
        '  <circle cx="50" cy="18" r="5" fill="#27c93f"/>',
        f'  <text x="{width/2}" y="22" class="term-title" text-anchor="middle">SYS://OPTICAL_TERMINAL.v3 [LIVE]</text>',
        '  <line x1="2" y1="34" x2="438" y2="34" stroke="#1f293d" stroke-width="1"/>',
        '',
        '  <!-- ASCII Portrait Terminal Area -->',
        '  <g transform="translate(20, 50)">'
    ]

    num_rows = len(safe_lines)
    y_start = 10
    line_height = 13.5

    for i, line in enumerate(safe_lines):
        y_pos = y_start + i * line_height
        delay = round(0.1 + i * 0.05, 3)
        
        ratio = i / max(num_rows - 1, 1)
        if ratio < 0.33:
            line_color = COLORS["neon_cyan"]
        elif ratio < 0.66:
            line_color = COLORS["neon_pink"]
        else:
            line_color = COLORS["neon_purple"]

        line_html = (
            f'    <text x="0" y="{y_pos}" class="ascii-text" fill="{line_color}" opacity="0">\n'
            f'      {line}\n'
            f'      <animate attributeName="opacity" values="0; 1" dur="0.12s" begin="{delay}s" fill="freeze"/>\n'
            f'      <animateTransform attributeName="transform" type="translate" values="-10 0; 0 0" dur="0.12s" begin="{delay}s" fill="freeze"/>\n'
            f'    </text>'
        )
        svg_lines.append(line_html)

    # Laser scanner line moving vertically across ASCII portrait
    scan_y_start = y_start - 5
    scan_y_end = y_start + (num_rows - 1) * line_height + 5
    total_reveal_time = round(0.1 + num_rows * 0.05, 3)

    laser_scan_html = (
        f'    <!-- Optical Laser Scanner Bar -->\n'
        f'    <rect x="0" y="{scan_y_start}" width="390" height="2" fill="url(#laser-line-grad)" opacity="0.95">\n'
        f'      <animate attributeName="y" values="{scan_y_start}; {scan_y_end}; {scan_y_start}" dur="3.2s" begin="0.1s" repeatCount="indefinite"/>\n'
        f'    </rect>'
    )
    svg_lines.append(laser_scan_html)
    svg_lines.append('  </g>')

    # Footer Section: Command Prompt Typewriter
    footer_y = height - 55
    typewriter_delay = round(total_reveal_time + 0.15, 3)

    svg_lines.extend([
        '',
        '  <!-- Terminal Footer Typewriter Command Prompt -->',
        '  <line x1="15" y1="' + str(footer_y - 15) + '" x2="425" y2="' + str(footer_y - 15) + '" stroke="#1f293d" stroke-width="1"/>',
        f'  <g transform="translate(20, {footer_y})">',
        '    <text x="0" y="0">',
        '      <tspan class="prompt-user">cyber</tspan>',
        '      <tspan class="prompt-cmd">@node-x</tspan>',
        '      <tspan class="prompt-user">:</tspan>',
        '      <tspan class="prompt-host">~</tspan>',
        '      <tspan class="prompt-cmd">$ </tspan>',
        '    </text>',
        '',
        '    <!-- Typewriter Command -->',
        f'    <text x="125" y="0" class="prompt-cmd" opacity="0">',
        '      whoami --verbose',
        f'      <animate attributeName="opacity" values="0; 1" dur="0.2s" begin="{typewriter_delay}s" fill="freeze"/>',
        '    </text>',
        '',
        '    <!-- Command Output -->',
        f'    <text x="0" y="24" class="prompt-out" opacity="0">',
        f'      &gt; USER: {html.escape(username)} | STATUS: ACTIVE',
        f'      <animate attributeName="opacity" values="0; 1" dur="0.25s" begin="{typewriter_delay + 0.25}s" fill="freeze"/>',
        '    </text>',
        '',
        '    <!-- Blinking Neon Cursor -->',
        f'    <rect x="{15 + (len(username)+18)*7.5}" y="13" width="8" height="13" fill="#00f0ff" opacity="0">',
        f'      <animate attributeName="opacity" values="0; 1; 1; 0" keyTimes="0; 0.1; 0.5; 1" dur="0.8s" begin="{typewriter_delay + 0.3}s" repeatCount="indefinite"/>',
        '    </rect>',
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 4. SVG GENERATOR 3: GLASSMOPHIC SKILL HUD CARD ---
def generate_info_card_svg(username, output_file="info-card.svg"):
    width = 440
    height = 440

    skills = [
        ("Python & AI Agents", 95, COLORS["neon_cyan"], COLORS["neon_pink"]),
        ("TypeScript & React", 92, COLORS["neon_pink"], COLORS["neon_purple"]),
        ("System Architecture", 88, COLORS["neon_purple"], COLORS["neon_blue"]),
        ("Docker & Cloud Dev", 85, COLORS["neon_gold"], COLORS["neon_green"]),
    ]

    info_rows = [
        ("OS", "CyberOS 2026.7 (x86_64)", COLORS["neon_pink"]),
        ("Host", "GitHub Cloud Workstation", COLORS["neon_gold"]),
        ("Kernel", "5.19.0-cyber-node-v6", COLORS["neon_green"]),
        ("Role", "Senior Full-Stack & Systems Dev", COLORS["neon_cyan"]),
        ("Focus", "AI Agents • High-Perf SVGs • WebApp", COLORS["neon_purple"]),
        ("Status", "100% OPERATIONAL", COLORS["neon_green"]),
    ]

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="info-bg-space" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#0d1424" stop-opacity="0.98"/>',
        '      <stop offset="100%" stop-color="#050812" stop-opacity="0.99"/>',
        '    </linearGradient>',
        '    <linearGradient id="info-hud-border" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ff007f"/>',
        '      <stop offset="50%" stop-color="#00f0ff"/>',
        '      <stop offset="100%" stop-color="#7928ca"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        '  <style>',
        '    .info-header { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 13px; font-weight: bold; }',
        '    .section-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10.5px; font-weight: bold; fill: #8b949e; letter-spacing: 1px; }',
        '    .info-key { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; font-weight: bold; }',
        '    .info-val { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; fill: #c9d1d9; }',
        '    .skill-label { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; font-weight: bold; fill: #f0f6fc; }',
        '    .skill-pct { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; font-weight: bold; fill: #00f0ff; }',
        '  </style>',
        '',
        '  <!-- Window Outer Frame -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" fill="url(#info-bg-space)" stroke="url(#info-hud-border)" stroke-width="1.5"/>',
        '',
        '  <!-- Cyber Corner HUD Accents -->',
        '  <path d="M 6 18 L 6 6 L 18 6" fill="none" stroke="#ff007f" stroke-width="2"/>',
        f'  <path d="M {width-18} 6 L {width-6} 6 L {width-6} 18" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        f'  <path d="M 6 {height-18} L 6 {height-6} L 18 {height-6}" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        f'  <path d="M {width-18} {height-6} L {width-6} {height-6} L {width-6} {height-18}" fill="none" stroke="#ff007f" stroke-width="2"/>',
        '',
        '  <!-- Header Title: user@github-node -->',
        '  <g transform="translate(22, 38)">',
        '    <text class="info-header">',
        f'      <tspan fill="{COLORS["neon_pink"]}">{html.escape(username)}</tspan>',
        f'      <tspan fill="{COLORS["text_bright"]}">@</tspan>',
        f'      <tspan fill="{COLORS["neon_cyan"]}">CYBER-NODE-X</tspan>',
        '    </text>',
        '    ',
        '    <!-- Multi-Segment Neofetch Accent Line -->',
        '    <g transform="translate(0, 10)">',
        '      <rect x="0" y="0" width="65" height="2" fill="' + COLORS["neon_pink"] + '"/>',
        '      <rect x="65" y="0" width="65" height="2" fill="' + COLORS["neon_gold"] + '"/>',
        '      <rect x="130" y="0" width="65" height="2" fill="' + COLORS["neon_green"] + '"/>',
        '      <rect x="195" y="0" width="65" height="2" fill="' + COLORS["neon_cyan"] + '"/>',
        '      <rect x="260" y="0" width="65" height="2" fill="' + COLORS["neon_purple"] + '"/>',
        '      <rect x="325" y="0" width="70" height="2" fill="' + COLORS["neon_blue"] + '"/>',
        '    </g>',
        '  </g>',
        '',
        '  <!-- SECTION 1: SYSTEM INFO -->',
        '  <g transform="translate(22, 70)">'
    ]

    y_spacing = 22
    for i, (key, val, color) in enumerate(info_rows):
        y_pos = i * y_spacing
        delay = round(0.12 + i * 0.05, 3)

        row_html = (
            f'    <g opacity="0">\n'
            f'      <text x="0" y="{y_pos}" class="info-key" fill="{color}">{key.ljust(9)}:</text>\n'
            f'      <text x="95" y="{y_pos}" class="info-val">{html.escape(val)}</text>\n'
            f'      <animate attributeName="opacity" values="0; 1" dur="0.2s" begin="{delay}s" fill="freeze"/>\n'
            f'      <animateTransform attributeName="transform" type="translate" values="0 6; 0 0" dur="0.2s" begin="{delay}s" fill="freeze"/>\n'
            f'    </g>'
        )
        svg_lines.append(row_html)

    svg_lines.append('  </g>')

    # SECTION 2: ANIMATED SKILL BARS
    skills_start_y = 220
    svg_lines.extend([
        '',
        f'  <!-- SECTION 2: SKILL MATRIX BARS -->',
        f'  <g transform="translate(22, {skills_start_y})">',
        '    <text x="0" y="0" class="section-title">// TECH SKILL MATRIX</text>',
        '  </g>',
        f'  <g transform="translate(22, {skills_start_y + 15})">'
    ])

    max_bar_width = 240
    for s_idx, (skill_name, pct, c1, c2) in enumerate(skills):
        sy = s_idx * 32
        target_w = int(max_bar_width * (pct / 100))
        s_delay = round(0.15 + len(info_rows) * 0.05 + s_idx * 0.08, 3)
        grad_id = f"skill-grad-{s_idx}"

        # Create gradient def for skill bar
        svg_lines.insert(8, (
            f'    <linearGradient id="{grad_id}" x1="0%" y1="0%" x2="100%" y2="0%">\n'
            f'      <stop offset="0%" stop-color="{c1}"/>\n'
            f'      <stop offset="100%" stop-color="{c2}"/>\n'
            f'    </linearGradient>'
        ))

        skill_html = (
            f'    <g opacity="0">\n'
            f'      <text x="0" y="{sy}" class="skill-label">{skill_name}</text>\n'
            f'      <text x="{width-45}" y="{sy}" class="skill-pct" text-anchor="end">{pct}%</text>\n'
            f'      <!-- Background Bar Track -->\n'
            f'      <rect x="0" y="{sy+6}" width="{max_bar_width+90}" height="8" rx="4" fill="#141c2e"/>\n'
            f'      <!-- Animated Progress Bar -->\n'
            f'      <rect x="0" y="{sy+6}" width="0" height="8" rx="4" fill="url(#{grad_id})">\n'
            f'        <animate attributeName="width" values="0; {target_w+90}" dur="0.8s" begin="{s_delay}s" fill="freeze"/>\n'
            f'      </rect>\n'
            f'      <animate attributeName="opacity" values="0; 1" dur="0.2s" begin="{s_delay}s" fill="freeze"/>\n'
            f'    </g>'
        )
        svg_lines.append(skill_html)

    svg_lines.append('  </g>')

    # Bottom Terminal Palette Swatches
    palette_colors = [
        COLORS["neon_pink"], COLORS["neon_gold"], COLORS["neon_green"],
        COLORS["neon_cyan"], COLORS["neon_blue"], COLORS["neon_purple"], COLORS["text_bright"]
    ]
    
    palette_y = height - 42
    svg_lines.extend([
        '',
        '  <!-- Bottom Palette Swatches -->',
        f'  <g transform="translate(22, {palette_y})">',
    ])

    for p_idx, p_color in enumerate(palette_colors):
        px = p_idx * 52
        p_delay = round(0.5 + p_idx * 0.04, 3)
        p_html = (
            f'    <rect x="{px}" y="0" width="42" height="12" rx="3" fill="{p_color}" opacity="0">\n'
            f'      <animate attributeName="opacity" values="0; 1" dur="0.25s" begin="{p_delay}s" fill="freeze"/>\n'
            f'      <animateTransform attributeName="transform" type="scale" values="0.2; 1" keyTimes="0; 1" dur="0.25s" begin="{p_delay}s" fill="freeze" transform-origin="{px+21}px 6px"/>\n'
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
    content = f"""# <h1 align="center">✨ Hi there, I'm {username} 👋</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=23&pause=1000&color=00F0FF&center=true&vcenter=true&width=650&lines=Full-Stack+Architect+%26+Systems+Developer;Building+Mind-Blowing+Interactive+Experiences;Cyberpunk+Aesthetics+%2B+High-Performance+Code" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/github/followers/{username}?label=Followers&style=for-the-badge&color=00f0ff&logo=github" alt="GitHub Followers"/>
  </a>
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/github/stars/{username}?label=Total%20Stars&style=for-the-badge&color=ff007f&logo=star" alt="GitHub Stars"/>
  </a>
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/badge/Status-100%25%20Operational-00ff66?style=for-the-badge&logo=terminal" alt="Status"/>
  </a>
</p>

<br />

<!-- Side-by-Side HUD Cards: Terminal ASCII Portrait + Glassmorphic Skill HUD -->
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
          <img src="./info-card.svg" alt="Glassmorphic Skill HUD" width="100%" />
        </a>
      </td>
    </tr>
  </table>
</div>

<br />

<!-- Centered Holographic Contribution Matrix -->
<div align="center">
  <a href="https://github.com/{username}">
    <img src="./github-contribution-animation.svg" alt="GitHub Holographic Contribution Graph" width="100%" />
  </a>
</div>

<br />

---

<p align="center">
  ⚡ <i>Powered by Cyberpunk Glassmorphic SVG Engine</i>
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

    print(f"[+] Generating Cyberpunk Glassmorphic SVGs for user '{username}'...")

    ascii_lines = fetch_avatar_ascii(username)

    contrib_path = os.path.join(outdir, "github-contribution-animation.svg")
    terminal_path = os.path.join(outdir, "terminal-card.svg")
    info_path = os.path.join(outdir, "info-card.svg")
    readme_path = os.path.join(outdir, "README.md")

    generate_contribution_svg(username, contrib_path)
    generate_terminal_card_svg(username, ascii_lines, terminal_path)
    generate_info_card_svg(username, info_path)
    generate_readme(username, readme_path)

    print("[🎉] All mind-blowing SVG cards generated successfully!")

if __name__ == "__main__":
    main()

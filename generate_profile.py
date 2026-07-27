#!/usr/bin/env python3
"""
Cosmic Galaxy & Planetary Orbit GitHub Profile SVG Generator
============================================================
Generates three mind-blowing, cosmic-themed SMIL-animated SVG cards:
  1. github-contribution-animation.svg (Cosmic Nebula Matrix with shooting stars & starlight flashes)
  2. terminal-card.svg (Planetary Orbit System with revolving tech planets & twinkling starfields)
  3. info-card.svg (Constellation HUD & Sci-Fi Circular Activity Telemetry Rings)

Also updates README.md with cosmic badges and side-by-side card layout.
"""

import os
import sys
import math
import random
import json
import argparse
import html
import urllib.request

DEFAULT_USERNAME = "Niveditagupta03"

# Cosmic Galaxy Color Palette
COLORS = {
    "space_dark": "#030712",
    "nebula_purple": "#160829",
    "nebula_blue": "#0d1124",
    "border_cyan": "#00f0ff",
    "border_pink": "#ff007f",
    "border_purple": "#7928ca",
    "text_bright": "#f0f6fc",
    "text_muted": "#8b949e",
    "star_gold": "#ffb800",
    "cyan": "#00f0ff",
    "pink": "#ff007f",
    "purple": "#a371f7",
    "green": "#00ff88",
    "blue": "#38bdf8",
    # Contribution level colors (Starlight progression)
    "l0": "#0c1222",
    "l1": "#123055",
    "l2": "#0066aa",
    "l3": "#00b4d8",
    "l4": "#00f0ff",
}

# --- 1. SVG GENERATOR 1: COSMIC NEBULA CONTRIBUTION MATRIX ---
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
            val = random.choices([0, 1, 2, 3, 4], weights=[0.30, 0.26, 0.22, 0.14, 0.08])[0]
            col_levels.append(val)
        grid_levels.append(col_levels)

    total_contributions = sum(sum(col) for col in grid_levels) * 3 + random.randint(600, 1500)

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <!-- Cosmic Glow Filters -->',
        '    <filter id="star-glow" x="-50%" y="-50%" width="200%" height="200%">',
        '      <feGaussianBlur stdDeviation="3" result="blur" />',
        '      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>',
        '    </filter>',
        '    <filter id="supernova-glow" x="-100%" y="-100%" width="300%" height="300%">',
        '      <feGaussianBlur stdDeviation="5" result="blur1" />',
        '      <feGaussianBlur stdDeviation="2" result="blur2" />',
        '      <feMerge><feMergeNode in="blur1" /><feMergeNode in="blur2" /><feMergeNode in="SourceGraphic" /></feMerge>',
        '    </filter>',
        '    <linearGradient id="nebula-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#160829"/>',
        '      <stop offset="40%" stop-color="#090d1f"/>',
        '      <stop offset="100%" stop-color="#030712"/>',
        '    </linearGradient>',
        '    <linearGradient id="cosmic-border" x1="0%" y1="0%" x2="100%" y2="0%">',
        '      <stop offset="0%" stop-color="#00f0ff"/>',
        '      <stop offset="50%" stop-color="#7928ca"/>',
        '      <stop offset="100%" stop-color="#ff007f"/>',
        '    </linearGradient>',
        '    <linearGradient id="meteor-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>',
        '      <stop offset="30%" stop-color="#00f0ff" stop-opacity="0.8"/>',
        '      <stop offset="100%" stop-color="#7928ca" stop-opacity="0"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        '  <style>',
        '    .title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 13px; font-weight: 700; fill: #f0f6fc; letter-spacing: 1px; }',
        '    .sub-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; fill: #00f0ff; font-weight: 600; }',
        '    .month-label { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9px; fill: #8b949e; }',
        '    .day-label { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9px; fill: #8b949e; }',
        '    .legend-label { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9px; fill: #8b949e; }',
        '  </style>',
        '',
        '  <!-- Background Canvas -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#nebula-bg)" stroke="url(#cosmic-border)" stroke-width="1.5"/>',
        ''
    ]

    # Add Twinkling Background Stars
    random.seed(101)
    svg_lines.append('  <!-- Twinkling Starfield -->')
    for s in range(30):
        sx = random.randint(15, width - 15)
        sy = random.randint(15, height - 15)
        sr = round(random.uniform(0.8, 1.8), 1)
        s_dur = round(random.uniform(1.2, 3.0), 1)
        s_delay = round(random.uniform(0, 2.0), 1)
        svg_lines.append(
            f'  <circle cx="{sx}" cy="{sy}" r="{sr}" fill="#ffffff" opacity="0.3">\n'
            f'    <animate attributeName="opacity" values="0.2; 0.9; 0.2" dur="{s_dur}s" begin="{s_delay}s" repeatCount="indefinite"/>\n'
            f'  </circle>'
        )

    # Shooting Star Meteors
    svg_lines.extend([
        '',
        '  <!-- Shooting Meteor Effect -->',
        '  <path d="M 50 10 L 170 130" stroke="url(#meteor-grad)" stroke-width="2" stroke-linecap="round" opacity="0">',
        '    <animate attributeName="opacity" values="0; 1; 0" keyTimes="0; 0.2; 1" dur="3.5s" begin="0.5s" repeatCount="indefinite"/>',
        '    <animateTransform attributeName="transform" type="translate" values="-100 -100; 300 300" dur="3.5s" begin="0.5s" repeatCount="indefinite"/>',
        '  </path>',
        '  <path d="M 400 5 L 550 125" stroke="url(#meteor-grad)" stroke-width="1.5" stroke-linecap="round" opacity="0">',
        '    <animate attributeName="opacity" values="0; 1; 0" keyTimes="0; 0.2; 1" dur="4.2s" begin="2.1s" repeatCount="indefinite"/>',
        '    <animateTransform attributeName="transform" type="translate" values="-80 -80; 250 250" dur="4.2s" begin="2.1s" repeatCount="indefinite"/>',
        '  </path>',
        ''
    ])

    # Live Header Title
    svg_lines.extend([
        '  <!-- Live Header -->',
        '  <g transform="translate(20, 24)">',
        '    <circle cx="0" cy="-4" r="4.5" fill="#ffb800" filter="url(#star-glow)">',
        '      <animate attributeName="opacity" values="0.4;1;0.4" dur="1.8s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <text x="14" y="0" class="title">COSMIC CONTRIBUTION MATRIX</text>',
        '  </g>',
        f'  <text x="{width-20}" y="24" class="sub-title" text-anchor="end">✦ {total_contributions:,} STARLIGHT COMMITS</text>',
        ''
    ])

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for i, month in enumerate(months):
        x_pos = margin_left + int(i * (cols / 12) * (square_size + gap))
        svg_lines.append(f'  <text x="{x_pos}" y="{margin_top - 10}" class="month-label">{month}</text>')

    day_names = [("Mon", 1), ("Wed", 3), ("Fri", 5)]
    for d_name, d_idx in day_names:
        y_pos = margin_top + d_idx * (square_size + gap) + 9
        svg_lines.append(f'  <text x="12" y="{y_pos}" class="day-label">{d_name}</text>')

    svg_lines.append('  <!-- Contribution Starlight Grid -->')
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
                filter_attr = ' filter="url(#star-glow)"'
            elif lvl == 4:
                filter_attr = ' filter="url(#supernova-glow)"'

            diag_idx = c + (rows - 1 - r)
            start_delay = round(diag_idx * 0.02, 3)

            sq_html = (
                f'    <rect x="{x}" y="{y}" width="{square_size}" height="{square_size}" rx="3" '
                f'fill="{fill_color}" opacity="0"{filter_attr}>\n'
                f'      <animate attributeName="opacity" values="0; 1" dur="0.25s" begin="{start_delay}s" fill="freeze"/>\n'
                f'      <animateTransform attributeName="transform" type="scale" values="0.1; 1.3; 1" keyTimes="0; 0.7; 1" '
                f'dur="0.3s" begin="{start_delay}s" fill="freeze" transform-origin="{cx}px {cy}px"/>\n'
                f'    </rect>'
            )
            svg_lines.append(sq_html)

            # Specular Starlight Flash
            glint_color = "#ffffff" if lvl < 3 else COLORS["cyan"]
            glint_html = (
                f'    <rect x="{x}" y="{y}" width="{square_size}" height="{square_size}" rx="3" '
                f'fill="{glint_color}" opacity="0" pointer-events="none">\n'
                f'      <animate attributeName="opacity" values="0; 0.95; 0" keyTimes="0; 0.3; 1" '
                f'dur="0.35s" begin="{round(start_delay + 0.04, 3)}s" fill="freeze"/>\n'
                f'    </rect>'
            )
            svg_lines.append(glint_html)

    svg_lines.append('  </g>')

    # Legend
    legend_y = height - 15
    legend_x_start = width - 130
    svg_lines.append(f'  <text x="{legend_x_start - 25}" y="{legend_y + 9}" class="legend-label">Less</text>')
    for l_idx in range(5):
        lx = legend_x_start + l_idx * (11 + 3)
        l_color = COLORS[f"l{l_idx}"]
        svg_lines.append(f'  <rect x="{lx}" y="{legend_y}" width="11" height="11" rx="3" fill="{l_color}"/>')
    svg_lines.append(f'  <text x="{legend_x_start + 5 * 14 + 5}" y="{legend_y + 9}" class="legend-label">More</text>')

    svg_lines.append('</svg>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 2. SVG GENERATOR 2: PLANETARY ORBIT SYSTEM ---
def generate_terminal_card_svg(username, ascii_lines, output_file="terminal-card.svg"):
    width = 440
    height = 440
    cx = 220
    cy = 230

    planets = [
        ("Python & AI", 75, "#00f0ff", 14, 0.4),    # Orbit 1
        ("TypeScript", 125, "#ff007f", 22, 0.7),    # Orbit 2
        ("React & Web", 165, "#a371f7", 32, 1.1),   # Orbit 3
    ]
    
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <filter id="sun-aura" x="-100%" y="-100%" width="300%" height="300%">',
        '      <feGaussianBlur stdDeviation="8" result="blur1" />',
        '      <feGaussianBlur stdDeviation="3" result="blur2" />',
        '      <feMerge><feMergeNode in="blur1" /><feMergeNode in="blur2" /><feMergeNode in="SourceGraphic" /></feMerge>',
        '    </filter>',
        '    <filter id="planet-glow" x="-50%" y="-50%" width="200%" height="200%">',
        '      <feGaussianBlur stdDeviation="3" result="blur" />',
        '      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>',
        '    </filter>',
        '    <linearGradient id="space-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#160829"/>',
        '      <stop offset="50%" stop-color="#070b18"/>',
        '      <stop offset="100%" stop-color="#030712"/>',
        '    </linearGradient>',
        '    <linearGradient id="orbit-border" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#00f0ff"/>',
        '      <stop offset="50%" stop-color="#ffb800"/>',
        '      <stop offset="100%" stop-color="#ff007f"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        '  <style>',
        '    .orbit-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; fill: #f0f6fc; font-weight: 700; letter-spacing: 1px; }',
        '    .orbit-sub { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; fill: #00f0ff; font-weight: 600; }',
        '    .planet-text { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9px; font-weight: bold; fill: #ffffff; }',
        '    .sun-text { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; font-weight: bold; fill: #030712; }',
        '  </style>',
        '',
        '  <!-- Window Outer Frame -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#space-bg)" stroke="url(#orbit-border)" stroke-width="1.5"/>',
        ''
    ]

    # Background Starfield
    random.seed(202)
    svg_lines.append('  <!-- Starfield -->')
    for s in range(25):
        sx = random.randint(15, width - 15)
        sy = random.randint(15, height - 15)
        sr = round(random.uniform(0.7, 1.6), 1)
        s_dur = round(random.uniform(1.2, 2.8), 1)
        svg_lines.append(
            f'  <circle cx="{sx}" cy="{sy}" r="{sr}" fill="#ffffff" opacity="0.3">\n'
            f'    <animate attributeName="opacity" values="0.1; 0.85; 0.1" dur="{s_dur}s" repeatCount="indefinite"/>\n'
            f'  </circle>'
        )

    # Card Title Header
    svg_lines.extend([
        '',
        '  <!-- Header -->',
        '  <g transform="translate(20, 26)">',
        f'    <text x="0" y="0" class="orbit-title">PLANETARY TECH ORBIT</text>',
        f'    <text x="{width-40}" y="0" class="orbit-sub" text-anchor="end">SYS://SOLAR_CORE</text>',
        '  </g>',
        '  <line x1="20" y1="36" x2="420" y2="36" stroke="#1f293d" stroke-width="1"/>',
        ''
    ])

    # Orbit Rings & Planets
    svg_lines.append('  <!-- Planetary Orbits & Revolving Satellites -->')
    
    for orbit_r, (p_name, r_dist, p_color, dur_sec, rot_offset) in enumerate(planets):
        svg_lines.append(
            f'  <!-- Orbit Ring {orbit_r + 1} -->\n'
            f'  <circle cx="{cx}" cy="{cy}" r="{r_dist}" fill="none" stroke="{p_color}" stroke-opacity="0.25" stroke-width="1.2" stroke-dasharray="4 4"/>'
        )
        
        # Revolving Group around Sun
        px = cx + r_dist
        py = cy
        start_deg = rot_offset * 360

        planet_html = (
            f'  <g transform="rotate({start_deg} {cx} {cy})">\n'
            f'    <g>\n'
            f'      <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="{dur_sec}s" repeatCount="indefinite"/>\n'
            f'      <!-- Planet Sphere -->\n'
            f'      <circle cx="{px}" cy="{py}" r="11" fill="{p_color}" filter="url(#planet-glow)"/>\n'
            f'      <!-- Planet Label Badge -->\n'
            f'      <rect x="{px + 14}" y="{py - 9}" width="{len(p_name)*7.2 + 8}" height="18" rx="4" fill="#0d1424" stroke="{p_color}" stroke-width="1" opacity="0.9"/>\n'
            f'      <text x="{px + 18}" y="{py + 3}" class="planet-text">{p_name}</text>\n'
            f'    </g>\n'
            f'  </g>'
        )
        svg_lines.append(planet_html)

    # Central Core Sun
    svg_lines.extend([
        '',
        '  <!-- Core Sun -->',
        f'  <circle cx="{cx}" cy="{cy}" r="32" fill="#ffb800" filter="url(#sun-aura)">',
        '    <animate attributeName="r" values="30; 34; 30" dur="3s" repeatCount="indefinite"/>',
        '  </circle>',
        f'  <circle cx="{cx}" cy="{cy}" r="28" fill="#ff9e3b"/>',
        f'  <text x="{cx}" y="{cy-3}" class="sun-text" text-anchor="middle">CORE</text>',
        f'  <text x="{cx}" y="{cy+10}" class="sun-text" text-anchor="middle" font-size="8px">{html.escape(username[:10])}</text>',
        ''
    ])

    # Footer Status Badge
    svg_lines.extend([
        '  <!-- Footer Telemetry -->',
        f'  <g transform="translate(20, {height - 25})">',
        '    <text x="0" y="0" class="orbit-sub">✦ ORBITAL VELOCITY: OPTIMAL</text>',
        f'    <text x="{width-40}" y="0" class="orbit-sub" text-anchor="end">STATUS: 100% OPERATIONAL</text>',
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 3. SVG GENERATOR 3: CONSTELLATION HUD & TELEMETRY RINGS ---
def generate_info_card_svg(username, output_file="info-card.svg"):
    width = 440
    height = 440

    info_rows = [
        ("PILOT", username, COLORS["star_gold"]),
        ("ROLE", "Full-Stack & Systems Architect", COLORS["cyan"]),
        ("STATION", "CyberOS Space Node 01", COLORS["green"]),
        ("TECH", "Python • TypeScript • React • AI", COLORS["pink"]),
        ("DEVOPS", "Docker • Kubernetes • AWS", COLORS["purple"]),
        ("STATUS", "EXPLORING THE FUTURE", COLORS["green"]),
    ]

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="info-space-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#160829"/>',
        '      <stop offset="50%" stop-color="#070b18"/>',
        '      <stop offset="100%" stop-color="#030712"/>',
        '    </linearGradient>',
        '    <linearGradient id="info-cosmic-border" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ff007f"/>',
        '      <stop offset="50%" stop-color="#ffb800"/>',
        '      <stop offset="100%" stop-color="#00f0ff"/>',
        '    </linearGradient>',
        '    <filter id="node-glow" x="-50%" y="-50%" width="200%" height="200%">',
        '      <feGaussianBlur stdDeviation="3" result="blur" />',
        '      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>',
        '    </filter>',
        '  </defs>',
        '',
        '  <style>',
        '    .hud-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; fill: #f0f6fc; font-weight: 700; letter-spacing: 1px; }',
        '    .section-lbl { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; font-weight: bold; fill: #8b949e; letter-spacing: 1px; }',
        '    .info-key { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; font-weight: bold; }',
        '    .info-val { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; fill: #c9d1d9; }',
        '    .ring-lbl { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9px; font-weight: bold; fill: #f0f6fc; }',
        '    .ring-pct { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; font-weight: bold; fill: #00f0ff; }',
        '  </style>',
        '',
        '  <!-- Window Outer Frame -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#info-space-bg)" stroke="url(#info-cosmic-border)" stroke-width="1.5"/>',
        ''
    ]

    # Starfield Background
    random.seed(303)
    svg_lines.append('  <!-- Starfield -->')
    for s in range(25):
        sx = random.randint(15, width - 15)
        sy = random.randint(15, height - 15)
        sr = round(random.uniform(0.7, 1.6), 1)
        s_dur = round(random.uniform(1.2, 2.8), 1)
        svg_lines.append(
            f'  <circle cx="{sx}" cy="{sy}" r="{sr}" fill="#ffffff" opacity="0.3">\n'
            f'    <animate attributeName="opacity" values="0.1; 0.85; 0.1" dur="{s_dur}s" repeatCount="indefinite"/>\n'
            f'  </circle>'
        )

    # Header Title
    svg_lines.extend([
        '',
        '  <!-- Header -->',
        '  <g transform="translate(20, 26)">',
        '    <text x="0" y="0" class="hud-title">CONSTELLATION TELEMETRY HUD</text>',
        f'    <text x="{width-40}" y="0" class="hud-title" text-anchor="end" fill="#ff007f">✦ NODE-X</text>',
        '  </g>',
        '  <line x1="20" y1="36" x2="420" y2="36" stroke="#1f293d" stroke-width="1"/>',
        '',
        '  <!-- SECTION 1: CONSTELLATION NODES -->',
        '  <g transform="translate(20, 55)">'
    ])

    y_spacing = 24
    for i, (key, val, color) in enumerate(info_rows):
        y_pos = i * y_spacing
        delay = round(0.12 + i * 0.05, 3)

        row_html = (
            f'    <g opacity="0">\n'
            f'      <!-- Glowing Node Point -->\n'
            f'      <circle cx="6" cy="{y_pos-3}" r="3.5" fill="{color}" filter="url(#node-glow)"/>\n'
            f'      <line x1="16" y1="{y_pos-3}" x2="35" y2="{y_pos-3}" stroke="{color}" stroke-opacity="0.5" stroke-width="1"/>\n'
            f'      <text x="42" y="{y_pos}" class="info-key" fill="{color}">{key.ljust(8)}:</text>\n'
            f'      <text x="125" y="{y_pos}" class="info-val">{html.escape(val)}</text>\n'
            f'      <animate attributeName="opacity" values="0; 1" dur="0.2s" begin="{delay}s" fill="freeze"/>\n'
            f'      <animateTransform attributeName="transform" type="translate" values="0 6; 0 0" dur="0.2s" begin="{delay}s" fill="freeze"/>\n'
            f'    </g>'
        )
        svg_lines.append(row_html)

    svg_lines.append('  </g>')

    # SECTION 2: CIRCULAR ACTIVITY TELEMETRY RINGS
    rings_y = 230
    cx_ring = 110
    cy_ring = 325

    svg_lines.extend([
        '',
        f'  <!-- SECTION 2: TELEMETRY CIRCULAR RINGS -->',
        f'  <g transform="translate(20, {rings_y})">',
        '    <text x="0" y="0" class="section-lbl">// SYSTEM ACTIVITY RINGS</text>',
        '  </g>',
        '',
        '  <!-- Concentric Circular Telemetry Rings -->',
        '  <g>',
        f'    <!-- Outer Ring: Velocity (95%) -->',
        f'    <circle cx="{cx_ring}" cy="{cy_ring}" r="65" fill="none" stroke="#1f293d" stroke-width="8"/>',
        f'    <circle cx="{cx_ring}" cy="{cy_ring}" r="65" fill="none" stroke="#00f0ff" stroke-width="8" stroke-dasharray="408" stroke-dashoffset="408" stroke-linecap="round" transform="rotate(-90 {cx_ring} {cy_ring})">',
        '      <animate attributeName="stroke-dashoffset" values="408; 20" dur="1.2s" begin="0.4s" fill="freeze"/>',
        '    </circle>',
        '',
        f'    <!-- Middle Ring: Uptime (99%) -->',
        f'    <circle cx="{cx_ring}" cy="{cy_ring}" r="48" fill="none" stroke="#1f293d" stroke-width="8"/>',
        f'    <circle cx="{cx_ring}" cy="{cy_ring}" r="48" fill="none" stroke="#ff007f" stroke-width="8" stroke-dasharray="301" stroke-dashoffset="301" stroke-linecap="round" transform="rotate(-90 {cx_ring} {cy_ring})">',
        '      <animate attributeName="stroke-dashoffset" values="301; 5" dur="1.2s" begin="0.55s" fill="freeze"/>',
        '    </circle>',
        '',
        f'    <!-- Inner Ring: AI Power (90%) -->',
        f'    <circle cx="{cx_ring}" cy="{cy_ring}" r="31" fill="none" stroke="#1f293d" stroke-width="8"/>',
        f'    <circle cx="{cx_ring}" cy="{cy_ring}" r="31" fill="none" stroke="#ffb800" stroke-width="8" stroke-dasharray="194" stroke-dashoffset="194" stroke-linecap="round" transform="rotate(-90 {cx_ring} {cy_ring})">',
        '      <animate attributeName="stroke-dashoffset" values="194; 20" dur="1.2s" begin="0.7s" fill="freeze"/>',
        '    </circle>',
        '  </g>',
        '',
        '  <!-- Ring Legend Entries -->',
        f'  <g transform="translate(200, {cy_ring - 40})">',
        '    <g>',
        '      <circle cx="8" cy="0" r="5" fill="#00f0ff"/>',
        '      <text x="20" y="4" class="ring-lbl">CODE VELOCITY</text>',
        '      <text x="180" y="4" class="ring-pct" text-anchor="end">95%</text>',
        '    </g>',
        '    <g transform="translate(0, 32)">',
        '      <circle cx="8" cy="0" r="5" fill="#ff007f"/>',
        '      <text x="20" y="4" class="ring-lbl">SYSTEM UPTIME</text>',
        '      <text x="180" y="4" class="ring-pct" fill="#ff007f" text-anchor="end">99.9%</text>',
        '    </g>',
        '    <g transform="translate(0, 64)">',
        '      <circle cx="8" cy="0" r="5" fill="#ffb800"/>',
        '      <text x="20" y="4" class="ring-lbl">AI ENGINEERING</text>',
        '      <text x="180" y="4" class="ring-pct" fill="#ffb800" text-anchor="end">92%</text>',
        '    </g>',
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 4. README GENERATOR ---
def generate_readme(username, readme_path="README.md"):
    content = f"""# <h1 align="center">✨ Hi there, I'm {username} 👋</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=23&pause=1000&color=00F0FF&center=true&vcenter=true&width=650&lines=Cosmic+Full-Stack+Architect+%26+AI+Engineer;Building+Next-Gen+Galactic+Applications;High-Performance+Code+%2B+Starlight+Graphics" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/github/followers/{username}?label=Followers&style=for-the-badge&color=00f0ff&logo=github" alt="GitHub Followers"/>
  </a>
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/github/stars/{username}?label=Total%20Stars&style=for-the-badge&color=ff007f&logo=star" alt="GitHub Stars"/>
  </a>
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/badge/Cosmic%20Status-Orbit%20Optimal-ffb800?style=for-the-badge&logo=rocket" alt="Status"/>
  </a>
</p>

<br />

<!-- Side-by-Side Cards: Planetary Orbit + Constellation Telemetry HUD -->
<div align="center">
  <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td width="50%" align="center" valign="top" style="padding-right: 8px;">
        <a href="https://github.com/{username}">
          <img src="./terminal-card.svg" alt="Planetary Tech Orbit" width="100%" />
        </a>
      </td>
      <td width="50%" align="center" valign="top" style="padding-left: 8px;">
        <a href="https://github.com/{username}">
          <img src="./info-card.svg" alt="Constellation Telemetry HUD" width="100%" />
        </a>
      </td>
    </tr>
  </table>
</div>

<br />

<!-- Centered Cosmic Contribution Matrix -->
<div align="center">
  <a href="https://github.com/{username}">
    <img src="./github-contribution-animation.svg" alt="Cosmic Contribution Matrix" width="100%" />
  </a>
</div>

<br />

---

<p align="center">
  ✨ <i>Powered by Cosmic Galaxy SVG Engine</i>
</p>
"""
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] Successfully updated '{readme_path}'")

# --- MAIN CLI EXECUTION ---
def main():
    parser = argparse.ArgumentParser(description="Generate Cosmic Galaxy & Planetary Orbit GitHub Profile README & SVGs")
    parser.add_argument("--username", type=str, default=DEFAULT_USERNAME, help="GitHub username")
    parser.add_argument("--outdir", type=str, default=".", help="Output directory")
    args = parser.parse_args()

    username = args.username
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    print(f"[+] Generating Cosmic Galaxy SVGs for user '{username}'...")

    ascii_lines = []

    contrib_path = os.path.join(outdir, "github-contribution-animation.svg")
    terminal_path = os.path.join(outdir, "terminal-card.svg")
    info_path = os.path.join(outdir, "info-card.svg")
    readme_path = os.path.join(outdir, "README.md")

    generate_contribution_svg(username, contrib_path)
    generate_terminal_card_svg(username, ascii_lines, terminal_path)
    generate_info_card_svg(username, info_path)
    generate_readme(username, readme_path)

    print("[🎉] All Cosmic Galaxy SVG cards generated successfully!")

if __name__ == "__main__":
    main()

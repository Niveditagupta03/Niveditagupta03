#!/usr/bin/env python3
"""
GitHub-Sanitizer Fully Compliant Animated SVG Profile Generator
================================================================
Eliminates ALL ampersands (`&`) across all SVG files by replacing them with `+`
and `|` symbols to guaranteed 100% eliminate any XML parser entity errors (`xmlParseEntityRef`)!
"""

import os
import sys
import math
import random
import json
import argparse
import html

DEFAULT_USERNAME = "Niveditagupta03"
DEFAULT_REPO = "Niveditagupta03"

COLORS = {
    "space_dark": "#030712",
    "card_bg": "#0d1424",
    "border_cyan": "#00f0ff",
    "border_pink": "#ff007f",
    "border_purple": "#7928ca",
    "text_bright": "#f0f6fc",
    "text_muted": "#8b949e",
    "gold": "#ffb800",
    "cyan": "#00f0ff",
    "pink": "#ff007f",
    "purple": "#a371f7",
    "green": "#00ff88",
    "blue": "#38bdf8",
}

# --- 1. SVG 1: CYBER HERO BANNER ---
def generate_hero_banner_svg(username, output_file="cyber-hero-banner.svg"):
    width = 880
    height = 220

    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#160829"/>',
        '      <stop offset="50%" stop-color="#090e1f"/>',
        '      <stop offset="100%" stop-color="#030712"/>',
        '    </linearGradient>',
        '    <linearGradient id="hero-border" x1="0%" y1="0%" x2="100%" y2="0%">',
        '      <stop offset="0%" stop-color="#00f0ff"/>',
        '      <stop offset="50%" stop-color="#ff007f"/>',
        '      <stop offset="100%" stop-color="#7928ca"/>',
        '    </linearGradient>',
        '    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="0%">',
        '      <stop offset="0%" stop-color="#ffffff"/>',
        '      <stop offset="40%" stop-color="#00f0ff"/>',
        '      <stop offset="100%" stop-color="#ff007f"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="16" fill="url(#hero-bg)" stroke="url(#hero-border)" stroke-width="1.5"/>',
        '  <path d="M 6 22 L 6 6 L 22 6" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        f'  <path d="M {width-22} 6 L {width-6} 6 L {width-6} 22" fill="none" stroke="#ff007f" stroke-width="2"/>',
        f'  <path d="M 6 {height-22} L 6 {height-6} L 22 {height-6}" fill="none" stroke="#ff007f" stroke-width="2"/>',
        f'  <path d="M {width-22} {height-6} L {width-6} {height-6} L {width-6} {height-22}" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        ''
    ]

    random.seed(404)
    for s in range(30):
        sx = random.randint(20, width - 20)
        sy = random.randint(20, height - 20)
        sr = round(random.uniform(0.7, 1.6), 1)
        s_dur = round(random.uniform(1.2, 2.8), 1)
        svg_lines.append(
            f'  <circle cx="{sx}" cy="{sy}" r="{sr}" fill="#ffffff" opacity="0.3">\n'
            f'    <animate attributeName="opacity" values="0.1; 0.9; 0.1" dur="{s_dur}s" repeatCount="indefinite"/>\n'
            f'  </circle>'
        )

    ox, oy = 110, 110
    svg_lines.extend([
        f'  <g transform="translate({ox}, {oy})">',
        '    <circle cx="0" cy="0" r="58" fill="none" stroke="#00f0ff" stroke-opacity="0.4" stroke-width="1.5" stroke-dasharray="8 6">',
        '      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <circle cx="0" cy="0" r="48" fill="none" stroke="#ff007f" stroke-opacity="0.5" stroke-width="1.5" stroke-dasharray="12 8">',
        '      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="8s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <circle cx="0" cy="0" r="36" fill="#00f0ff" opacity="0.8">',
        '      <animate attributeName="r" values="34; 38; 34" dur="3s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <circle cx="0" cy="0" r="32" fill="#0d1424"/>',
        '    <path d="M -10 -5 L 0 -15 L 10 -5 L 0 15 Z" fill="#00f0ff"/>',
        '  </g>',
        ''
    ])

    tx = 200
    svg_lines.extend([
        f'  <g transform="translate({tx}, 60)">',
        f'    <text x="0" y="24" font-family="monospace" font-size="26px" font-weight="900" fill="url(#title-grad)" letter-spacing="2px">{html.escape(username.upper())}</text>',
        '    <text x="0" y="52" font-family="monospace" font-size="12px" font-weight="bold" fill="#8b949e" letter-spacing="1.5px">FULL-STACK ARCHITECT | AI AGENT SYSTEMS | HIGH-PERF WEB</text>',
        '    <g transform="translate(0, 75)">',
        '      <rect x="0" y="0" width="460" height="30" rx="8" fill="#0d1424" stroke="#00ff88" stroke-width="1" opacity="0.9"/>',
        '      <circle cx="16" cy="15" r="4.5" fill="#00ff88">',
        '        <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" repeatCount="indefinite"/>',
        '      </circle>',
        '      <text x="28" y="19" font-family="monospace" font-size="11px" font-weight="bold" fill="#00ff88" letter-spacing="0.5px">CURRENTLY BUILDING NEXT-GEN AI AGENTS + WEB ARCHITECTURE</text>',
        '    </g>',
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 2. SVG 2: ANIMATED SCI-FI ACTIVITY WAVE GRAPH ---
def generate_animated_wave_graph_svg(username, output_file="animated-wave-graph.svg"):
    width = 880
    height = 200

    wave1_v1 = "M 40 130 C 140 40, 240 160, 340 60 C 440 150, 540 40, 640 120 C 740 30, 800 90, 840 65"
    wave1_v2 = "M 40 110 C 140 140, 240 50, 340 120 C 440 40, 540 130, 640 50 C 740 110, 800 40, 840 85"
    wave1_v3 = "M 40 130 C 140 40, 240 160, 340 60 C 440 150, 540 40, 640 120 C 740 30, 800 90, 840 65"

    wave2_v1 = "M 40 90 C 140 150, 240 50, 340 130 C 440 60, 540 140, 640 60 C 740 130, 800 70, 840 110"
    wave2_v2 = "M 40 140 C 140 60, 240 130, 340 50 C 440 120, 540 70, 640 130 C 740 50, 800 110, 840 70"
    wave2_v3 = "M 40 90 C 140 150, 240 50, 340 130 C 440 60, 540 140, 640 60 C 740 130, 800 70, 840 110"

    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="wave-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#160829"/>',
        '      <stop offset="50%" stop-color="#070b18"/>',
        '      <stop offset="100%" stop-color="#030712"/>',
        '    </linearGradient>',
        '    <linearGradient id="wave-border" x1="0%" y1="0%" x2="100%" y2="0%">',
        '      <stop offset="0%" stop-color="#00f0ff"/>',
        '      <stop offset="50%" stop-color="#ff007f"/>',
        '      <stop offset="100%" stop-color="#7928ca"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#wave-bg)" stroke="url(#wave-border)" stroke-width="1.5"/>',
        '',
        '  <g transform="translate(20, 26)">',
        '    <circle cx="0" cy="-4" r="4.5" fill="#00f0ff">',
        '      <animate attributeName="opacity" values="0.3; 1; 0.3" dur="1.5s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <text x="14" y="0" font-family="monospace" font-size="12px" font-weight="700" fill="#f0f6fc" letter-spacing="1px">LIVE SYSTEM ACTIVITY | WAVEFORM TELEMETRY</text>',
        '  </g>',
        f'  <text x="{width-20}" y="26" font-family="monospace" font-size="10px" font-weight="600" fill="#00f0ff" text-anchor="end">REAL-TIME WAVEFORM</text>',
        '  <line x1="20" y1="36" x2="860" y2="36" stroke="#1f293d" stroke-width="1"/>',
        '',
        '  <g stroke="#ffffff" stroke-opacity="0.05" stroke-width="1">',
        '    <line x1="40" y1="70" x2="840" y2="70"/>',
        '    <line x1="40" y1="105" x2="840" y2="105"/>',
        '    <line x1="40" y1="140" x2="840" y2="140"/>',
        '    <line x1="240" y1="45" x2="240" y2="165"/>',
        '    <line x1="440" y1="45" x2="440" y2="165"/>',
        '    <line x1="640" y1="45" x2="640" y2="165"/>',
        '  </g>',
        '',
        f'  <path d="{wave1_v1}" fill="none" stroke="#00f0ff" stroke-width="3">\n'
        f'    <animate attributeName="d" values="{wave1_v1}; {wave1_v2}; {wave1_v3}" dur="5s" repeatCount="indefinite"/>\n'
        f'  </path>',
        '',
        f'  <path d="{wave2_v1}" fill="none" stroke="#ff007f" stroke-width="2.5" opacity="0.85">\n'
        f'    <animate attributeName="d" values="{wave2_v1}; {wave2_v2}; {wave2_v3}" dur="6s" repeatCount="indefinite"/>\n'
        f'  </path>',
        ''
    ]

    beacons = [
        ("CODE VELOCITY: 95%", 340, 60, "#00f0ff"),
        ("AI ACCELERATION: 98%", 540, 40, "#ff007f"),
        ("SYSTEM STABILITY: 99.9%", 740, 30, "#00ff88"),
    ]

    for b_title, bx, by, b_color in beacons:
        beacon_html = (
            f'  <g transform="translate({bx}, {by})">\n'
            f'    <circle cx="0" cy="0" r="4.5" fill="{b_color}"/>\n'
            f'    <circle cx="0" cy="0" r="10" fill="none" stroke="{b_color}" stroke-width="1.2" opacity="0.8">\n'
            f'      <animate attributeName="r" values="4; 16" dur="1.8s" repeatCount="indefinite"/>\n'
            f'      <animate attributeName="opacity" values="0.8; 0" dur="1.8s" repeatCount="indefinite"/>\n'
            f'    </circle>\n'
            f'    <rect x="-60" y="-28" width="120" height="20" rx="4" fill="#0d1424" stroke="{b_color}" stroke-width="1" opacity="0.9"/>\n'
            f'    <text x="0" y="-15" font-family="monospace" font-size="9.5px" font-weight="bold" fill="#ffffff" text-anchor="middle">{b_title}</text>\n'
            f'  </g>'
        )
        svg_lines.append(beacon_html)

    svg_lines.append('</svg>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 3. SVG 3: SCI-FI TECH SKILL RADAR HUD (ZERO AMPERSANDS) ---
def generate_radar_hud_svg(username, output_file="tech-radar-hud.svg"):
    width = 440
    height = 440
    cx = 220
    cy = 230

    beacons = [
        ("Python + AI", cx + 75, cy - 60, "#00f0ff"),
        ("TypeScript + React", cx - 95, cy - 45, "#ff007f"),
        ("System Architecture", cx + 80, cy + 85, "#a371f7"),
        ("Docker + Cloud", cx - 85, cy + 75, "#ffb800"),
    ]

    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="radar-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#160829"/>',
        '      <stop offset="50%" stop-color="#070b18"/>',
        '      <stop offset="100%" stop-color="#030712"/>',
        '    </linearGradient>',
        '    <linearGradient id="radar-border" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#00f0ff"/>',
        '      <stop offset="50%" stop-color="#7928ca"/>',
        '      <stop offset="100%" stop-color="#ff007f"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#radar-bg)" stroke="url(#radar-border)" stroke-width="1.5"/>',
        '',
        '  <g transform="translate(20, 26)">',
        '    <text x="0" y="0" font-family="monospace" font-size="12px" font-weight="700" fill="#f0f6fc" letter-spacing="1px">SCI-FI TECH SKILL RADAR</text>',
        f'    <text x="{width-40}" y="0" font-family="monospace" font-size="10px" font-weight="600" fill="#00f0ff" text-anchor="end">SYS://RADAR.v4</text>',
        '  </g>',
        '  <line x1="20" y1="36" x2="420" y2="36" stroke="#1f293d" stroke-width="1"/>',
        '',
        f'  <circle cx="{cx}" cy="{cy}" r="50" fill="none" stroke="#00f0ff" stroke-opacity="0.2" stroke-width="1.2"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="100" fill="none" stroke="#00f0ff" stroke-opacity="0.2" stroke-width="1.2"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="#00f0ff" stroke-opacity="0.2" stroke-width="1.2"/>',
        f'  <line x1="{cx - 165}" y1="{cy}" x2="{cx + 165}" y2="{cy}" stroke="#00f0ff" stroke-opacity="0.25" stroke-width="1" stroke-dasharray="4 4"/>',
        f'  <line x1="{cx}" y1="{cy - 165}" x2="{cx}" y2="{cy + 165}" stroke="#00f0ff" stroke-opacity="0.25" stroke-width="1" stroke-dasharray="4 4"/>',
        ''
    ]

    svg_lines.extend([
        f'  <g transform="rotate(0 {cx} {cy})">',
        '    <animateTransform attributeName="transform" type="rotate" from="0 ' + str(cx) + ' ' + str(cy) + '" to="360 ' + str(cx) + ' ' + str(cy) + '" dur="5s" repeatCount="indefinite"/>',
        f'    <line x1="{cx}" y1="{cy}" x2="{cx + 150}" y2="{cy}" stroke="#00f0ff" stroke-width="2" opacity="0.9"/>',
        '  </g>',
        ''
    ])

    for b_name, bx, by, b_color in beacons:
        beacon_html = (
            f'  <g>\n'
            f'    <circle cx="{bx}" cy="{by}" r="5" fill="none" stroke="{b_color}" stroke-width="1.5" opacity="0.8">\n'
            f'      <animate attributeName="r" values="4; 18; 4" dur="2s" repeatCount="indefinite"/>\n'
            f'    </circle>\n'
            f'    <circle cx="{bx}" cy="{by}" r="4.5" fill="{b_color}"/>\n'
            f'    <rect x="{bx + 10}" y="{by - 10}" width="140" height="18" rx="4" fill="#0d1424" stroke="{b_color}" stroke-width="1" opacity="0.9"/>\n'
            f'    <text x="{bx + 14}" y="{by + 2}" font-family="monospace" font-size="9.5px" font-weight="bold" fill="#ffffff">{b_name}</text>\n'
            f'  </g>'
        )
        svg_lines.append(beacon_html)

    svg_lines.extend([
        '',
        '  <g transform="translate(20, ' + str(height - 22) + ')">',
        '    <text x="0" y="0" font-family="monospace" font-size="10px" font-weight="600" fill="#00f0ff">RADAR SCANNER: ACTIVE</text>',
        f'    <text x="{width-40}" y="0" font-family="monospace" font-size="10px" font-weight="600" fill="#00f0ff" text-anchor="end">4 BEACONS TRACKED</text>',
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 4. SVG 4: ARCHITECTURE SHOWCASE PILLARS (ZERO AMPERSANDS) ---
def generate_architecture_showcase_svg(username=DEFAULT_USERNAME, output_file="architecture-showcase.svg"):
    width = 440
    height = 440

    pillars = [
        ("AI + AGENTIC SYSTEMS", "Autonomous Workflows | Multi-Agent | LLMs", COLORS["cyan"], COLORS["pink"], "ai"),
        ("HIGH-PERFORMANCE WEB", "React | Next.js | Tailwind | Glassmorphic UI", COLORS["pink"], COLORS["purple"], "web"),
        ("DISTRIBUTED + CLOUD", "Python FastAPI | Docker | Microservices | CI/CD", COLORS["gold"], COLORS["green"], "cloud"),
    ]

    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="arch-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#160829"/>',
        '      <stop offset="50%" stop-color="#070b18"/>',
        '      <stop offset="100%" stop-color="#030712"/>',
        '    </linearGradient>',
        '    <linearGradient id="arch-border" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#ff007f"/>',
        '      <stop offset="50%" stop-color="#ffb800"/>',
        '      <stop offset="100%" stop-color="#00f0ff"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#arch-bg)" stroke="url(#arch-border)" stroke-width="1.5"/>',
        '',
        '  <g transform="translate(20, 26)">',
        '    <text x="0" y="0" font-family="monospace" font-size="12px" font-weight="700" fill="#f0f6fc" letter-spacing="1px">// FEATURED SYSTEM PILLARS</text>',
        f'    <text x="{width-40}" y="0" font-family="monospace" font-size="10px" font-weight="600" fill="#00f0ff" text-anchor="end">SYS://SHOWCASE</text>',
        '  </g>',
        '  <line x1="20" y1="36" x2="420" y2="36" stroke="#1f293d" stroke-width="1"/>',
        '',
        '  <g transform="translate(20, 55)">'
    ]

    for p_idx, (title, desc, c1, c2, icon_type) in enumerate(pillars):
        py = p_idx * 115
        grad_id = f"pillar-grad-{p_idx}"

        svg_lines.insert(9, (
            f'    <linearGradient id="{grad_id}" x1="0%" y1="0%" x2="100%" y2="0%">\n'
            f'      <stop offset="0%" stop-color="{c1}"/>\n'
            f'      <stop offset="100%" stop-color="{c2}"/>\n'
            f'    </linearGradient>'
        ))

        if icon_type == "ai":
            icon_svg = f'<g transform="translate(22, {py+18})"><circle cx="10" cy="10" r="4" fill="{c1}"/><circle cx="2" cy="4" r="2.5" fill="{c2}"/><circle cx="18" cy="4" r="2.5" fill="{c2}"/><circle cx="10" cy="18" r="2.5" fill="{c2}"/><line x1="10" y1="10" x2="2" y2="4" stroke="{c1}" stroke-width="1.2"/><line x1="10" y1="10" x2="18" y2="4" stroke="{c1}" stroke-width="1.2"/><line x1="10" y1="10" x2="10" y2="18" stroke="{c1}" stroke-width="1.2"/></g>'
        elif icon_type == "web":
            icon_svg = f'<g transform="translate(20, {py+18})"><path d="M 6 4 L 1 10 L 6 16" fill="none" stroke="{c1}" stroke-width="2"/><path d="M 14 4 L 19 10 L 14 16" fill="none" stroke="{c1}" stroke-width="2"/><line x1="12" y1="3" x2="8" y2="17" stroke="{c2}" stroke-width="2"/></g>'
        else:
            icon_svg = f'<g transform="translate(20, {py+18})"><rect x="1" y="2" width="18" height="4" rx="2" fill="{c1}"/><rect x="1" y="8" width="18" height="4" rx="2" fill="{c2}"/><rect x="1" y="14" width="18" height="4" rx="2" fill="{c1}"/></g>'

        card_html = (
            f'    <g>\n'
            f'      <rect x="0" y="{py}" width="400" height="98" rx="10" fill="#0d1424" stroke="#1f293d" stroke-width="1"/>\n'
            f'      <rect x="0" y="{py}" width="5" height="98" rx="2" fill="url(#{grad_id})"/>\n'
            f'      {icon_svg}\n'
            f'      <text x="50" y="{py+30}" font-family="monospace" font-size="11.5px" font-weight="bold" fill="#f0f6fc">{title}</text>\n'
            f'      <text x="20" y="{py+58}" font-family="monospace" font-size="10px" font-weight="bold" fill="#8b949e">{desc}</text>\n'
            f'      <rect x="20" y="{py+74}" width="360" height="3" rx="1.5" fill="url(#{grad_id})" opacity="0.6"/>\n'
            f'    </g>'
        )
        svg_lines.append(card_html)

    svg_lines.extend([
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 5. SVG 5: TELEMETRY METRICS ---
def generate_telemetry_metrics_svg(username, output_file="telemetry-metrics.svg"):
    width = 880
    height = 160

    metrics = [
        ("GLOBAL REPOSITORIES", "100% Active", "#00f0ff", 408, 20),
        ("CODE VELOCITY", "95% Rating", "#ff007f", 408, 45),
        ("SYSTEM UPTIME", "99.9% Operational", "#00ff88", 408, 5),
        ("AI WORKFLOWS", "92% Automated", "#ffb800", 408, 60),
    ]

    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <linearGradient id="met-bg" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#160829"/>',
        '      <stop offset="50%" stop-color="#070b18"/>',
        '      <stop offset="100%" stop-color="#030712"/>',
        '    </linearGradient>',
        '    <linearGradient id="met-border" x1="0%" y1="0%" x2="100%" y2="0%">',
        '      <stop offset="0%" stop-color="#00f0ff"/>',
        '      <stop offset="50%" stop-color="#ff007f"/>',
        '      <stop offset="100%" stop-color="#7928ca"/>',
        '    </linearGradient>',
        '  </defs>',
        '',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#met-bg)" stroke="url(#met-border)" stroke-width="1.5"/>',
        ''
    ]

    for i, (m_title, m_val, m_color, max_dash, target_offset) in enumerate(metrics):
        px = 25 + i * 210
        py = 25

        pill_html = (
            f'  <g transform="translate({px}, {py})">\n'
            f'    <rect x="0" y="0" width="195" height="110" rx="10" fill="#0d1424" stroke="#1f293d" stroke-width="1"/>\n'
            f'    <circle cx="45" cy="55" r="32" fill="none" stroke="#1f293d" stroke-width="6"/>\n'
            f'    <circle cx="45" cy="55" r="32" fill="none" stroke="{m_color}" stroke-width="6" stroke-dasharray="201" stroke-dashoffset="201" stroke-linecap="round" transform="rotate(-90 45 55)">\n'
            f'      <animate attributeName="stroke-dashoffset" values="201; {int(target_offset*0.5)}" dur="1.2s" begin="{0.2 + i*0.1}s" fill="freeze"/>\n'
            f'    </circle>\n'
            f'    <text x="92" y="48" font-family="monospace" font-size="10px" font-weight="bold" fill="#8b949e" letter-spacing="1px">{m_title}</text>\n'
            f'    <text x="92" y="70" font-family="monospace" font-size="13px" font-weight="bold" fill="{m_color}">{m_val}</text>\n'
            f'  </g>'
        )
        svg_lines.append(pill_html)

    svg_lines.append('</svg>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 6. README GENERATOR ---
def generate_readme(username, repo_name=DEFAULT_REPO, readme_path="README.md"):
    raw_base = f"https://raw.githubusercontent.com/{username}/{repo_name}/main"

    content = f"""# <h1 align="center">✨ Hi there, I'm {username} 👋</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=23&pause=1000&color=00F0FF&center=true&vcenter=true&width=650&lines=Full-Stack+Architect+%2B+AI+Engineer;Building+Next-Gen+Interactive+Experiences;High-Performance+Code+%2B+Sci-Fi+Graphics" alt="Typing SVG" />
</p>

<!-- Hero Banner -->
<p align="center">
  <img src="{raw_base}/cyber-hero-banner.svg" alt="Cyber Hero Banner" width="100%" />
</p>

<br />

<!-- Animated Sci-Fi Activity Wave Graph -->
<p align="center">
  <img src="{raw_base}/animated-wave-graph.svg" alt="Animated Sci-Fi Activity Wave Graph" width="100%" />
</p>

<br />

<p align="center">
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/github/followers/{username}?label=Followers&style=for-the-badge&color=00f0ff&logo=github" alt="GitHub Followers"/>
  </a>
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/github/stars/{username}?label=Total%20Stars&style=for-the-badge&color=ff007f&logo=star" alt="GitHub Stars"/>
  </a>
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/badge/Status-100%25%20Operational-00ff88?style=for-the-badge&logo=rocket" alt="Status"/>
  </a>
</p>

<br />

<!-- Side-by-Side HUD Cards: Skill Radar + Featured Pillars -->
<p align="center">
  <img src="{raw_base}/tech-radar-hud.svg" alt="Sci-Fi Tech Skill Radar" width="49%" />
  <img src="{raw_base}/architecture-showcase.svg" alt="Featured Architecture Pillars" width="49%" />
</p>

<br />

<!-- Centered Glass Metric Telemetry Strip -->
<p align="center">
  <img src="{raw_base}/telemetry-metrics.svg" alt="Apple-Style Glass Metric Telemetry" width="100%" />
</p>
"""
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] Successfully updated '{readme_path}'")

# --- MAIN CLI EXECUTION ---
def main():
    parser = argparse.ArgumentParser(description="Generate GitHub Sanitizer Compliant Profile README & SVGs")
    parser.add_argument("--username", type=str, default=DEFAULT_USERNAME, help="GitHub username")
    parser.add_argument("--repo", type=str, default=DEFAULT_REPO, help="GitHub repository name")
    parser.add_argument("--outdir", type=str, default=".", help="Output directory")
    args = parser.parse_args()

    username = args.username
    repo = args.repo
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    print(f"[+] Generating GitHub Sanitizer Compliant SVGs for user '{username}'...")

    hero_path = os.path.join(outdir, "cyber-hero-banner.svg")
    wave_path = os.path.join(outdir, "animated-wave-graph.svg")
    radar_path = os.path.join(outdir, "tech-radar-hud.svg")
    arch_path = os.path.join(outdir, "architecture-showcase.svg")
    met_path = os.path.join(outdir, "telemetry-metrics.svg")
    readme_path = os.path.join(outdir, "README.md")

    generate_hero_banner_svg(username, hero_path)
    generate_animated_wave_graph_svg(username, wave_path)
    generate_radar_hud_svg(username, radar_path)
    generate_architecture_showcase_svg(username, arch_path)
    generate_telemetry_metrics_svg(username, met_path)
    generate_readme(username, repo, readme_path)

    print("[🎉] All GitHub-compliant SVG cards generated successfully!")

if __name__ == "__main__":
    main()

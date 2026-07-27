#!/usr/bin/env python3
"""
Innovative Animated Wave Graph & Profile SVG Generator
======================================================
Generates four high-end, self-contained SMIL-animated SVG cards:
  1. cyber-hero-banner.svg (Cinematic Glass Hero Header with 3D Cyber Orb & Live Status)
  2. animated-wave-graph.svg (NEW: Sci-Fi Activity Wave Graph with morphing neon curves & peak metrics)
  3. tech-radar-hud.svg (Sci-Fi Radar HUD with 360° rotating beam & signal pings)
  4. telemetry-metrics.svg (Apple-Style Glass Metric Telemetry with animated progress arcs)

Updates README.md using raw GitHub CDN URLs to fix broken image loading on GitHub!
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

# --- 1. SVG GENERATOR 1: CYBER HERO BANNER ---
def generate_hero_banner_svg(username, output_file="cyber-hero-banner.svg"):
    width = 880
    height = 220

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <filter id="orb-glow" x="-100%" y="-100%" width="300%" height="300%">',
        '      <feGaussianBlur stdDeviation="8" result="blur1"/>',
        '      <feGaussianBlur stdDeviation="3" result="blur2"/>',
        '      <feMerge><feMergeNode in="blur1"/><feMergeNode in="blur2"/><feMergeNode in="SourceGraphic"/></feMerge>',
        '    </filter>',
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
        '  <style>',
        '    .hero-name { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 26px; font-weight: 900; letter-spacing: 2px; }',
        '    .hero-tag { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; font-weight: 700; fill: #8b949e; letter-spacing: 1.5px; }',
        '    .status-txt { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11px; font-weight: bold; fill: #00ff88; letter-spacing: 0.5px; }',
        '  </style>',
        '',
        '  <!-- Background Canvas -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="16" fill="url(#hero-bg)" stroke="url(#hero-border)" stroke-width="1.5"/>',
        '',
        '  <!-- Cyber Corner HUD Accents -->',
        '  <path d="M 6 22 L 6 6 L 22 6" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        f'  <path d="M {width-22} 6 L {width-6} 6 L {width-6} 22" fill="none" stroke="#ff007f" stroke-width="2"/>',
        f'  <path d="M 6 {height-22} L 6 {height-6} L 22 {height-6}" fill="none" stroke="#ff007f" stroke-width="2"/>',
        f'  <path d="M {width-22} {height-6} L {width-6} {height-6} L {width-6} {height-22}" fill="none" stroke="#00f0ff" stroke-width="2"/>',
        ''
    ]

    random.seed(404)
    for s in range(35):
        sx = random.randint(20, width - 20)
        sy = random.randint(20, height - 20)
        sr = round(random.uniform(0.7, 1.6), 1)
        s_dur = round(random.uniform(1.2, 2.8), 1)
        svg_lines.append(
            f'  <circle cx="{sx}" cy="{sy}" r="{sr}" fill="#ffffff" opacity="0.3">\n'
            f'    <animate attributeName="opacity" values="0.1; 0.9; 0.1" dur="{s_dur}s" repeatCount="indefinite"/>\n'
            f'  </circle>'
        )

    ox = 110
    oy = 110
    svg_lines.extend([
        '',
        '  <!-- 3D Holographic Cyber Orb -->',
        f'  <g transform="translate({ox}, {oy})">',
        '    <circle cx="0" cy="0" r="58" fill="none" stroke="#00f0ff" stroke-opacity="0.4" stroke-width="1.5" stroke-dasharray="8 6">',
        '      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <circle cx="0" cy="0" r="48" fill="none" stroke="#ff007f" stroke-opacity="0.5" stroke-width="1.5" stroke-dasharray="12 8">',
        '      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="8s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <circle cx="0" cy="0" r="36" fill="#00f0ff" filter="url(#orb-glow)">',
        '      <animate attributeName="r" values="34; 38; 34" dur="3s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <circle cx="0" cy="0" r="32" fill="#0d1424"/>',
        '    <text x="0" y="7" font-family="monospace" font-size="22px" font-weight="bold" fill="#00f0ff" text-anchor="middle">⚡</text>',
        '  </g>',
        ''
    ])

    tx = 200
    svg_lines.extend([
        '  <!-- Main Hero Content -->',
        f'  <g transform="translate({tx}, 60)">',
        f'    <text x="0" y="24" class="hero-name" fill="url(#title-grad)">{html.escape(username.upper())}</text>',
        '    <text x="0" y="52" class="hero-tag">FULL-STACK ARCHITECT • AI AGENT SYSTEMS • HIGH-PERF WEB</text>',
        '    <g transform="translate(0, 75)">',
        '      <rect x="0" y="0" width="460" height="30" rx="8" fill="#0d1424" stroke="#00ff88" stroke-width="1" opacity="0.9"/>',
        '      <circle cx="16" cy="15" r="4.5" fill="#00ff88">',
        '        <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" repeatCount="indefinite"/>',
        '      </circle>',
        '      <text x="28" y="19" class="status-txt">CURRENTLY BUILDING NEXT-GEN AI AGENTS &amp; WEB ARCHITECTURE</text>',
        '    </g>',
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 2. SVG GENERATOR 2: NEW ANIMATED SCI-FI ACTIVITY WAVE GRAPH ---
def generate_animated_wave_graph_svg(username, output_file="animated-wave-graph.svg"):
    width = 880
    height = 200

    # Path morphing data for dual waves
    wave1_v1 = "M 40 130 C 140 40, 240 160, 340 60 C 440 150, 540 40, 640 120 C 740 30, 800 90, 840 65"
    wave1_v2 = "M 40 110 C 140 140, 240 50, 340 120 C 440 40, 540 130, 640 50 C 740 110, 800 40, 840 85"
    wave1_v3 = "M 40 130 C 140 40, 240 160, 340 60 C 440 150, 540 40, 640 120 C 740 30, 800 90, 840 65"

    wave2_v1 = "M 40 90 C 140 150, 240 50, 340 130 C 440 60, 540 140, 640 60 C 740 130, 800 70, 840 110"
    wave2_v2 = "M 40 140 C 140 60, 240 130, 340 50 C 440 120, 540 70, 640 130 C 740 50, 800 110, 840 70"
    wave2_v3 = "M 40 90 C 140 150, 240 50, 340 130 C 440 60, 540 140, 640 60 C 740 130, 800 70, 840 110"

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <filter id="wave-cyan-glow" x="-50%" y="-50%" width="200%" height="200%">',
        '      <feGaussianBlur stdDeviation="3.5" result="blur"/>',
        '      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>',
        '    </filter>',
        '    <filter id="wave-pink-glow" x="-50%" y="-50%" width="200%" height="200%">',
        '      <feGaussianBlur stdDeviation="3.5" result="blur"/>',
        '      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>',
        '    </filter>',
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
        '  <style>',
        '    .wave-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; font-weight: 700; fill: #f0f6fc; letter-spacing: 1px; }',
        '    .wave-sub { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; font-weight: 600; fill: #00f0ff; }',
        '    .beacon-lbl { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9.5px; font-weight: bold; fill: #ffffff; }',
        '  </style>',
        '',
        '  <!-- Background Canvas -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#wave-bg)" stroke="url(#wave-border)" stroke-width="1.5"/>',
        '',
        '  <!-- Header Telemetry Title -->',
        '  <g transform="translate(20, 26)">',
        '    <circle cx="0" cy="-4" r="4.5" fill="#00f0ff">',
        '      <animate attributeName="opacity" values="0.3; 1; 0.3" dur="1.5s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <text x="14" y="0" class="wave-title">LIVE SYSTEM ACTIVITY &amp; WAVEFORM TELEMETRY</text>',
        '  </g>',
        f'  <text x="{width-20}" y="26" class="wave-sub" text-anchor="end">✦ REAL-TIME WAVEFORM</text>',
        '  <line x1="20" y1="36" x2="860" y2="36" stroke="#1f293d" stroke-width="1"/>',
        '',
        '  <!-- Background Telemetry Grid Lines -->',
        '  <g stroke="#ffffff" stroke-opacity="0.05" stroke-width="1">',
        '    <line x1="40" y1="70" x2="840" y2="70"/>',
        '    <line x1="40" y1="105" x2="840" y2="105"/>',
        '    <line x1="40" y1="140" x2="840" y2="140"/>',
        '    <line x1="240" y1="45" x2="240" y2="165"/>',
        '    <line x1="440" y1="45" x2="440" y2="165"/>',
        '    <line x1="640" y1="45" x2="640" y2="165"/>',
        '  </g>',
        '',
        '  <!-- Continuous Morphing Neon Wave 1 (Cyan) -->',
        f'  <path d="{wave1_v1}" fill="none" stroke="#00f0ff" stroke-width="3" filter="url(#wave-cyan-glow)">\n'
        f'    <animate attributeName="d" values="{wave1_v1}; {wave1_v2}; {wave1_v3}" dur="5s" repeatCount="indefinite"/>\n'
        f'  </path>',
        '',
        '  <!-- Continuous Morphing Neon Wave 2 (Pink) -->',
        f'  <path d="{wave2_v1}" fill="none" stroke="#ff007f" stroke-width="2.5" opacity="0.85" filter="url(#wave-pink-glow)">\n'
        f'    <animate attributeName="d" values="{wave2_v1}; {wave2_v2}; {wave2_v3}" dur="6s" repeatCount="indefinite"/>\n'
        f'  </path>',
        ''
    ]

    # Peak Metric Beacons along the wave
    beacons = [
        ("CODE VELOCITY: 95%", 340, 60, "#00f0ff"),
        ("AI ACCELERATION: 98%", 540, 40, "#ff007f"),
        ("SYSTEM STABILITY: 99.9%", 740, 30, "#00ff88"),
    ]

    for b_title, bx, by, b_color in beacons:
        beacon_html = (
            f'  <!-- Peak Metric Beacon -->\n'
            f'  <g transform="translate({bx}, {by})">\n'
            f'    <circle cx="0" cy="0" r="4.5" fill="{b_color}"/>\n'
            f'    <circle cx="0" cy="0" r="10" fill="none" stroke="{b_color}" stroke-width="1.2" opacity="0.8">\n'
            f'      <animate attributeName="r" values="4; 16" dur="1.8s" repeatCount="indefinite"/>\n'
            f'      <animate attributeName="opacity" values="0.8; 0" dur="1.8s" repeatCount="indefinite"/>\n'
            f'    </circle>\n'
            f'    <rect x="-60" y="-28" width="120" height="20" rx="4" fill="#0d1424" stroke="{b_color}" stroke-width="1" opacity="0.9"/>\n'
            f'    <text x="0" y="-15" class="beacon-lbl" text-anchor="middle">{b_title}</text>\n'
            f'  </g>'
        )
        svg_lines.append(beacon_html)

    svg_lines.append('</svg>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 3. SVG GENERATOR 3: SCI-FI TECH SKILL RADAR HUD ---
def generate_radar_hud_svg(username, output_file="tech-radar-hud.svg"):
    width = 440
    height = 440
    cx = 220
    cy = 230

    beacons = [
        ("Python & AI", cx + 75, cy - 60, "#00f0ff"),
        ("TypeScript & React", cx - 95, cy - 45, "#ff007f"),
        ("System Architecture", cx + 80, cy + 85, "#a371f7"),
        ("Docker & Cloud", cx - 85, cy + 75, "#ffb800"),
    ]

    svg_lines = [
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
        '    <linearGradient id="beam-sweep-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.4"/>',
        '      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>',
        '    </linearGradient>',
        '    <filter id="ping-glow" x="-50%" y="-50%" width="200%" height="200%">',
        '      <feGaussianBlur stdDeviation="3" result="blur" />',
        '      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>',
        '    </filter>',
        '  </defs>',
        '',
        '  <style>',
        '    .hud-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; fill: #f0f6fc; font-weight: 700; letter-spacing: 1px; }',
        '    .hud-sub { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; fill: #00f0ff; font-weight: 600; }',
        '    .beacon-txt { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 9.5px; font-weight: bold; fill: #ffffff; }',
        '  </style>',
        '',
        '  <!-- Window Outer Frame -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#radar-bg)" stroke="url(#radar-border)" stroke-width="1.5"/>',
        '',
        '  <!-- Header -->',
        '  <g transform="translate(20, 26)">',
        '    <text x="0" y="0" class="hud-title">SCI-FI TECH SKILL RADAR</text>',
        f'    <text x="{width-40}" y="0" class="hud-sub" text-anchor="end">SYS://RADAR.v4</text>',
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
        '  <!-- 360 Degree Rotating Radar Beam -->',
        f'  <g transform="rotate(0 {cx} {cy})">',
        '    <animateTransform attributeName="transform" type="rotate" from="0 ' + str(cx) + ' ' + str(cy) + '" to="360 ' + str(cx) + ' ' + str(cy) + '" dur="5s" repeatCount="indefinite"/>',
        f'    <path d="M {cx} {cy} L {cx+150} {cy-40} A 150 150 0 0 0 {cx+150} {cy+40} Z" fill="url(#beam-sweep-grad)"/>',
        f'    <line x1="{cx}" y1="{cy}" x2="{cx + 150}" y2="{cy}" stroke="#00f0ff" stroke-width="2" opacity="0.9"/>',
        '  </g>',
        ''
    ])

    for b_name, bx, by, b_color in beacons:
        beacon_html = (
            f'  <g>\n'
            f'    <circle cx="{bx}" cy="{by}" r="5" fill="none" stroke="{b_color}" stroke-width="1.5" opacity="0.8">\n'
            f'      <animate attributeName="r" values="4; 18; 4" dur="2s" repeatCount="indefinite"/>\n'
            f'      <animate attributeName="opacity" values="0.8; 0; 0.8" dur="2s" repeatCount="indefinite"/>\n'
            f'    </circle>\n'
            f'    <circle cx="{bx}" cy="{by}" r="4.5" fill="{b_color}" filter="url(#ping-glow)"/>\n'
            f'    <rect x="{bx + 10}" y="{by - 10}" width="{len(b_name)*7.2 + 8}" height="18" rx="4" fill="#0d1424" stroke="{b_color}" stroke-width="1" opacity="0.9"/>\n'
            f'    <text x="{bx + 14}" y="{by + 2}" class="beacon-txt">{b_name}</text>\n'
            f'  </g>'
        )
        svg_lines.append(beacon_html)

    svg_lines.extend([
        '',
        '  <g transform="translate(20, ' + str(height - 22) + ')">',
        '    <text x="0" y="0" class="hud-sub">✦ RADAR SCANNER: ACTIVE</text>',
        f'    <text x="{width-40}" y="0" class="hud-sub" text-anchor="end">4 BEACONS TRACKED</text>',
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 4. SVG GENERATOR 4: TELEMETRY METRICS ---
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
        '  <style>',
        '    .met-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; font-weight: bold; fill: #8b949e; letter-spacing: 1px; }',
        '    .met-val { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 13px; font-weight: bold; fill: #f0f6fc; }',
        '  </style>',
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
            f'    <text x="92" y="48" class="met-title">{m_title}</text>\n'
            f'    <text x="92" y="70" class="met-val" fill="{m_color}">{m_val}</text>\n'
            f'  </g>'
        )
        svg_lines.append(pill_html)

    svg_lines.append('</svg>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 5. README GENERATOR (RAW GITHUB URLS) ---
def generate_readme(username, repo_name=DEFAULT_REPO, readme_path="README.md"):
    raw_base = f"https://raw.githubusercontent.com/{username}/{repo_name}/main"

    content = f"""# <h1 align="center">✨ Hi there, I'm {username} 👋</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=23&pause=1000&color=00F0FF&center=true&vcenter=true&width=650&lines=Full-Stack+Architect+%26+AI+Engineer;Building+Next-Gen+Interactive+Experiences;High-Performance+Code+%2B+Sci-Fi+Graphics" alt="Typing SVG" />
</p>

<!-- Hero Banner -->
<div align="center">
  <a href="https://github.com/{username}">
    <img src="{raw_base}/cyber-hero-banner.svg" alt="Cyber Hero Banner" width="100%" />
  </a>
</div>

<br />

<!-- Animated Sci-Fi Activity Wave Graph -->
<div align="center">
  <a href="https://github.com/{username}">
    <img src="{raw_base}/animated-wave-graph.svg" alt="Animated Sci-Fi Activity Wave Graph" width="100%" />
  </a>
</div>

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
<div align="center">
  <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td width="50%" align="center" valign="top" style="padding-right: 8px;">
        <a href="https://github.com/{username}">
          <img src="{raw_base}/tech-radar-hud.svg" alt="Sci-Fi Tech Skill Radar" width="100%" />
        </a>
      </td>
      <td width="50%" align="center" valign="top" style="padding-left: 8px;">
        <a href="https://github.com/{username}">
          <img src="{raw_base}/architecture-showcase.svg" alt="Featured Architecture Pillars" width="100%" />
        </a>
      </td>
    </tr>
  </table>
</div>

<br />

<!-- Centered Glass Metric Telemetry Strip -->
<div align="center">
  <a href="https://github.com/{username}">
    <img src="{raw_base}/telemetry-metrics.svg" alt="Apple-Style Glass Metric Telemetry" width="100%" />
  </a>
</div>

<br />

---

<p align="center">
  ⚡ <i>Powered by Sci-Fi Wave Engine</i>
</p>
"""
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] Successfully updated '{readme_path}'")

# --- MAIN CLI EXECUTION ---
def main():
    parser = argparse.ArgumentParser(description="Generate Fresh Innovative Profile README & Animated Wave SVGs")
    parser.add_argument("--username", type=str, default=DEFAULT_USERNAME, help="GitHub username")
    parser.add_argument("--repo", type=str, default=DEFAULT_REPO, help="GitHub repository name")
    parser.add_argument("--outdir", type=str, default=".", help="Output directory")
    args = parser.parse_args()

    username = args.username
    repo = args.repo
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    print(f"[+] Generating Fresh Innovative SVGs for user '{username}' (repo: '{repo}')...")

    hero_path = os.path.join(outdir, "cyber-hero-banner.svg")
    wave_path = os.path.join(outdir, "animated-wave-graph.svg")
    radar_path = os.path.join(outdir, "tech-radar-hud.svg")
    arch_path = os.path.join(outdir, "architecture-showcase.svg")
    met_path = os.path.join(outdir, "telemetry-metrics.svg")
    readme_path = os.path.join(outdir, "README.md")

    generate_hero_banner_svg(username, hero_path)
    generate_animated_wave_graph_svg(username, wave_path)
    generate_radar_hud_svg(username, radar_path)
    generate_architecture_showcase_svg(output_file=arch_path)
    generate_telemetry_metrics_svg(username, met_path)
    generate_readme(username, repo, readme_path)

    print("[🎉] All fresh innovative SVG cards and README generated successfully!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Fresh Innovative GitHub Profile SVG Generator (No Matrix / No Terminal)
======================================================================
Generates four high-end, self-contained SMIL-animated SVG cards:
  1. cyber-hero-banner.svg (Cinematic Glass Hero Header with 3D Cyber Orb & Live Status)
  2. tech-radar-hud.svg (Sci-Fi Radar HUD with 360° rotating beam & signal pings)
  3. architecture-showcase.svg (Glassmorphic Feature Cards for AI, Web & Cloud)
  4. telemetry-metrics.svg (Apple-Style Glass Metric Telemetry with animated progress arcs)

Also updates README.md with side-by-side card layout & telemetry footer.
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
        '    .stat-badge { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; font-weight: bold; fill: #00f0ff; }',
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

    # Starfield
    random.seed(404)
    svg_lines.append('  <!-- Starfield -->')
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

    # 3D Holographic Cyber Orb (Left side)
    ox = 110
    oy = 110
    svg_lines.extend([
        '',
        '  <!-- 3D Holographic Cyber Orb -->',
        f'  <g transform="translate({ox}, {oy})">',
        '    <!-- Outer Rotating Aura Ring 1 -->',
        '    <circle cx="0" cy="0" r="58" fill="none" stroke="#00f0ff" stroke-opacity="0.4" stroke-width="1.5" stroke-dasharray="8 6">',
        '      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <!-- Outer Rotating Aura Ring 2 -->',
        '    <circle cx="0" cy="0" r="48" fill="none" stroke="#ff007f" stroke-opacity="0.5" stroke-width="1.5" stroke-dasharray="12 8">',
        '      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="8s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <!-- Core Glowing Orb -->',
        '    <circle cx="0" cy="0" r="36" fill="#00f0ff" filter="url(#orb-glow)">',
        '      <animate attributeName="r" values="34; 38; 34" dur="3s" repeatCount="indefinite"/>',
        '    </circle>',
        '    <circle cx="0" cy="0" r="32" fill="#0d1424"/>',
        '    <!-- Center Hologram Icon -->',
        '    <text x="0" y="7" font-family="monospace" font-size="22px" font-weight="bold" fill="#00f0ff" text-anchor="middle">⚡</text>',
        '  </g>',
        ''
    ])

    # Right Content Details
    tx = 200
    svg_lines.extend([
        '  <!-- Main Hero Content -->',
        f'  <g transform="translate({tx}, 60)">',
        '    <!-- Name Title -->',
        f'    <text x="0" y="24" class="hero-name" fill="url(#title-grad)">{html.escape(username.upper())}</text>',
        '    <!-- Subtitle Tagline -->',
        '    <text x="0" y="52" class="hero-tag">FULL-STACK ARCHITECT • AI AGENT SYSTEMS • HIGH-PERF WEB</text>',
        '    ',
        '    <!-- Live Status Pill -->',
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

# --- 2. SVG GENERATOR 2: SCI-FI TECH SKILL RADAR HUD ---
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
        '  <!-- Concentric Radar Grid Rings -->',
        f'  <circle cx="{cx}" cy="{cy}" r="50" fill="none" stroke="#00f0ff" stroke-opacity="0.2" stroke-width="1.2"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="100" fill="none" stroke="#00f0ff" stroke-opacity="0.2" stroke-width="1.2"/>',
        f'  <circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="#00f0ff" stroke-opacity="0.2" stroke-width="1.2"/>',
        f'  <!-- Axis Crosshairs -->',
        f'  <line x1="{cx - 165}" y1="{cy}" x2="{cx + 165}" y2="{cy}" stroke="#00f0ff" stroke-opacity="0.25" stroke-width="1" stroke-dasharray="4 4"/>',
        f'  <line x1="{cx}" y1="{cy - 165}" x2="{cx}" y2="{cy + 165}" stroke="#00f0ff" stroke-opacity="0.25" stroke-width="1" stroke-dasharray="4 4"/>',
        ''
    ]

    # Rotating 360 Degree Radar Sweep Beam
    svg_lines.extend([
        '  <!-- 360 Degree Rotating Radar Beam -->',
        f'  <g transform="rotate(0 {cx} {cy})">',
        '    <animateTransform attributeName="transform" type="rotate" from="0 ' + str(cx) + ' ' + str(cy) + '" to="360 ' + str(cx) + ' ' + str(cy) + '" dur="5s" repeatCount="indefinite"/>',
        f'    <path d="M {cx} {cy} L {cx+150} {cy-40} A 150 150 0 0 0 {cx+150} {cy+40} Z" fill="url(#beam-sweep-grad)"/>',
        f'    <line x1="{cx}" y1="{cy}" x2="{cx + 150}" y2="{cy}" stroke="#00f0ff" stroke-width="2" opacity="0.9"/>',
        '  </g>',
        ''
    ])

    # Signal Ping Beacons
    svg_lines.append('  <!-- Signal Beacons on Radar -->')
    for b_name, bx, by, b_color in beacons:
        beacon_html = (
            f'  <g>\n'
            f'    <!-- Pulsing Aura Ping -->\n'
            f'    <circle cx="{bx}" cy="{by}" r="5" fill="none" stroke="{b_color}" stroke-width="1.5" opacity="0.8">\n'
            f'      <animate attributeName="r" values="4; 18; 4" dur="2s" repeatCount="indefinite"/>\n'
            f'      <animate attributeName="opacity" values="0.8; 0; 0.8" dur="2s" repeatCount="indefinite"/>\n'
            f'    </circle>\n'
            f'    <!-- Center Beacon Point -->\n'
            f'    <circle cx="{bx}" cy="{by}" r="4.5" fill="{b_color}" filter="url(#ping-glow)"/>\n'
            f'    <!-- Label Card -->\n'
            f'    <rect x="{bx + 10}" y="{by - 10}" width="{len(b_name)*7.2 + 8}" height="18" rx="4" fill="#0d1424" stroke="{b_color}" stroke-width="1" opacity="0.9"/>\n'
            f'    <text x="{bx + 14}" y="{by + 2}" class="beacon-txt">{b_name}</text>\n'
            f'  </g>'
        )
        svg_lines.append(beacon_html)

    # Footer
    svg_lines.extend([
        '',
        '  <!-- Footer Status -->',
        f'  <g transform="translate(20, {height - 22})">',
        '    <text x="0" y="0" class="hud-sub">✦ RADAR SCANNER: ACTIVE</text>',
        f'    <text x="{width-40}" y="0" class="hud-sub" text-anchor="end">4 BEACONS TRACKED</text>',
        '  </g>',
        '</svg>'
    ])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 3. SVG GENERATOR 3: ARCHITECTURE SHOWCASE PILLARS ---
def generate_architecture_showcase_svg(username, output_file="architecture-showcase.svg"):
    width = 440
    height = 440

    pillars = [
        ("🤖 AI & AGENTIC SYSTEMS", "Autonomous Workflows • Multi-Agent • LLMs", COLORS["cyan"], COLORS["pink"]),
        ("⚡ HIGH-PERFORMANCE WEB", "React • Next.js • Tailwind • Glassmorphic UI", COLORS["pink"], COLORS["purple"]),
        ("☁️ DISTRIBUTED & CLOUD", "Python FastAPI • Docker • Microservices • CI/CD", COLORS["gold"], COLORS["green"]),
    ]

    svg_lines = [
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
        '  <style>',
        '    .hud-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 12px; fill: #f0f6fc; font-weight: 700; letter-spacing: 1px; }',
        '    .hud-sub { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; fill: #00f0ff; font-weight: 600; }',
        '    .card-title { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11.5px; font-weight: bold; fill: #f0f6fc; }',
        '    .card-desc { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10px; fill: #8b949e; }',
        '  </style>',
        '',
        '  <!-- Window Outer Frame -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#arch-bg)" stroke="url(#arch-border)" stroke-width="1.5"/>',
        '',
        '  <!-- Header -->',
        '  <g transform="translate(20, 26)">',
        '    <text x="0" y="0" class="hud-title">// FEATURED SYSTEM PILLARS</text>',
        f'    <text x="{width-40}" y="0" class="hud-sub" text-anchor="end">SYS://SHOWCASE</text>',
        '  </g>',
        '  <line x1="20" y1="36" x2="420" y2="36" stroke="#1f293d" stroke-width="1"/>',
        '',
        '  <!-- 3 Glassmorphic Feature Cards -->',
        '  <g transform="translate(20, 55)">'
    ]

    for p_idx, (title, desc, c1, c2) in enumerate(pillars):
        py = p_idx * 115
        delay = round(0.15 + p_idx * 0.1, 3)
        grad_id = f"pillar-grad-{p_idx}"

        svg_lines.insert(8, (
            f'    <linearGradient id="{grad_id}" x1="0%" y1="0%" x2="100%" y2="0%">\n'
            f'      <stop offset="0%" stop-color="{c1}"/>\n'
            f'      <stop offset="100%" stop-color="{c2}"/>\n'
            f'    </linearGradient>'
        ))

        card_html = (
            f'    <g opacity="0">\n'
            f'      <!-- Card Background -->\n'
            f'      <rect x="0" y="{py}" width="400" height="98" rx="10" fill="#0d1424" stroke="#1f293d" stroke-width="1"/>\n'
            f'      <!-- Accent Side Bar -->\n'
            f'      <rect x="0" y="{py}" width="5" height="98" rx="2" fill="url(#{grad_id})"/>\n'
            f'      <!-- Content -->\n'
            f'      <text x="20" y="{py+30}" class="card-title">{title}</text>\n'
            f'      <text x="20" y="{py+58}" class="card-desc">{desc}</text>\n'
            f'      <!-- Bottom Accent Glow Bar -->\n'
            f'      <rect x="20" y="{py+74}" width="360" height="3" rx="1.5" fill="url(#{grad_id})" opacity="0.6"/>\n'
            f'      <animate attributeName="opacity" values="0; 1" dur="0.25s" begin="{delay}s" fill="freeze"/>\n'
            f'      <animateTransform attributeName="transform" type="translate" values="0 10; 0 0" dur="0.25s" begin="{delay}s" fill="freeze"/>\n'
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

# --- 4. SVG GENERATOR 4: APPLE-STYLE TELEMETRY METRICS ---
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
        '  <!-- Background Strip -->',
        f'  <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="14" fill="url(#met-bg)" stroke="url(#met-border)" stroke-width="1.5"/>',
        ''
    ]

    pill_w = 200
    for i, (m_title, m_val, m_color, max_dash, target_offset) in enumerate(metrics):
        px = 25 + i * 210
        py = 25
        cx_ring = px + 40
        cy_ring = py + 55

        pill_html = (
            f'  <!-- Metric Pill {i+1} -->\n'
            f'  <g transform="translate({px}, {py})">\n'
            f'    <rect x="0" y="0" width="195" height="110" rx="10" fill="#0d1424" stroke="#1f293d" stroke-width="1"/>\n'
            f'    <!-- Circular Progress Arc -->\n'
            f'    <circle cx="45" cy="55" r="32" fill="none" stroke="#1f293d" stroke-width="6"/>\n'
            f'    <circle cx="45" cy="55" r="32" fill="none" stroke="{m_color}" stroke-width="6" stroke-dasharray="201" stroke-dashoffset="201" stroke-linecap="round" transform="rotate(-90 45 55)">\n'
            f'      <animate attributeName="stroke-dashoffset" values="201; {int(target_offset*0.5)}" dur="1.2s" begin="{0.2 + i*0.1}s" fill="freeze"/>\n'
            f'    </circle>\n'
            f'    <!-- Label Content -->\n'
            f'    <text x="92" y="48" class="met-title">{m_title}</text>\n'
            f'    <text x="92" y="70" class="met-val" fill="{m_color}">{m_val}</text>\n'
            f'  </g>'
        )
        svg_lines.append(pill_html)

    svg_lines.append('</svg>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"[✓] Successfully generated '{output_file}'")

# --- 5. README GENERATOR ---
def generate_readme(username, readme_path="README.md"):
    content = f"""# <h1 align="center">✨ Hi there, I'm {username} 👋</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=23&pause=1000&color=00F0FF&center=true&vcenter=true&width=650&lines=Full-Stack+Architect+%26+AI+Engineer;Building+Next-Gen+Interactive+Experiences;High-Performance+Code+%2B+Sci-Fi+Graphics" alt="Typing SVG" />
</p>

<!-- Hero Banner -->
<div align="center">
  <a href="https://github.com/{username}">
    <img src="./cyber-hero-banner.svg" alt="Cyber Hero Banner" width="100%" />
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
          <img src="./tech-radar-hud.svg" alt="Sci-Fi Tech Skill Radar" width="100%" />
        </a>
      </td>
      <td width="50%" align="center" valign="top" style="padding-left: 8px;">
        <a href="https://github.com/{username}">
          <img src="./architecture-showcase.svg" alt="Featured Architecture Pillars" width="100%" />
        </a>
      </td>
    </tr>
  </table>
</div>

<br />

<!-- Centered Glass Metric Telemetry Strip -->
<div align="center">
  <a href="https://github.com/{username}">
    <img src="./telemetry-metrics.svg" alt="Apple-Style Glass Metric Telemetry" width="100%" />
  </a>
</div>

<br />

---

<p align="center">
  ⚡ <i>Powered by Sci-Fi Glass Engine</i>
</p>
"""
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] Successfully updated '{readme_path}'")

# --- MAIN CLI EXECUTION ---
def main():
    parser = argparse.ArgumentParser(description="Generate Fresh Non-Terminal Profile README & SVGs")
    parser.add_argument("--username", type=str, default=DEFAULT_USERNAME, help="GitHub username")
    parser.add_argument("--outdir", type=str, default=".", help="Output directory")
    args = parser.parse_args()

    username = args.username
    outdir = args.outdir
    os.makedirs(outdir, exist_ok=True)

    print(f"[+] Generating Fresh Innovative SVGs for user '{username}'...")

    hero_path = os.path.join(outdir, "cyber-hero-banner.svg")
    radar_path = os.path.join(outdir, "tech-radar-hud.svg")
    arch_path = os.path.join(outdir, "architecture-showcase.svg")
    met_path = os.path.join(outdir, "telemetry-metrics.svg")
    readme_path = os.path.join(outdir, "README.md")

    generate_hero_banner_svg(username, hero_path)
    generate_radar_hud_svg(username, radar_path)
    generate_architecture_showcase_svg(username, arch_path)
    generate_telemetry_metrics_svg(username, met_path)
    generate_readme(username, readme_path)

    print("[🎉] All fresh innovative SVG cards generated successfully!")

if __name__ == "__main__":
    main()

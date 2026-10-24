"""Generates assets/stack.svg and assets/cards/*.svg. Run `python assets/gen.py`."""
import base64
import os
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
WORDS = ["Backend developer, .NET and Rails", "SCP:SL server plugins", "Shared plugin frameworks", "Game and web bridges"]
STACK = ["C#", ".NET", "Ruby", "Rails", "Go", "TypeScript", "Unity", "GraphQL", "Docker", "PostgreSQL", "Redis", "RabbitMQ"]
SANS = "'Segoe UI',-apple-system,Helvetica,Arial,sans-serif"
MONO = "Consolas,Menlo,'DejaVu Sans Mono',monospace"
PROJECTS = [
    ("Swappy", "Auto-updates chosen SCP:SL plugins at server startup. 250+ downloads.", "C#", ["SCP:SL", "Tooling"]),
    ("LabTesting", "In-process integration tests for LabAPI plugins on a real SCP:SL server.", "C#", ["Testing", "CI", "NuGet"]),
    ("Steam.Net", "Lightweight and minimal Steam wrapper for .NET 7+.", "C#", [".NET", "Library"]),
    ("StreamBlur", "Vencord plugin: blur DMs you open while streaming, click to reveal.", "TypeScript", ["Vencord", "Discord"]),
]
STEP = .6
CYCLE = len(STACK) * STEP

CSS = (
    f":root{{--t:#1f2328;--m:#656d76;--a:#7C3AED;--l:#d0d7de}}"
    f"@media (prefers-color-scheme:dark){{:root{{--t:#e6edf3;--m:#8b949e;--a:#A78BFA;--l:#30363d}}}}"
    f"text{{font-family:{SANS}}}.mono{{font-family:{MONO}}}.t{{fill:var(--t)}}.m{{fill:var(--m)}}"
    ".rise{opacity:0;animation:rise .8s cubic-bezier(.16,1,.3,1) forwards}"
    "@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}"
    ".slide{animation:slide 6s ease-in-out infinite alternate}"
    "@keyframes slide{from{transform:translateX(0)}to{transform:translateX(1096px)}}"
    f".s{{animation:lit {CYCLE}s infinite}}"
    f"@keyframes lit{{0%,{100 / len(STACK):.1f}%{{fill:var(--a)}}{200 / len(STACK):.1f}%,100%{{fill:var(--m)}}}}"
    "@media (prefers-reduced-motion:reduce){*{animation:none!important;opacity:1!important}}"
)


def build():
    x, row = 8, []
    for i, s in enumerate(STACK):
        row.append(f'<text class="mono m s" x="{x}" y="112" font-size="19" style="animation-delay:{i * STEP:.1f}s">{s}</text>')
        x += len(s) * 11 + 28
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 158" width="1200" height="158">'
        f"<style>{CSS}</style>"
        '<text class="rise t" x="6" y="64" font-size="60" font-weight="700" letter-spacing="-2">Morgan</text>'
        f'<text class="rise m" x="228" y="64" font-size="24" style="animation-delay:.2s">{WORDS[0]}</text>'
        + "".join(row)
        + '<line x1="8" y1="142" x2="1192" y2="142" stroke="var(--l)"/>'
        '<rect class="slide" x="8" y="141" width="96" height="2" rx="1" fill="var(--a)"/></svg>'
    )


ORGS = [
    ("Hexagone", "Official French SCP: Secret Laboratory servers.", "logos/hexagone.png", "image/png", "Servers"),
    ("Access Community", "The community behind Hexagone. Core developer since May 2023.", "logos/access.svg", "image/svg+xml", "Core developer"),
]
STATS = [("413", "commits since 2023"), ("15+", "repositories"), ("3+", "years on live servers")]


def about():
    cols = "".join(
        f'<g class="rise" style="animation-delay:{.3 + i * .15:.2f}s">'
        f'<line x1="{x - 24}" y1="30" x2="{x - 24}" y2="110" stroke="var(--l)"/>'
        f'<text class="t" x="{x}" y="76" font-size="46" font-weight="700" letter-spacing="-1">{n}</text>'
        f'<text class="mono m" x="{x}" y="102" font-size="13">{label}</text></g>'
        for i, (n, label) in enumerate(STATS) for x in [660 + i * 180])
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 140" width="1200" height="140">'
        f"<style>{CSS}</style>"
        '<text class="rise t" x="8" y="66" font-size="28" font-weight="600">Game servers, APIs and web bridges</text>'
        '<text class="rise m" x="8" y="98" font-size="18" style="animation-delay:.15s">Backend work in C# and Ruby, from plugins to dashboards.</text>'
        + cols + "</svg>")


def org(i, name, desc, path, mime, role):
    data = base64.b64encode(open(os.path.join(HERE, path), "rb").read()).decode()
    lines = "".join(f'<text class="m" x="116" y="{76 + n * 22}" font-size="15">{l}</text>' for n, l in enumerate(textwrap.wrap(desc, 46)[:2]))
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 590 132" width="590" height="132">'
        f'<style>{CSS}</style><g class="rise" style="animation-delay:{i * .12:.2f}s">'
        '<rect x=".5" y=".5" width="589" height="131" rx="12" fill="none" stroke="var(--l)"/>'
        '<clipPath id="r"><rect x="24" y="26" width="80" height="80" rx="16"/></clipPath>'
        f'<image clip-path="url(#r)" x="24" y="26" width="80" height="80" href="data:{mime};base64,{data}"/>'
        f'<text class="t" x="116" y="50" font-size="22" font-weight="600">{name}</text>'
        f'<text class="mono" x="562" y="48" font-size="13" text-anchor="end" fill="var(--a)">{role}</text>'
        + lines + "</g></svg>")


def contact(email):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 96" width="1200" height="96">'
        f'<style>{CSS}</style><g class="rise">'
        '<rect x=".5" y=".5" width="1199" height="95" rx="12" fill="none" stroke="var(--l)"/>'
        '<rect x="0" y="34" width="3" height="28" rx="1.5" fill="var(--a)"/>'
        '<text class="mono m" x="32" y="40" font-size="13">Email</text>'
        f'<text class="t" x="32" y="70" font-size="26" font-weight="600">{email}</text>'
        '<text class="mono" x="1168" y="58" font-size="15" text-anchor="end" fill="var(--a)">Send a message -&gt;</text></g></svg>')


def card(i, name, desc, lang, tags):
    lines = "".join(f'<text class="m" x="28" y="{74 + n * 22}" font-size="15">{l}</text>' for n, l in enumerate(textwrap.wrap(desc, 62)[:2]))
    x, pills = 28, []
    for t in tags:
        w = len(t) * 8 + 22
        pills.append(f'<rect x="{x}" y="112" width="{w}" height="24" rx="12" fill="none" stroke="var(--l)"/>'
                     f'<text class="mono m" x="{x + w / 2}" y="129" font-size="12" text-anchor="middle">{t}</text>')
        x += w + 8
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 590 156" width="590" height="156">'
        f'<style>{CSS}</style><g class="rise" style="animation-delay:{i * .12:.2f}s">'
        '<rect x=".5" y=".5" width="589" height="155" rx="12" fill="none" stroke="var(--l)"/>'
        '<rect x="0" y="28" width="3" height="28" rx="1.5" fill="var(--a)"/>'
        f'<text class="t" x="28" y="48" font-size="22" font-weight="600">{name}</text>'
        f'<text class="mono" x="562" y="46" font-size="13" text-anchor="end" fill="var(--a)">{lang}</text>'
        + lines + "".join(pills) + "</g></svg>")


if __name__ == "__main__":
    with open(os.path.join(HERE, "stack.svg"), "w", encoding="utf-8") as f:
        f.write(build())
    with open(os.path.join(HERE, "about.svg"), "w", encoding="utf-8") as f:
        f.write(about())
    os.makedirs(os.path.join(HERE, "cards"), exist_ok=True)
    with open(os.path.join(HERE, "cards", "contact.svg"), "w", encoding="utf-8") as f:
        f.write(contact("lilnesquuikpro@gmail.com"))
    for i, o in enumerate(ORGS):
        with open(os.path.join(HERE, "cards", o[0].split()[0].lower() + "-org.svg"), "w", encoding="utf-8") as f:
            f.write(org(i, *o))
    os.makedirs(os.path.join(HERE, "cards"), exist_ok=True)
    for i, pr in enumerate(PROJECTS):
        with open(os.path.join(HERE, "cards", pr[0].lower().replace(".", "") + ".svg"), "w", encoding="utf-8") as f:
            f.write(card(i, *pr))

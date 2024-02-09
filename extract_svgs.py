from opentypesvg import fonts2svg
from fontTools import ttLib

GLYPHS = {
    "ed5e6a": "↫⚂ηπτ∞",  # noadic-function
    "95d16a": "¬±¯`⌵√○⌊⌈⁅⧻△⇡⊢⇌♭¤⋯⍉⍏⍖⊚⊛◴◰□⋕",  # monadic-function
    "54b0fc": "=≠<≤>≥+-×*÷%◿ⁿₙ↧↥∠ℂ≍⊟⊂⊏⊡↯☇↙↘↻◫▽⌕∊⊗",  # dyadic-function
    "f0c36f": "/∧\\∵≡⊞⍥⊕⊜⊔⋅⊙∩°↬",  # monadic-modifier
    "cc6be9": "⍤⍜⊃⊓⋔⍢⬚⍣",  # dyadic-modifier
}

font = ttLib.TTFont("Uiua386.ttf")

glyphset = font.getGlyphSet()

cmap = font.getBestCmap()

for color in GLYPHS:
    print(color, GLYPHS[color])
    namelist = ",".join(cmap[ord(g)] for g in GLYPHS[color])
    fonts2svg.main(["-o", "build/SVGs", "-c", color, "-g", namelist, "Uiua386.ttf"])

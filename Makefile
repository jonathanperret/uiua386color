SRCSVGS := $(wildcard glyphs/*.svg)
PICOSVGS := $(patsubst glyphs/%.svg,build/SVGs/%.svg,$(SRCSVGS))

default: Uiua386Color.ttf Uiua386Color.woff2

build/SVGs/%.svg: glyphs/%.svg
	mkdir -p build/SVGs
	venv/bin/picosvg $< > $@

build/SVGs/pi.svg: Uiua386.ttf
	venv/bin/python extract_svgs.py

build/Uiua386ColorSVG.ttf: Uiua386.ttf $(PICOSVGS) build/SVGs/pi.svg
	cp Uiua386.ttf build/svg.ttf
	venv/bin/addsvg -m build/SVGs build/svg.ttf
	cp build/svg.ttf $@

Uiua386Color.ttf: build/Uiua386ColorSVG.ttf
	venv/bin/maximum_color --output_file COLRv1.ttf $<
	cp build/COLRv1.ttf $@

Uiua386Color.woff2: Uiua386Color.ttf
	venv/bin/fonttools ttLib $< --flavor woff2 -o $@

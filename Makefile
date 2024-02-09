SRCSVGS := $(wildcard glyphs/*.svg)
PICOSVGS := $(patsubst glyphs/%.svg,build/SVGs/%.svg,$(SRCSVGS))

default: Uiua386Color.ttf

build/SVGs/%.svg: glyphs/%.svg
	mkdir -p build/SVGs
	picosvg $< > $@

build/Uiua386ColorSVG.ttf: Uiua386.ttf $(PICOSVGS)
	cp Uiua386.ttf $@
	addsvg -m build/SVGs $@

Uiua386Color.ttf: build/Uiua386ColorSVG.ttf
	maximum_color --output_file $@ $<
	cp build/$@ $@

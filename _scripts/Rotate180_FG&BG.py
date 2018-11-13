# Rotate both "foreground" and "background" 180 degrees.
# Use your preferred shortcut and commonly used background layer name below.
# 2018/11/12

# menuTitle: Rotate 180 FG & BG
# shortCut: shift+command+r

font = CurrentFont()
glyph = CurrentGlyph()

def rotate180BothLayers(centerX, centerY):
    glyph.rotateBy(180, 
        (centerX,centerY)
        )
    
    l = glyph.getLayer("background")
    l.rotateBy(180, 
        (centerX,centerY)
        )

midpointX = glyph.bounds[0] + (glyph.bounds[2] - glyph.bounds[0]) / 2
midpointY = glyph.bounds[1] + (glyph.bounds[3] - glyph.bounds[1]) / 2

rotate180BothLayers(midpointX, midpointY)

glyph.performUndo()
glyph.update()

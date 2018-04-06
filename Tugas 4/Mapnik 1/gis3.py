import mapnik
m = mapnik.Map(1920,1080)
m.background = mapnik.Color('red')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#fcff00')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="Indonesia_Kab_Kota/Indo_Kab_Kot.shp")
layer = mapnik.Layer('indo')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'indo.jpeg', 'jpeg')
print "rendered image to 'indo.jpeg' "

#JPEG
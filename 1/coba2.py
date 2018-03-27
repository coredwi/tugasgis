import mapnik
m = mapnik.Map(3500,1500)
m.background = mapnik.Color('green')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#ff0000')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 1)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="shp1/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'world.pdf', 'pdf')
print "rendered image to 'world.pdf' "

#PDF
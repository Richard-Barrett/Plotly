1 import plotly.graph_objects as go
  2 
  3 planets = ['My Spaceship', 'Zeta Pyxidis', 'Kappa Pyxidis', 'Theta Pyxidis', 'Alpha Pyxidis', 'Betta Pyxi    dis', 'Delta Pyxidis', 'Gamma Pyxidis', 'Lambda Pyxidis']
  4 planet_colors = ['rgb(135, 135, 125)', 'rgb(210, 50, 0)', 'rgb(50, 90, 255)',
  5                  'rgb(178, 0, 0)', 'rgb(235, 235, 210)', 'rgb(235, 205, 130)',
  6                  'rgb(55, 255, 217)', 'rgb(38, 0, 171)', 'rgb(255, 255, 255)']
  7 distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
  8 density = [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638, 2095]
  9 gravity = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
 10 planet_diameter = [5000, 10000, 60000, 10000, 110000, 75000, 20000, 150000, 10000]
 11 
 12 # Create trace, sizing bubbles by planet diameter
 13 fig = go.Figure(data=go.Scatter3d(
 14     x = distance_from_sun,
 15     y = density,
 16     z = gravity,
 17     text = planets,
 18     mode = 'markers',
 19     marker = dict(
 20         sizemode = 'diameter',
 21         sizeref = 750, # info on sizeref: https://plot.ly/python/reference/#scatter-marker-sizeref
 22         size = planet_diameter,
 23         color = planet_colors,
 24         )
 25 ))
 26 
 27 fig.update_layout(width=800, height=800, title = 'Pyxis Constellation by Jasmine Morgan!',
 28                   scene = dict(xaxis=dict(title='Distance from Sun', titlefont_color='white'),
 29                                yaxis=dict(title='Density', titlefont_color='white'),
 30                                zaxis=dict(title='Gravity', titlefont_color='white'),
 31                                bgcolor = 'rgb(20, 24, 54)'
 32                            ))
 33 
 34 fig.show()

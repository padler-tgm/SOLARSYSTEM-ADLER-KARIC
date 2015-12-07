from adler_karic.ddd import MyApp

# Liste der Planeten 1.Name, 2.Groesse, 3.Position
planeten = [["sun", 8.37800000E+06, 0],["earth", 3.73000000E+06, 3.88960000E+08], ["moon", 1.73000000E+06, 5.88960000E+08]]
app = MyApp(planeten)
app.run()
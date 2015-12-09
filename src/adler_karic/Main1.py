from adler_karic.ddd import MyApp

# Liste der Planeten 1.Name, 2.Groesse, 3.Position --> nicht wahrheitsgetreu!
planeten = [["sun", 17.37800000E+06, 0],["earth", 7.7000000E+06, 1.000E+08],["mercury", 6.73000000E+06, 0.3E+08], ["moon", 2.1000000E+06, 1.3E+08],["jupiter", 10.000000E+06, 4.88960000E+08],["mars", 6.73000000E+06, 2.30000E+08],["venus", 7.2E+06, 0.50E+08],["saturn", 9.9000000E+06, 7.88960000E+08],["uranus", 8.73000000E+06, 9.88960000E+08],["neptune", 8.73000000E+06, 11.88960000E+08]]
app = MyApp(planeten)
app.run()
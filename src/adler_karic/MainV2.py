from adler_karic.v2.Planet import Planet

# Liste der Planeten 1.Name, 2.Groesse, 3.Position, 4.Rotation, 5.Translation --> nicht wahrheitsgetreu!
planeten = [["sun", 17.37800000E+06, 0, 10, 0],["earth", 7.7000000E+06, 1.000E+08, 10, 10],["mercury", 6.73000000E+06, 0.3E+08, 10, 10], ["moon", 2.1000000E+06, 1.3E+08, 10, 10],["jupiter", 10.000000E+06, 4.88960000E+08, 10, 10],["mars", 6.73000000E+06, 2.30000E+08, 10, 10],["venus", 7.2E+06, 0.50E+08, 10, 10],["saturn", 9.9000000E+06, 7.88960000E+08, 10, 10],["uranus", 8.73000000E+06, 9.88960000E+08, 10, 10],["neptune", 8.73000000E+06, 11.88960000E+08, 10, 10]]
app = Planet(planeten)
#Ausfuehren
app.run()
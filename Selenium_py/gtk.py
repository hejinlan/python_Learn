import gtk

window = gtk.Window()

screen = window.get_screen()
print ("screen size: %d x %d" % (gtk.gdk.screen_width(),gtk.gdk.screen_height()))




class Mode(object):
    "A class descrbing what a mode must be like."
    def on_draw(self, display, a_screen, camera):
        "Handles the drawing functions."
        pass
    def on_input(self, a_input):
        "Takes a list of events."
        pass
    def on_update(self):
        "Something to run every frame. (Every frame?)"
        pass
    def save_data(self):
        "Returns a JSON object describing the modes state."
        pass
    
        

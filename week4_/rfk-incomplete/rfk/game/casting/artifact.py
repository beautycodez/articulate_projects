from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact (Actor):
    def __init__(self):
        super().__init__()
        self.message = ""
    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message
    
    # def __init__(self, text):
    #     super().__init__(text)

    # def set_text(self,text):
    #     text



    # def _get_front_size(self):
    # def _get_color(self):
    # def _get_position(self):
    # def _get_message(self):                

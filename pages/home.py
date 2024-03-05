from flet import *

class Home(UserControl):
    
    def __int__(self,page):
        super().__init__()
        self.page = page

    def did_mount(self):
        # self.page.overlay.extend([pick_jd_dialog,pick_resume_dialog])
        self.page.update()

    def build(self):

        return Row(
           controls=[Text("Home Page")]
        )
    
   
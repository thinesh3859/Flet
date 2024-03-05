from flet import *

class ISLInputField(UserControl):
    def __init__(self,width,height,hint_text,icon,password=False):
        super().__init__()
        self.body = Container(
            Row([
                TextField(
                    hint_text=hint_text,
                    border=InputBorder.NONE,
                    hint_style=TextStyle(
                        color='black'
                    ),
                    height=height,
                    width=width/5*4,
                    bgcolor='white',
                    text_style=TextStyle(size=18,weight='w400',color='black'),
                    password=password
                ),
                Icon(icon,color='black')
            ]),

            border=border.all(1,'black'),
            border_radius=10,
            bgcolor='white',
            alignment=alignment.center,
            width=width
        )
    def build(self):
        return self.body
    

class ISLButtonField(UserControl):
    def __init__(self,width,height,strtext):
        super().__init__()
        self.body = Container(
            
            # gradient=LinearGradient(begin=alignment.top_left,end=alignment.bottom_right),
            content  = Row([
                ElevatedButton(
                    content= Text(strtext),
                    height=height,
                    width=width,
                    # border_radius =border_radius.all(10),
                    # filled = True,
                    bgcolor="yellow",
                    elevation=2,
                ),
            ]),

            # border=border.all(1,'black'),
            # border_radius=10,
            # bgcolor='white',
            # alignment=alignment.center,
            
        )
    def build(self):
        return self.body
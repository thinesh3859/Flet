from flet import *
import flet
from DataBase.UsersDb import CreateTable

from pages.usrControl import *

class Welcome(UserControl):
    def __int__(self,page):
        super().__init__()
        self.page = page

    def build(self):

        def ClickSignIn(e):
            # if(CreateTable()):
            self.page.go('/login')

        WelcomeText =Container(content=Row([ Text("Welcome Back",size=40,weight=FontWeight.W_900,color="white")],alignment=MainAxisAlignment.CENTER)) 
        WelcomeText2 = Text("Login to your account",size=20,weight=FontWeight.W_900,color="white")
        AppLogo = Container(content=Row([Image(src="assets/Images/inspirisys-logonew.png",width=150)],alignment=MainAxisAlignment.CENTER)) 
        SignInBtn = OutlinedButton(content=Text("SIGN IN",weight=FontWeight.W_900,size=20),width=self.page.width - 50,height=50,style=ButtonStyle(color="White",side=BorderSide(color="white",width=1.0)),on_click=ClickSignIn)
        SignUpBtn = ElevatedButton(content=Text("SIGN UP",weight=FontWeight.W_900,size=20,color="#F8A337"),width=self.page.width - 50,height=50,on_click=lambda _: self.page.go('/signup'))
        
        return Column([
            Container(
                alignment=alignment.center,
                content= Column([
                    AppLogo,
                    WelcomeText,
                    # WelcomeText2,
                ])
            ),
            Container(
                alignment=alignment.center,
                content= Column([
                    SignInBtn,
                    Container(
                        padding=padding.only(top=15),
                        content=SignUpBtn
                    ),
                    
                ])
            )
        ],
        alignment=MainAxisAlignment.SPACE_EVENLY)
        
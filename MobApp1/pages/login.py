import sqlite3
from flet import *
import flet
from DataBase.UsersDb import ValidateDBLogin

from pages.usrControl import *

class Login(UserControl):
    def __int__(self,page):
        super().__init__()
        self.page = page

    def build(self):
        WelcomeText = Container(content=Row([Text("Hello",size=40,weight=FontWeight.W_900,color="white")]),padding=padding.only(left=25,top=10)) 
        WelcomeText2 = Container(content=Row([Text("Sign in!",size=35,weight=FontWeight.W_900,color="white")]),padding=padding.only(left=25,top=-5)) 
        UserID = TextField(
                    hint_text="User Name",
                    # border=InputBorder.UNDERLINE,
                    hint_style=TextStyle(
                        color='black'
                    ),
                    height=50,
                    width=330,
                    bgcolor='white',
                    text_style=TextStyle(size=18,weight='w400',color='black'),
                    password=False
                   )
        Password = TextField(
                    hint_text="Password",
                    # border=InputBorder.NONE,
                    hint_style=TextStyle(
                        color='black'
                    ),
                    height=50,
                    width=330,
                    bgcolor='white',
                    text_style=TextStyle(size=18,weight='w400',color='black'),
                    password=True,
                    can_reveal_password=True
                   )
        
        def ValidateLogin(e):
            usernametxt = UserID.value
            passwordtxt = Password.value
            sqliteConnection = sqlite3.connect('DataBase/mobiledb.db')
            cursor = sqliteConnection.cursor()   
            cursor.execute("SELECT COUNT(1) FROM UserTable WHERE username = ? AND password = ?", (usernametxt, passwordtxt))
            userdt = cursor.fetchone()[0]
            print(userdt)

            if(userdt > 0):
                print("valid")
                print(UserID.value)
                self.page.go('/')
            else:
                e.control.page.snack_bar = SnackBar(Text(f"Invalid Credentials"))
                e.control.page.snack_bar.open = True
                e.control.page.update()
   
            
        LoginBtn = CupertinoButton(
                    content= Text("Log In"),
                    height=50,
                    width=330,
                    border_radius =border_radius.all(10),
                    #filled = True,
                    bgcolor="#FD8D00",
                    on_click=ValidateLogin
                    # on_click=lambda _: self.page.go('/')
                )
        AppLogo = Image(src="assets/Images/inspirisys-logonew.png",width=150)
        


        return Column(
            [
                # AppLogo,
                WelcomeText,
                WelcomeText2,
                Container(
                    bgcolor="white",
                    width=self.page.width,
                    height=self.page.height-100,
                    border_radius=BorderRadius(top_left=35,top_right=35,bottom_left=0,bottom_right=0),
                    padding=padding.only(top=70,left=25),
                    margin=margin.only(top=30),
                    content=Column([
                        Container(
                            padding=padding.only(bottom=20),
                            content=Column([
                                UserID,
                                Password,
                            ])),
                        LoginBtn,
                        Container(
                            padding=padding.only(top=35),
                            alignment=alignment.bottom_left,
                            content=Column([
                                Text("Don't have account?"),
                                TextButton("Sign up",on_click=lambda _: self.page.go('/signup'))
                            ])
                        )
                    ],alignment=MainAxisAlignment.START)
                ),
                
            ],
            
            # alignment=MainAxisAlignment.START,
            # horizontal_alignment=CrossAxisAlignment.CENTER,
            # alignment= MainAxisAlignment.START
            alignment=alignment.center
        )
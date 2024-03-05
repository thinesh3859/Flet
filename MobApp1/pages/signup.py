import sqlite3
from flet import *
import flet

from pages.usrControl import *

class SignUp(UserControl):
    def __int__(self,page):
        super().__init__()
        self.page = page

    def build(self):
        WelcomeText = Container(content=Row([Text("Create Your",size=40,weight=FontWeight.W_900,color="white")]),padding=padding.only(left=25,top=10)) 
        WelcomeText2 = Container(content=Row([Text("Account",size=35,weight=FontWeight.W_900,color="white")]),padding=padding.only(left=25,top=-5)) 

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
        Mobile = TextField(
                    hint_text="Contact Number",
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
        Email = TextField(
                    hint_text="Email ID",
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
                    # border=InputBorder.UNDERLINE,
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
        
        def CreateUser(e):
            print("")
            usernametxt = str(UserID.value)
            passwordtxt = str(Password.value)
            mobiletxt = str(Mobile.value)
            emailtxt = str(Email.value)

            
            sqliteConnection = sqlite3.connect('DataBase/mobiledb.db')
            cursor = sqliteConnection.cursor() 
            # cursor.execute("SELECT COUNT(1) FROM UserTable WHERE username = '"+ usernametxt +"' ")
            # userdt = cursor.fetchone()[0]
            # print(userdt)
            userdt = 0
            if(userdt > 0):
                print("Old User")
                # e.control.page.snack_bar = SnackBar(Text(f"User Already Exists"))
                # e.control.page.snack_bar.open = True
                # e.control.page.update()
            else:
                try:
                    print("New User")
                    # sqliteConnection = sqlite3.connect('DataBase/mobiledb.db')

                    print("New User1")
                    # cursor.execute("insert into UserTable values ('"+ usernametxt +"','"+ passwordtxt +"','"+ mobiletxt +"','"+ emailtxt +"','"+ usernametxt +"','"+ usernametxt +"')")
                    cursor.execute("""
                        insert into UserTable values
                       (?,?,'1234567890','thinesh@gmail.com','add1','172.19.0')
                    """,(usernametxt,passwordtxt))
                    print("New User2")
                    sqliteConnection.commit()
                    print("New User3")
                    cursor.close()
                    e.control.page.snack_bar = SnackBar(Text(f"User Registered Successfuly"))
                    e.control.page.snack_bar.open = True
                    e.control.page.update()
                    self.page.go('/login')
                except sqlite3.Error as error:
                    print('Error occurred - ', error)
                
   
            
        LoginBtn = CupertinoButton(
                    content= Text("Sign Up"),
                    height=50,
                    width=330,
                    border_radius =border_radius.all(10),
                    #filled = True,
                    bgcolor="#FD8D00",
                    on_click=CreateUser
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
                                Mobile,
                                Email
                            ])),
                        LoginBtn,
                        Container(
                            padding=padding.only(top=35),
                            alignment=alignment.bottom_left,
                            content=Column([
                                Text("Already haveing account?"),
                                TextButton("Sign In",on_click=lambda _: self.page.go('/login'))
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
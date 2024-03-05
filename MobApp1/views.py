from flet import *
from pages.login import Login
from pages.home import Home
from pages.signup import SignUp
from pages.welcome import Welcome

def views_handler(page):
    AppBarElm = AppBar(
                bgcolor='#FFE66F',
                title=Text("Inspirisys"),
                actions=[
                    IconButton(icons.LOGOUT_ROUNDED,on_click=lambda _: page.go('/login')),
                ]
            )
    
    return {
        '/': View(
            appbar=AppBarElm,
            bgcolor='#FFF9AE',
            padding=padding.all(5),
            route='/',
            controls=[
                Home(page)
            ]
        ),
        '/login': View(
            padding=padding.all(0),
            route='/login',
            controls=[
                Container(
                    height =page.height,
                    width=page.width,
                    margin=0,
                    gradient=LinearGradient(begin=alignment.bottom_left,end=alignment.top_right,colors=["#FD8D00","#f8a337"]),
                    content= Login(page)
                )

               
            ]
        ),
        '/signup': View(
            scroll=ScrollMode.ADAPTIVE,
            padding=padding.all(0),
            route='/signup',
            controls=[
                Container(
                    height =page.height,
                    width=page.width,
                    margin=0,
                    gradient=LinearGradient(begin=alignment.bottom_left,end=alignment.top_right,colors=["#FD8D00","#f8a337"]),
                    content= SignUp(page)
                )
            ]
        ),
        '/welcome': View(
            bgcolor="red",
            padding=padding.all(0),
            route='/welcome',
            controls=[
                Container(
                    height =page.height,
                    width=page.width,
                    margin=0,
                    gradient=LinearGradient(begin=alignment.top_left,end=alignment.bottom_left,colors=["#FD8D00","#f8a337"]),
                    content= Welcome(page)
                )

               
            ]
        )
    }
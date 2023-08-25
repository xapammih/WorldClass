import customtkinter
from Application import MainWindow


app_window = MainWindow()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def render():
    app_window.personal_info()
    app_window.step_1()
    app_window.step_2()
    app_window.step_3()


if __name__ == '__main__':
    render()
    app_window.app.mainloop()




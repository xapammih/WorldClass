import customtkinter
from Application import app_window

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def main():
    app_window.personal_info()
    app_window.doctor_info()
    app_window.wanted_result()
    app_window.step_1()
    app_window.step_2()
    app_window.step_3()
    app_window.step_4()
    app_window.save_document()
    app_window.print_document()
    app_window.clear_all()
    app_window.app.mainloop()


if __name__ == '__main__':
    main()


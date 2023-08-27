import customtkinter
from Application import MainWindow

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class AdminPanel:

    def __init__(self):
        self.admin_app = customtkinter.CTk()

    def doctor_info_callback(self):
        with open('doctors.txt', 'w') as f:
            f.write(self.doctor_names_textbox.get("0.0", "end"))

    def doctor_info(self):
        doctor_names_label = customtkinter.CTkLabel(master=self.admin_app,
                                                    text='Введите имя докторов, каждого доктора с новой строчки! ')
        doctor_names_label.grid(row=0, column=0, padx=20, pady=0)
        self.doctor_names_textbox = customtkinter.CTkTextbox(master=self.admin_app, corner_radius=10)
        self.doctor_names_textbox.grid(row=1, column=0, padx=20, pady=20)

        doctor_names_button = customtkinter.CTkButton(master=self.admin_app, text='Записать!',
                                                            command=self.doctor_info_callback)
        doctor_names_button.grid(row=2, column=0, padx=20, pady=20)

    def procedures_callback(self):
        with open('procedures.txt', 'w') as f:
            f.write(self.procedures_textbox.get("0.0", "end"))

    def procedures(self):
        procedures = customtkinter.CTkLabel(master=self.admin_app,
                                            text='Введите название процедур, каждую процедуру с новой строчки!')
        procedures.grid(row=0, column=1, padx=20, pady=0)
        self.procedures_textbox = customtkinter.CTkTextbox(master=self.admin_app, corner_radius=10)
        self.procedures_textbox.grid(row=1, column=1, padx=20, pady=20)

        procedures_button = customtkinter.CTkButton(master=self.admin_app, text='Записать!',
                                                            command=self.procedures_callback)
        procedures_button.grid(row=2, column=1, padx=20, pady=20)

    def period_callback(self):
        with open('periods.txt', 'w') as f:
            f.write(self.periods_textbox.get("0.0", "end"))

    def period(self):
        periods = customtkinter.CTkLabel(master=self.admin_app,
                                            text='Введите период назначения, каждый период с новой строчки!')
        periods.grid(row=3, column=0, padx=20, pady=0)
        self.periods_textbox = customtkinter.CTkTextbox(master=self.admin_app, corner_radius=10)
        self.periods_textbox.grid(row=4, column=0, padx=20, pady=20)

        periods_button = customtkinter.CTkButton(master=self.admin_app, text='Записать!',
                                                            command=self.period_callback)
        periods_button.grid(row=5, column=0, padx=20, pady=20)


def admin():
    admin_app = AdminPanel()
    admin_app.admin_app.title('Admin panel')
    admin_app.admin_app.geometry('1000x1000')
    admin_app.doctor_info()
    admin_app.procedures()
    admin_app.period()
    admin_app.admin_app.mainloop()


admin()



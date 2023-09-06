import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class AdminPanel:

    def __init__(self):
        self.admin_app = customtkinter.CTk()
        w, h = self.admin_app.winfo_screenwidth(), self.admin_app.winfo_screenheight()
        self.admin_app.geometry("%dx%d+0+0" % (w, h))
        self.frame = customtkinter.CTkScrollableFrame(self.admin_app,
                                                      width=self.admin_app.winfo_screenwidth(),
                                                      height=self.admin_app.winfo_screenheight())
        self.frame.pack()
        self.doctor_names_textbox = None
        self.procedure_1_textbox = None
        self.procedure_2_textbox = None
        self.procedure_3_textbox = None
        self.procedure_4_textbox = None
        self.procedure_5_textbox = None
        self.procedure_6_textbox = None
        self.procedure_7_textbox = None
        self.procedure_8_textbox = None
        self.procedure_9_textbox = None
        self.periods_textbox = None

    def warning_info(self):
        warning_label = customtkinter.CTkLabel(master=self.frame,
                                               text='Убедительная просьба, '
                                                    'каждый новый элемент вводить с новой строчки!'
                                                    ' А также нажимать на кнопку подтвердить после введения текста '
                                                    'в каждое поле.',
                                               font=('Arial', 16), text_color='yellow')
        warning_label.grid(row=0, column=0, padx=20, pady=20, columnspan=4)

    def doctor_info_callback(self):
        with open('doctors.txt', 'w') as f:
            f.write(self.doctor_names_textbox.get("0.0", "end"))

    def doctor_info(self):
        doctor_names_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Введите имена докторов')
        doctor_names_label.grid(row=1, column=0, padx=20, pady=0)
        self.doctor_names_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=10)
        with open('doctors.txt', 'r') as f:
            self.doctor_names_textbox.insert("0.0", f.read())
        self.doctor_names_textbox.grid(row=2, column=0, padx=20, pady=10)

        doctor_names_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                      command=self.doctor_info_callback)
        doctor_names_button.grid(row=3, column=0, padx=20, pady=10)

    def procedure_1_callback(self):
        with open('procedure_1.txt', 'w') as f:
            f.write(self.procedure_1_textbox.get("0.0", "end"))

    def procedure_2_callback(self):
        with open('procedure_2.txt', 'w') as f:
            f.write(self.procedure_2_textbox.get("0.0", "end"))

    def procedure_3_callback(self):
        with open('procedure_3.txt', 'w') as f:
            f.write(self.procedure_3_textbox.get("0.0", "end"))

    def procedure_4_callback(self):
        with open('procedure_4.txt', 'w') as f:
            f.write(self.procedure_4_textbox.get("0.0", "end"))

    def procedure_5_callback(self):
        with open('procedure_5.txt', 'w') as f:
            f.write(self.procedure_5_textbox.get("0.0", "end"))

    def procedure_6_callback(self):
        with open('procedure_6.txt', 'w') as f:
            f.write(self.procedure_6_textbox.get("0.0", "end"))

    def procedure_7_callback(self):
        with open('procedure_7.txt', 'w') as f:
            f.write(self.procedure_7_textbox.get("0.0", "end"))

    def procedure_8_callback(self):
        with open('procedure_8.txt', 'w') as f:
            f.write(self.procedure_8_textbox.get("0.0", "end"))

    def procedure_9_callback(self):
        with open('procedure_9.txt', 'w') as f:
            f.write(self.procedure_9_textbox.get("0.0", "end"))

    def procedures(self):
        procedures_1_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Процедуры консультации')
        procedures_1_label.grid(row=1, column=1, padx=20, pady=0)

        self.procedure_1_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=0)
        self.procedure_1_textbox.grid(row=2, column=1, padx=20, pady=10)
        with open('procedure_1.txt', 'r') as f:
            self.procedure_1_textbox.insert("0.0", f.read())

        procedures_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                    command=self.procedure_1_callback)
        procedures_button.grid(row=3, column=1, padx=20, pady=10)

        procedures_2_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Процедуры диагностики')
        procedures_2_label.grid(row=1, column=2, padx=20, pady=0)

        self.procedure_2_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=0)
        self.procedure_2_textbox.grid(row=2, column=2, padx=20, pady=10)
        with open('procedure_2.txt', 'r') as f:
            self.procedure_2_textbox.insert("0.0", f.read())

        procedures_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                    command=self.procedure_2_callback)
        procedures_button.grid(row=3, column=2, padx=20, pady=10)

        procedures_3_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Процедуры аппаратной косметологии лица')
        procedures_3_label.grid(row=1, column=3, padx=20, pady=0)

        self.procedure_3_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=0)
        self.procedure_3_textbox.grid(row=2, column=3, padx=20, pady=10)
        with open('procedure_3.txt', 'r') as f:
            self.procedure_3_textbox.insert("0.0", f.read())

        procedures_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                    command=self.procedure_3_callback)
        procedures_button.grid(row=3, column=3, padx=20, pady=10)

        procedures_4_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Процедуры аппаратной косметологии тела')
        procedures_4_label.grid(row=4, column=0, padx=20, pady=0)

        self.procedure_4_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=0)
        self.procedure_4_textbox.grid(row=5, column=0, padx=20, pady=10)
        with open('procedure_4.txt', 'r') as f:
            self.procedure_4_textbox.insert("0.0", f.read())

        procedures_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                    command=self.procedure_4_callback)
        procedures_button.grid(row=6, column=0, padx=20, pady=20)

        procedures_5_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Процедуры инъекционной косметологии для лица')
        procedures_5_label.grid(row=4, column=1, padx=20, pady=0)

        self.procedure_5_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=0)
        self.procedure_5_textbox.grid(row=5, column=1, padx=20, pady=10)
        with open('procedure_5.txt', 'r') as f:
            self.procedure_5_textbox.insert("0.0", f.read())

        procedures_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                    command=self.procedure_5_callback)
        procedures_button.grid(row=6, column=1, padx=20, pady=20)

        procedures_6_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Процедуры инъекционной косметологии для тела')
        procedures_6_label.grid(row=4, column=2, padx=20, pady=0)

        self.procedure_6_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=0)
        self.procedure_6_textbox.grid(row=5, column=2, padx=20, pady=10)
        with open('procedure_6.txt', 'r') as f:
            self.procedure_6_textbox.insert("0.0", f.read())

        procedures_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                    command=self.procedure_6_callback)
        procedures_button.grid(row=6, column=2, padx=20, pady=20)

        procedures_7_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Процедуры эстетической косметологии для лица')
        procedures_7_label.grid(row=4, column=3, padx=20, pady=0)

        self.procedure_7_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=0)
        self.procedure_7_textbox.grid(row=5, column=3, padx=20, pady=10)
        with open('procedure_7.txt', 'r') as f:
            self.procedure_7_textbox.insert("0.0", f.read())

        procedures_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                    command=self.procedure_7_callback)
        procedures_button.grid(row=6, column=3, padx=20, pady=20)

        procedures_8_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Процедуры эстетической косметологии для тела')
        procedures_8_label.grid(row=7, column=0, padx=20, pady=0)

        self.procedure_8_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=0)
        self.procedure_8_textbox.grid(row=8, column=0, padx=20, pady=10)
        with open('procedure_8.txt', 'r') as f:
            self.procedure_8_textbox.insert("0.0", f.read())

        procedures_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                    command=self.procedure_8_callback)
        procedures_button.grid(row=9, column=0, padx=20, pady=20)

        procedures_9_label = customtkinter.CTkLabel(master=self.frame,
                                                    text='Процедуры СПА ритуалов и услуг')
        procedures_9_label.grid(row=7, column=1, padx=20, pady=0)

        self.procedure_9_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=0)
        self.procedure_9_textbox.grid(row=8, column=1, padx=20, pady=10)
        with open('procedure_9.txt', 'r') as f:
            self.procedure_9_textbox.insert("0.0", f.read())

        procedures_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                    command=self.procedure_9_callback)
        procedures_button.grid(row=9, column=1, padx=20, pady=20)

    def period_callback(self):
        with open('periods.txt', 'w') as f:
            f.write(self.periods_textbox.get("0.0", "end"))

    def period(self):
        periods = customtkinter.CTkLabel(master=self.frame,
                                         text='Введите периоды назначений')
        periods.grid(row=7, column=2, padx=20, pady=0)
        self.periods_textbox = customtkinter.CTkTextbox(master=self.frame, corner_radius=10)
        self.periods_textbox.grid(row=8, column=2, padx=20, pady=10)
        with open('periods.txt', 'r') as f:
            self.periods_textbox.insert("0.0", f.read())

        periods_button = customtkinter.CTkButton(master=self.frame, text='Подтвердить',
                                                 command=self.period_callback)
        periods_button.grid(row=9, column=2, padx=20, pady=10)

    def clear_all_callback(self):
        self.doctor_names_textbox.delete('0.0', customtkinter.END)
        self.procedure_1_textbox.delete('0.0', customtkinter.END)
        self.procedure_2_textbox.delete('0.0', customtkinter.END)
        self.procedure_3_textbox.delete('0.0', customtkinter.END)
        self.procedure_4_textbox.delete('0.0', customtkinter.END)
        self.procedure_5_textbox.delete('0.0', customtkinter.END)
        self.procedure_6_textbox.delete('0.0', customtkinter.END)
        self.procedure_7_textbox.delete('0.0', customtkinter.END)
        self.procedure_8_textbox.delete('0.0', customtkinter.END)
        self.procedure_9_textbox.delete('0.0', customtkinter.END)
        self.periods_textbox.delete('0.0', customtkinter.END)

    def clear_all(self) -> None:
        clear_all_button = customtkinter.CTkButton(master=self.frame, text='Очистить все',
                                                   command=self.clear_all_callback)
        clear_all_button.grid(row=9, column=3, padx=20, pady=0)


def admin():
    admin_app = AdminPanel()
    admin_app.admin_app.title('Admin panel')
    admin_app.warning_info()
    admin_app.doctor_info()
    admin_app.procedures()
    admin_app.period()
    admin_app.clear_all()
    admin_app.admin_app.mainloop()


admin()

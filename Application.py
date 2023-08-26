import customtkinter
import datetime


class Data:

    def __init__(self):
        self.phone =


class MainWindow:

    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry('2000x2000')
        self.app.title = 'World Class'
        self.name = None
        self.surname = None
        self.phone = None
        self.app.grid_columnconfigure(0, weight=1)

    def personal_info_callback(self):


    def personal_info(self):
        name = customtkinter.CTkEntry(master=self.app, placeholder_text="Имя...")
        name.grid(row=0, column=0, padx=20, pady=20)
        surname = customtkinter.CTkEntry(master=self.app, placeholder_text="Фамилия...")
        surname.grid(row=0, column=1, padx=20, pady=20)
        phone = customtkinter.CTkEntry(master=self.app, placeholder_text="Телефон...")
        phone.grid(row=0, column=2, padx=20, pady=20)
        personal_info_button = customtkinter.CTkButton(master=self.app, text='Принять!', command=self.personal_info_callback)

    def step_1_combobox_callback_1(self, choise):
        print(choise)

    def step_1_combobox_callback_2(self, choise):
        print(choise)

    def step_1_combobox_callback_3(self, choise):
        print(choise)

    def step_1_combobox_callback_4(self, choise):
        print(choise)

    def step_1_combobox_callback_5(self, choise):
        print(choise)

    def step_1(self):
        step_1_label = customtkinter.CTkLabel(master=self.app, text='Шаг 1: ТОП решения...')
        step_1_label.grid(row=1, column=0, padx=30, pady=(10, 0))

        step_1_combobox_1 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_1)
        step_1_combobox_1.grid(row=2, column=0, padx=20, pady=0)

        step_1_combobox_2 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_2)
        step_1_combobox_2.grid(row=2, column=1, padx=20, pady=0)

        step_1_combobox_3 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_3)
        step_1_combobox_3.grid(row=2, column=2, padx=20, pady=0)

        step_1_combobox_4 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_4)
        step_1_combobox_4.grid(row=2, column=3, padx=20, pady=0)

        step_1_combobox_5 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_5)
        step_1_combobox_5.grid(row=2, column=4, padx=20, pady=0)

        step_1_label_procedures_count = customtkinter.CTkLabel(master=self.app, text='Кол-во процедур')
        step_1_label_procedures_count.grid(row=3, column=0, padx=20, pady=0)
        step_1_procedures_1 = customtkinter.CTkEntry(master=self.app)
        step_1_procedures_1.grid(row=4, column=0, padx=20, pady=0)

        step_1_procedures_2 = customtkinter.CTkEntry(master=self.app)
        step_1_procedures_2.grid(row=4, column=1, padx=20, pady=0)

        step_1_procedures_3 = customtkinter.CTkEntry(master=self.app)
        step_1_procedures_3.grid(row=4, column=2, padx=20, pady=0)

        step_1_procedures_4 = customtkinter.CTkEntry(master=self.app)
        step_1_procedures_4.grid(row=4, column=3, padx=20, pady=0)

        step_1_procedures_5 = customtkinter.CTkEntry(master=self.app)
        step_1_procedures_5.grid(row=4, column=4, padx=20, pady=0)

        step_1_label_period = customtkinter.CTkLabel(master=self.app, text='Период')
        step_1_label_period.grid(row=5, column=0, padx=20, pady=0)
        step_1_period = customtkinter.CTkEntry(master=self.app)
        step_1_period.grid(row=6, column=0, padx=20, pady=0)

        step_1_period = customtkinter.CTkEntry(master=self.app)
        step_1_period.grid(row=6, column=1, padx=20, pady=0)

        step_1_period = customtkinter.CTkEntry(master=self.app)
        step_1_period.grid(row=6, column=2, padx=20, pady=0)

        step_1_period = customtkinter.CTkEntry(master=self.app)
        step_1_period.grid(row=6, column=3, padx=20, pady=0)

        step_1_period = customtkinter.CTkEntry(master=self.app)
        step_1_period.grid(row=6, column=4, padx=20, pady=0)



        step_1_label_period = customtkinter.CTkLabel(master=self.app, text='Комментарий')
        step_1_label_period.grid(row=7, column=0, padx=20, pady=0)
        step_1_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        step_1_commentary.grid(row=8, column=0, padx=20, pady=0)



    def step_2_combobox_callback_1(self, choise):
        print(choise)

    def step_2_combobox_callback_2(self, choise):
        print(choise)

    def step_2_combobox_callback_3(self, choise):
        print(choise)

    def step_2_combobox_callback_4(self, choise):
        print(choise)

    def step_2_combobox_callback_5(self, choise):
        print(choise)

    def step_2(self):
        step_2_label = customtkinter.CTkLabel(master=self.app, text='Шаг 2: Улучшение и закрепление')
        step_2_label.grid(row=1, column=5, padx=20, pady=0)

        step_2_combobox_1 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_1)
        step_2_combobox_1.grid(row=2, column=5, padx=20, pady=0)

        step_2_combobox_2 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_2)
        step_2_combobox_2.grid(row=2, column=6, padx=20, pady=0)

        step_2_combobox_3 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_3)
        step_2_combobox_3.grid(row=2, column=7, padx=20, pady=0)

        step_2_combobox_4 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_4)
        step_2_combobox_4.grid(row=2, column=8, padx=20, pady=0)

        step_2_combobox_5 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_5)
        step_2_combobox_5.grid(row=2, column=9, padx=20, pady=0)

        step_2_label_procedures_count = customtkinter.CTkLabel(master=self.app, text='Кол-во процедур')
        step_2_label_procedures_count.grid(row=3, column=5, padx=20, pady=0)
        step_2_procedures_1 = customtkinter.CTkEntry(master=self.app)
        step_2_procedures_1.grid(row=4, column=5, padx=20, pady=0)

        step_2_procedures_2 = customtkinter.CTkEntry(master=self.app)
        step_2_procedures_2.grid(row=4, column=6, padx=20, pady=0)

        step_2_procedures_3 = customtkinter.CTkEntry(master=self.app)
        step_2_procedures_3.grid(row=4, column=7, padx=20, pady=0)

        step_2_procedures_4 = customtkinter.CTkEntry(master=self.app)
        step_2_procedures_4.grid(row=4, column=8, padx=20, pady=0)

        step_2_procedures_5 = customtkinter.CTkEntry(master=self.app)
        step_2_procedures_5.grid(row=4, column=9, padx=20, pady=0)

        step_2_label_period = customtkinter.CTkLabel(master=self.app, text='Период')
        step_2_label_period.grid(row=5, column=5, padx=20, pady=0)
        step_2_period = customtkinter.CTkEntry(master=self.app)
        step_2_period.grid(row=6, column=5, padx=20, pady=0)

        step_2_period = customtkinter.CTkEntry(master=self.app)
        step_2_period.grid(row=6, column=6, padx=20, pady=0)

        step_2_period = customtkinter.CTkEntry(master=self.app)
        step_2_period.grid(row=6, column=7, padx=20, pady=0)

        step_2_period = customtkinter.CTkEntry(master=self.app)
        step_2_period.grid(row=6, column=8, padx=20, pady=0)

        step_2_period = customtkinter.CTkEntry(master=self.app)
        step_2_period.grid(row=6, column=9, padx=20, pady=0)

        step_2_label_period = customtkinter.CTkLabel(master=self.app, text='Комментарий')
        step_2_label_period.grid(row=7, column=5, padx=20, pady=0)
        step_2_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        step_2_commentary.grid(row=8, column=5, padx=20, pady=0)

    def step_3(self):
        step_3_label = customtkinter.CTkLabel(master=self.app, text='Шаг 3: Поддержка и...')
        step_3_label.grid(row=9, column=0, padx=30, pady=(10, 0))

        step_3_combobox_1 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_1)
        step_3_combobox_1.grid(row=10, column=0, padx=20, pady=0)

        step_3_combobox_2 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_2)
        step_3_combobox_2.grid(row=10, column=1, padx=20, pady=0)

        step_3_combobox_3 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_3)
        step_3_combobox_3.grid(row=10, column=2, padx=20, pady=0)

        step_3_combobox_4 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_4)
        step_3_combobox_4.grid(row=10, column=3, padx=20, pady=0)

        step_3_combobox_5 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_combobox_callback_5)
        step_3_combobox_5.grid(row=10, column=4, padx=20, pady=0)

        step_3_label_procedures_count = customtkinter.CTkLabel(master=self.app, text='Кол-во процедур')
        step_3_label_procedures_count.grid(row=11, column=0, padx=20, pady=0)
        step_3_procedures_1 = customtkinter.CTkEntry(master=self.app)
        step_3_procedures_1.grid(row=12, column=0, padx=20, pady=0)

        step_3_procedures_2 = customtkinter.CTkEntry(master=self.app)
        step_3_procedures_2.grid(row=12, column=1, padx=20, pady=0)

        step_3_procedures_3 = customtkinter.CTkEntry(master=self.app)
        step_3_procedures_3.grid(row=12, column=2, padx=20, pady=0)

        step_3_procedures_4 = customtkinter.CTkEntry(master=self.app)
        step_3_procedures_4.grid(row=12, column=3, padx=20, pady=0)

        step_3_procedures_5 = customtkinter.CTkEntry(master=self.app)
        step_3_procedures_5.grid(row=12, column=4, padx=20, pady=0)

        step_3_label_period = customtkinter.CTkLabel(master=self.app, text='Период')
        step_3_label_period.grid(row=13, column=0, padx=20, pady=0)
        step_3_period = customtkinter.CTkEntry(master=self.app)
        step_3_period.grid(row=14, column=0, padx=20, pady=0)

        step_3_period = customtkinter.CTkEntry(master=self.app)
        step_3_period.grid(row=14, column=1, padx=20, pady=0)

        step_3_period = customtkinter.CTkEntry(master=self.app)
        step_3_period.grid(row=14, column=2, padx=20, pady=0)

        step_3_period = customtkinter.CTkEntry(master=self.app)
        step_3_period.grid(row=14, column=3, padx=20, pady=0)

        step_3_period = customtkinter.CTkEntry(master=self.app)
        step_3_period.grid(row=14, column=4, padx=20, pady=0)

        step_3_label_period = customtkinter.CTkLabel(master=self.app, text='Комментарий')
        step_3_label_period.grid(row=15, column=0, padx=20, pady=0)
        step_3_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        step_3_commentary.grid(row=16, column=0, padx=20, pady=0)




import customtkinter
import datetime
from tkinter.filedialog import asksaveasfilename


class Data:

    def __init__(self):
        self.phone = None
        self.name = None
        self.surname = None
        self.fathername = None
        self.doctor = None
        self.current_date = datetime.date.today().strftime('%d-%m-%Y')
        self.current_time = datetime.datetime.now().strftime("%H:%M")
        self.step_1_procedure_1 = None
        self.step_1_procedure_2 = None
        self.step_1_procedure_3 = None
        self.step_1_procedure_4 = None
        self.step_1_procedure_5 = None
        self.step_1_procedure_count_1 = None
        self.step_1_procedure_count_2 = None
        self.step_1_procedure_count_3 = None
        self.step_1_procedure_count_4 = None
        self.step_1_procedure_count_5 = None
        self.step_1_procedure_period_1 = None
        self.step_1_procedure_period_2 = None
        self.step_1_procedure_period_3 = None
        self.step_1_procedure_period_4 = None
        self.step_1_procedure_period_5 = None
        self.step_1_commentary = None
        self.step_2_procedure_1 = None
        self.step_2_procedure_2 = None
        self.step_2_procedure_3 = None
        self.step_2_procedure_4 = None
        self.step_2_procedure_5 = None
        self.step_2_procedure_count_1 = None
        self.step_2_procedure_count_2 = None
        self.step_2_procedure_count_3 = None
        self.step_2_procedure_count_4 = None
        self.step_2_procedure_count_5 = None
        self.step_2_procedure_period_1 = None
        self.step_2_procedure_period_2 = None
        self.step_2_procedure_period_3 = None
        self.step_2_procedure_period_4 = None
        self.step_2_procedure_period_5 = None
        self.step_2_commentary = None
        self.step_3_procedure_1 = None
        self.step_3_procedure_2 = None
        self.step_3_procedure_3 = None
        self.step_3_procedure_4 = None
        self.step_3_procedure_5 = None
        self.step_3_procedure_count_1 = None
        self.step_3_procedure_count_2 = None
        self.step_3_procedure_count_3 = None
        self.step_3_procedure_count_4 = None
        self.step_3_procedure_count_5 = None
        self.step_3_procedure_period_1 = None
        self.step_3_procedure_period_2 = None
        self.step_3_procedure_period_3 = None
        self.step_3_procedure_period_4 = None
        self.step_3_procedure_period_5 = None
        self.step_3_commentary = None


class MainWindow:

    def __init__(self, data):
        self.app = customtkinter.CTk()
        self.app.title = 'World Class'
        self.app.grid_columnconfigure(0, weight=1)
        self.data = data

    def personal_info_callback(self):
        self.data.name = self.name_entry.get()
        self.data.surname = self.surname_entry.get()
        self.data.fathername = self.fathername_entry.get()
        self.data.phone = self.phone_entry.get()

    def personal_info(self):
        self.surname_entry = customtkinter.CTkEntry(master=self.app, placeholder_text="Фамилия...")
        self.surname_entry.grid(row=0, column=0, padx=20, pady=20)
        self.name_entry = customtkinter.CTkEntry(master=self.app, placeholder_text="Имя...")
        self.name_entry.grid(row=0, column=1, padx=20, pady=20)
        self.fathername_entry = customtkinter.CTkEntry(master=self.app, placeholder_text="Отчество...")
        self.fathername_entry.grid(row=0, column=2, padx=20, pady=20)
        self.phone_entry = customtkinter.CTkEntry(master=self.app, placeholder_text="Телефон...")
        self.phone_entry.grid(row=0, column=3, padx=20, pady=20)

        personal_info_button = customtkinter.CTkButton(master=self.app, text='Принять!',
                                                       command=self.personal_info_callback)
        personal_info_button.grid(row=0, column=4, padx=20, pady=20)

    def doctor_combobox_callback(self, choise):
        self.data.doctor = choise

    def doctor_info(self):
        step_1_label = customtkinter.CTkLabel(master=self.app, text='Выберите специалиста: ')
        step_1_label.grid(row=0, column=5, padx=30, pady=(10, 0))
        doctor_combobox = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.doctor_combobox_callback)
        doctor_combobox.grid(row=0, column=6, padx=20, pady=0)

    def step_1_combobox_callback_1(self, choise):
        self.data.step_1_procedure_1 = choise

    def step_1_combobox_callback_2(self, choise):
        self.data.step_1_procedure_2 = choise

    def step_1_combobox_callback_3(self, choise):
        self.data.step_1_procedure_3 = choise

    def step_1_combobox_callback_4(self, choise):
        self.data.step_1_procedure_4 = choise

    def step_1_combobox_callback_5(self, choise):
        self.data.step_1_procedure_5 = choise

    def step_1_procedures_count_1_callback(self, choise):
        self.data.step_1_procedures_count_1 = choise

    def step_1_procedures_count_2_callback(self, choise):
        self.data.step_1_procedures_count_2 = choise

    def step_1_procedures_count_3_callback(self, choise):
        self.data.step_1_procedures_count_3 = choise

    def step_1_procedures_count_4_callback(self, choise):
        self.data.step_1_procedures_count_4 = choise

    def step_1_procedures_count_5_callback(self, choise):
        self.data.step_1_procedures_count_5 = choise

    def step_1_period_1_callback(self, choise):
        self.data.step_1_procedure_period_1 = choise

    def step_1_period_2_callback(self, choise):
        self.data.step_1_procedure_period_1 = choise

    def step_1_period_3_callback(self, choise):
        self.data.step_1_procedure_period_2 = choise

    def step_1_period_4_callback(self, choise):
        self.data.step_1_procedure_period_3 = choise

    def step_1_period_5_callback(self, choise):
        self.data.step_1_procedure_period_4 = choise

    def step1_confirmation_button_callback(self):
        self.data.step_1_commentary = self.step_1_commentary.get("0.0", "end")

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

        self.step_1_procedures_count_1 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                             command=self.step_1_procedures_count_1_callback)
        self.step_1_procedures_count_1.grid(row=4, column=0, padx=20, pady=0)

        self.step_1_procedures_count_2 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_1_combobox_callback_5)
        self.step_1_procedures_count_2.grid(row=4, column=1, padx=20, pady=0)

        self.step_1_procedures_count_3 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_1_combobox_callback_5)
        self.step_1_procedures_count_3.grid(row=4, column=2, padx=20, pady=0)

        self.step_1_procedures_count_4 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_1_combobox_callback_5)
        self.step_1_procedures_count_4.grid(row=4, column=3, padx=20, pady=0)

        self.step_1_procedures_count_5 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_1_combobox_callback_5)
        self.step_1_procedures_count_5.grid(row=4, column=4, padx=20, pady=0)

        step_1_label_period = customtkinter.CTkLabel(master=self.app, text='Период')
        step_1_label_period.grid(row=5, column=0, padx=20, pady=0)

        self.step_1_period_1 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_period_1_callback)
        self.step_1_period_1.grid(row=6, column=0, padx=20, pady=0)

        self.step_1_period_2 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_period_2_callback)
        self.step_1_period_2.grid(row=6, column=1, padx=20, pady=0)

        self.step_1_period_3 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_period_3_callback)
        self.step_1_period_3.grid(row=6, column=2, padx=20, pady=0)

        self.step_1_period_4 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_period_4_callback)
        self.step_1_period_4.grid(row=6, column=3, padx=20, pady=0)

        self.step_1_period_5 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_1_period_5_callback)
        self.step_1_period_5.grid(row=6, column=4, padx=20, pady=0)

        step_1_label_period = customtkinter.CTkLabel(master=self.app, text='Комментарий')
        step_1_label_period.grid(row=7, column=0, padx=20, pady=0)
        self.step_1_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        self.step_1_commentary.grid(row=8, column=0, padx=20, pady=0)

        step1_confirmation_button = customtkinter.CTkButton(master=self.app, text='Принять!',
                                                            command=self.step1_confirmation_button_callback)
        step1_confirmation_button.grid(row=8, column=1, padx=20, pady=20)



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

    def step_2_procedures_count_1_callback(self, choise):
        self.data.step_1_procedures_count_1 = choise

    def step_2_procedures_count_2_callback(self, choise):
        self.data.step_1_procedures_count_2 = choise

    def step_2_procedures_count_3_callback(self, choise):
        self.data.step_1_procedures_count_3 = choise

    def step_2_procedures_count_4_callback(self, choise):
        self.data.step_1_procedures_count_4 = choise

    def step_2_procedures_count_5_callback(self, choise):
        self.data.step_1_procedures_count_5 = choise

    def step_2_period_1_callback(self, choise):
        self.data.step_1_procedure_period_1 = choise

    def step_2_period_2_callback(self, choise):
        self.data.step_1_procedure_period_1 = choise

    def step_2_period_3_callback(self, choise):
        self.data.step_1_procedure_period_2 = choise

    def step_2_period_4_callback(self, choise):
        self.data.step_1_procedure_period_3 = choise

    def step_2_period_5_callback(self, choise):
        self.data.step_1_procedure_period_4 = choise

    def step2_confirmation_button_callback(self):
        self.data.step_2_commentary = self.step_2_commentary.get("0.0", "end")

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

        self.step_2_procedures_1 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_2_combobox_callback_1)
        self.step_2_procedures_1.grid(row=4, column=5, padx=20, pady=0)

        self.step_2_procedures_2 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_2_combobox_callback_2)
        self.step_2_procedures_2.grid(row=4, column=6, padx=20, pady=0)

        self.step_2_procedures_3 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_2_combobox_callback_3)
        self.step_2_procedures_3.grid(row=4, column=7, padx=20, pady=0)

        self.step_2_procedures_4 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_2_combobox_callback_4)
        self.step_2_procedures_4.grid(row=4, column=8, padx=20, pady=0)

        self.step_2_procedures_5 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_2_combobox_callback_5)
        self.step_2_procedures_5.grid(row=4, column=9, padx=20, pady=0)

        step_2_label_period = customtkinter.CTkLabel(master=self.app, text='Период')
        step_2_label_period.grid(row=5, column=5, padx=20, pady=0)

        self.step_2_period_1 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_2_period_1_callback)
        self.step_2_period_1.grid(row=6, column=5, padx=20, pady=0)

        self.step_2_period_2 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_2_period_2_callback)
        self.step_2_period_2.grid(row=6, column=6, padx=20, pady=0)

        self.step_2_period_3 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_2_period_3_callback)
        self.step_2_period_3.grid(row=6, column=7, padx=20, pady=0)

        self.step_2_period_4 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_2_period_4_callback)
        self.step_2_period_4.grid(row=6, column=8, padx=20, pady=0)

        self.step_2_period_5 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_2_period_5_callback)
        self.step_2_period_5.grid(row=6, column=9, padx=20, pady=0)

        step_2_label_period = customtkinter.CTkLabel(master=self.app, text='Комментарий')
        step_2_label_period.grid(row=7, column=5, padx=20, pady=0)
        self.step_2_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        self.step_2_commentary.grid(row=8, column=5, padx=20, pady=0)

        step2_confirmation_button = customtkinter.CTkButton(master=self.app, text='Принять!',
                                                       command=self.personal_info_callback)
        step2_confirmation_button.grid(row=8, column=6, padx=20, pady=20)

    def step_3_combobox_callback_1(self, choise):
        print(choise)

    def step_3_combobox_callback_2(self, choise):
        print(choise)

    def step_3_combobox_callback_3(self, choise):
        print(choise)

    def step_3_combobox_callback_4(self, choise):
        print(choise)

    def step_3_combobox_callback_5(self, choise):
        print(choise)

    def step_3_procedures_count_1_callback(self, choise):
        self.data.step_3_procedures_count_1 = choise

    def step_3_procedures_count_2_callback(self, choise):
        self.data.step_3_procedures_count_2 = choise

    def step_3_procedures_count_3_callback(self, choise):
        self.data.step_3_procedures_count_3 = choise

    def step_3_procedures_count_4_callback(self, choise):
        self.data.step_3_procedures_count_4 = choise

    def step_3_procedures_count_5_callback(self, choise):
        self.data.step_3_procedures_count_5 = choise

    def step_3_period_1_callback(self, choise):
        self.data.step_3_procedure_period_1 = choise

    def step_3_period_2_callback(self, choise):
        self.data.step_3_procedure_period_1 = choise

    def step_3_period_3_callback(self, choise):
        self.data.step_3_procedure_period_2 = choise

    def step_3_period_4_callback(self, choise):
        self.data.step_3_procedure_period_3 = choise

    def step_3_period_5_callback(self, choise):
        self.data.step_3_procedure_period_4 = choise

    def step3_confirmation_button_callback(self):
        self.data.step_3_commentary = self.step_3_commentary.get("0.0", "end")

    def step_3(self):
        step_3_label = customtkinter.CTkLabel(master=self.app, text='Шаг 3: Поддержка и...')
        step_3_label.grid(row=9, column=0, padx=30, pady=(10, 0))

        step_3_combobox_1 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_combobox_callback_1)
        step_3_combobox_1.grid(row=10, column=0, padx=20, pady=0)

        step_3_combobox_2 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_combobox_callback_2)
        step_3_combobox_2.grid(row=10, column=1, padx=20, pady=0)

        step_3_combobox_3 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_combobox_callback_3)
        step_3_combobox_3.grid(row=10, column=2, padx=20, pady=0)

        step_3_combobox_4 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_combobox_callback_4)
        step_3_combobox_4.grid(row=10, column=3, padx=20, pady=0)

        step_3_combobox_5 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_combobox_callback_5)
        step_3_combobox_5.grid(row=10, column=4, padx=20, pady=0)

        step_3_label_procedures_count = customtkinter.CTkLabel(master=self.app, text='Кол-во процедур')
        step_3_label_procedures_count.grid(row=11, column=0, padx=20, pady=0)

        self.step_3_procedures_1 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_3_combobox_callback_1)
        self.step_3_procedures_1.grid(row=12, column=0, padx=20, pady=0)

        self.step_3_procedures_2 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_3_combobox_callback_2)
        self.step_3_procedures_2.grid(row=12, column=1, padx=20, pady=0)

        self.step_3_procedures_3 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_3_combobox_callback_3)
        self.step_3_procedures_3.grid(row=12, column=2, padx=20, pady=0)

        self.step_3_procedures_4 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_3_combobox_callback_4)
        self.step_3_procedures_4.grid(row=12, column=3, padx=20, pady=0)

        self.step_3_procedures_5 = customtkinter.CTkComboBox(self.app, values=[str(i) for i in range(1, 11)],
                                                                   command=self.step_3_combobox_callback_5)
        self.step_3_procedures_5.grid(row=12, column=4, padx=20, pady=0)

        step_3_label_period = customtkinter.CTkLabel(master=self.app, text='Период')
        step_3_label_period.grid(row=13, column=0, padx=20, pady=0)

        self.step_3_period_1 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_period_1_callback)
        self.step_3_period_1.grid(row=14, column=0, padx=20, pady=0)

        self.step_3_period_2 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_period_2_callback)
        self.step_3_period_2.grid(row=14, column=1, padx=20, pady=0)

        self.step_3_period_3 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_period_3_callback)
        self.step_3_period_3.grid(row=14, column=2, padx=20, pady=0)

        self.step_3_period_4 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_period_4_callback)
        self.step_3_period_4.grid(row=14, column=3, padx=20, pady=0)

        self.step_3_period_5 = customtkinter.CTkComboBox(self.app, values=["option 1", "option 2"],
                                             command=self.step_3_period_5_callback)
        self.step_3_period_5.grid(row=14, column=4, padx=20, pady=0)

        step_3_label_period = customtkinter.CTkLabel(master=self.app, text='Комментарий')
        step_3_label_period.grid(row=15, column=0, padx=20, pady=0)
        self.step_3_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        self.step_3_commentary.grid(row=16, column=0, padx=20, pady=0)

        step3_confirmation_button = customtkinter.CTkButton(master=self.app, text='Принять!',
                                                       command=self.personal_info_callback)
        step3_confirmation_button.grid(row=16, column=1, padx=20, pady=20)

    def step4_confirmation_button_callback(self):
        self.data.step_4_commentary = self.step_4_commentary.get("0.0", "end")

    def step_4(self):
        step_4_label_period = customtkinter.CTkLabel(master=self.app, text='Для улучшения эффекта...')
        step_4_label_period.grid(row=15, column=5, padx=20, pady=0)
        self.step_4_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        self.step_4_commentary.grid(row=16, column=5, padx=20, pady=0)
        step4_confirmation_button = customtkinter.CTkButton(master=self.app, text='Принять!',
                                                       command=self.step4_confirmation_button_callback)
        step4_confirmation_button.grid(row=16, column=6, padx=20, pady=20)

    def save_document_callback(self):
        save_path_name = asksaveasfilename(initialfile='Untitled.pdf', defaultextension=".pdf",
                                           filetypes=[("All Files", "*.*"), ("PDF documents", "*.pdf")])

    def save_document(self):
        step4_confirmation_button = customtkinter.CTkButton(master=self.app, text='Сохранить PDF файл',
                                                       command=self.save_document_callback)
        step4_confirmation_button.grid(row=17, column=8, padx=20, pady=20)

    def print_document_callback(self):
        pass

    def print_document(self):
        step4_confirmation_button = customtkinter.CTkButton(master=self.app, text='Распечатать',
                                                       command=self.print_document_callback)
        step4_confirmation_button.grid(row=17, column=9, padx=20, pady=20)
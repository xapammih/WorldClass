import customtkinter
import datetime
from tkinter.filedialog import asksaveasfilename
import pandas as pd


class Data:
    """
    Датакласс, собирающий значения со всего активного окна
    """

    def __init__(self):
        self.fio = ''
        self.phone = ''
        self.doctor = ''
        self.wanted_result = ''
        self.current_date = ''
        self.current_time = ''

        self.step_1_procedure_1 = ''
        self.step_1_procedure_2 = ''
        self.step_1_procedure_3 = ''
        self.step_1_procedure_4 = ''
        self.step_1_procedure_5 = ''
        self.step_1_count_procedures_1 = ''
        self.step_1_count_procedures_2 = ''
        self.step_1_count_procedures_3 = ''
        self.step_1_count_procedures_4 = ''
        self.step_1_count_procedures_5 = ''
        self.step_1_procedure_period_1 = ''
        self.step_1_procedure_period_2 = ''
        self.step_1_procedure_period_3 = ''
        self.step_1_procedure_period_4 = ''
        self.step_1_procedure_period_5 = ''
        self.step_1_commentary = ''

        self.step_2_procedure_1 = ''
        self.step_2_procedure_2 = ''
        self.step_2_procedure_3 = ''
        self.step_2_procedure_4 = ''
        self.step_2_procedure_5 = ''
        self.step_2_count_procedures_1 = ''
        self.step_2_count_procedures_2 = ''
        self.step_2_count_procedures_3 = ''
        self.step_2_count_procedures_4 = ''
        self.step_2_count_procedures_5 = ''
        self.step_2_procedure_period_1 = ''
        self.step_2_procedure_period_2 = ''
        self.step_2_procedure_period_3 = ''
        self.step_2_procedure_period_4 = ''
        self.step_2_procedure_period_5 = ''
        self.step_2_commentary = ''

        self.step_3_procedure_1 = ''
        self.step_3_procedure_2 = ''
        self.step_3_procedure_3 = ''
        self.step_3_procedure_4 = ''
        self.step_3_procedure_5 = ''
        self.step_3_count_procedures_1 = ''
        self.step_3_count_procedures_2 = ''
        self.step_3_count_procedures_3 = ''
        self.step_3_count_procedures_4 = ''
        self.step_3_count_procedures_5 = ''
        self.step_3_procedure_period_1 = ''
        self.step_3_procedure_period_2 = ''
        self.step_3_procedure_period_3 = ''
        self.step_3_procedure_period_4 = ''
        self.step_3_procedure_period_5 = ''
        self.step_3_commentary = ''

        self.step_4_commentary = ''

    def get_init_attributes(self):
        return list(vars(self).values())


class MainWindow:
    """
    Класс для отрисовки главного окна, заполняет датакласс Data значениями
    """

    def __init__(self, data):
        self.app = customtkinter.CTk()
        self.app.title('World Class')
        self.app.grid_columnconfigure(0, weight=1)
        self.data = data
        self.df = pd.read_excel('log.xlsx')
        self.fio_entry = None
        self.phone_entry = None
        self.wanted_result_entry = None

        self.step_1_combobox_1 = None
        self.step_1_combobox_2 = None
        self.step_1_combobox_3 = None
        self.step_1_combobox_4 = None
        self.step_1_combobox_5 = None
        self.step_1_count_procedures_1 = None
        self.step_1_count_procedures_2 = None
        self.step_1_count_procedures_3 = None
        self.step_1_count_procedures_4 = None
        self.step_1_count_procedures_5 = None
        self.step_1_period_1 = None
        self.step_1_period_2 = None
        self.step_1_period_3 = None
        self.step_1_period_4 = None
        self.step_1_period_5 = None

        self.step_2_combobox_1 = None
        self.step_2_combobox_2 = None
        self.step_2_combobox_3 = None
        self.step_2_combobox_4 = None
        self.step_2_combobox_5 = None
        self.step_2_count_procedures_1 = None
        self.step_2_count_procedures_2 = None
        self.step_2_count_procedures_3 = None
        self.step_2_count_procedures_4 = None
        self.step_2_count_procedures_5 = None
        self.step_2_period_1 = None
        self.step_2_period_2 = None
        self.step_2_period_3 = None
        self.step_2_period_4 = None
        self.step_2_period_5 = None

        self.step_3_combobox_1 = None
        self.step_3_combobox_2 = None
        self.step_3_combobox_3 = None
        self.step_3_combobox_4 = None
        self.step_3_combobox_5 = None
        self.step_3_count_procedures_1 = None
        self.step_3_count_procedures_2 = None
        self.step_3_count_procedures_3 = None
        self.step_3_count_procedures_4 = None
        self.step_3_count_procedures_5 = None
        self.step_3_period_1 = None
        self.step_3_period_2 = None
        self.step_3_period_3 = None
        self.step_3_period_4 = None
        self.step_3_period_5 = None

        self.step_1_commentary = None
        self.step_2_commentary = None
        self.step_3_commentary = None
        self.step_4_commentary = None

        #получаем все значения для выпадающих полей из текстовых файлов, генерирующихся в админке
        with open('Administration/procedures.txt', 'r') as procedures_file:
            self.procedures_list = [i for i in procedures_file.readlines()]
            self.procedures_list.insert(0, '')

        self.procedure_count_lst = [str(i) for i in range(1, 21)]
        self.procedure_count_lst.insert(0, '')

        with open('Administration/periods.txt', 'r') as periods_file:
            self.periods_list = [i for i in periods_file.readlines()]
            self.periods_list.insert(0, '')

    def personal_info(self):
        """
        Получаем данные про ФИО пациента и телефон
        :return:
        """
        self.fio_entry = customtkinter.CTkEntry(master=self.app, placeholder_text="ФИО...")
        self.fio_entry.grid(row=0, column=0, padx=20, pady=20, columnspan=3, sticky="nsew")

        self.phone_entry = customtkinter.CTkEntry(master=self.app, placeholder_text="Телефон...")
        self.phone_entry.grid(row=0, column=3, padx=20, pady=20)

    def doctor_combobox_callback(self, choise: str) -> None:
        self.data.doctor = choise

    def doctor_info(self):
        """
        Получаем данные о докторе
        :return:
        """
        with open('Administration/doctors.txt', 'r') as doctors_file:
            doctors = [i for i in doctors_file.readlines()]
        self.data.doctor = doctors[0]
        step_1_label = customtkinter.CTkLabel(master=self.app, text='Выберите специалиста: ')
        step_1_label.grid(row=0, column=5, padx=30, pady=20)
        doctor_combobox = customtkinter.CTkComboBox(self.app, values=doctors,
                                                    command=self.doctor_combobox_callback)
        doctor_combobox.grid(row=0, column=6, padx=20, pady=0)

    def wanted_result(self):
        """
        Получаем данные о желаемом результате
        :return:
        """
        self.wanted_result_entry = customtkinter.CTkEntry(master=self.app, width=350,
                                                          placeholder_text="Желаемый результат: ")
        self.wanted_result_entry.grid(row=0, column=7, padx=20, pady=20, columnspan=3, sticky="nsew")

    #колбэки для шага 1
    def step_1_combobox_callback_1(self, choise: str) -> None:
        self.data.step_1_procedure_1 = choise

    def step_1_combobox_callback_2(self, choise: str) -> None:
        self.data.step_1_procedure_2 = choise

    def step_1_combobox_callback_3(self, choise: str) -> None:
        self.data.step_1_procedure_3 = choise

    def step_1_combobox_callback_4(self, choise: str) -> None:
        self.data.step_1_procedure_4 = choise

    def step_1_combobox_callback_5(self, choise: str) -> None:
        self.data.step_1_procedure_5 = choise

    def step_1_count_procedures_1_callback(self, choise: str) -> None:
        self.data.step_1_count_procedures_1 = choise

    def step_1_count_procedures_2_callback(self, choise: str) -> None:
        self.data.step_1_count_procedures_2 = choise

    def step_1_count_procedures_3_callback(self, choise: str) -> None:
        self.data.step_1_count_procedures_3 = choise

    def step_1_count_procedures_4_callback(self, choise: str) -> None:
        self.data.step_1_count_procedures_4 = choise

    def step_1_count_procedures_5_callback(self, choise: str) -> None:
        self.data.step_1_count_procedures_5 = choise

    def step_1_period_1_callback(self, choise: str) -> None:
        self.data.step_1_procedure_period_1 = choise

    def step_1_period_2_callback(self, choise: str) -> None:
        self.data.step_1_procedure_period_2 = choise

    def step_1_period_3_callback(self, choise: str) -> None:
        self.data.step_1_procedure_period_3 = choise

    def step_1_period_4_callback(self, choise: str) -> None:
        self.data.step_1_procedure_period_4 = choise

    def step_1_period_5_callback(self, choise: str) -> None:
        self.data.step_1_procedure_period_5 = choise

    def step_1(self) -> None:
        """
        Собираем данные для шага 1(процедуры, кол-во процедур, период)
        :return:
        """
        step_1_label = customtkinter.CTkLabel(master=self.app, text='Шаг 1: ТОП решения...')
        step_1_label.grid(row=1, column=0, padx=30, pady=(10, 0))

        self.step_1_combobox_1 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_1_combobox_callback_1)
        self.step_1_combobox_1.grid(row=2, column=0, padx=20, pady=0)

        self.step_1_combobox_2 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_1_combobox_callback_2)
        self.step_1_combobox_2.grid(row=2, column=1, padx=20, pady=0)

        self.step_1_combobox_3 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_1_combobox_callback_3)
        self.step_1_combobox_3.grid(row=2, column=2, padx=20, pady=0)

        self.step_1_combobox_4 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_1_combobox_callback_4)
        self.step_1_combobox_4.grid(row=2, column=3, padx=20, pady=0)

        self.step_1_combobox_5 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_1_combobox_callback_5)
        self.step_1_combobox_5.grid(row=2, column=4, padx=20, pady=0)

        step_1_label_procedures_count = customtkinter.CTkLabel(master=self.app, text='Кол-во процедур')
        step_1_label_procedures_count.grid(row=3, column=0, padx=20, pady=0)

        self.step_1_count_procedures_1 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_1_count_procedures_1_callback)
        self.step_1_count_procedures_1.grid(row=4, column=0, padx=20, pady=0)

        self.step_1_count_procedures_2 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_1_count_procedures_2_callback)
        self.step_1_count_procedures_2.grid(row=4, column=1, padx=20, pady=0)

        self.step_1_count_procedures_3 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_1_count_procedures_3_callback)
        self.step_1_count_procedures_3.grid(row=4, column=2, padx=20, pady=0)

        self.step_1_count_procedures_4 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_1_count_procedures_4_callback)
        self.step_1_count_procedures_4.grid(row=4, column=3, padx=20, pady=0)

        self.step_1_count_procedures_5 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_1_count_procedures_5_callback)
        self.step_1_count_procedures_5.grid(row=4, column=4, padx=20, pady=0)

        step_1_label_period = customtkinter.CTkLabel(master=self.app, text='Период')
        step_1_label_period.grid(row=5, column=0, padx=20, pady=0)

        self.step_1_period_1 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_1_period_1_callback)
        self.step_1_period_1.grid(row=6, column=0, padx=20, pady=0)

        self.step_1_period_2 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_1_period_2_callback)
        self.step_1_period_2.grid(row=6, column=1, padx=20, pady=0)

        self.step_1_period_3 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_1_period_3_callback)
        self.step_1_period_3.grid(row=6, column=2, padx=20, pady=0)

        self.step_1_period_4 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_1_period_4_callback)
        self.step_1_period_4.grid(row=6, column=3, padx=20, pady=0)

        self.step_1_period_5 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_1_period_5_callback)
        self.step_1_period_5.grid(row=6, column=4, padx=20, pady=0)

        step_1_label_period = customtkinter.CTkLabel(master=self.app, text='Комментарий')
        step_1_label_period.grid(row=7, column=0, padx=20, pady=0)

        self.step_1_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        self.step_1_commentary.grid(row=8, column=0, padx=20, pady=0)

    #колбэки для шага 2
    def step_2_combobox_callback_1(self, choise: str) -> None:
        self.data.step_2_procedure_1 = choise

    def step_2_combobox_callback_2(self, choise: str) -> None:
        self.data.step_2_procedure_2 = choise

    def step_2_combobox_callback_3(self, choise: str) -> None:
        self.data.step_2_procedure_3 = choise

    def step_2_combobox_callback_4(self, choise: str) -> None:
        self.data.step_2_procedure_4 = choise

    def step_2_combobox_callback_5(self, choise: str) -> None:
        self.data.step_2_procedure_5 = choise

    def step_2_count_procedures_1_callback(self, choise: str) -> None:
        self.data.step_2_count_procedures_1 = choise

    def step_2_count_procedures_2_callback(self, choise: str) -> None:
        self.data.step_2_count_procedures_2 = choise

    def step_2_count_procedures_3_callback(self, choise: str) -> None:
        self.data.step_2_count_procedures_3 = choise

    def step_2_count_procedures_4_callback(self, choise: str) -> None:
        self.data.step_2_count_procedures_4 = choise

    def step_2_count_procedures_5_callback(self, choise: str) -> None:
        self.data.step_2_count_procedures_5 = choise

    def step_2_period_1_callback(self, choise: str) -> None:
        self.data.step_2_procedure_period_1 = choise

    def step_2_period_2_callback(self, choise: str) -> None:
        self.data.step_2_procedure_period_2 = choise

    def step_2_period_3_callback(self, choise: str) -> None:
        self.data.step_2_procedure_period_3 = choise

    def step_2_period_4_callback(self, choise: str) -> None:
        self.data.step_2_procedure_period_4 = choise

    def step_2_period_5_callback(self, choise: str) -> None:
        self.data.step_2_procedure_period_5 = choise

    def step_2(self) -> None:
        """
        Собираем данные для шага 2(процедуры, кол-во процедур, период)
        :return:
        """
        step_2_label = customtkinter.CTkLabel(master=self.app, text='Шаг 2: Улучшение и закрепление')
        step_2_label.grid(row=1, column=5, padx=20, pady=0)

        self.step_2_combobox_1 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_2_combobox_callback_1)
        self.step_2_combobox_1.grid(row=2, column=5, padx=20, pady=0)

        self.step_2_combobox_2 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_2_combobox_callback_2)
        self.step_2_combobox_2.grid(row=2, column=6, padx=20, pady=0)

        self.step_2_combobox_3 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_2_combobox_callback_3)
        self.step_2_combobox_3.grid(row=2, column=7, padx=20, pady=0)

        self.step_2_combobox_4 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_2_combobox_callback_4)
        self.step_2_combobox_4.grid(row=2, column=8, padx=20, pady=0)

        self.step_2_combobox_5 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_2_combobox_callback_5)
        self.step_2_combobox_5.grid(row=2, column=9, padx=20, pady=0)

        step_2_label_procedures_count = customtkinter.CTkLabel(master=self.app, text='Кол-во процедур')
        step_2_label_procedures_count.grid(row=3, column=5, padx=20, pady=0)

        self.step_2_count_procedures_1 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_2_count_procedures_1_callback)
        self.step_2_count_procedures_1.grid(row=4, column=5, padx=20, pady=0)

        self.step_2_count_procedures_2 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_2_count_procedures_2_callback)
        self.step_2_count_procedures_2.grid(row=4, column=6, padx=20, pady=0)

        self.step_2_count_procedures_3 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_2_count_procedures_3_callback)
        self.step_2_count_procedures_3.grid(row=4, column=7, padx=20, pady=0)

        self.step_2_count_procedures_4 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_2_count_procedures_4_callback)
        self.step_2_count_procedures_4.grid(row=4, column=8, padx=20, pady=0)

        self.step_2_count_procedures_5 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_2_count_procedures_5_callback)
        self.step_2_count_procedures_5.grid(row=4, column=9, padx=20, pady=0)

        step_2_label_period = customtkinter.CTkLabel(master=self.app, text='Период')
        step_2_label_period.grid(row=5, column=5, padx=20, pady=0)

        self.step_2_period_1 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_2_period_1_callback)
        self.step_2_period_1.grid(row=6, column=5, padx=20, pady=0)

        self.step_2_period_2 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_2_period_2_callback)
        self.step_2_period_2.grid(row=6, column=6, padx=20, pady=0)

        self.step_2_period_3 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_2_period_3_callback)
        self.step_2_period_3.grid(row=6, column=7, padx=20, pady=0)

        self.step_2_period_4 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_2_period_4_callback)
        self.step_2_period_4.grid(row=6, column=8, padx=20, pady=0)

        self.step_2_period_5 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_2_period_5_callback)
        self.step_2_period_5.grid(row=6, column=9, padx=20, pady=0)

        step_2_label_period = customtkinter.CTkLabel(master=self.app, text='Комментарий')
        step_2_label_period.grid(row=7, column=5, padx=20, pady=0)
        self.step_2_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        self.step_2_commentary.grid(row=8, column=5, padx=20, pady=0)

    #колбэки для шага 3
    def step_3_combobox_callback_1(self, choise: str) -> None:
        self.data.step_3_procedure_1 = choise

    def step_3_combobox_callback_2(self, choise: str) -> None:
        self.data.step_3_procedure_2 = choise

    def step_3_combobox_callback_3(self, choise: str) -> None:
        self.data.step_3_procedure_3 = choise

    def step_3_combobox_callback_4(self, choise: str) -> None:
        self.data.step_3_procedure_4 = choise

    def step_3_combobox_callback_5(self, choise: str) -> None:
        self.data.step_3_procedure_5 = choise

    def step_3_count_procedures_1_callback(self, choise: str) -> None:
        self.data.step_3_count_procedures_1 = choise

    def step_3_count_procedures_2_callback(self, choise: str) -> None:
        self.data.step_3_count_procedures_2 = choise

    def step_3_count_procedures_3_callback(self, choise: str) -> None:
        self.data.step_3_count_procedures_3 = choise

    def step_3_count_procedures_4_callback(self, choise: str) -> None:
        self.data.step_3_count_procedures_4 = choise

    def step_3_count_procedures_5_callback(self, choise: str) -> None:
        self.data.step_3_count_procedures_5 = choise

    def step_3_period_1_callback(self, choise: str) -> None:
        self.data.step_3_procedure_period_1 = choise

    def step_3_period_2_callback(self, choise: str) -> None:
        self.data.step_3_procedure_period_2 = choise

    def step_3_period_3_callback(self, choise: str) -> None:
        self.data.step_3_procedure_period_3 = choise

    def step_3_period_4_callback(self, choise: str) -> None:
        self.data.step_3_procedure_period_4 = choise

    def step_3_period_5_callback(self, choise: str) -> None:
        self.data.step_3_procedure_period_5 = choise

    def step_3(self) -> None:
        """
        Собираем данные для шага 3(процедуры, кол-во процедур, период)
        :return:
        """
        step_3_label = customtkinter.CTkLabel(master=self.app, text='Шаг 3: Поддержка и...')
        step_3_label.grid(row=9, column=0, padx=30, pady=(10, 0))

        self.step_3_combobox_1 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_3_combobox_callback_1)
        self.step_3_combobox_1.grid(row=10, column=0, padx=20, pady=0)

        self.step_3_combobox_2 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_3_combobox_callback_2)
        self.step_3_combobox_2.grid(row=10, column=1, padx=20, pady=0)

        self.step_3_combobox_3 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_3_combobox_callback_3)
        self.step_3_combobox_3.grid(row=10, column=2, padx=20, pady=0)

        self.step_3_combobox_4 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_3_combobox_callback_4)
        self.step_3_combobox_4.grid(row=10, column=3, padx=20, pady=0)

        self.step_3_combobox_5 = customtkinter.CTkComboBox(self.app, values=self.procedures_list,
                                                           command=self.step_3_combobox_callback_5)
        self.step_3_combobox_5.grid(row=10, column=4, padx=20, pady=0)

        step_3_label_procedures_count = customtkinter.CTkLabel(master=self.app, text='Кол-во процедур')
        step_3_label_procedures_count.grid(row=11, column=0, padx=20, pady=0)

        self.step_3_count_procedures_1 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_3_count_procedures_1_callback)
        self.step_3_count_procedures_1.grid(row=12, column=0, padx=20, pady=0)

        self.step_3_count_procedures_2 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_3_count_procedures_2_callback)
        self.step_3_count_procedures_2.grid(row=12, column=1, padx=20, pady=0)

        self.step_3_count_procedures_3 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_3_count_procedures_3_callback)
        self.step_3_count_procedures_3.grid(row=12, column=2, padx=20, pady=0)

        self.step_3_count_procedures_4 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_3_count_procedures_4_callback)
        self.step_3_count_procedures_4.grid(row=12, column=3, padx=20, pady=0)

        self.step_3_count_procedures_5 = customtkinter.CTkComboBox(self.app, values=self.procedure_count_lst,
                                                                   command=self.step_3_count_procedures_5_callback)
        self.step_3_count_procedures_5.grid(row=12, column=4, padx=20, pady=0)

        step_3_label_period = customtkinter.CTkLabel(master=self.app, text='Период')
        step_3_label_period.grid(row=13, column=0, padx=20, pady=0)

        self.step_3_period_1 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_3_period_1_callback)
        self.step_3_period_1.grid(row=14, column=0, padx=20, pady=0)

        self.step_3_period_2 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_3_period_2_callback)
        self.step_3_period_2.grid(row=14, column=1, padx=20, pady=0)

        self.step_3_period_3 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_3_period_3_callback)
        self.step_3_period_3.grid(row=14, column=2, padx=20, pady=0)

        self.step_3_period_4 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_3_period_4_callback)
        self.step_3_period_4.grid(row=14, column=3, padx=20, pady=0)

        self.step_3_period_5 = customtkinter.CTkComboBox(self.app, values=self.periods_list,
                                                         command=self.step_3_period_5_callback)
        self.step_3_period_5.grid(row=14, column=4, padx=20, pady=0)

        step_3_label_period = customtkinter.CTkLabel(master=self.app, text='Комментарий')
        step_3_label_period.grid(row=15, column=0, padx=20, pady=0)
        self.step_3_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        self.step_3_commentary.grid(row=16, column=0, padx=20, pady=0)

    def step_4(self) -> None:
        """
        Собираем данные для шага 4(улучшение эффекта)
        :return:
        """
        step_4_label_period = customtkinter.CTkLabel(master=self.app, text='Для улучшения эффекта...')
        step_4_label_period.grid(row=15, column=5, padx=20, pady=0)
        self.step_4_commentary = customtkinter.CTkTextbox(master=self.app, corner_radius=10)
        self.step_4_commentary.grid(row=16, column=5, padx=20, pady=0)

    def save_document_callback(self) -> None:
        """
        Колбэк для кнопки сохранения документа, также получает значения с текстовых полей и логгирует в xlsx файл
        :return:
        """
        self.data.fio = self.fio_entry.get()
        self.data.phone = self.phone_entry.get()
        self.data.wanted_result = self.wanted_result_entry.get()
        self.data.step_1_commentary = self.step_1_commentary.get("0.0", "end")
        self.data.step_2_commentary = self.step_2_commentary.get("0.0", "end")
        self.data.step_3_commentary = self.step_3_commentary.get("0.0", "end")
        self.data.step_4_commentary = self.step_4_commentary.get("0.0", "end")
        self.data.current_date = datetime.date.today().strftime('%d-%m-%Y')
        self.data.current_time = datetime.datetime.now().strftime("%H:%M")
        self.df.drop_duplicates(inplace=True)
        self.logging()
        save_path_name = asksaveasfilename(initialfile=f'{self.data.fio}.pdf', defaultextension=".pdf",
                                           filetypes=[("All Files", "*.*"), ("PDF documents", "*.pdf")])

    def save_document(self) -> None:
        step4_confirmation_button = customtkinter.CTkButton(master=self.app, text='Сохранить PDF файл',
                                                            command=self.save_document_callback)
        step4_confirmation_button.grid(row=17, column=8, padx=20, pady=20)

    def print_document_callback(self) -> None:
        """
        Колбэк для кнопки печати документа, также получает значения с текстовых полей и логгирует в xlsx файл
        :return:
        """
        self.data.fio = self.fio_entry.get()
        self.data.phone = self.phone_entry.get()
        self.data.wanted_result = self.wanted_result_entry.get()
        self.data.step_1_commentary = self.step_1_commentary.get("0.0", "end")
        self.data.step_2_commentary = self.step_2_commentary.get("0.0", "end")
        self.data.step_3_commentary = self.step_3_commentary.get("0.0", "end")
        self.data.step_4_commentary = self.step_4_commentary.get("0.0", "end")
        self.data.current_date = datetime.date.today().strftime('%d-%m-%Y')
        self.data.current_time = datetime.datetime.now().strftime("%H:%M")
        self.df.drop_duplicates(inplace=True)
        self.logging()

    def print_document(self) -> None:
        step4_confirmation_button = customtkinter.CTkButton(master=self.app, text='Распечатать',
                                                            command=self.print_document_callback)
        step4_confirmation_button.grid(row=17, column=9, padx=20, pady=20)

    def clear_all_callback(self) -> None:
        """
        Колбэк кнопки очистки формы, также сбрасывает значения всех атрибутов датакласса
        :return:
        """
        self.data.phone = ''
        self.data.fio = ''
        self.data.doctor = ''
        self.data.wanted_result = ''
        self.data.current_date = ''
        self.data.current_time = ''
        self.data.step_1_procedure_1 = ''
        self.data.step_1_procedure_2 = ''
        self.data.step_1_procedure_3 = ''
        self.data.step_1_procedure_4 = ''
        self.data.step_1_procedure_5 = ''
        self.data.step_1_count_procedures_1 = ''
        self.data.step_1_count_procedures_2 = ''
        self.data.step_1_count_procedures_3 = ''
        self.data.step_1_count_procedures_4 = ''
        self.data.step_1_count_procedures_5 = ''
        self.data.step_1_procedure_period_1 = ''
        self.data.step_1_procedure_period_2 = ''
        self.data.step_1_procedure_period_3 = ''
        self.data.step_1_procedure_period_4 = ''
        self.data.step_1_procedure_period_5 = ''
        self.data.step_1_commentary = ''

        self.data.step_2_procedure_1 = ''
        self.data.step_2_procedure_2 = ''
        self.data.step_2_procedure_3 = ''
        self.data.step_2_procedure_4 = ''
        self.data.step_2_procedure_5 = ''
        self.data.step_2_count_procedures_1 = ''
        self.data.step_2_count_procedures_2 = ''
        self.data.step_2_count_procedures_3 = ''
        self.data.step_2_count_procedures_4 = ''
        self.data.step_2_count_procedures_5 = ''
        self.data.step_2_procedure_period_1 = ''
        self.data.step_2_procedure_period_2 = ''
        self.data.step_2_procedure_period_3 = ''
        self.data.step_2_procedure_period_4 = ''
        self.data.step_2_procedure_period_5 = ''
        self.data.step_2_commentary = ''

        self.data.step_3_procedure_1 = ''
        self.data.step_3_procedure_2 = ''
        self.data.step_3_procedure_3 = ''
        self.data.step_3_procedure_4 = ''
        self.data.step_3_procedure_5 = ''
        self.data.step_3_count_procedures_1 = ''
        self.data.step_3_count_procedures_2 = ''
        self.data.step_3_count_procedures_3 = ''
        self.data.step_3_count_procedures_4 = ''
        self.data.step_3_count_procedures_5 = ''
        self.data.step_3_procedure_period_1 = ''
        self.data.step_3_procedure_period_2 = ''
        self.data.step_3_procedure_period_3 = ''
        self.data.step_3_procedure_period_4 = ''
        self.data.step_3_procedure_period_5 = ''
        self.data.step_3_commentary = ''
        self.fio_entry.delete('0', customtkinter.END)
        self.phone_entry.delete('0', customtkinter.END)
        self.wanted_result_entry.delete('0', customtkinter.END)

        self.step_1_combobox_1.set(self.procedures_list[0])
        self.step_1_combobox_2.set(self.procedures_list[0])
        self.step_1_combobox_3.set(self.procedures_list[0])
        self.step_1_combobox_4.set(self.procedures_list[0])
        self.step_1_combobox_5.set(self.procedures_list[0])
        self.step_1_count_procedures_1.set(1)
        self.step_1_count_procedures_2.set(1)
        self.step_1_count_procedures_3.set(1)
        self.step_1_count_procedures_4.set(1)
        self.step_1_count_procedures_5.set(1)
        self.step_1_period_1.set(self.periods_list[0])
        self.step_1_period_2.set(self.periods_list[0])
        self.step_1_period_3.set(self.periods_list[0])
        self.step_1_period_4.set(self.periods_list[0])
        self.step_1_period_5.set(self.periods_list[0])
        self.step_1_commentary.delete('0.0', customtkinter.END)

        self.step_2_combobox_1.set(self.procedures_list[0])
        self.step_2_combobox_2.set(self.procedures_list[0])
        self.step_2_combobox_3.set(self.procedures_list[0])
        self.step_2_combobox_4.set(self.procedures_list[0])
        self.step_2_combobox_5.set(self.procedures_list[0])
        self.step_2_count_procedures_1.set(1)
        self.step_2_count_procedures_2.set(1)
        self.step_2_count_procedures_3.set(1)
        self.step_2_count_procedures_4.set(1)
        self.step_2_count_procedures_5.set(1)
        self.step_2_period_1.set(self.periods_list[0])
        self.step_2_period_2.set(self.periods_list[0])
        self.step_2_period_3.set(self.periods_list[0])
        self.step_2_period_4.set(self.periods_list[0])
        self.step_2_period_5.set(self.periods_list[0])
        self.step_2_commentary.delete('0.0', customtkinter.END)

        self.step_3_combobox_1.set(self.procedures_list[0])
        self.step_3_combobox_2.set(self.procedures_list[0])
        self.step_3_combobox_3.set(self.procedures_list[0])
        self.step_3_combobox_4.set(self.procedures_list[0])
        self.step_3_combobox_5.set(self.procedures_list[0])
        self.step_3_count_procedures_1.set(1)
        self.step_3_count_procedures_2.set(1)
        self.step_3_count_procedures_3.set(1)
        self.step_3_count_procedures_4.set(1)
        self.step_3_count_procedures_5.set(1)
        self.step_3_period_1.set(self.periods_list[0])
        self.step_3_period_2.set(self.periods_list[0])
        self.step_3_period_3.set(self.periods_list[0])
        self.step_3_period_4.set(self.periods_list[0])
        self.step_3_period_5.set(self.periods_list[0])
        self.step_3_commentary.delete('0.0', customtkinter.END)

        self.step_4_commentary.delete('0.0', customtkinter.END)

    def clear_all(self) -> None:
        clear_all_button = customtkinter.CTkButton(master=self.app, text='Очистить все',
                                                   command=self.clear_all_callback)
        clear_all_button.grid(row=16, column=9, padx=20, pady=20)

    def insert_logo(self) -> None:
        pass

    def logging(self) -> None:
        """
        Функция логгер, добавляет в датафрейм строку в конец со всеми данными датакласса и записывает в xlsx
        :return:
        """
        cur_data = self.data.get_init_attributes()
        print(cur_data)
        self.df.loc[len(self.df.index)] = cur_data
        self.df.to_excel('log.xlsx', index=False)


data = Data()
app_window = MainWindow(data)

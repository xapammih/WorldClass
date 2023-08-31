from blank_manager import BlankManager
from printer import LazyPrinter
from pdf_generator import PdfGenerator


class Data:
    """
    Датакласс, собирающий значения со всего активного окна
    """

    def __init__(self):
        self.fio = 'Антонов Александр Владимирович'
        self.phone = '89999999999'
        self.doctor = 'Корнеплод Виктор Евгениевич'
        self.wanted_result = 'Что хочу того уже нет. ~Джейсон Стетхем'
        self.current_date = '20-08-2023'
        self.current_time = '12:15'

        self.step_1_procedure_1 = 'процедура 1'
        self.step_1_procedure_2 = 'процедура 2'
        self.step_1_procedure_3 = 'процедура 3'
        self.step_1_procedure_4 = 'процедура 4'
        self.step_1_procedure_5 = 'процедура 5'
        self.step_1_procedure_6 = 'процедура 6'
        self.step_1_procedure_7 = 'процедура 7'
        self.step_1_procedure_8 = 'процедура 8'
        self.step_1_procedure_9 = 'процедура 9'
        self.step_1_count_procedures_1 = '1'
        self.step_1_count_procedures_2 = '2'
        self.step_1_count_procedures_3 = '3'
        self.step_1_count_procedures_4 = '4'
        self.step_1_count_procedures_5 = '5'
        self.step_1_count_procedures_6 = '6'
        self.step_1_count_procedures_7 = '7'
        self.step_1_count_procedures_8 = '8'
        self.step_1_count_procedures_9 = '9'
        self.step_1_procedure_period_1 = '1'
        self.step_1_procedure_period_2 = '2'
        self.step_1_procedure_period_3 = '3'
        self.step_1_procedure_period_4 = '4'
        self.step_1_procedure_period_5 = '5'
        self.step_1_procedure_period_6 = '6'
        self.step_1_procedure_period_7 = '7'
        self.step_1_procedure_period_8 = '8'
        self.step_1_procedure_period_9 = '9'
        self.step_1_commentary = 'Комментарии нужны только если не совсем понятно как проводить те или иные шаги.'

        self.step_2_procedure_1 = 'процедура 1'
        self.step_2_procedure_2 = 'процедура 2'
        self.step_2_procedure_3 = 'процедура 3'
        self.step_2_procedure_4 = 'процедура 4'
        self.step_2_procedure_5 = 'процедура 5'
        self.step_2_procedure_6 = 'процедура 6'
        self.step_2_procedure_7 = 'процедура 7'
        self.step_2_procedure_8 = 'процедура 8'
        self.step_2_procedure_9 = 'процедура 9'
        self.step_2_count_procedures_1 = '1'
        self.step_2_count_procedures_2 = '2'
        self.step_2_count_procedures_3 = '3'
        self.step_2_count_procedures_4 = '4'
        self.step_2_count_procedures_5 = '5'
        self.step_2_count_procedures_6 = '6'
        self.step_2_count_procedures_7 = '7'
        self.step_2_count_procedures_8 = '8'
        self.step_2_count_procedures_9 = '9'
        self.step_2_procedure_period_1 = '1'
        self.step_2_procedure_period_2 = '2'
        self.step_2_procedure_period_3 = '3'
        self.step_2_procedure_period_4 = '4'
        self.step_2_procedure_period_5 = '5'
        self.step_2_procedure_period_6 = '6'
        self.step_2_procedure_period_7 = '7'
        self.step_2_procedure_period_8 = '8'
        self.step_2_procedure_period_9 = '9'
        self.step_2_commentary = 'А если всё ясно, то их можно не оставлять.'

        self.step_3_procedure_1 = 'процедура 1'
        self.step_3_procedure_2 = 'процедура 2'
        self.step_3_procedure_3 = 'процедура 3'
        self.step_3_procedure_4 = 'процедура 4'
        self.step_3_procedure_5 = 'процедура 5'
        self.step_3_procedure_6 = 'процедура 6'
        self.step_3_procedure_7 = 'процедура 7'
        self.step_3_procedure_8 = 'процедура 8'
        self.step_3_procedure_9 = 'процедура 9'
        self.step_3_count_procedures_1 = '1'
        self.step_3_count_procedures_2 = '2'
        self.step_3_count_procedures_3 = '3'
        self.step_3_count_procedures_4 = '4'
        self.step_3_count_procedures_5 = '5'
        self.step_3_count_procedures_6 = '6'
        self.step_3_count_procedures_7 = '7'
        self.step_3_count_procedures_8 = '8'
        self.step_3_count_procedures_9 = '9'
        self.step_3_procedure_period_1 = '1'
        self.step_3_procedure_period_2 = '2'
        self.step_3_procedure_period_3 = '3'
        self.step_3_procedure_period_4 = '4'
        self.step_3_procedure_period_5 = '5'
        self.step_3_procedure_period_6 = '6'
        self.step_3_procedure_period_7 = '7'
        self.step_3_procedure_period_8 = '8'
        self.step_3_procedure_period_9 = '9'
        self.step_3_commentary = 'Мы же всего лишь проверяем как они будут отображаться на бланке.'

        self.step_4_commentary = '''Выделяют следующие группы лекарственных средств: Психостимуляторы-адаптогены. Препараты природного происхождения, которые стимулируют умственную и физическую работоспособность на фоне утомления, повышая энергопродукцию.
Ноотропы. Нейрометаболические стимуляторы, которые оказывают прямое активирующее влияние на процессы обучения, повышая устойчивость головного мозга к агрессивным воздействиям.
Корректоры энергетического метаболизма. Специально разработанные натуральные составы, которые действуют постепенно. Результат заключается в улучшении деятельности головного мозга.Выделяют следующие группы лекарственных средств:
Психостимуляторы-адаптогены. Препараты природного происхождения, которые стимулируют умственную и физическую работоспособность на фоне утомления, повышая энергопродукцию.
Ноотропы. Нейрометаболические стимуляторы, которые оказывают прямое активирующее влияние на процессы обучения, повышая устойчивость головного мозга к агрессивным воздействиям.
Корректоры энергетического метаболизма. Специально разработанные натуральные составы, которые действуют постепенно. Результат заключается в улучшении деятельности головного мозга.'''


p = r'C:\Users\Эрик\Desktop\123.pdf'
bm = BlankManager(PdfGenerator, Data(), LazyPrinter)
bm.save_pdf(p)
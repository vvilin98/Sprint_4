import pytest
import allure
from pages.home_page import YaScooterHomePage
from utils.test_data import YaScooterHomePageFAQ
from utils.locators import YaScooterHomePageLocator

@allure.story('Тестировани выпадающего раздела "Вопросы о важном".')
class TestYaScooterFAQPage:
    @allure.title('Нажатие на каждый из 8 вопросов в блоке "Вопросы о важном"')
    @allure.description('Проверка что при нажатии на поле вопроса в блоке "Вопросы о важном", '
                        'данный вопрос раскрывается и текст в нем соответствует ТЗ')
    @pytest.mark.parametrize (
        "question,answer,expected_answer",
        [
            (0, 0, YaScooterHomePageFAQ.answer1),
            (1, 1, YaScooterHomePageFAQ.answer2),
            (2, 2, YaScooterHomePageFAQ.answer3),
            (3, 3, YaScooterHomePageFAQ.answer4),
            (4, 4, YaScooterHomePageFAQ.answer5),
            (5, 5, YaScooterHomePageFAQ.answer6),
            (6, 6, YaScooterHomePageFAQ.answer7),
            (7, 7, YaScooterHomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_faq_question(question_number=question)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.FAQ_ANSWER(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым значением '

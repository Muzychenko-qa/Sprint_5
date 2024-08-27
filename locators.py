from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка 'Войти в аккаунт'
    TEXT_SING_IN = (By.XPATH, "//h2[text()='Вход']")  # Заголовок страницы
    REGISTRATION_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка 'Зарегистрироваться'
    TEXT_REGISTRATION = (By.XPATH, "//h2[text()='Регистрация']")  # Заголовок страницы
    REGISTRATION_NAME_INPUT = (By.XPATH, '//fieldset[1]//input[@name="name"]')  # Поле ввода Имя
    REGISTRATION_EMAIL_INPUT = (By.XPATH, '//fieldset[2]//input[@name="name"]')  # Поле ввода Email
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, '//fieldset[3]//input[@name="Пароль"]')  # Поле ввода Пароль
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка 'Зарегистрироваться'

    REGISTRATION_H2_TEXT = (By.TAG_NAME, "h2")  # Заголовок страницы
    INCORRECT_PASSWORD_H2_TEXT = (By.XPATH, "//fieldset[3]//p[text()='Некорректный пароль']")  # Текст ошибки
    RESTORE_PASSWORD_H2_TEXT = (By.XPATH, "//h2[text()='Восстановление пароля']")  # Заголовок Восстановление пароля

    SIGN_IN_EMAIL = (By.XPATH, "//fieldset[1]//input[@name='name']")
    SIGN_IN_PASSWORD = (By.XPATH, "//fieldset[2]//input[@type='password']")
    SIGN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка Войти
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка Оформить заказ

    PERSONAL_LINK = (By.XPATH, "//a[@href='/account']")  # Ссылка "Личный Кабинет"
    SIGN_IN_LINK = (By.XPATH, "//a[@href='/login']")  # Ссылка "Войти"
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка "Забыли пароль"

    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']")  # Ссылка
    CONSTRUCTOR_H1_TEXT = (By.XPATH, "//div/main/section[1]/h1")  # Заголовок
    STELLA_BURGER_LINK = (By.XPATH, "//div/header/nav/div/a[@href='/']")  # Ссылка

    SIGN_OUT = (By.XPATH, "//button[text()='Выход']")  # Кнопка 'Выход'

    BURGER_BUN_H2 = (By.XPATH, "//section/div/h2[1]")  # Текст ингридиента из раздела Булки
    BURGER_SAUCE_TEXT = (By.XPATH, "//p[text()='Соус с шипами Антарианского плоскоходца']")  # Текст ингридиента из раздела Соусы

    BREAD_SECTION = (By.XPATH, "//section/div/div[1]/span")  # Секция "Булки"
    SAUCES_SECTION = (By.XPATH, "//section/div/div[2]/span")  # Секция "Соусы"
    DIPS_SECTION = (By.XPATH, "//section/div/div[3]/span")  # Секция "Начинки"
    CONSTRUCTOR_ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")


from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.XPATH, '//fieldset[2]//input')  #плашка ввода имейла на странице регистрации
    PASSWORD = (By.NAME, 'Пароль')  #плашка ввода пароля на странице регистрации
    ERROR_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default']")    #сигнал с надписью "некорректный пароль" на странице регистрации
    AUTH_BUTTON = (By.XPATH, '//*[text()="Зарегистрироваться"]')    #кнопка "зарегистрироваться" на странице регистрации

    LOGIN_BUTTON_MAIN = (By.XPATH, "//section[2]//button[text()='Войти в аккаунт']") #кнопка "войти в аккаунт" на главной
    LOGIN_PLACE = (By.XPATH, '//fieldset[1]//input') #плашка ввода имейла на странице входа
    PASSWORD_PLACE = (By.NAME, 'Пароль') #плашка ввода пароля на главной
    LOGIN_BUTTON_LAST = (By.XPATH, '//*[text() = "Войти"]') #кнопка "войти в аккаунт" на странице входа

    BUTTON_PROFILE = (By.XPATH, '//*[text()="Личный Кабинет"]')  #кнопка входа в личный кабинет
    BUTTON_LOGIN_FORM_REG = (By.CLASS_NAME, "Auth_link__1fOlj") #кнопка "войти" через форму регистрации
    BUTTON_RESET_PASSWORD = (By.XPATH, '//*[text() = "Восстановить пароль"]') #кнопка "восстановить пароль"
    BUTTON_LOGIN_RESET_PASSWORD = (By.CLASS_NAME, "Auth_link__1fOlj") #кнопка "войти" через форму восстановления пароля

    BUTTON_CONSTRUCT = (By.XPATH, '//p[text()="Конструктор"]')  #кнопка конструктор
    BUTTON_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") #кнопка логотипа
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']") #кнопка "выход" в личном кабинете

    BUTTON_FILLING = (By.XPATH, "//span[text()='Начинки']") #переход в раздел "начинки"
    BUTTON_SOUS = (By.XPATH, "//span[text()='Соусы']") #переход в раздел "соусы"
    BUTTON_BUN = (By.XPATH, "//span[text()='Булки']") #переход в раздел "булки"

    TRIGGER_REG = (By.XPATH, '//*[@id="root"]//h2[text()="Регистрация"]') #надпись "регистрация" на странице регистрации
    TRIGGER_RES_PASSWORD = (By.XPATH, '//h2[text()="Восстановление пароля"]') #надпись "восстановление пароля" на странице восстановления
    TRIGGER_IN = (By.XPATH, '//h2[text()="Вход"]') #надпись "Вход" на странице входа
    TRIGGER_ASSEMBLE_BURGER = (By.XPATH, '//section[1]/h1[text()="Соберите бургер"]') #надпись "Соберите бургер" на главной
    TRIGGER_ERR_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default']") #надпись "некорректный пароль"

    TRIGGER_FILLING = (By.XPATH, "//p[text()='Биокотлета из марсианской Магнолии']") #значок биокотлеты
    TRIGGER_SOUS = (By.XPATH, "//p[text()='Соус с шипами Антарианского плоскоходца']") #значок соуса с шипами
    TRIGGER_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']") #значок флюоресцентной булки

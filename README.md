## Проект API автотестов reqres.in

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="./attachments/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="./attachments/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="./attachments/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="./attachments/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="./attachments/logo/github.png"></code>
  <code><img width="5%" title="Allure Report" src="./attachments/logo/allure_report.png"></code>
  <code><img width="5%" title="Jenkins" src="./attachments/logo/jenkins.png"></code>
  <code><img width="5%" title="Requests" src="./attachments/logo/requests.png"></code>
  <code><img width="5%" title="Telegram" src="./attachments/logo/tg.png"></code>
</p>

### Что выполняет тест:
![This is an image](attachments/screenshots/test.png)


## :computer: Запуск тестов из терминала
```bash
pytest tests/test_reqres.py --env=prod
pytest tests/test_demoshop.py --env=prod 
```

В проекте используется встроенный logger - logging:
![This is an image](attachments/screenshots/logger.png)

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="attachments/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/qa_guru_api/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение
![This is an image](attachments/screenshots/jenkins1.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="attachments/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты автоматически сохраняются. Чтобы посмотреть Allure отчет нужно нажать на иконке allure report у сборки.
![This is an image](attachments/screenshots/allure1.png)

##### Во вкладке Suites находятся подробные данные о прохождении теста с приложенными логами
![This is an image](attachments/screenshots/suites.png)

<!-- Telegram -->

### <img width="3%" title="Telegram" src="attachments/logo/tg.png"> Telegram

##### Настроен телеграм-бот, после прохождения тестов в Jenkins присылает уведомление с отчетом в Телеграм

##### Скриншот отчета в телеграм
![This is an image](attachments/screenshots/telegram1.png)

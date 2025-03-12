# Миграции
## Запуск миграции
```bash 
make migrate
```
## Откат миграций
```bash 
make unmigrateMessangerApp # потребует имя новой HEAD миграции
```
## Заполнение тестовыми данными
```bash 
make fillDBWithRandomDataMigration # миграцией
make fillDBWithRandomDataMigration # залив напрямую
```

# Замечания

### 1
    не стал создавать папку для базы - а зачем,
    если и так работа с ней на django models,
    а dockerfile писать тоже мало смысла, если
    есть image в dockerhub, которые запустим 
    в compose

### 2
    Swagger - не стал делать конфиг, но нашёл либу,
    совместимую с DRF, которая настроила сваггер

### 3 
    Сделал мок данные через mixer

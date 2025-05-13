# Salary Report Generator

## Установка
```bash
git clone <repository-url>
cd salary_report
pip install -r requirements.txt
```

## Использование
```bash
# Вывод в консоль (по умолчанию)
python3 salary_report/main.py data.csv --report payout

# Сохранение в текстовый файл
python3 salary_report/main.py data.csv --report payout --output report.txt

# Сохранение в JSON формат
python3 salary_report/main.py data.csv --report payout --format json --output report.json

# Обработка нескольких файлов
python3 salary_report/main.py data1.csv data2.csv data3.csv --report payout
```

## Форматы вывода

### Текстовый (по умолчанию)
```
Marketing
----------------  Alice Johnson        160     50  $8000.00
                                      Total:   160  $8000.00
```

### JSON
```json
{
  "departments": {
    "Marketing": {
      "employees": [
        {"name": "Alice Johnson", "hours": 160, "rate": 50, "payout": 8000.00}
      ],
      "total_hours": 160,
      "total_payout": 8000.00
    }
  }
}
```

## Параметры запуска
- `--report` - тип отчета (обязательный параметр)
- `--format` - формат вывода (text или json, по умолчанию text)
- `--output` - путь для сохранения отчета (опционально)

## Поддерживаемые форматы файлов
- Текстовый отчет: `.txt`, `.text`
- JSON отчет: `.json`

## Добавление нового отчета
1. Создайте новый класс в `reports/` наследующий `BaseReport`
2. Реализуйте методы `generate()` и `to_dict()`
3. Зарегистрируйте в `REPORTS` в `reports/__init__.py`

## Примеры входных данных
```csv
id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
3,carol@example.com,Carol Williams,Design,170,60
```

## Особенности
- Поддержка множественных входных файлов
- Автоматическая нормализация заголовков (hourly_rate, rate, salary)
- Валидация форматов выходных файлов
- Группировка по департаментам в отчетах
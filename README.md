# Spellchecker
Python 3 утилита для проверки орфографии.
### Before run
Установить зависиости

``pip3 install -r requirments.txt``

### Примеры запуска

``python3 spellcheck.py тоезд ушел! но куда по дорое, интересный вопро?``

``python3 spellcheck.py -i input.txt -o output.txt``

``python3 spellcheck.py -r '(\d+)-ый' '\1-й' 534-ый 2-й``

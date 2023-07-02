# Микросервис для сортировки задач

Этот микросервис разработан для сортировки задач на основе их зависимостей. Он принимает имя билда и возвращает список задач, отсортированных с учетом их зависимостей.

## Установка и настройка

1. Клонируйте репозиторий на свою локальную машину:
   ```shell
   git clone <ссылка_на_репозиторий>

2. Перейдите в директорию проекта:
   ```shell
    cd <директория>

3. Установите зависимости с помощью pip:
    ```shell
    pip install -r requirements.txt

4. Запустите микросервис с помощью команды:
    ```shell
    uvicorn main:app --reload
   ```
    
    перейдите по адресу  http://localhost:8000/docs
    воспользуйтесь ui видом 

## Использование микросервиса
Микросервис имеет один эндпоинт /get_tasks, который принимает POST-запрос с JSON-телом, содержащим имя билда. Он возвращает отсортированный список задач, соответствующих указанному билду.

Пример запроса:
```json
{
  "build_name": "forward_interest"
}
```
Пример ответа:
```json
[
  "build_teal_leprechauns",
  "enable_yellow_centaurs",
  "bring_olive_centaurs",
  "coloring_white_centaurs",
  "create_teal_centaurs",
  "design_lime_centaurs",
  "train_purple_centaurs",
  "upgrade_navy_centaurs",
  "create_maroon_centaurs",
  "bring_blue_centaurs",
  "read_yellow_centaurs",
  "create_olive_centaurs",
  "coloring_aqua_centaurs",
  "coloring_aqua_golems",
  "coloring_navy_golems",
  "map_black_leprechauns",
  "upgrade_white_leprechauns",
  "map_olive_leprechauns",
  "enable_lime_leprechauns",
  "create_aqua_humans",
  "enable_olive_humans",
  "build_maroon_humans",
  "write_silver_humans",
  "write_white_humans",
  "create_purple_humans",
  "train_white_humans",
  "write_teal_humans",
  "enable_silver_humans",
  "bring_blue_ogres",
  "design_white_ogres",
  "train_green_ogres",
  "upgrade_aqua_ogres",
  "write_silver_ogres",
  "enable_fuchsia_ogres",
  "bring_green_ogres",
  "build_yellow_ogres",
  "create_maroon_ogres",
  "design_green_ogres",
  "upgrade_navy_ogres",
  "write_blue_ogres",
  "write_fuchsia_golems"
]
```

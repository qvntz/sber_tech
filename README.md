# SberZvuk hackaton

## Command gentlemen

---

1) _Серверная часть_ решения находится в ветке ***backend***
    * Все необходимые зависимости описаны в setup.py
    * Собран докер образ для контейнера
2) Часть с _обработкой видео и аудио_ находится в ***data_science***
    * Распознование звука реализовано с помощью перевода звука в текст и последующего поиска подходящего имени артиста с помощью измерения расстояния по Левенштейну
    * Для обработки видео используются предобученные модели для детекции лиц и составления эмбеддингов. Например openface и resnet. Загружаются в фотографии людей, по ним строятся embeddings, затем тренируется SVC. Непосредственно перфоманс - берется каждый кадр видео, на нем находятся лица, рисуются bounding_boxes, лицо блюрится, встраивается в исходный кадр и выводится.

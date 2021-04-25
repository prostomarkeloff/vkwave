# Мультитокен

Для обхода ограничений по частоте запросов к API ВКонтакте при создании бота можно указать несколько токенов:

``` python
bot = SimpleLongPollBot(
    tokens=["MyToken1","MyToken2","MyToken3"],
    group_id=123456789
)
```

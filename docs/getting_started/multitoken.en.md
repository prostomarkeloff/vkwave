# Multitoken 

To bypass the restrictions on the frequency of requests to the VK API when using a bot, you can specify several tokens:

``` python
bot = SimpleLongPollBot(
    tokens=["MyToken1","MyToken2","MyToken3"],
    group_id=123456789
)
```

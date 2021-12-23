# Программа для вывода строки курсивом и жирно
![markdown](https://i.morioh.com/2019/11/06/362222e42d54.jpg)
Программа принимает строку и проверяет количество зведдочек с каждой стороны, чтобы понять как этот текст будет записан в markdown

____

## module_flot
Модуль, содержащий в себе две функции: **bold** для жирного текста и *itallic* для курсива.
```python
>>> s = '**abc**'
>>> itallic(s)
'<em>*abc*</em>'
>>> bold(s)
'<strong>abc</strong>'
>>> s = '*abc*'
>>> itallic(s)
'<em>abc</em>'
```

______
### Использовавшиеся ресурсы
* https://github.com/OlgaVlasova/markdown-doc
* https://dillinger.io/

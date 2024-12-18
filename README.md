# Lesta-Games-test

### Вопрос №1.
**На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. Пример:** 
```python
def isEven(value):
	return value % 2 == 0
```

Код представлен в файле `even.py`

***Пояснение:*** отличие алгоритма, приведенного в примере, с алгоритмом в файле `even.py` заключается в операции проверки числа - взятия остатка от деления `%` на 2, и побитовое И `&` с единицей.

Плюсы приведенного примера:
- наглядная и однозначно понятная операция

Минусы приведенного примера:
- меньшее быстродействие, т.к. в общем случае операция выполняется за несколько шагов (целочисленное деление, умножение делителя и вычитание). Однако, если я не ошибаюсь, в Python вшита оптимизация взятие остатка от деления на 2, как раз за счет проверки младшего бита. Но даже в таком случае, будут происходить лишние операции, и алгоритм сработает несколько медленнее.

Плюсы алгоритма с ипользованием `value & 1`:
- быстродействие, т.к. данная операция лишь проверяет совпадение младшего бита числа с 1. Она способна выполняться на низком уровне за 1 тик процессора.

Минусы алгоритма с ипользованием `value & 1`:
- менее наглядна и очевидна

### Вопрос №2
**На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.**

Код классов представлен в файлах `fifo1.py` и `fifo2.py`. В данных реализациях старые данные перезаписываются в случае переполнения буфера.

Плюсы реализации `fifo1.py`:
- память будет выделяться непосредственно при добавлении объекта в буфер, и освобождаться при его удалении
- быстрое обращение к ключевым элементам буфера по ссылкам
- простотая логика переполнения, добавления и удаления объектов

Минусы реализации `fifo1.py`:
- меньшее быстродействие, из-за работы с указателями и использования объектов дополнительного вспомогательного класса

Плюсы реализации `fifo2.py`:
- быстродействие, за счет работы с динамическим массивом через индексы
- простота, нагдяность и компактность
- отсутсвие доп. класса для элементов буфера

Минусы реализации `fifo2.py`:
- моментальное выделение памяти под объекты, что может быть избыточным
- ненаглядная индексация данных - новые объекты (которые были добавлены позже) могут иметь индексы меньше, чем у старых объектов, либо же, индексация объектов может начинатся не с нуля (если буфер был заполнен частично, затем очищен, и вновь заполнен)

### Вопрос №3
**На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.**

По скольку массив может быть уже отсортированным - логично в таком случае использовать алгоритм сортровки Timsort, т.к. он обработает такой массив за время `O(n)`. 
Верное решение по заданным критериям - использовать встроенный метод `sort()` или `sorted()` сортировки динамического массива. Данный метод представляет собой встроенную реализацию сортировки Timsort на языке C, что делает его в несколько раз быстрее любой реализации (даже идентичной) на языке Python.

Исходя из приведенных фактов, предложенный алгоритм должен использовать метод `sort()`, однако он и реализует всю необходимую логику.

Поэтому, мое решение, предствелнное в файле `sort.py`, содержит исключительно метод `sort()`. Данная реализация справляется в несколько раз быстрее (*по времени в ~10 раз быстрее, для небольших массивов до 100 элементов, и более, с ростом количества элементов*) сортировки Timsort на Python, представленной в файле `timsort.py`, с учетом оптимизаций: 
- вставки (уже отсортированные части не будут проходить стадию слияния), за счет чего достигается время обработки отсортированного массива за время `O(n)`
- использование буфера для слияния, а не создание копий срезов списка

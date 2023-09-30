# Python basic

## open with jupyter notebook
```sh
jupyter notebook
```

> open 
> - [arrays](./arrays.ipynb)
> - [tuple-set](./tuple-set.ipynb)
> - [dictionary](./dictionary.ipynb)
> - [loop](./loop.ipynb)
> - [list-comprehension](./list-comprehension.ipynb)

# Small tips to code Python efficiently

### Use more `list comprehension`

#### **`example.py`**
```py
  with open("foo.csv", "r") as file:
    lines = [i.rstrip().split(",") for i in file]
    for line in lines:
      print(line)
```

### Spread operator

#### `List`

> javascript

#### **`spread-list.js`**
```js
  function multiply(a, b) {
    return a * b;
  }
  const numbers = [3, 5];
  console.log(multiply(...numbers));
  // Output: 15

  const numbers = [1, 2, 3];
  const newNumbers = [0, ...numbers, 4]
  console.log(newNumbers);
  // Output: [ 0, 1, 2, 3, 4 ]
```

> python

#### **`spread-list.py`**
```py
  def multiply(a, b):
    return a * b
  numbers = [3, 5]
  print(multiply(*numbers))
  # Output: 15

  numbers = [1, 2, 3]
  new_numbers = [0, *numbers, 4]
  print(new_numbers)
  # Output: [0, 1, 2, 3, 4]
```

#### `Object`

> javascript

#### **`spread-object.js`**
```js
  const testObj = { foo: 'bar' };
  console.log({ ...testObj, foo2: 'bar2' });
  // Output: { foo: 'bar', foo2: 'bar2' }
```

> python

#### **`spread-object.py`**
```py
  test_obj = { 'foo': 'bar' }
  print({ **test_obj, 'foo2': 'bar2' })
  # Output: {'foo': 'bar', 'foo2': 'bar2'}
```
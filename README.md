### 1 Bug found
Method ConvertToAtlasCopcoString returns "ERROR:)" when passing 87 as inparameter. Expected result is "Atlas" since 87 is a multiple of 3.

### Setup

Python 3

> To run the tests with coverage

```shell
$ pip install -r requirements.txt
$ coverage run -m pytest
$ coverage report (to report on the results)
```

**Methods choosen**
```shell
ConvertToAtlasCopcoString(self, toConvert):
ReverseString(self, toReverse):
```

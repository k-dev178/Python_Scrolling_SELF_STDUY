# class
데이터에 대한 청사진으로, 구조정의와 캡슐화를 제공.<br>
이라고 구글이 알려주는데 걍 보는게 더 빠름.

## 선언
puppy라는 클래스 생성.
```py
class Puppy:
  pass
```

# method
클래스 안에 있는 함수.

## 선언
한번 기본 메소드를 puppy 클래스안에 추가해봄.
```py
class Puppy:
  def __init__(self):
    print("Puppy is born!")
```
__init__ 메소드는 self 인자를 받아야함.

## 사용
```py
ruffus = Puppy()
```

Puppy()클래스가 하나 만들어지면, __init__코드가 자동으로 실행됨.

## self
저 self로 뭘 할 수 있을까.

```py
class Puppy:
  def __init__(self):
    self.name = "Ruffus"
    self.age = 0.1
    self.breed = "Beagle"
```

이런걸 만들고

```py
ruffus = Puppy()

print(ruffus.name, ruffus.age, ruffus.bread)
```
이런게 가능해짐.

각 강아지 정보의 대한 변수이름을 생각해내지 않아도 되고, 관리도 쉬워짐.
"강아지이름.name" 이런식으로 이름을 받기만 하면 됨.

---

# Methods
근데 좀 이상하지 않음?<br>
Puppy()를 실행하면 이름을 준다는게...

이름이 "Ruffus"가 아니면 어칼거임?

그래서 이걸 이렇게 쓸 수 있음.

```py
class Puppy:
  def __init__(self, name, age ,breed):
    self.name = name
    self.age = age
    self.bread = breed
```

이렇게 클래스를 만들고,

```py
ruffus = Puppy("Ruffus",0.1,Beagle)
bibi = Puppy(name="bibi",breed=Dalmatian,age=0.1) # 참고로 이렇게 하면 순서 상관 없음.
```

이런식으로 만들면 됨.

## __str___
여기에 메소드 하나 더 추가해봄.

```py
class Puppy:
  def __init__(self, name, age ,breed):
    self.name = name
    self.age = age
    self.breed = breed
  def __str__(self):
    return f"name: {self.name}, age: {self.age}, breed: {self.breed}"
```

이렇게 하고

```py
a = Puppy()

print(a)
```

하면 저 리턴값이 출력됨.

---

# Inheritance(상속)

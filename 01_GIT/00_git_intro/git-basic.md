# 마크다운(MarkDown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용이 쉽고 간결하다.
>
> 단, 모든 HTML 마크업을 대체하지 않는다.

## 1.문법

### 1.1 Header

> 헤더는 제목을 표현할 때 사용합니다.
>
> 단순히 글자의 크기를 나타낼 때 사용하는 것이 아니라 의미론적인 중요도를 갖습니다.

- h1 ~ h6 까지 표현이 가능합니다.
- #의 갯수로 표현하거나 <h1></h1> 형태로 표현 가능합니다.



### 1.2 List

> 목록을 나열할 때 사용합니다.
>
> 순서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다.
>
> 순서/순서x 항목을 같이 사용할 수 있습니다.

- 순서가 없는 항목
  - 순서가 없는 하위 항목
  - 순서가 없는 하위 항목

1. 순서가 있는 항목
2. 순서가 있는 항목
   1. 순서가 있는 하위 항목
   2. 순서가 있는 하위 항목



- 순서가 있는 항목
  1. 순서가 있는 하위 항목



### 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶을 때 사용합니다.
>
> 코드 블럭은 인라인과 블럭 단위로 구분할 수 있습니다.

- Inline
  - 인라인으로 처리하고 싶은 부분을 `(백틱)으로 감싸줍니다.
- Block
  - (백틱)을 3번 입력하고 `Enter`를 눌러서 생성합니다.



```bash
$ git add .
$ git commit -m "commit message"
$ git push origin master
```



### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용하여 표시합니다.

- `![]()`를 작성하고 `()` 안에 주소를 입력합니다.
  - 이때 `[]` 안에는 이미지 이름을 입력합니다.
- 로컬에 있는 이미지 파일을 로드할 때는 절대 경로가 아닌 상대 경로를 사용합니다.

![git(hub)-image](data:image/png;base64,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)



![](.\Images\1543751883978.jpg)



### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다.

- `[]()` 를 작성하고 `()` 안에 링크를 걸 주소를 입력합니다.

[Tensorflow](https://github.com/tensorflow/tensorflow)



### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다.

- `|` (파이스) 사이에 컬럼을 작성하고 `Enter` 를 입력합니다.
- 마지막 컬럼을 작성하고 뒤에 `|` 를 붙여줍니다.

| Working Directory | Staging Area | Remote Repo |
| :---------------: | :----------: | :---------: |
|   working tree    |    INDEX     |   history   |
|   working copy    |    cache     |    tree     |



### 1.7 기타

#### 인용문

- `>`를 입력하고 `Enter` 키를 누릅니다.

> git은 컴퓨터의 파일 변경 사항을 추적합니다.

- 중첩된 인용문을 사용할 수 있습니다.

> $ git add .
>
> >  
> >
> > > $ git commit -m "first commit"



#### 수평선 

- `---` , `***` , `___` 를 입력하여 작성합니다.



#### Working Directory 

---

#### Staging Area

---

#### Remote Repository(Github)



**강조**

- 이탤릭체는 해당 부분을 `*` , `_` 1개로 감싸줍니다.

- 보드체는 해당 부분을 `**`, `__` 2개로 감싸줍니다.
- 취소선은 `~~` 2개로 감싸줍니다.



이것은 *이탤릭체*입니다.



이것은 **보드체**입니다.



이것은 ~~취소선~~입니다.




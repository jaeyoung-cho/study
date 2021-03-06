# TypeScript

## 개요

요즘은 Javascript, Node.js, React.js 등으로 업무를 주로하고, 이들과 주변 기반지식들 공부하랴 육아에 영어공부 그리고 일일커밋까지 정신이 하나도 없어서 못하고 있는 공부 중 하나인 스칼라의 도입부에 이러한 이야기가 있다.

스칼라를 창시한 마틴 오더스키는 스칼라를 정적 타입기반의 객체지향과 함수형 개발을 모두 할 수 있는 확장성이 뛰어난 언어를 목적으로 만들었다고 한다. 그러면서 스칼라를 요즘 대두가 되고 있는 동적 타입이 아닌 정적 타입을 기반으로 한 것에 대해서 언급한 내용이 있는데 이 내용을 요약하면 대강 다음과 같다.

1. 프로퍼티 검증
  동적타입의 특성상 다른 타입간의 연산이 암묵적으로 이루어진다던가, 함수의 인자를 명시할 수 없거나, 배열에 타입을 섞어서 넣을 수 있는 등의 특징들은 정적타입을 제공하는 언어들에 비해 개발자의 많은 주의를 필요로하게 되고 버그를 양산해낼 여지가 많다는 것. 동적타입 기반을 좋아하는 개발자들의 경우 이러한 문제들은 단위 테스트를 통해 해결할 수 있다고 하지만, 정적타입 기반인 경우는 타입에 대한 부분까지 고민하며 테스트를 하지 않아도 된다는 것.
2. 안전한 리펙토링
  위와 같은 맥락의 이야기인데, 타입이 검증해주는 여러가지 안전장치들 덕분에 리펙토링을 할 때 동적타입 기반의 언어들보다 수월하다는 것.
3. 문서화
  동적타입 언어에 비해 코드 자체로의 문서화가 좀 더 잘 이루어진다는 것이다. 예를들어 다음과 같이 함수에 인자 x는 문자열이라는 것을 명시해준다는 것은 함수를 코드 자체로 동적타입 기반의 언어보다는 좀 더 가독성이 뛰어나다는 것.

    ```scala
    def f(x: String) = ...
    ```
    ```javascript
    function (x) { // x에 어떤 값을 넣어줘야하지?
      ...
    }    
    ```

물론, 위와 같이 정적 타입 시스템을 옹호하는 부류와 동적 타입 시스템을 옹호하는 부류 사이의 논쟁이 여전하고 뜨겁지만 나는 뭐가 좋다 그르다고 말할 수 없는 것 같다. 결국은 개발자 개개인의 경험과 습관 그리고 기술의 익숙함 정도에 따라 다른 시각으로 타입 시스템에 대한 생각을 갖고 개발을 할테니 말이다.

하지만 적어도 지난 9년이란 세월을 C++, Java, C# 등 정적 타입 시스템 기반의 언어들을 다뤄 온 나로서는 동적 타입 기반의 자바스크립트를 다루면서 마틴 오더스키가 했던 위의 이야기들에 굉장히 공감을 하고 있다.

함수의 인자를 잘못 전달하거나, 어떤 속성의 인자를 넘겨줘야하는지 확인이 잘 안되는 것부터, 글자를 틀렸는데 모르고 코드를 진행하다가 해당 코드를 탔을 때서야 갑자기 에러를 발생시킨다던가(사실 이 부분이 가장 짜증난다.) 그리고 지금 개발을 하고 있을 때야 코드에 익숙해서 괜찮지만 추후 다른 프로젝트를 하다가 지금 개발한 코드를 봤을 때 얼마나 이해가 될런지 등등의 걱정들을 하게 된다.

하지만, 자바스크립트를 하면서 많은 것을 배우고 다룰수 있게 되었기 때문에 이것을 또 포기할 수 없고 해서 자바스크립트에 타입을 더할 수 있는 TypeScript를 공부해보기로 했다.

## 개발환경

Javascript와 Node.js 그리고 React.js로 이쪽 세계에 입문하고부터 쭉 Atom을 쓰고 있으므로 Atom을 통해 TypeScript도 공부할 생각이다. 이를 위해 Atom에 다음 플러그인을 설치해야한다.

[atom-typescript](https://atom.io/packages/atom-typescript)


## 참조

* Programming in Scala seond Edition 한국어판
* [TypeScript](https://www.typescriptlang.org/index.html)

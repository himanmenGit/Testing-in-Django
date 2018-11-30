# Testing in Django - Best Practices and Examples

좀더 완벽(?)한 테스트를 짜기 위한 공부

Part1과 Part2로 나누어져 있다.

본 포스팅의 장고 버전은 `Django==2.1.3`이다.

# Part1
## 모범 사례 및 예시

Link: [요기](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#next-timed-and-examples/#next-time)

### 목차

* [장고 테스트의 소개](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#intro-to-testing-in-django)
    * [테스트들의 유형](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#types-of-tests)
    * [모범 사례](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#best-practices)
    * [구조](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#structure)
    * [서드파티 패키지](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#third-party-packages)
* [예제](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#examples)
    * [설정](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#setup)
    * [모델 테스팅](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#testing-models)
    * [뷰 테스팅](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#testing-views)
    * [폼 테스팅](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#testing-forms)
    * [API 테스팅](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#testing-the-api)
    

# Part2
## 모델 Mommy Vs 장고 테스트 Fixtures

Link: [요기](https://realpython.com/testing-in-django-part-2-model-mommy-vs-django-testing-fixtures/)

### 목차

* [왜 신경 써서 해야 하나?](https://realpython.com/testing-in-django-part-2-model-mommy-vs-django-testing-fixtures/#why-should-you-care)
* [장고 테스트 도구](https://realpython.com/testing-in-django-part-2-model-mommy-vs-django-testing-fixtures/#django-testing-fixtures)
* [모델 Mommy](https://realpython.com/testing-in-django-part-2-model-mommy-vs-django-testing-fixtures/#model-mommy)
* [새 모델](https://realpython.com/testing-in-django-part-2-model-mommy-vs-django-testing-fixtures/#new-model)
    * [설정](https://realpython.com/testing-in-django-part-2-model-mommy-vs-django-testing-fixtures/#setup)
    * [테스트](https://realpython.com/testing-in-django-part-2-model-mommy-vs-django-testing-fixtures/#test)
* [Well?](https://realpython.com/testing-in-django-part-2-model-mommy-vs-django-testing-fixtures/#well)

# 후기

일단 좀 오래된 예제와 포스팅을 가지고 공부를 했다.
그래서 그런지 테스트 형식은 지금의 방식과 약간 맞지 않았던것 같다. 
하지만 테스트를 하기 위해 필요한 좋은 서드파티 툴을 알게 되었고
테스트를 모든 방향에서 가능하다는것을 알게 되었다.

이제 궁금한것은 테스트를 얼마만큼 해야 하는가 에 대한 것이다.
테스트를 짜다 보면 로직이 맞는지 테스트를 해야 하는것은 당연하지만
잘못된 값에 대한 테스트또한 해야 하는지 헷갈린다.

좀더 테스트에 대한 본질적인 생각을 해봐야 하나 싶다.
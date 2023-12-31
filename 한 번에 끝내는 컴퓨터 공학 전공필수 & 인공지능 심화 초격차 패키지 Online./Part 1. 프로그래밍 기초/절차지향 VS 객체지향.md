절차지향(Procedural Programming)이란, 물이 위에서 아래로 흐르는 것처럼 순차적인 처리가 중요시 되며 프로그램 전체가 유기적으로 연결되도록 만드는 프로그래밍 기법입니다.

절차지향(Procedural Programming) 특징

  - 대표적인 예로는 C언어가 있습니다.
  - 컴퓨터의 작업 처리 방식과 유사하기 때문에 객체지향 언어를 사용하는 것에 비해 더 빨리 처리 되어 시간적으로 유리합니다.

장점

  - 컴퓨터의 처리구조와 유사해 실행속도가 빠릅니다.
 
단점
  - 유지보수가 어렵습니다.
  - 실행 순서가 정해져 있으므로 코드의 순서가 바뀌면 동일한 결과를 보장하기 어렵습니다.
  - 디버깅이 어렵습니다.

---------------------------------------------------------------------------------------------------------------------------------------------

객체지향(Object Oriented Programming)
객체지향 프로그래밍에서는 데이터와 절차를 하나의 덩어리로 묶어서 생각하게 됩니다. 이는 마치 컴퓨터 부품을 하나씩 사다가 컴퓨터를 조립하는 것과 같은 방법입니다.
 
옛날에는 하드웨어와 소프트웨어의 개발 속도차이가 크지 않았지만 소프트웨어 언어의 발달과 컴파일러의 발달로 하드웨어가 소프트웨어의 발달을 따라오지 못하는 상황이 발생했습니다. 이는 객체지향(Object Oriented Programming) 언어가 등장하게 되는 계기로 작용했습니다. 객체지향 프로그래밍은 개발하려는 것을 기능별로 묶어 모듈화를 함으로써 하드웨어가 같은 기능을 중복으로 연산하지 않도록 하고, 모듈을 재활용하기 때문에 하드웨어의 처리양을 획기적으로 줄여주었습니다.
 
이론적으로만 본다면 객체지향 언어는 절차지향 언어에 비행 장점이 많습니다. 하지만 프로그래밍을 할 때 항상 객체지향 언어만 사용하는 것은 아닙니다. 객체지향 언어는 어떤 모듈에 있는 하나의 기능만 필요하더라도 모듈 전체를 가져와야 하기 때문에 절차지향 프로그래밍보다 프로그램 사이즈가 더 커질 수도 있습니다. 또한 데이터에 대한 접근도 상대적으로 절차지향식보다 느려질 가능성이 많습니다. 메소드를 통해서만 접근이 가능하기 때문에 절차지향식처럼 특정 함수에 접근할 수 없고, 식으로만 접근이 가능해 속도적인 측면에서 불이익이 있습니다.

객체지향(Object Oriented Programming) 특성

  - 캡슐화(Encapsulation)- 객체를 캡슐로 싸서 그 내부를 보호하고 볼 수 없게 하는 것으로 객체의 가장 본질적인 특징입니다.- 실세계를 예를 들면, 캡슐에 든 약은 어떤 색인지, 어떤 성분인지 보이지 않으며, 캡슐로부터 보호받기 때문에 외    부의 접근으로부터 안전합니다.- JAVA로 예를 들면, 클래스(Class)는 객체의 모양을 선언한 틀이며, 클래스 모양 그대로 생성된 실체(Instance)가 객체 가 됩니다. 자바는 필드(Field)와 Method(Method)를 클래스 내에 모두 구현하고 캡슐화를 통해 객체 내 필드에 대한 외부로부터의 접근을 제한합니다. (이해를 돕자면 붕어빵 틀이 클래스가 되고, 붕어빵이 객체가 된다고 생각하시면 됩니다!)*필드 : 물체의 상태 / Ex) String name, String CarName, Int age  등*메소드 : 물체의 행동 / Car에 이름과 번호가 있기도 하지만, Car는 앞으로 전진할 수도 있고 후진하는 행동도 할 수 있습니다. / Ex)void go(); , void Back(); 등

  - 상속(Inheritance)- 상위 개체의 속성이 하위 개체에 물려져서, 하위 개체가 상위 개체의 속성을 모두 가지는 관계입니다.- 실세계를 예를 들면, '동물'은 '생물'의 속성을 가지고 있으며, '어류'는 '동물'의 속성과 '생물'의 속성을 모두 가지고 있습니다.- JAVA로 예를 들면, 자식 클래스가 부모 클래스의 속성을 물려받아 부모 클래스에 기능을 확장(Extends)하는 개념입니다. 이때 자바에서 부모 클래스를 슈퍼 클래스(Super Class)라고 부르며 자식 클래스를 서브 클래스(Sub Class)라고 부릅니다.- 상속은 슈퍼클래스에 만들어진 필드와 메소드를 물려받음으로써 코드의 중복 작성을 방지하고, 코드를 재사용함으로써 코드 작성에 드는 시간과 비용을 줄입니다.

  - 다형성(Polymorphism)- 같은 이름의 메소드가 클래스 혹은 객체에 따라 다르게 구현되는 것을 말합니다.- 실세계에서 예를 들면, 동물들은 소리(음성)를 낼 수 있지만, 강아지는 '멍멍', 고양이는 '야옹', 닭은 '꼬꼬댁'하고 우는 것처럼 낼 수 있는 소리(음성)는 다양합니다.- JAVA로 예를 들면, 슈퍼 클래스에 구현된 메소드를, 서브 클래스에서 자신의 특징에 맞게 동일한 이름으로 다시 구현하는 이른바 메소드 오버라이딩(Overriding)으로 부르고, 클래스 내에서 같은 이름의 메소드를 여러 개 만드는 메소드 오버로딩(Overloading)이 있습니다.

 
객체지향(Object Oriented Programming) 장단점

장점

  - 코드의 재활용성이 높습니다.
  - 코딩이 절차지향보다 간편합니다.
  - 디버깅이 쉽습니다.

 
단점

  - 처리속도가 절차지향보다 느립니다.
  - 설계에 많은 시간소요가 들어갑니다.


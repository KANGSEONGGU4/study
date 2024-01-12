Lambda architecture

Lamb architecture의 경우 batch processing, realtime stream processing이 결합된 구조

장점
 -  속도, 안전성이 우수하다. ( 장애시, batch layer로 데이터 재구성 가능 )
 -  확장이 용이하다.

단점
  -  중복 모듈이 많아진다.
  -  같은 코드가 batch layer, stream layer에 중복 된다.
  -  batch, stream에서 재처리를 할 수도 있다.

Kappa architecture

Kappa architecture의 경우 realtime stream processing만 이용하는 구조

장점
  -  리소스 절감 (batch layer가 없음)
  -  데이터 생성 / 처리하는 부분이 단일화 되어 시스템 이해가 쉽다.

단점
  -  중복 이벤트 처리나, 이벤트 상호 참조 혹은 순서 관련 처리에 대한 설계가 필요
  -  예를 들어 장애 발생시, 데이터 재생 관련한 부분 처리의 어려움.
  -  

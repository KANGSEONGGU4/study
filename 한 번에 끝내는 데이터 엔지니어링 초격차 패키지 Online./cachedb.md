Cache DB 란?

데이터를 빠르게 조회할 수 있는 곳.

원본 데이터는 다른 곳에 있고 그것으로부터 copy된 데이터가 Cache에 존재한다.
일반 DB는 디스크IO를 기반으로 동작하고 효율을 높이기 위해 memory를 사용한다.
in-memory DB는 모든 데이터를 메모리에서 다루기 때문에 조회속도가 빠르다.
 


Cache hit
조회하는 데이터를 cache에서 찾을 때


Cache miss
조회하는 데이터를 cache에서 찾지 못했을 때


Hit ratio(rate)
access 시도 횟수 대비 cache hit의 비율 -> 이 값이 높아야 캐시가 Cost-Effective 하다.

 

 


Cache 주의점
Cache는 임시 데이터이다. 원본이 다른 곳에 있어야 하고, 언제든 유실될 수 있음을 고려하고 시스템을 설계해야 한다.
Cache 저장소는 용량이 상대적으로 적고, 비용이 비싸다.
Cost-Effectiveness를 위해 Cache hit ratio를 측정하고 높일 수 있는 방법을 고민해야 한다.
 

Cache DB 종류


1. Memcached
key-value 형식 데이터 저장, 조회 제공하는 in-memory DB

 

멀티스레드로 데이터를 다룬다. -> 트래픽이 몰려도 응답속도가 Redis에 비해서는 안정적이다.
내부적으로 slab allocator를 사용하기 때문에 memory fragmentation 문제가 적다. 단, 데이터 변경이 잦은 경우에는 발생하기 쉽다.
메모리 사용량이 Redis에 비해 낮다.
 

사용목적: 트래픽이 많고 한번 저장된 후 변경되지 않는 정보를 저장할 때 유용하다.



2. Redis

기본은 key-value 형식 데이터, 다양한 자료구조로 저장, 조회 제공하는 in-memory DB

 

싱글스레드로 데이터를 다룬다. -> 한번에 하나의 client만 자료를 저장/조회 하기 때문에 데이터 lock없이 빠르게 데이터 조회가 가능하다. -> 트래픽이 몰리면 응답속도가 불안정할 수 있다.
실제 데이터의 양보다 더 많은 메모리가 필요하다. (메타데이터, CoW(copy on write) 사용 여부)
in-memory DB 중 가장 기능이 풍부하고 레퍼런스도 많다.
원하는 경우 disk에 persistent하게 데이터 백업 가능하다 (대신 성능의 손해를 고려해야한다)
 

사용 목적: 자주 변경되는 정보를 저장할 때 유용하다.

 


3. Couchbase

in-memory First Document DB이다.

 

데이터를 document 단위로 저장하고 document 내의 필드도 key-value로 조회할 수 있다.
memory-first이기 때문에 조회 속도도 빠르고 분산 클러스터 아키텍처로 구성되어 있어 확장성도 좋다.
secondary-index, SQL 등 다른 in-memory DB에서 지원하지 않는 기능들도 지원한다.
특정 자료구조를 원하는 경우에는 Redis, Memcached보다 느릴 수 있다.
client 라이브러리가 충분히 효율적이지 않고, 무료 버전의 안정성과 기능에 한계가 있다.

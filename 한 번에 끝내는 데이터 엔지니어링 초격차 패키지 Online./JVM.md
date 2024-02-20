![image](https://github.com/KANGSEONGGU4/study/assets/132239219/5692ec31-05f3-4961-ba92-c2fd33cdf559)   

Java Virtual Machine의 줄임말.   
직역하면 '자바를 실행하기 위한 가상 기계(컴퓨터)'라고 할 수 있다.   
Java 는 OS에 종속적이지 않다는 특징을 가지고 있다. OS에 종속받지 않고 실행되기 위해선 OS 위에서 Java 를 실행시킬 무언가가 필요하다. 그게 바로 JVM이다.   
즉, OS에 종속받지 않고 CPU 가 Java를 인식, 실행할 수 있게 하는 가상 컴퓨터이다.   

 컴파일 과정
 
Java 소스코드, 즉 원시코드(*.java)는 CPU가 인식을 하지 못하므로 기계어로 컴파일을 해줘야한다.

하지만 Java는 이 JVM 이라는 가상머신을 거쳐서 OS에 도달하기 때문에 OS가 인식할 수 있는 기계어로 바로 컴파일 되는게 아니라 JVM이 인식할 수 있는 Java bytecode(*.class)로 변환된다.

Java compiler 가 .java 파일을 .class 라는 Java bytecode로 변환한다.

💡 여기서 Java compiler는 JDK를 설치하면 bin 에 존재하는 javac.exe를 말한다. (즉, JDK에 Java compiler가 포함되어 있다는 소리임)
javac 명령어를 통해 .java를 .class로 컴파일 할 수 있다.
변환된 bytecode는 기계어가 아니기 때문에 OS에서 바로 실행되지 않는다.

이 때, JVM이 OS가 bytecode를 이해할 수 있도록 해석해준다. 따라서 Byte Code는 JVM 위에서 OS 상관없이 실행될 수 있는 것이다.

OS에 종속적이지 않고, Java 파일 하나만 만들면 어느 디바이스든 JVM 위에서 실행할 수 있다.

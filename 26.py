
'''
제너레이터 (Generator)

    오늘 배운 내용

이번에는 파이썬에서 데이터를 하나씩 생성하고 반환하는
제너레이터(Generator)에 대해 배웠다.

제너레이터는 일반 함수와 달리 yield를 사용하며,
값을 반환한 뒤 함수의 실행 상태를 기억한다.

반복자와의 관계와 yield, next()의 사용 방법을 학습했다.

    정의

1) 제너레이터(Generator)

제너레이터는 값을 한 번에 모두 생성하지 않고,
필요할 때마다 하나씩 만들어 반환하는 객체이다.

제너레이터 함수는 yield를 사용하여 만들 수 있으며,
실행 결과로 반복자 역할을 하는 제너레이터 객체를 반환한다.

2) yield

yield는 값을 반환하면서 함수의 실행 상태를 잠시 멈추는 명령어이다.

다음에 다시 호출되면 이전에 멈췄던 위치부터 실행을 이어간다.

3) return과 yield의 차이

return은 값을 반환하고 함수의 실행을 완전히 종료한다.

yield는 값을 반환한 뒤 함수의 실행을 잠시 멈추고,
다음 호출에서 이어서 실행한다.

    사용 방법

1) 기본적인 제너레이터 만들기

def numbers():
    yield 1
    yield 2
    yield 3

result = numbers()

print(next(result))
print(next(result))
print(next(result))

실행 결과
1
2
3

2) for문으로 제너레이터 사용하기

def numbers():
    yield 10
    yield 20
    yield 30

for num in numbers():
    print(num)

실행 결과
10
20
30

3) 반복문을 활용한 제너레이터

def count_up():
    for num in range(1, 6):
        yield num

for num in count_up():
    print(num)

실행 결과
1
2
3
4
5

4) 조건문을 활용한 제너레이터

def even_numbers():
    for num in range(1, 11):
        if num % 2 == 0:
            yield num

for num in even_numbers():
    print(num)

실행 결과
2
4
6
8
10

    코드 분석

1) 제너레이터 함수 호출

result = numbers()

일반 함수처럼 호출하지만, 함수 내부의 코드가
바로 전부 실행되는 것은 아니다.
제너레이터 객체가 생성된다.

2) next() 실행

print(next(result))

next()를 호출하면 함수가 실행되어
첫 번째 yield까지 진행하고 값을 반환한다.

3) 실행 상태 기억

다음 next()를 실행하면 처음부터 다시 실행하는 것이 아니라
이전에 멈췄던 yield 다음 부분부터 실행한다.

4) 반복 종료

더 이상 반환할 yield가 없으면 StopIteration이 발생한다.
for문은 이를 자동으로 처리하여 반복을 종료한다.

    복습하면서 알게 된 점

제너레이터는 반복자와 관련된 개념이며,
yield를 사용해 직접 값을 하나씩 생성할 수 있다는 것을 알게 되었다.

일반 함수의 return은 함수 실행을 종료하지만,
yield는 실행 상태를 기억했다가 다음 호출에서 이어서 실행한다.

또한 데이터를 한꺼번에 저장하지 않고 필요할 때 생성하기 때문에
많은 데이터를 처리할 때 메모리를 효율적으로 사용할 수 있다는 점을 이해했다.

📌 AI 활용 복습 문제

1) 제너레이터 함수를 만들 때 사용하는 명령어는?

정답: yield

2) yield와 return의 차이점은?

정답: return은 함수 실행을 종료하지만,
yield는 값을 반환하고 실행 상태를 기억한 채 잠시 멈춘다.

3) 제너레이터 객체에서 다음 값을 가져오는 함수는?

정답: next()

4) 다음 코드의 실행 결과는?

def test():
    yield 5
    yield 10
    yield 15

result = test()

print(next(result))
print(next(result))

정답:
5
10

5) 제너레이터가 반복자와 관련 있는 이유는?

정답: 제너레이터 객체도 반복자처럼 next()를 사용해
값을 하나씩 가져올 수 있기 때문이다.

6) 제너레이터를 사용하면 좋은 점은?

정답: 필요한 순간에 값을 하나씩 생성하기 때문에
많은 데이터를 처리할 때 메모리를 효율적으로 사용할 수 있다.
'''

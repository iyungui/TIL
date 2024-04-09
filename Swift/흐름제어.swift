// MARK: -  if
let first: Int = 5
let second: Int = 5
var biggerValue: Int = 0

// 조건 수식을 소괄호로 묶어주는 것은 선택사항.
if (first > second) {
    biggerValue = first
} else if (first == second) {
    biggerValue = first
} else if (first < second) {
    biggerValue = second
} else if (first == 5) {
    // first == 5 라는 조건을 충족하나, 이미 위 조건 first == second 를 충족했기에 그 곳에서 실행하고 if 문은 종료. 따라서 실행 되지 않는다.
    biggerValue = 100
}
// 마지막 else 는 생략 가능. 즉 if 단독으로도 사용 가능
print(biggerValue)  // 5


// MARK: - switch
let someCharacter: Character = "z"
switch someCharacter {
case "a":
    print("The first letter of the alphabet")
case "z":
    print("The last letter of the alphabet")
    fallthrough
default:
    print("Some other character")
}

// 와일드카드 식별자를 사용한 튜플 switch case 구성
typealias NameAge = (name: String, age: Int)

let tupleValue: NameAge = ("yungui", 99)

switch tupleValue {
case ("yungui", 50):
    print("정확히 맞췄습니다")
case ("yungui", _):
    print("이름만 맞았습니다. 나이는 \(tupleValue.age)입니다.")
case (_, 99):
    print("나이만 맞았습니다. 이름은 \(tupleValue.name)입니다.")
default:
    print("누굴 찾나요?")
}



// 값 바인딩을 사용한 튜플 switch case 구성
switch tupleValue {
case ("yungui", 50):
    print("정확히 맞췄습니다")
case ("yungui", let age):
    print("이름만 맞았습니다. 나이는 \(age)입니다.")
case (let name, 99):
    print("나이만 맞았습니다. 이름은 \(name)입니다.")
default:
    print("누굴 찾나요?")
}


// 이름만 맞았습니다. 나이는 99입니다.

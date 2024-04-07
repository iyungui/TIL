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


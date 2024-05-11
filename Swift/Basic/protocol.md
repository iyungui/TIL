# Protocols

## 프로토콜이란
- 프로토콜은 특정 역할을 하기 위한 메서드, 프로퍼티, 기타 요구사항 등의 청사진을 정의합니다.
- 구조체, 클래스, 열거형에서 프로토콜을 채택 해서 프로토콜의 요구사항을 구현
- <span style="color:yellow"> 프로토콜은 정의를 하고 제시를 할 뿐, 스스로 기능을 구현하지는 않습니다. </span>


</br>

## 프로토콜 구문
```swift
protocol SomeProtocol {
    // protocol definition goes here
}
```
</br>

구조체, 클래스, 열거형에서 프로토콜을 채택 예시
```swift
struct SomeStructure: FirstProtocol, AnotherProtocol {
    // structure definition goes here
}
```

```swift
class SomeClass: SomeSuperclass, FirstProtocol, AnotherProtocol {
    // class definition goes here
}
```

</br>

## 프로토콜 요구사항

```swift
protocol SomeProtocol {
    var mustBeSettable: Int { get set }
    var doesNotNeedToBeSettable: Int { get }
}
```

SomeProtocol 에 정의된 mustBeSettable 프로퍼티는 get set 모두를 요구했고,
doesNotNeedToBeSettable 은 읽기만 가능하다면 어떻게 구현되어도 괜찮다는 요구사항.

</br>

```swift
protocol AnotherProtocol {
    static var someTypeProperty: Int { get set }
}
```

상속 가능한 class 타입 프로퍼티 , 상속 불가능한 static 타입 프로퍼티 모두, 프로토콜에서는 static 으로 표현

</br>

```swift
protocol FullyNamed {
    var fullName: String { get }
}

struct Person: FullyNamed {
    var fullName: String
}
let john = Person(fullName: "John Appleseed")
// john.fullName is "John Appleseed"

class Starship: FullyNamed {
    var prefix: String?
    var name: String
    init(name: String, prefix: String? = nil) {
        self.name = name
        self.prefix = prefix
    }
    var fullName: String {
        return (prefix != nil ? prefix! + " " : "") + name
    }
}
var ncc1701 = Starship(name: "Enterprise", prefix: "USS")
// ncc1701.fullName is "USS Enterprise"
```

</br>

## 메서드 요구사항

**프로토콜에는 메서드의 바디 (중괄호 부분) 을 제외한, 메서드의 이름, 매개변수, 반환 타입 등만 작성**

```swift
protocol SomeProtocol {
    static func someTypeMethod()
}
```

```swift
protocol RandomNumberGenerator {
    func random() -> Double
}
```

```swift
class LinearCongruentialGenerator: RandomNumberGenerator {
    var lastRandom = 42.0
    let m = 139968.0
    let a = 3877.0
    let c = 29573.0
    func random() -> Double {
        lastRandom = ((lastRandom * a + c)
            .truncatingRemainder(dividingBy:m))
        return lastRandom / m
    }
}
let generator = LinearCongruentialGenerator()
print("Here's a random number: \(generator.random())")
// Prints "Here's a random number: 0.3746499199817101"
print("And another one: \(generator.random())")
// Prints "And another one: 0.729023776863283"
```

</br>

### mutating 메서드 (가변 메서드) 요구사항

<span style="color:yellowgreen"> 값 타입(struct, enum) </span>의 인스턴스 메서드에서 자신 내부의 값을 변경하고자 할 때, func 앞에 mutating 키워드를 적어 메서드에서 인스턴스 내부의 값을 변경하겠다는 것을 명시.

> **mutating** 으로 프로토콜 인스턴스 메서드 요구사항을 표시하면 **클래스**에 대한 해당 메서드의 구현을 작성할 때 mutating 키워드를 작성할 필요가 없습니다. mutating 키워드는 구조체와 열거형에 의해서만 사용됩니다.

</br>

```swift
protocol Togglable {
    mutating func toggle()
}
```

```swift
enum OnOffSwitch: Togglable {
    case off, on
    mutating func toggle() {
        switch self {
        case .off:
            self = .on
        case .on:
            self = .off
        }
    }
}
var lightSwitch = OnOffSwitch.off
lightSwitch.toggle()
// lightSwitch is now equal to .on
```

</br>

## 초기화 구문 요구사항 

프로토콜에서 이니셜라이저를 요구할 때, 이니셜라이저의 매개변수만 지정하고, 중괄호 부분은 구현하지 않습니다.
```swift
protocol SomeProtocol {
    init(someParameter: Int)
}
```

클래스에서 프로토콜에서 요구한 이니셜라이저를 구현할 경우에는, **required** 키워드를 앞에 붙여서 구현한다.

클래스는 상속할 수 있기에, SomeClass 를 상속 받는 모든 하위 클래스는 SomeProtocol 을 준수해야 하며, 이는 곧 상속 받는 클래스에 해당 이니셜라이저를 모두 구현해야 함.

```swift
class SomeClass: SomeProtocol {
    required init(someParameter: Int) {
        // initializer implementation goes here
    }
}
```

> final 클래스는 하위 클래스가 될 수 없으므로 final 수식어로 표시된 클래스에 required 수식어를 프로토콜 초기화 구문 구현에 표시할 필요가 없습니다. 

</br>


```swift
protocol SomeProtocol {
    init()
}

class SomeSuperClass {
    init() {
        // initializer implementation goes here
    }
}

class SomeSubClass: SomeSuperClass, SomeProtocol {
    // "required" from SomeProtocol conformance; "override" from SomeSuperClass
    required override init() {
        // initializer implementation goes here
    }
}
```

### 실패 가능한 초기화 구문 요구사항

---

## 타입으로서 프로토콜

---

## 위임 (Delegation)

**위임 (Delegation) 은 클래스 또는 구조체가 책임의 일부를 다른 타입의 인스턴스에 넘겨주거나 위임할 수 있도록 하는 디자인 패턴**

- 책무를 위임하기 위해 정의한 프로토콜을 준수하는 타입은 자신에게 위임될 일정 책무를 할 수 있다는 것을 보장하게 됩니다.
(자신이 해야할 일을 믿고 맡기는 것)

- 위임은 특정 작업에 응답하거나 해당 소스의 기본 타입을 알 필요 없이 외부 소스에서 데이터를 검색하는데 사용할 수 있습니다.

- 비동기 처리에도 많이 사용

위임 패턴에서는 위임자(delegatee)와 위임받는 객체(delegate)가 있습니다. 위임자는 일부 작업을 위임받는 객체에게 넘겨주고, 위임받는 객체는 이 요구사항을 충족시키기 위해 프로토콜을 준수합니다.

### 위임 패턴의 예시
UITableView 타입의 인스턴스가 해야 하는 일을 위임받아 처리하는 인스턴스는 UITableViewDelegate 프로토콜을 준수하면 됩니다. (UITableViewDelegate 프로토콜을 준수하는 인스턴스는 UITableView 인스턴스가 해야할 일을 대신 처리)

</br>

## 확장으로 프로토콜 준수성 추가 (Adding Protocol Conformance with an Extension)

```swift
protocol TextRepresentable {
    var textualDescription: String { get }
}

extension Dice: TextRepresentable {
    var textualDescription: String {
        return "A \(sides)-sided dice"
    }
}

let d12 = Dice(sides: 12, generator: LinearCongruentialGenerator())
print(d12.textualDescription)
// Prints "A 12-sided dice"
```

### 조건적으로 프로토콜 준수 (Conditionally Conforming to a Protocol)

```swift
extension Array: TextRepresentable where Element: TextRepresentable {
    var textualDescription: String {
        let itemsAsText = self.map { $0.textualDescription }
        return "[" + itemsAsText.joined(separator: ", ") + "]"
    }
}
let myDice = [d6, d12]
print(myDice.textualDescription)
// Prints "[A 6-sided dice, A 12-sided dice]"
```

 Array가 TextRepresentable 프로토콜을 준수하도록 하는 확장은 Element가 TextRepresentable을 준수할 때만 활성화

 </br>

 ### 확장으로 프로토콜 채택 선언 (Declaring Protocol Adoption with an Extension)

```swift
struct Hamster {
    var name: String
    var textualDescription: String {
        return "A hamster named \(name)"
    }
}
extension Hamster: TextRepresentable {}

let simonTheHamster = Hamster(name: "Simon")
let somethingTextRepresentable: TextRepresentable = simonTheHamster
print(somethingTextRepresentable.textualDescription)
// Prints "A hamster named Simon"
```
> 타입은 요구사항이 충족된다고 해서 프로토콜을 자동으로 채택하지 않습니다. 항상 프로토콜 채택을 명시적으로 선언해야 합니다.

</br>

## 합성된 구현을 사용하여 프로토콜 채택 (Adopting a Protocol Using a Synthesized Implementation)

Equatable, Hashable, Comparable 프로토콜이 자동으로 구현
스위프트는 합성된 구현을 제공하여 특정 프로토콜에 대한 요구사항을 자동으로 구현할 수 있게 해줍니다. 

### Equatable
구조체: 모든 저장된 프로퍼티가 Equatable을 준수하는 경우
열거형: 모든 연관된 타입이 Equatable을 준수하거나 연관된 타입이 없는 경우

이 경우에는, == 연산자를 직접 구현하지 않고, 해당 타입의 선언에서 Equatable 프로토콜을 채택하기만 하면 됨

### Hashable
구조체: 모든 저장된 프로퍼티가 Hashable을 준수하는 경우
열거형: 모든 연관된 타입이 Hashable을 준수하거나 연관된 타입이 없는 경우

hash(into:) 메서드를 직접 구현하지 않고, Hashable 프로토콜을 채택

### Comparable
Comparable 프로토콜은 <, <=, >, >= 연산자를 사용하여 인스턴스 간의 순서를 비교

열거형: 원시값이 없고, 모든 연관된 타입이 Comparable을 준수하는 경우

 < 연산자를 직접 구현하지 않고, 열거형 선언에서 Comparable 준수를 선언

</br>

## 프로토콜 타입의 콜렉션 (Collections of Protocol Types)

프로토콜을 타입으로 사용한 예시

```swift
let things: [TextRepresentable] = [game, d12, simonTheHamster]

for thing in things {
    print(thing.textualDescription)
}
// A game of Snakes and Ladders with 25 squares
// A 12-sided dice
// A hamster named Simon
```
각 요소의 구체적인 타입을 몰라도 TextRepresentable 프로토콜을 통해 textualDescription 프로퍼티에 접근할 수 있다.

</br>

## 프로토콜 상속 (Protocol Inheritance)
프로토콜이 하나 이상의 다른 프로토콜을 상속할 수 있다.

```swift
protocol PrettyTextRepresentable: TextRepresentable {
    var prettyTextualDescription: String { get }
}
```

</br>

## 클래스 전용 프로토콜 (Class-Only Protocols)

```swift
protocol SomeClassOnlyProtocol: AnyObject, SomeInheritedProtocol {
    // class-only protocol definition goes here
}
```

## 프로토콜 혼합 (Protocol Composition)

```swift
SomeProtocol & AnotherProtocol
```

```swift
protocol Named {
    var name: String { get }
}
protocol Aged {
    var age: Int { get }
}
struct Person: Named, Aged {
    var name: String
    var age: Int
}
func wishHappyBirthday(to celebrator: Named & Aged) {
    print("Happy birthday, \(celebrator.name), you're \(celebrator.age)!")
}
let birthdayPerson = Person(name: "Malcolm", age: 21)
wishHappyBirthday(to: birthdayPerson)
// Prints "Happy birthday, Malcolm, you're 21!"
```

프로토콜 혼합은 여러 프로토콜을 한 타입이 동시에 준수해야 하는 요구사항을 표현할 때 사용

</br>

## 프로토콜 준수에 대한 검사 (Checking for Protocol Conformance)
타입 캐스팅의 is, as 연산자 사용 가능

- is: 프로토콜을 준수한다면 true 를, 아니라면 false
- as?: 프로토콜 타입의 옵셔널 값을 반환함. 프로토콜을 준수 하지 않으면 nil 반환
- as!: 프로토콜 타입으로 강제 다운 캐스팅을 하고, 강제 다운 캐스팅 성공하지 못하면 런타임 에러


```swift
protocol HasArea {
    var area: Double { get }
}

class Circle: HasArea {
    let pi = 3.1415927
    var radius: Double
    var area: Double { return pi * radius * radius }
    init(radius: Double) { self.radius = radius }
}
class Country: HasArea {
    var area: Double
    init(area: Double) { self.area = area }
}
class Animal {
    var legs: Int
    init(legs: Int) { self.legs = legs }
}

let objects: [AnyObject] = [
    Circle(radius: 2.0),
    Country(area: 243_610),
    Animal(legs: 4)
]

for object in objects {
    if let objectWithArea = object as? HasArea {
        print("Area is \(objectWithArea.area)")
    } else {
        print("Something that doesn't have an area")
    }
}
// Area is 12.5663708
// Area is 243610.0
// Something that doesn't have an area
```
다양한 타입의 인스턴스를 포함하는 컬렉션에서 특정 프로토콜을 준수하는 인스턴스만을 찾아 그 기능을 사용

</br>

## 옵셔널 프로토콜 요구사항 (Optional Protocol Requirements)

- 프로토콜의 요구사항을 옵셔널로 정의.
- @objc 속성으로 표시됨
- **@objc 프로토콜은 클래스에만 가능** (구조체, 열거형은 x)

(Int) -> String 타입의 메서드는 ((Int) -> String)? 이 됩니다.
- 메서드의 반환값이 옵셔널이 된 것이 아니라, 메서드 자체 타입이 옵셔널이 된 것.

- 옵셔널 프로토콜 요구사항은 옵셔널 체이닝으로 호출한다. (프로토콜을 준수하는 타입에 의해 요구사항이 구현되지 않았을 가능성)
someOptionalMethod?(someArgument)

```swift
@objc protocol CounterDataSource {
    @objc optional func increment(forCount count: Int) -> Int
    @objc optional var fixedIncrement: Int { get }
}

class Counter {
    var count = 0
    var dataSource: CounterDataSource?
    func increment() {
        if let amount = dataSource?.increment?(forCount: count) {
            count += amount
        } else if let amount = dataSource?.fixedIncrement {
            count += amount
        }
    }
}
```

</br>

## 프로토콜 확장 (Protocol Extensions)

프로토콜 확장을 사용하면 프로토콜에 기본 구현을 추가할 수 있으며, 이 구현은 프로토콜을 준수하는 모든 타입에서 자동으로 사용할 수 있습니다. 이 기능은 타입마다 **동작을 별도로 정의하지 않고도 프로토콜에 정의된 메서드나 프로퍼티를 기본적으로 사용할 수 있게 해줍니다.**

```swift
protocol RandomNumberGenerator {
    func random() -> Double
}

extension RandomNumberGenerator {
    func randomBool() -> Bool {
        return random() > 0.5
    }
}
```

```swift
class LinearCongruentialGenerator: RandomNumberGenerator {
    func random() -> Double {
        // 예시를 위한 간단한 랜덤 수 생성 로직
        return Double(arc4random()) / Double(UInt32.max)
    }
}

let generator = LinearCongruentialGenerator()
print("Here's a random number: \(generator.random())")
print("And here's a random Boolean: \(generator.randomBool())")
```

### 프로토콜 확장에 제약사항 추가
프로토콜 확장에 제약사항을 추가하여, 확장의 메서드와 프로퍼티가 특정 조건을 만족하는 타입에만 적용되도록 할 수 있습니다. 이는 where 절을 사용하여 구현

```swift
extension Collection where Element: Equatable {
    func allEqual() -> Bool {
        guard let firstElement = first else { return true }
        return allSatisfy { $0 == firstElement }
    }
}

let equalNumbers = [100, 100, 100, 100, 100]
let differentNumbers = [100, 100, 200, 100, 200]

print(equalNumbers.allEqual()) // Prints "true"
print(differentNumbers.allEqual()) // Prints "false"
```
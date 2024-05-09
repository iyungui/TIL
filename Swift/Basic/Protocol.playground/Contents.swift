import Foundation

// MARK: - ERROR HANDLING
enum WebsiteError: Error {
    case noInternetConnection
    case siteDown
    case wrongURL
}

func checkWebsite(siteUp: Bool) throws -> String {
    if siteUp == false {
        throw WebsiteError.siteDown
    }
    return "Site is up"
}

let siteStatus = true
do {
    print(try checkWebsite(siteUp: siteStatus))
} catch {
    print(error)
}


// MARK: - Protocol
protocol CalorieCount {
    var calories: Int { get }
    func description() -> String
}

class Burger: CalorieCount {
    var calories: Int = 800
    
    func description() -> String {
        return "This burger has \(calories) calories"
    }
}

struct Fries: CalorieCount {
    var calories: Int = 500
    func description() -> String {
        return "These fries have \(calories) calories"
    }
}

enum Sauce {
    case chili
    case tomato
}

extension Sauce: CalorieCount {
    var calories: Int {
        switch self {
        case .chili:
            return 50
        case .tomato:
            return 80
        }
    }
    func description() -> String {
        return "This sauce has \(calories) calories"
    }
}

let burger = Burger()
let fries = Fries()
let sauce = Sauce.chili

let foodArray: [CalorieCount] = [burger, fries, sauce]

var totalCalories = 0

for food in foodArray {
    totalCalories += food.calories
}

print(totalCalories)







// 무언가를 수신받을 수 있는 기능
protocol Receiveable {
    func received(data: Any, from: Sendable)
}

// 무언가를 발신할 수 있는 기능
protocol Sendable {
    var from: Sendable { get }
    var to: Receiveable? { get }
    
    func send(data: Any)
    
    static func isSendableInstance(_ instance: Any) -> Bool
}

// 수신 발신이 가능한 클래스
class Message: Sendable, Receiveable {
    // 발신은 발신 가능한 객체, 즉 Sendable 프로토콜을 준수하는 타입의 인스턴스여야 한다.
    var from: Sendable {
        return self
    }
    
    // 상대방은 수신 가능한 객체, 즉 Receiveable 프로토콜을 준수하는 타입의 인스턴스여야 한다.
    var to: Receiveable?
    
    // 메시지를 발신한다
    func send(data: Any) {
        guard let receiver: Receiveable = self.to else {
            print("Message has no receiver")
            return
        }
        // 수신 가능한 인스턴스의 received 메서드를 호출한다
        receiver.received(data: data, from: self.from)
    }
    
    // 메시지를 수신
    func received(data: Any, from: Sendable) {
        print("Message received \(data) from \(from)")
    }
    
    // class 메서드이므로 상속이 가능하다
    class func isSendableInstance(_ instance: Any) -> Bool {
        if let sendableInstance: Sendable = instance as? Sendable {
            return sendableInstance.to != nil
        }
        return false
    }
}

// 수신 발신 가능한 클래스
class Mail: Sendable, Receiveable {
    var from: Sendable {
        return self
    }
    
    var to: Receiveable?
    
    func send(data: Any) {
        guard let receiver: Receiveable = self.to else {
            print("Mail has no receiver")
            return
        }
        receiver.received(data: data, from: self.from)
    }
    
    func received(data: Any, from: Sendable) {
        print("Mail received \(data) from \(from)")
    }
    
    // static 메서드이므로 상속이 불가능하다
    static func isSendableInstance(_ instance: Any) -> Bool {
        if let sendableInstance: Sendable = instance as? Sendable {
            return sendableInstance.to != nil
        }
        return false
    }
}

// 두 Message 인스턴스를 생성한다
let myPhoneMessage: Message = Message()
let yourPhoneMessage: Message = Message()

// 아직 수신받을 인스턴스가 없습니다
myPhoneMessage.send(data: "Hello")  // Message has no receiver


// Message 인스턴스는 발신 수신이 모두 가능하므로 메시지 주고 받기 가능
myPhoneMessage.to = yourPhoneMessage
myPhoneMessage.send(data: "Hello")  // Message received Hello from __lldb_expr_6.Message


// 두 Mail 인스턴스를 생성한다
let myMail: Mail = Mail()
let yourMail: Mail = Mail()

myMail.send(data: "Hi") // Mail has no receiver
myMail.to = yourMail

myMail.send(data: "Hi") // Mail received Hi from __lldb_expr_16.Mail

myMail.to = myPhoneMessage
myMail.send(data: "Bye")    // Message received Bye from __lldb_expr_20.Mail

// String 은 Sendable 프로토콜을 준수하지 않습니다
Message.isSendableInstance("Hello") // false

// Mail 과 Message 는 Sendable 프로토콜을 준수합니다
Message.isSendableInstance(myPhoneMessage)  // true

// yourPhoneMessage 는 to 프로퍼티가 설정되지 않아서 보낼 수 없는 상태입니다
Message.isSendableInstance(yourPhoneMessage)    // false
Mail.isSendableInstance(myPhoneMessage) // true
Mail.isSendableInstance(myMail) // true



protocol Resettable {
    mutating func reset()
}

//class Person: Resettable {
//    var name: String?
//    var age: Int?
//    
//    func reset() {  // class 에는 mutating 키워드를 제외함
//        self.name = nil
//        self.age = nil
//    }
//}
//
//struct Point: Resettable {
//    var x: Int = 0
//    var y: Int = 0
//    
//    mutating func reset() {
//        self.x = 0
//        self.y = 0
//    }
//}
//
//enum Direction: Resettable {
//    case east, west, south, north, unknown
//    
//    mutating func reset() {
//        self = Direction.unknown
//    }
//}


//protocol Named {
//    var name: String { get }
//    
//    init(name: String)
//}
//
//struct Pet: Named {
//    var name: String
//    
//    init(name: String) {
//        self.name = name
//    }
//}
//
//final class Person: Named {
//    var name: String
//    
//    init(name: String) {
//        self.name = name
//    }
//}

//class School {
//    var name: String
//    
//    // School 클래스는 Named 프로토콜을 채택하지 않았지만, Named 프로토콜이 요구하는 이니셜라이저를 구현한 경우.
//    init(name: String) {
//        self.name = name
//    }
//}
//
//class MiddleSchool: School, Named {
//    // 이렇게 부모 클래스에서 프로토콜이 요구하는 이니셜라이저를 모두 구현한 경우, required 와 override 식별자를 모두 명시하도록 한다
//    // School 클래스에서 상속받은 init(name: ) 이니셜라이저를 재정의해야 하며, 동시에 Named 프로토콜의 이니셜라이저 요구도 충족시켜줘야 하므로, 모두 표기한다. (override required 도 가능)
//    required override init(name: String) {
//        super.init(name: name)
//    }
//}


//protocol Named {
//    var name: String { get }
//    
//    init?(name: String)
//}

struct Animal: Named {
    var name: String
    
    init!(name: String) {
        self.name = name
    }
}

struct Pet: Named {
    var name: String
    
    init(name: String) {
        self.name = name
    }
}

//class Person: Named {
//    var name: String
//    
//    required init(name: String) {
//        self.name = name
//    }
//}

class School: Named {
    var name: String
    
    required init?(name: String) {
        self.name = name
    }
}

protocol Readable {
    func read()
}

protocol Writeable {
    func write()
}

protocol ReadSpeakable: Readable {
    func speak()
}

protocol ReadWriteSpeakable: Readable, Writeable {
    func speak()
}

//class SomeClass: ReadWriteSpeakable {
//    func read() {
//        print("Read")
//    }
//    
//    func write() {
//        print("Write")
//    }
//    
//    func speak() {
//        print("Speak")
//    }
//}


protocol ClassOnlyProtocol: class, Readable, Writeable {
    
}

class SomeClass: ClassOnlyProtocol {
    func read() { }
    func write() { }
}

// Non-class type 'SomeStruct' cannot conform to class protocol 'ClassOnlyProtocol'
//struct SomeStruct: ClassOnlyProtocol {
//    func read() { }
//    func write() { }
//}


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

class Car: Named {
    var name: String
    
    init(name: String) {
        self.name = name
    }
}

class Truck: Car, Aged {
    var age: Int
    
    init(name: String, age: Int) {
        self.age = age
        super.init(name: name)
    }
}

func celebrateBirthday(to celebrator: Named & Aged)  {
    print("Happy birthday \(celebrator.name)!! Now you are \(celebrator.age)")
}

let iyungui = Person(name: "iyungui", age: 25)

celebrateBirthday(to: iyungui)

let myCar: Car = Car(name: "Genesis Motor")
//celebrateBirthday(to: myCar)    // Argument type 'Car' does not conform to expected type 'Aged'

// class & protocol 조합에서 class 타입은 한 타입만 조합 가능
//var someVariable: Car & Truck & Aged // Protocol-constrained type cannot contain class 'Truck' because it already contains class 'Car'

// Car class 의 인스턴스 역할을 수행할 수 있고, Aged 프로토콜을 준수하는 인스턴스만 할당할 수 있다. !!
var someVariable: Car & Aged

// Truck 인스턴스는 Car 클래스 역할도 할 수 있고, Aged 프로토콜도 준수하므로 할당할 수 있다.
someVariable = Truck(name: "Truck", age: 5)



// MARK: - Protocol 확인 및 캐스팅

print(iyungui is Named)
print(iyungui is Aged)

print(myCar is Named)
print(myCar is Aged)


if let castedInstance: Named = iyungui as? Named {
    print("\(castedInstance) is Named")
} // Person is Named

if let castedInstance: Named = myCar as? Named {
    print("\(castedInstance) is Named")
    // Car is Named
}

if let castedInstance: Aged = myCar as? Aged {
    print("\(castedInstance) is Aged")
}


// MARK: - 프로토콜의 선택적 요구
@objc protocol Moveable {
    func walk()
    @objc optional func fly() // optional 식별자 필요
}

// objc 속성의 프로토콜을 사용하기 위해 Objective-C 클래스인 NSObject를 상속 받음.
class Tiger: NSObject, Moveable {
    func walk() {
        print("Tiger walks")
    }
}

class Bird: NSObject, Moveable {
    func walk() {
        print("Bird walks")
    }
    
    func fly() {
        print("Bird flys")
    }
}

let tiger: Tiger = Tiger()
let bird: Bird = Bird()

tiger.walk()
bird.walk()
bird.fly()
var moveableInstance: Moveable = tiger
moveableInstance.fly?() // nil

moveableInstance = bird
moveableInstance.fly?() // Bird flys


// MARK: - 프로토콜 변수/ 상수

//protocol Named {
//    var name: String { get }
//
//    init?(name: String)
//}
//
//struct Animal: Named {
//    var name: String
//    
//    init!(name: String) {
//        self.name = name
//    }
//}
//
//struct Pet: Named {
//    var name: String
//    
//    init(name: String) {
//        self.name = name
//    }
//}
//
//class Person: Named {
//    var name: String
//
//    required init(name: String) {
//        self.name = name
//    }
//}
//
//class School: Named {
//    var name: String
//    
//    required init?(name: String) {
//        self.name = name
//    }
//}
//
//var someNamed: Named = Animal(name: "Animal")
//someNamed = Pet(name: "Pet")
//someNamed = Person(name: "Person")
//someNamed = School(name: "School")



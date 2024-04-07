// // MARK: -  tuple

// var person: (name: String, age: Int, height: Double) = ("iyungui", 24, 171.1)

// print(person)
// print(person.0)
// print(person.name)

// typealias PersonTuple = (name: String, age: Int, height: Double)
// let william: PersonTuple = ("will", 12, 158.2)

// MARK: - Array

var names: [String] = []


names.append("iyungui")
names.append(contentsOf: ["yagom", "iOS"])
names.insert("minsoo", at: 0)
print(names.firstIndex(of: "minsoo"))
print(names)


// MARK: - Overloading

func printNumber(number: Int) {
    print("Int: \(number)")
}

func printNumber(number: Double) {
    print("Double: \(number)")
}

func printNumber(number: Int, extra: String) {
    print("Int: \(number), Extra: \(extra)")
}

// 이러한 함수들은 모두 오버로딩되어 있으며, 호출 시 매개변수의 타입과 개수에 따라 적절한 함수가 실행됨
printNumber(number: 5)              // Int: 5
printNumber(number: 3.14)           // Double: 3.14
printNumber(number: 10, extra: "USD") // Int: 10, Extra: USD



// MARK: - Overriding

class Animal {
    func makeSound() {
        print("animal sound")
    }
}

class Dog: Animal {
    override func makeSound() {
        print("bark")
    }
}

let myDog = Dog()
myDog.makeSound()  // "bark", 서브클래스에서 오버라이드한 메서드가 호출됨




// MARK: - Basic Function

func hello(name: String) -> String {
    return "Hello \(name)!"
}

let helloJenny: String = hello(name: "Jenny")
print(helloJenny)    // Hello Jenny!


// Argument Label
func sayHello(from myName:String, to name:String) -> String {
    return "Hello \(name)! I'm \(myName)"
}

print(sayHello(from: "iyungui", to: "Jenny"))    // Hello Jenny! I'm iyungui


// No use argument label
func sayHello(_ name: String, _ times: Int) -> String {
    var result: String = ""
    
    for _ in 0..<times {
        result += "Hello \(name)!" + " "
    }
    
    return result
}

print(sayHello("Chope", 2))     // Hello Chope! Hello Chope!




// MARK: -  Default parameter

func sayHello(_ name: String, times: Int = 3) -> String {
    var result: String = ""
    
    for _ in 0..<times {
        result += "Hello \(name)!" + " "
    }
    
    return result
}

print(sayHello("Hana"))
print(sayHello("Joe", times: 2))



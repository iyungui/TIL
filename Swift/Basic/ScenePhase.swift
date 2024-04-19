

import SwiftUI

@main
struct LifecycleDemoApp: App {
    
    @Environment(\.scenePhase) private var scenePhase
    
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: scenePhase) { (oldScenePhase, newScenePhase) in
            switch newScenePhase {
            case .active:
                print("Active \(oldScenePhase)")
            case .inactive:
                print("Inactive \(oldScenePhase)")
            case .background:
                print("Background")
            default:
                print("Unknown scenephase")
            }
        }
    }
}

/*

ScenePhase 는 현재 화면의 상태를 저장하기 위해 SwiftUI 에서 사용하는 @Environment 속성이다.

다음 예제와 같이 onChange() 수정자와 함께 쓰여, 화면 활성화/비활성화, 포그라운드/백그라운드 전환을 모니터링 할 수 있다.

*/
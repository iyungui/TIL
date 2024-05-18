//
//  ContentView.swift
//  HelloAR
//
//  Created by 이융의 on 5/17/24.
//

import SwiftUI
import RealityKit

struct ContentView : View {
    var body: some View {
        ARViewContainer().edgesIgnoringSafeArea(.all)
    }
}

struct ARViewContainer: UIViewRepresentable {
    
    func makeUIView(context: Context) -> ARView {
        
        let arView = ARView(frame: .zero)
        
        let anchor = AnchorEntity(plane: .horizontal)
        
        let material = SimpleMaterial(color: .blue, isMetallic: true)
        let box = ModelEntity(mesh: MeshResource.generateBox(size: 0.3), materials: [material])
        
        anchor.addChild(box)
        arView.scene.anchors.append(anchor)
        
        return arView
        
    }
    
    func updateUIView(_ uiView: ARView, context: Context) {}
    
}

#Preview {
    ContentView()
}

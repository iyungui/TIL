//
//  Coordinator.swift
//  HelloAR
//
//  Created by 이융의 on 5/19/24.
//

import Foundation
import ARKit
import RealityKit

class Coordinator: NSObject {
    
    weak var view: ARView?
    
    @objc func handleTap(_ recognizer: UITapGestureRecognizer) {
        
        guard let view = self.view else { return }
        
        let tapLocation = recognizer.location(in: view)
        
        let results = view.raycast(from: tapLocation, allowing: .estimatedPlane, alignment: .horizontal)
        
        if let result = results.first {
            // ARAnchor - ARKit Framework
            // AnchorEntity - RealityKit Framework
            
            let anchorEntity = AnchorEntity(raycastResult: result)
            
            let modelEntity = ModelEntity(mesh: MeshResource.generateBox(size: 0.3))
            modelEntity.generateCollisionShapes(recursive: true)
            modelEntity.model?.materials = [SimpleMaterial(color: .blue, isMetallic: true)]
            anchorEntity.addChild(modelEntity)
            
            view.scene.addAnchor(anchorEntity)
            view.installGestures(.all, for: modelEntity)
        }
        
    }
}

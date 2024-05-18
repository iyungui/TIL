//
//  ContentView.swift
//  halfModal
//
//  Created by 이융의 on 5/18/24.
//

import SwiftUI

struct ContentView: View {
    @State private var showModal: Bool = false
    @State private var text: String = ""
    var body: some View {
        VStack {
            Button {
                showModal = true
            } label: {
                Text("show Modal")
                    .font(.headline)
            }
        }
        .sheet(isPresented: $showModal) {
            VStack {
                HStack {
                    Button("Cancel") {
                        showModal = false
                    }
                    .padding()
                    Spacer()
                }
                
                Spacer()
                
                TextField("TextField", text: $text)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding()
                Spacer()

            }
            .presentationDetents([.medium])
            .presentationDragIndicator(.visible)
        }
        .padding()
    }
}

#Preview {
    ContentView()
}

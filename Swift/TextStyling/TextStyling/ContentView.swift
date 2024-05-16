//
//  ContentView.swift
//  TextStyling
//
//  Created by 이융의 on 5/16/24.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        Button("Standard Button") {}
            .buttonStyle(DefaultButtonStyle())
    }
}

struct DefaultButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding(16)
            .background(Color(red: 0.725, green: 0.568, blue: 0.960))
            .foregroundStyle(Color(red: 0.149, green: 0.149, blue: 0.149))
            .font(.headline)
            .clipShape(
                RoundedRectangle(
                    cornerRadius: 16, style: .continuous
                )
            )
    }
}

#Preview {
    ContentView()
}

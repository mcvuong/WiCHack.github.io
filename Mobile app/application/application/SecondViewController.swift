//
//  SecondViewController.swift
//  application
//
//  Created by Mary Vuong on 2/29/20.
//  Copyright © 2020 Mary Vuong. All rights reserved.
//

import Foundation
import UIKit
import WebKit

class SecondViewController: UIViewController {
    @IBOutlet weak var WebView: WKWebView!
    override func viewDidLoad() {
        super.viewDidLoad()
        self.navigationItem.hidesBackButton = true
        self.navigationController?.navigationBar.topItem?.title = " "
            
        let url = URL(string: "https://google.com")
        let request = URLRequest(url: url!)
    
        WebView.load(request)
    }
}

package com.example.projectManagement;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ServerStatusController {
    @RequestMapping("/")
    public String hello(){
        return "Server is up and running";
        
    }
    @RequestMapping("/page1")
    public String page1(){
        return "this is page 1";
    }

}
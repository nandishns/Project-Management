package com.example.bootApp;

/**
 * ServerStatusController
 */
@RestController
public class ServerStatusController {

    @RequestMapping('/')
    public String hello() {
        return "Server is up and running";
    }

}
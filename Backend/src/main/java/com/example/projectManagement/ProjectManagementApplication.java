package com.example.projectManagement;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ProjectManagementApplication {

	public static void main(String[] args) {
	FileInputStream serviceAccount = new FileInputStream("");
	
    @SuppressWarnings("deprecation")
    FirebaseOptions options = new FirebaseOptions.Builder()
            .setCredentials(GoogleCredentials.fromStream(serviceAccount))
            .build();
    FirebaseApp.initializeApp(options);
		SpringApplication.run(ProjectManagementApplication.class, args);
	}

}

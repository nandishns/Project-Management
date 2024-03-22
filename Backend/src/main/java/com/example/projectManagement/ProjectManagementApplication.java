package com.example.projectManagement;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ProjectManagementApplication {

	public static void main(String[] args) {
		FileInputStream serviceAccount = new FileInputStream("Backend\\java-project-638c1-firebase-adminsdk-6oqtc-c450021a14.json");
    	@SuppressWarnings("deprecation")
    FirebaseOptions options = new FirebaseOptions.Builder()
            .setCredentials(GoogleCredentials.fromStream(serviceAccount))
            .build();
    FirebaseApp.initializeApp(options);
		SpringApplication.run(ProjectManagementApplication.class, args);
	}

}

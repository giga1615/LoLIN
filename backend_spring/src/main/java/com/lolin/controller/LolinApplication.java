package com.lolin.controller;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@ComponentScan("com.lolin.*")
@SpringBootApplication
public class LolinApplication {

	public static void main(String[] args) {
		SpringApplication.run(LolinApplication.class, args);
	}

}

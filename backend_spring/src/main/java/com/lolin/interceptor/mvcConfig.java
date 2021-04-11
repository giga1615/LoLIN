package com.lolin.interceptor;

import java.util.Arrays;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.MediaType;
import org.springframework.http.converter.HttpMessageConverter;
import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.servlet.config.annotation.*;

import com.lolin.service.RecommendationService;

@Configuration
@EnableWebMvc
public class mvcConfig implements WebMvcConfigurer {
	//파이썬 다룰때 기본적용 경로만 사용하면됨
	private static final String[] EXCLUDE_PATHS = { "/", "/member/login",  "/lolin/**"

	};




// 전역의 Corss Origin 처리를 해준다.
	@Override
	public void addCorsMappings(CorsRegistry registry) {
		registry.addMapping("/**").allowedOrigins("*").allowedMethods("GET", "POST", "PUT", "DELETE");

	}
	
	
	
			
			
			

}

package com.lolin.interceptor;

import java.util.Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.*;

@Configuration
@EnableWebMvc
public class InterceptorConfig implements WebMvcConfigurer {
	//파이썬 다룰때 기본적용 경로만 사용하면됨
	private static final String[] EXCLUDE_PATHS = { "/", "/member/login",  "/lolin/**"

	};

	@Autowired
	private Interceptor jwtInterceptor;

	@Override
	public void addInterceptors(InterceptorRegistry registry) {


	}

//Interceptor를 이용해서 처리하므로 전역의 Corss Origin 처리를 해준다.
	@Override
	public void addCorsMappings(CorsRegistry registry) {
		registry.addMapping("/**").allowedOrigins("*").allowedMethods("GET", "POST", "PUT", "DELETE");

	}

}

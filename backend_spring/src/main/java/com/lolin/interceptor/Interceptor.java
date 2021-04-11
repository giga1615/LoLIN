package com.lolin.interceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.servlet.HandlerInterceptor;

import com.lolin.service.JwtService;




@Component
public class Interceptor implements HandlerInterceptor{
	
	public static final Logger logger = LoggerFactory.getLogger(Interceptor.class);
	
	private static final String HEADER_AUTH = "jwt";

	@Autowired
	private JwtService jwtService;

	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		
		

		return false;

	}
}

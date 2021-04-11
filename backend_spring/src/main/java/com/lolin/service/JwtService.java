package com.lolin.service;

import java.io.UnsupportedEncodingException;
import java.sql.SQLException;
import java.util.Map;

import org.springframework.security.core.Authentication;

import com.lolin.model.MemberDto;

import io.jsonwebtoken.ExpiredJwtException;
import io.jsonwebtoken.MalformedJwtException;
import io.jsonwebtoken.SignatureException;
import io.jsonwebtoken.UnsupportedJwtException;

public interface JwtService {

	String createToken(String id, String nickName);

	public String getIdByJWT(String jwt) throws UnsupportedEncodingException;

	public String getNickNameByJWT(String jwt) throws UnsupportedEncodingException;



}

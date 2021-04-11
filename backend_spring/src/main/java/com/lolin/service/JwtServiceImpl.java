package com.lolin.service;

import java.io.UnsupportedEncodingException;
import java.sql.SQLException;
import java.util.Base64;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

import com.lolin.model.MemberDto;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.ExpiredJwtException;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.MalformedJwtException;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.SignatureException;
import io.jsonwebtoken.UnsupportedJwtException;

@Service
public class JwtServiceImpl implements JwtService {
	@Autowired
	private SqlSession session;

	@Autowired
	CustomUserDetailService userDetailsService;

	static String secretKey = "mysecurityjwtservicesuccess";
	private static final String SECRET_KEY = Base64.getEncoder().encodeToString(secretKey.getBytes());

	Long expiredTime = 1000 * 60L * 60L * 8L; // 토큰 유효 시간 (8시간)

	// 최초 로그인시에 생성해서 프론트에서 localstorage나 쿠키에 저장을 해준다.
	@Override
	public String createToken(String id, String nickName) {

		// Header 부분 설정
		Map<String, Object> headers = new HashMap<>();
		headers.put("typ", "JWT");
		headers.put("alg", "HS256");

		// payload 부분 설정
		Map<String, Object> payloads = new HashMap<>();
		// 여기서 dao로 불러와서 payloads에 삽입
		payloads.put("id", id);
		payloads.put("nickName", nickName);

		Date ext = new Date(); // 토큰 만료 시간
		ext.setTime(ext.getTime() + expiredTime);

		// 토큰 Builder
		String jwt = Jwts.builder().setHeader(headers) // Headers 설정
				.setClaims(payloads) // Claims 설정
				.setExpiration(ext) // 토큰 만료 시간 설정
				.signWith(SignatureAlgorithm.HS256, SECRET_KEY.getBytes()) // HS256과 Key로 Sign
				.compact(); // 토큰 생성

		return jwt;// jwt생성된것임 따로 세션이나 저장할 필요없음

	}

	@Override
	public String getIdByJWT(String jwt) throws UnsupportedEncodingException {

		Map<String, Object> claimMap = null;

		try {
			Claims claims = Jwts.parser().setSigningKey(SECRET_KEY.getBytes("UTF-8")) // Set Key
					.parseClaimsJws(jwt) // 파싱 및 검증, 실패 시 에러
					.getBody();

			claimMap = claims;

			// Date expiration = claims.get("exp", Date.class);
			// String data = claims.get("data", String.class);

		} catch (ExpiredJwtException e) { // 토큰이 만료되었을 경우

			System.out.println(e);

		} catch (Exception e) { // 그외 에러났을 경우

			System.out.println(e);

		}
		return (String) claimMap.get("id");// 토큰이 검증되면, map을 가져다가 쓸수있음 claim은 map으로 이루어져있음
	}

	@Override
	public String getNickNameByJWT(String jwt) throws UnsupportedEncodingException {

		Map<String, Object> claimMap = null;

		try {
			Claims claims = Jwts.parser().setSigningKey(SECRET_KEY.getBytes("UTF-8")) // Set Key
					.parseClaimsJws(jwt) // 파싱 및 검증, 실패 시 에러
					.getBody();

			claimMap = claims;

			// Date expiration = claims.get("exp", Date.class);
			// String data = claims.get("data", String.class);

		} catch (ExpiredJwtException e) { // 토큰이 만료되었을 경우

			System.out.println(e);

		} catch (Exception e) { // 그외 에러났을 경우

			System.out.println(e);

		}
		return (String) claimMap.get("nickName");// 토큰이 검증되면, map을 가져다가 쓸수있음 claim은 map으로 이루어져있음
	}

}

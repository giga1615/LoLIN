package com.lolin.controller;

import java.io.UnsupportedEncodingException;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.lolin.model.ConnectionDto;
import com.lolin.model.RecommendedUserDto;
import com.lolin.service.JwtService;
import com.lolin.service.MemberService;
import com.lolin.service.PythonService;
import com.lolin.service.RecommendationService;

@CrossOrigin(origins = { "*" }, maxAge = 6000)
@RestController
@RequestMapping("/api/recommend")
public class RecommendationController {

	@Autowired
	JwtService jwtService;

	@Autowired
	PythonService pythonService;
	
	@Autowired
	MemberService memberService;

	@Autowired
	RecommendationService recommendationService;

	@GetMapping("/getRecommendedUser")
	public ResponseEntity<List<RecommendedUserDto>> recommand(
			@RequestParam(value = "selectedPosition", required = false) String selectedPosition,
			@RequestParam(value = "selectedGameStyle", required = false) String selectedGameStyle,
			@RequestParam(value = "jwt", required = false) String jwt) throws UnsupportedEncodingException {

		RecommendedUserDto recommendedUserDto = new RecommendedUserDto();

		try {
			recommendedUserDto = recommendationService.getMyInfo(jwtService.getNickNameByJWT(jwt),memberService.getID(jwtService.getNickNameByJWT(jwt)) );
		} catch (Exception e1) {
			e1.printStackTrace();
		}
		String nickName = recommendedUserDto.getNickname();
		double time = recommendedUserDto.getTime_predict();
		String tier = recommendedUserDto.getTier();

		List<RecommendedUserDto> list = null;
		HttpStatus status = null;

		try {
			list = recommendationService.getRecommendedUser(selectedPosition, selectedGameStyle, tier, nickName, time);

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		System.out.println(list);

		status = HttpStatus.ACCEPTED;

		return new ResponseEntity<List<RecommendedUserDto>>(list, status);

	}
	
	

	@GetMapping("/getMyInfo")
	public ResponseEntity<RecommendedUserDto> getMyInfo(@RequestParam(value = "jwt", required = false) String jwt)
			throws UnsupportedEncodingException {

		RecommendedUserDto recommendedUserDto = new RecommendedUserDto();

		HttpStatus status = null;

		String nickName = jwtService.getNickNameByJWT(jwt);

		try {
			recommendedUserDto = recommendationService.getMyInfo(nickName,memberService.getID(jwtService.getNickNameByJWT(jwt)));

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		status = HttpStatus.ACCEPTED;

		return new ResponseEntity<RecommendedUserDto>(recommendedUserDto, status);

	}
	
	@GetMapping("/getYourInfo")
	public ResponseEntity<RecommendedUserDto> getYourInfo(
			@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "yourNickname", required = false) String yourNickname)
			throws UnsupportedEncodingException {

		RecommendedUserDto recommendedUserDto = new RecommendedUserDto();

		HttpStatus status = null;

		

		try {
			recommendedUserDto = recommendationService.getMyInfo(yourNickname,memberService.getID(yourNickname));

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		status = HttpStatus.ACCEPTED;

		return new ResponseEntity<RecommendedUserDto>(recommendedUserDto, status);

	}
	
	@GetMapping("/getRecommendedUserAll")
	public ResponseEntity<List<RecommendedUserDto>> recommandAll(
			@RequestParam(value = "jwt", required = false) String jwt) throws UnsupportedEncodingException{
		
		
		RecommendedUserDto recommendedUserDto = new RecommendedUserDto();

		String nickName=jwtService.getNickNameByJWT(jwt);



		List<RecommendedUserDto> list = null;
		HttpStatus status = null;

		try {
			//nickName not like;
			list = recommendationService.getReadAllrecommend(nickName);

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		System.out.println(list);

		status = HttpStatus.ACCEPTED;

		return new ResponseEntity<List<RecommendedUserDto>>(list, status);
	}
			
	

}

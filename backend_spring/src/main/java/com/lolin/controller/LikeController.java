package com.lolin.controller;

import java.io.UnsupportedEncodingException;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.lolin.model.ConnectionDto;
import com.lolin.model.LikeDto;
import com.lolin.service.JwtService;
import com.lolin.service.LikeService;
import com.lolin.service.LoginService;
import com.lolin.service.MemberService;
import com.lolin.service.MultiChatService;
import com.lolin.service.RiotApiService;

@RestController
@RequestMapping("/api/like")
public class LikeController {

	@Autowired
	LikeService likeService;

	@Autowired
	JwtService jwtService;

	@PostMapping("/ilikeU/plus")
	public ResponseEntity<Map<String, Object>> iLikeUPlus(@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "yourNickname", required = false) String your_nickname)
			throws UnsupportedEncodingException {

		
		String my_id = jwtService.getIdByJWT(jwt);
		String my_nickname = jwtService.getNickNameByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();
		System.out.println("my"+my_id);
		System.out.println("my"+my_nickname);
		System.out.println(your_nickname);
		HttpStatus status = null;

		try {
			likeService.likePlus(my_id, my_nickname, your_nickname);

			resultMap.put("message", "SUCCESS");

			status = HttpStatus.ACCEPTED;

		} catch (SQLException e) {

			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");

			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);

	}

	@DeleteMapping("/ilikeU/minus")
	public ResponseEntity<Map<String, Object>> iLikeUMinus(@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "yourNickname", required = false) String your_nickname)
			throws UnsupportedEncodingException {

		String id = jwtService.getIdByJWT(jwt);
		String my_nickname = jwtService.getNickNameByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {
			likeService.likeMinus(my_nickname, your_nickname);

			resultMap.put("message", "SUCCESS");

			status = HttpStatus.ACCEPTED;

		} catch (SQLException e) {

			// 로그인 실패
			// 클라이언트에게 전달
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");

			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);

	}

	@GetMapping("/ilikeU/readMyList")
	public ResponseEntity<List<LikeDto>> iLikeUread(@RequestParam(value = "jwt", required = false) String jwt)
			throws UnsupportedEncodingException {

		// 아이디만 넘겨주면됨
		String my_id = jwtService.getIdByJWT(jwt);

		HttpStatus status = null;

		List<LikeDto> list = null;

		try {
			list = likeService.likeRead(my_id);
			status = HttpStatus.ACCEPTED;
		} catch (SQLException e) {
			list = null;

			e.printStackTrace();
			status = HttpStatus.INTERNAL_SERVER_ERROR;
		}

		return new ResponseEntity<List<LikeDto>>(list, status);
	}

}

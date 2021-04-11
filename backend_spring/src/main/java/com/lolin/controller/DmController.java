package com.lolin.controller;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.lolin.model.DmMessageDto;
import com.lolin.service.DmService;
import com.lolin.service.JwtService;
import com.lolin.service.MemberService;
import com.lolin.service.RiotApiService;

@CrossOrigin(origins = { "*" }, maxAge = 6000)
@RestController
@RequestMapping("/api/chat")
public class DmController {

	@Autowired
	DmService chatService;

	@Autowired
	MemberService memberService;

	@Autowired
	JwtService jwtService;

	@Autowired
	RiotApiService riotApiService;

	// DM 보내기
	@PostMapping("/sendDm")
	public ResponseEntity<Map<String, Object>> sendDm(@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "yourNickName", required = false) String yourNickName,
			@RequestParam(value = "messageData", required = false) String messageData) throws Exception {

		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		String myNickName = jwtService.getNickNameByJWT(jwt);
		String myId = jwtService.getIdByJWT(jwt);
		// 메시지 객체
		DmMessageDto message = new DmMessageDto(myNickName, yourNickName, messageData);
		if (messageData != null)
			try {
				// 아이디, 닉네임, 메시지 설정
				// System.out.println(myNickName);
				String yourId = memberService.getID(yourNickName);
				// System.out.println(yourNickName);

				message.setMyId(myId);
				message.setYourId(yourId);
				message.setMyNickName(myNickName);
				message.setYourNickName(yourNickName);
				message.setMessageData(messageData);
				// insert
				System.out.println(message);
				chatService.sendDm(message);
				resultMap.put("message", "SUCCESS");
				status = HttpStatus.ACCEPTED;
			} catch (SQLException e) {
				status = HttpStatus.INTERNAL_SERVER_ERROR;
				resultMap.put("message", "FAIL");
				e.printStackTrace();
			}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	// DM 읽기
	@GetMapping("/readDm")
	public ResponseEntity<Map<String, Object>> readDm(@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "yourNickName", required = false) String yourNickName) throws Exception {

		String myNickName = jwtService.getNickNameByJWT(jwt);

		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {
			// 상대닉네임을 통해 채팅 내역 불러옴
			System.out.println(myNickName + " " + yourNickName);
			List<DmMessageDto> messagelist = chatService.readDmByNickName(myNickName, yourNickName);
			System.out.println(messagelist);
			resultMap.put("message", "SUCCESS");
			resultMap.put("dmData", messagelist);
			status = HttpStatus.ACCEPTED;
		} catch (SQLException e) {
			resultMap.put("message", "FAIL");
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	@GetMapping("/readDmList")
	public ResponseEntity<Map<String, Object>> readDmList(@RequestParam(value = "jwt", required = false) String jwt)
			throws Exception {

		String myId = jwtService.getIdByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {
			// 내 아이디를 검색해서 나와 채팅이 있는 사람들 ID 얻음
			List<String> dmlist = chatService.getDmList(myId);

			resultMap.put("message", "SUCCESS");
			resultMap.put("dmList", dmlist);
			// System.out.println(urlList);
			status = HttpStatus.ACCEPTED;
		} catch (SQLException e) {
			resultMap.put("message", "FAIL");
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			e.printStackTrace();
		}
		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

}

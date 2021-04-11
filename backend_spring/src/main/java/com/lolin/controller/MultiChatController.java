package com.lolin.controller;

import java.io.UnsupportedEncodingException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.lolin.model.MultiChatRoomMessageDto;
import com.lolin.model.IconDto;
import com.lolin.model.MemberDto;
import com.lolin.model.MyRoomListDto;
import com.lolin.service.MultiChatService;
import com.lolin.service.JwtService;
import com.lolin.service.LoginService;
import com.lolin.service.MemberService;
import com.lolin.service.RiotApiService;

@RestController
@RequestMapping("/api/chat")
public class MultiChatController {

	@Autowired
	MultiChatService chattingService;

	@Autowired
	JwtService jwtService;

	@Autowired
	MemberService memberService;

	@Autowired
	RiotApiService riotApiService;

	@PostMapping("/makeChatRoom")
	public ResponseEntity<Map<String, Object>> makeChatRoom(@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "roomName", required = false) String roomName) throws UnsupportedEncodingException {
		String id = jwtService.getIdByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;

		try {
			// 닉네임을 가져와서 닉네임리스트에다가 bangJangList
			String nickName = memberService.getNickName(id);
			// String id2 = memberService.getID(nickName);

			chattingService.makeChatRoom(id, nickName, roomName);

			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");

			// System.out.println(nickName);
		} catch (SQLException e) {
			// TODO Auto-generated catch block

			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	// 초대절차 -1 어떤방에 초대할지 방장이 선택함
	// 방장의 채팅목록을 보여줌
	// 방장뿐만아니라 이걸사용해서 다른사람도 채팅 목록을 가져올 수 있음
	// @이건 초대하는사람
	// 방이름과, 방번호(번호는 안보여줘도됨)
	@GetMapping("/showMyRoomList")
	public ResponseEntity<Map<String, Object>> showMyRoomList(@RequestParam(value = "jwt", required = false) String jwt)
			throws UnsupportedEncodingException {
		String id = jwtService.getIdByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;

		try {
			// 닉네임을 가져와서 닉네임리스트에다가 bangJangList
			String nickName = memberService.getNickName(id);
			List<MyRoomListDto> list = chattingService.getMyRoomList(nickName);
			// String id2 = memberService.getID(nickName);

			// System.out.println(list);

			// 채팅방 인원수 리스트
			List<Integer> countList = new ArrayList<>();

			for (int i = 0; i < list.size(); i++) {
				String roomNumber = list.get(i).getRoomNumber();
				int num = Integer.parseInt(roomNumber);
				countList.add(chattingService.getCountRoomMember(num) + 1);
			}

			// chattingService.makeChatRoom(id, nickName, roomName);
			// System.out.println(countList);
			// System.out.println(nickName);
			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");
			resultMap.put("myRoomList", list);
			resultMap.put("countList", countList);

		} catch (SQLException e) {
			// TODO Auto-generated catch block
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	// 초대절차 -2 1번으로 방을 선택하고, 그 방이름을 초대받는 사람에게 보내서 방에 입장시킴
	// @이건 초대받는사람
	@PostMapping("/inviteMember")
	public ResponseEntity<Map<String, Object>> inviteMember(@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "roomName", required = false) String roomName,
			@RequestParam(value = "memberNickName", required = false) String memberNickName) {

		// 내아이디로 내가 만든 방 목록을 프론트엔드에 줘서
		// 프론트엔드가 방목록중 어떤방에 이 사용자를 초대할 것인지 선택하도록함
		// 그래서 방을 선택하고,

		// chatno를 가져와야할 때는 이름과 방장이름으로 가져온다.
		// 그리고 그거는 중복안되게 해야함
		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;

		try {
			// 닉네임을 가져와서 닉네임리스트에다가 bangJangList
			String id = memberService.getID(memberNickName);
			String roomNumber = chattingService.getRoomNumberByRoomName(roomName);

			// 방제목으로 들어가기 사용자는 번호는 몰라도됨

			chattingService.enterToChatRoom(id, memberNickName, roomName, roomNumber);

			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");

			// System.out.println(nickName);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	@GetMapping("/roomMemberList")
	public ResponseEntity<Map<String, Object>> getRoomMemberList(
			@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "roomNumber", required = false) int roomNumber) {

		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;

		try {

			// 방제목으로 들어가기 사용자는 번호는 몰라도됨

			List<String> list = chattingService.getRoomMemberList(roomNumber);
			String bangjang = chattingService.getBangJang(roomNumber);
			list.add(bangjang);
			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");
			resultMap.put("memberList", list);

			// System.out.println(nickName);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	// 방 이름에다가, 채팅보내는거
	@PostMapping("/detail/sendMessage/chattingRoom")
	public ResponseEntity<Map<String, Object>> sendMessageToChatRoom(
			@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "roomNumber", required = false) int roomNumber,
			@RequestParam(value = "messageData", required = false) String messageData

	) throws UnsupportedEncodingException {

		String id = jwtService.getIdByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;

		try {
			String roomName = chattingService.getRoomNameByRoomNumber(roomNumber);
			String nickName = memberService.getNickName(id);

			MultiChatRoomMessageDto sendMessageDto = new MultiChatRoomMessageDto(roomNumber, roomName, id, nickName,
					messageData);
			// 채팅 메세지를 보냄 sql에
			chattingService.sendMessageToChatRoom(sendMessageDto);

			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");

		} catch (SQLException e) {

			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	// 방에서 채팅 하던거 읽어오기, 영속성
	@GetMapping("/detail/ReadAll/chattingRoom")
	public ResponseEntity<Map<String, Object>> chattingRoomDetail(
			@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "roomNumber", required = false) String roomNumber) throws Exception {

		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;
		try {
			// 닉네임을 가져와서 닉네임리스트에다가 bangJangList
			List<MultiChatRoomMessageDto> list = chattingService.getRoomsAllMessageByRoomNumber(roomNumber);
			// String id2 = memberService.getID(nickName);

			// chattingService.makeChatRoom(id, nickName, roomName);

			// System.out.println(nickName);
			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");
			resultMap.put("allMessage", list);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

}

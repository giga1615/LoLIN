
package com.lolin.controller;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.lolin.model.ConnectionDto;
import com.lolin.model.MemberDto;
import com.lolin.service.MultiChatService;
import com.lolin.service.RecommendationService;
import com.lolin.service.JwtService;
import com.lolin.service.LoginService;
import com.lolin.service.MemberService;
import com.lolin.service.RiotApiService;

@RestController
@RequestMapping("/api/member")
public class MemberController {

	@Autowired
	private AuthenticationManager authenticationManager;

	@Autowired
	MultiChatService chattingService;

	@Autowired
	MemberService memberService;

	@Autowired
	LoginService loginService;

	@Autowired
	RiotApiService riotApiService;

	@Autowired
	JwtService jwtService;

	@Autowired
	RecommendationService recommendationService;

	@PostMapping("/login")
	public ResponseEntity<Map<String, Object>> login(@RequestParam(value = "id", required = false) String id,
			@RequestParam(value = "pw", required = false) String pw) {

		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {

			// 비밀번호 암호화해서 전달, 해시로 비교
			pw = memberService.makeHashPassword(pw);

			boolean loginCheck = loginService.login(id, pw).equals("YES");
			// authenticationManager.authenticate(new
			// UsernamePasswordAuthenticationToken(id,pw));

			// 로그인 서비스 실행부분
			if (loginCheck == true) {
				// 클라이언트에게 전달, 메세지 부분(로그인 성공)

				// db에 접속상태로 표시
				String nickName = memberService.getNickName(id);

				String jwt = jwtService.createToken(id, nickName);
				chattingService.connected(id, nickName);
				resultMap.put("message", "SUCCESS");

				resultMap.put("jwt", jwt);
			} else {
				resultMap.put("message", "FAIL");
			}
			status = HttpStatus.ACCEPTED;

		} catch (SQLException e) {

			// 로그인 실패
			// 클라이언트에게 전달
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");
			// resultMap.put("message", "SERVER_ERROR");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);

	}

	@PostMapping("/logout")
	public ResponseEntity<Map<String, Object>> logout(@RequestParam(value = "jwt", required = false) String jwt)
			throws UnsupportedEncodingException {

		String id = jwtService.getIdByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {
			chattingService.disConnected(id);

			resultMap.put("message", "SUCCESS");
			status = HttpStatus.ACCEPTED;
		} catch (SQLException e) {
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "FAIL");

			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	@GetMapping("/connectionCheck")
	public ResponseEntity<Map<String, Object>> connectionCheck(
			@RequestParam(value = "jwt", required = false) String jwt) throws UnsupportedEncodingException {

		String id = jwtService.getIdByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {
			ConnectionDto check = chattingService.connectionCheck(id);

			resultMap.put("message", "SUCCESS");
			resultMap.put("check", check);

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

	// 이미지 난수생성
	@GetMapping("/make/auth/makeRandomNumber")
	public ResponseEntity<Map<String, Object>> randomNumber(
			@RequestParam(value = "nickName", required = false) String nickName) {
		nickName = nickName.replaceAll(" ", "");
		System.out.println("첫번째부분" + nickName);
		Map<String, Object> resultMap = new HashMap<>();

		// 자기자신의 프로필 아이콘 아이디를 제외한 난수를 생성해서 넘겨준다.

		int randomNumber = memberService.makeRandomNumber(nickName);

		HttpStatus status = null;

		System.out.println("과연");
		System.out.println(randomNumber);

		// service를 사용해서, dao mapper에 집어넣는다.
		try {
			resultMap.put("message", "SUCCESS");
			resultMap.put("iconNumber", randomNumber);
			memberService.authPre(nickName, randomNumber);
			status = HttpStatus.ACCEPTED;
		} catch (SQLException e) {

			resultMap.put("message", "FAIL");
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	// 확인만 해봄, 아이디를 만들 수 있나
	@GetMapping("/make/authImgChangeCheck")
	public ResponseEntity<Map<String, Object>> authorizationCheck(
			@RequestParam(value = "nickName", required = false) String nickName) {
		String searchNickName = nickName.replaceAll(" ", "");
		System.out.println("두번째 부분" + nickName);
		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		// 클라이언트에게 전달, 메세지 부분(라이엇에서 프로필 이미지 가져오기 성공)
		status = HttpStatus.ACCEPTED;

		///// 이제여기서 라이엇에이피아이에 보내주면서 확인해준다.
		int imgNumberGetFromRiot = 0;
		int imgNumberGetFromLocalDB = 1;
		try {
			imgNumberGetFromRiot = Integer.parseInt(riotApiService.getLolProfileID(searchNickName));
			imgNumberGetFromLocalDB = memberService.getAuthPreImg(searchNickName);
		} catch (NumberFormatException | SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} // String으로 빼줘야함

		// 이미지는 0번부터시작인듯

		// 보안오류 고침 백에서 확인해줬음 진짜 바뀌었는지
		if (imgNumberGetFromRiot == imgNumberGetFromLocalDB) {

			resultMap.put("message", "SUCCESS");
		} else {

			// 인증통과안되서 실행이안됨
			resultMap.put("message", "FAIL");
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	// 인증부분
	@PostMapping("/make")
	public ResponseEntity<Map<String, Object>> memberMake(@RequestParam(value = "id", required = false) String id,
			@RequestParam(value = "nickName", required = false) String nickName,
			@RequestParam(value = "pw", required = false) String pw) {

		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {

			// 클라이언트에게 전달, 메세지 부분(라이엇에서 프로필 이미지 가져오기 성공)
			status = HttpStatus.ACCEPTED;

			///// 이제여기서 라이엇에이피아이에 보내주면서 확인해준다.
			int imgNumberGetFromRiot = Integer.parseInt(riotApiService.getLolProfileID(nickName.replaceAll(" ", "")));// String으로 빼줘야함
			int imgNumberGetFromLocalDB = memberService.getAuthPreImg(nickName.replaceAll(" ", ""));

			System.out.println("비교");
			System.out.println(imgNumberGetFromRiot);
			System.out.println(imgNumberGetFromLocalDB);
			// 이미지는 0번부터시작인듯

			// 보안오류 고침 백에서 확인해줬음 진짜 바뀌었는지
			if (imgNumberGetFromRiot == imgNumberGetFromLocalDB) {

				try {

					// 회원가입 서비스 실행부분
					pw = memberService.makeHashPassword(pw);
					MemberDto memberDto = new MemberDto(id, nickName, pw);
					memberService.make(memberDto);

					// 여기가 api에서 불러와서 넣어주는 로직 0404
					Object obj = recommendationService.getMainUserInfoFromPython(nickName.replaceAll(" ", ""));
					System.out.println(obj.toString());
					try {
						recommendationService.makeMemberForRecommendation(nickName, obj);

					} catch (Exception e) {
						// 예외처리
						e.printStackTrace();
					}

					// 가입완료하고 회원정보 수정을 위해 auth_pre는 초기화
					memberService.authPre(nickName, -1);
					// 클라이언트에게 전달, 메세지 부분(회원가입 성공)
					status = HttpStatus.ACCEPTED;
					resultMap.put("message", "SUCCESS");
				} catch (SQLException e) {

					// 오류시 디버깅
					// 클라이언트에게 전달
					System.out.println("해쉬형성부 오류가 뜨지않는다면, create 오류");
					status = HttpStatus.INTERNAL_SERVER_ERROR;
					resultMap.put("message", "SERVER_ERROR");
					e.printStackTrace();
				}

				resultMap.put("message", "SUCCESS");
			} else {

				// 인증통과안되서 실행이안됨
				resultMap.put("message", "FAIL");
			}

		} catch (SQLException e) {

			// 클라이언트에게 전달
			// 이건 단순 localDB에서 가져오는 오류 떳을떄, sqlexception이 내부랑 다름
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "SERVER_ERROR");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);

	}

	// 프론트에서 해줘야할 부분
	// 가입이되면, 로그인(axios)시키고, 바로, 메인페이지로 이동(라우터)하면서, 로그인시 jwt발급받은거로
	// executePredict해주면,
	// 가입할때만 최초 한번 실행되는 로직이되고, 다른사람이 get으로 요청 함부로 할수 없다 jwt가 막아줘서
	@GetMapping("/executeInitPredictTime")
	public ResponseEntity<Map<String, Object>> executeTime(@RequestParam(value = "jwt", required = false) String jwt) {

		String nickName = null;
		try {
			nickName = jwtService.getNickNameByJWT(jwt);
		} catch (UnsupportedEncodingException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {
			recommendationService.executePredictTimeAtPython(nickName);
		} catch (IOException e) {
			e.printStackTrace();
		}

		resultMap.put("message", "SUCCESS");
		status = HttpStatus.ACCEPTED;

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	@PutMapping("/update")
	public ResponseEntity<Map<String, Object>> memberUpdate(@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "id", required = false) String id,
			@RequestParam(value = "nickName", required = false) String nickName,
			@RequestParam(value = "pw", required = false) String pw) throws UnsupportedEncodingException {

		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {
			// 비밀번호 암호화해서 전달, 해시로 비교
			pw = memberService.makeHashPassword(pw);

			// 로그인도 체크해줘야함
			boolean loginCheck = loginService.login(id, pw).equals("YES");

			// 클라이언트에게 전달, 메세지 부분(라이엇에서 프로필 이미지 가져오기 성공)
			status = HttpStatus.ACCEPTED;

			///// 이제여기서 라이엇에이피아이에 보내주면서 확인해준다.
			int imgNumberGetFromRiot = Integer.parseInt(riotApiService.getLolProfileID(nickName));// String으로 빼줘야함
			int imgNumberGetFromLocalDB = memberService.getAuthPreImg(nickName);

			// 이미지는 0번부터시작인듯

			// 보안오류 고침 백에서 확인해줬음 진짜 바뀌었는지
			if (imgNumberGetFromRiot == imgNumberGetFromLocalDB && loginCheck == true) {

				try {

					// 회원가입 서비스 실행부분

					MemberDto memberDto = new MemberDto(id, nickName, pw);
					memberService.make(memberDto);

					// 가입완료하고 회원정보 수정을 위해 auth_pre는 초기화
					memberService.authPre(nickName, -1);
					// 클라이언트에게 전달, 메세지 부분(회원가입 성공)
					status = HttpStatus.ACCEPTED;
					resultMap.put("message", "SUCCESS");
				} catch (SQLException e) {

					// 오류시 디버깅
					// 클라이언트에게 전달
					System.out.println("해쉬형성부 오류가 뜨지않는다면, create 오류");
					status = HttpStatus.INTERNAL_SERVER_ERROR;
					resultMap.put("message", "SERVER_ERROR");
					e.printStackTrace();
				}

				resultMap.put("message", "SUCCESS");
			} else {

				// 인증통과안되서 실행이안됨
				resultMap.put("message", "FAIL");
			}

		} catch (SQLException e) {

			// 클라이언트에게 전달
			// 이건 단순 localDB에서 가져오는 오류 떳을떄, sqlexception이 내부랑 다름

			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "SERVER_ERROR");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);

	}

	@DeleteMapping("/delete")
	public ResponseEntity<Map<String, Object>> delete(@RequestParam(value = "jwt", required = false) String jwt)
			throws UnsupportedEncodingException {
		String id = jwtService.getIdByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;
		try {
			memberService.delete(id);
			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");

		} catch (SQLException e) {
			System.out.println("삭제 오류");
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "SERVER_ERROR");
			e.printStackTrace();
		}
		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	@PutMapping("/updatePW")
	public ResponseEntity<Map<String, Object>> updatePW(@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "id", required = true) String id,
			@RequestParam(value = "pw", required = true) String pw) {

		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;
		MemberDto member = new MemberDto(id, pw);
		try {
			memberService.pwUpdate(member);
			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");

		} catch (SQLException e) {
			System.out.println("비밀번호 업데이트 오류");
			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "SERVER_ERROR");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	// 회원가입전 체크
	@GetMapping("/membershipCheck")
	public ResponseEntity<Map<String, Object>> memberCheck(@RequestParam(value = "id", required = false) String id) {

		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;

		String nickName = null;

		try {
			nickName = memberService.getNickName(id);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		if (nickName != null) {
			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "존재");
		} else {
			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "존재하지않음");

		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);

	}

	// 개인 아이콘 얻는 곳
	@GetMapping("/getIconNo")
	public ResponseEntity<Map<String, Object>> getIconNo(@RequestParam(value = "jwt", required = false) String jwt,
			@RequestParam(value = "nickName", required = false) String nickName) throws Exception {
		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;
		int iconNo;
		try {
			iconNo = Integer.parseInt(riotApiService.getLolProfileID(nickName));
			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");
			resultMap.put("iconNo", iconNo);

		} catch (Exception e) {
			System.out.println("아이콘넘버 검색안되서  그런거라 랜덤으로 값을줌 어쩔수없는 오류");
			resultMap.put("mseesage", "SUCCESS");
			
			resultMap.put("iconNo",(int)(Math.random()*27));
			status = HttpStatus.ACCEPTED;
			//e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}

	@GetMapping("/getAllNickName")
	public ResponseEntity<Map<String, Object>> getAllNickNames(
			@RequestParam(value = "jwt", required = false) String jwt) throws Exception {

		Map<String, Object> resultMap = new HashMap<>();
		HttpStatus status = null;
		String myNickName = jwtService.getNickNameByJWT(jwt);
		try {
			List<String> list = memberService.getAllNickName(myNickName);
			status = HttpStatus.ACCEPTED;
			resultMap.put("message", "SUCCESS");
			resultMap.put("memberList", list);
		} catch (SQLException e) {

			status = HttpStatus.INTERNAL_SERVER_ERROR;
			resultMap.put("message", "SERVER_ERROR");
			e.printStackTrace();
		}

		return new ResponseEntity<Map<String, Object>>(resultMap, status);
	}
	
	
	@PutMapping("/connectionOn")
	public ResponseEntity<Map<String, Object>> connectionOn(
			@RequestParam(value = "jwt", required = false) String jwt) throws UnsupportedEncodingException {

		String id = jwtService.getIdByJWT(jwt);
		String nickName = jwtService.getNickNameByJWT(jwt);
		Map<String, Object> resultMap = new HashMap<>();

		HttpStatus status = null;

		try {
			chattingService.connected(id, nickName);

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
	
	
	

}

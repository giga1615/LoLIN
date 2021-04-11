package com.lolin.service;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URI;
import java.net.URISyntaxException;
import java.sql.SQLException;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.ibatis.session.SqlSession;
import org.apache.tomcat.util.json.JSONParser;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.lolin.dao.MultiChatDao;
import com.lolin.dao.RecommendDao;
import com.lolin.model.RecommendedUserDto;
import com.lolin.model.UserInfoFromDjangoDto;

@Service
public class RecommendationServiceImpl implements RecommendationService {

	@Autowired
	private SqlSession session;

	// 이파리미터 두개로 추천하는 사람의 모든값을 가져오려면
	// 1차적으로, recommend member테이블이 형성이 되어있어야된다.
	// 애초에 내가 고른 포지션을 제외 한다기보다.
	// 내가 selected position한애로 가져오는게 좋다.
	// 왜냐면, 친구추가를 하는데,
	// 나랑은 안겹쳐도 지금 구성되어있는 팀원이랑 겹칠 확률 이있기때문에

	// selectedPosition, selectedGameStyle둘 다 나랑 일치하는 것을 가져온다.
	// 게임유형이랑, 포지션이 일치하는 선수를 가져온다.
	@Override
	public List<RecommendedUserDto> getRecommendedUser(String selectedPosition, String selectedGameStyle, String tier,
			String nickName, double time) throws Exception {

		// 조건해주면됨 xml이랑 같이 컨트롤
		// dao는 같게 넣어주고 level제한값만 30이랑 0으로 두면되네

		if (selectedGameStyle.equals("솔랭") || selectedGameStyle.equals("자유랭크")) {
			// 티어같아야됨, 레벨 30이상

			return session.getMapper(RecommendDao.class).getRecommendedUser(selectedPosition, selectedGameStyle, tier,
					nickName, time, 30);

		} else if (selectedGameStyle.equals("일반게임") || selectedGameStyle.equals("칼바람나락")) {
			// 티어같아야됨, 레벨 0이상
			return session.getMapper(RecommendDao.class).getRecommendedUser(selectedPosition, selectedGameStyle, tier,
					nickName, time, 0);
		} else {
			return session.getMapper(RecommendDao.class).getRecommendedUser(selectedPosition, selectedGameStyle, tier,
					nickName, time, 0);
		}

		// 2솔랭일때, xml 2번 즉 dao2를 만들어줘야한다는 로직

	}

	@Override
	public RecommendedUserDto getMyInfo(String nickName,String id) throws Exception {

		return session.getMapper(RecommendDao.class).getMyInfo(nickName, id);

	}

	@Override
	public void makeMemberForRecommendation(String nickName, Object obj) throws Exception {

		UserInfoFromDjangoDto userInfoFromDjangoDto = new UserInfoFromDjangoDto();
		// 앞이랑 다르게 gson 사용해서 파싱
		ObjectMapper mapper = new ObjectMapper();
		JsonNode returnNode;
		try {
			returnNode = mapper.readTree(obj.toString());
			int user_level = Integer.parseInt(returnNode.path("level").asText());
			int wins = Integer.parseInt(returnNode.path("wins").asText());
			int losses = Integer.parseInt(returnNode.path("losses").asText());
			String tier = returnNode.path("tier").asText();
			String win_rate = returnNode.path("winRatio").asText();
			String liked_position = returnNode.path("LikePosition").asText();
			
			
			if(liked_position.equals("ADC")) {
				
				liked_position="원딜";
			}else if(liked_position.equals("Top")) {
				liked_position="탑";
			}else if(liked_position.equals("Middle")) {
				liked_position="미드";
			}else if(liked_position.equals("Support")) {
				liked_position="서포터";
			}else if(liked_position.equals("Jungle")) {
				liked_position="정글";
			}

			System.out.println("만들기전체크");

			session.getMapper(RecommendDao.class).makeRecommendationUserInfo(tier, user_level, wins, losses, win_rate,
					liked_position, nickName);

		} catch (JsonProcessingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return;

	}

	@Override
	public void executePredictTimeAtPython(String BangJang) {

		// final String RequestUrl =
		// "http://localhost:8000/server1/predictTime?BangJang=" + BangJang;
	
		URIBuilder builder = new URIBuilder();
		builder.setScheme("http").setHost("j4a104.p.ssafy.io:8080").setPath("/server1/predictTime").setParameter("BangJang",
				BangJang);
		URI RequestUrl = null;
		try {
			RequestUrl = builder.build();
		} catch (URISyntaxException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

		final HttpClient client = HttpClientBuilder.create().build();

		final HttpGet get = new HttpGet(RequestUrl);

		JsonNode returnNode = null;
		try {
			get.addHeader("User-Agent",
					"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36");
			get.addHeader("Accept-Language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7");
			get.addHeader("Accept-Charset", "application/x-www-form-urlencoded; charset=UTF-8");

			final HttpResponse response = client.execute(get);
			// JSON 형태 반환값 처리
			ObjectMapper mapper = new ObjectMapper();
			returnNode = mapper.readTree(response.getEntity().getContent());
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		} catch (ClientProtocolException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// clear resources
		}

		return;

	}

	@Override
	public Object getMainUserInfoFromPython(String BangJang) {

		// final String RequestUrl =
		// "http://localhost:8000/server1/memberInfo?BangJang=" + BangJang;

		URIBuilder builder = new URIBuilder();
		builder.setScheme("http").setHost("j4a104.p.ssafy.io:8080").setPath("/server1/memberInfo").setParameter("BangJang",
				BangJang);
		URI RequestUrl = null;
		try {
			RequestUrl = builder.build();
		} catch (URISyntaxException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

		final HttpClient client = HttpClientBuilder.create().build();

		final HttpGet get = new HttpGet(RequestUrl);

		JsonNode returnNode = null;
		try {
			get.addHeader("User-Agent",
					"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36");
			get.addHeader("Accept-Language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7");
			get.addHeader("Accept-Charset", "application/x-www-form-urlencoded; charset=UTF-8");

			final HttpResponse response = client.execute(get);
			// JSON 형태 반환값 처리
			ObjectMapper mapper = new ObjectMapper();
			returnNode = mapper.readTree(response.getEntity().getContent());
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		} catch (ClientProtocolException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			// clear resources
		}

		String nickName = BangJang;
		String level = returnNode.path("level").asText();
		String tier = returnNode.path("tier").asText();
		String winRatio = returnNode.path("winRatio").asText();
		String LikePosition = returnNode.path("LikePosition").asText();

		return returnNode;
	}

	@Override
	public List<RecommendedUserDto> getReadAllrecommend(String nickName) throws Exception {

		return session.getMapper(RecommendDao.class).getReadAllrecommend(nickName);
	}

}

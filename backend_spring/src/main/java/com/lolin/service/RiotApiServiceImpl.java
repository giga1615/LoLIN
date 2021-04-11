package com.lolin.service;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.message.BasicNameValuePair;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.lolin.dao.MemberDao;

@Service
public class RiotApiServiceImpl implements RiotApiService {

	@Autowired
	private SqlSession session;
	//private final static String RIOT_API_KEY = "RGAPI-93e766dd-059c-4528-8c95-992c075af144";
	
	
	@Override
	public String getLolProfileID(String nickName) throws SQLException {
		
		String RIOT_API_KEY=session.getMapper(MemberDao.class).get_api_key();		
		nickName = nickName.replaceAll(" ", "");

		final String RequestUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + nickName;

		final HttpClient client = HttpClientBuilder.create().build();

		final HttpGet get = new HttpGet(RequestUrl);

		JsonNode returnNode = null;
		try {
			get.addHeader("User-Agent",
					"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36");
			get.addHeader("Accept-Language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7");
			get.addHeader("Accept-Charset", "application/x-www-form-urlencoded; charset=UTF-8");
			get.addHeader("Origin", "https://developer.riotgames.com");
			get.addHeader("X-Riot-Token", RIOT_API_KEY);

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

		String name = returnNode.path("name").asText();
		String profileId = returnNode.path("profileIconId").asText();
		System.out.println(name);
		System.out.println(profileId);

		return profileId;
	}

}

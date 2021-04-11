package com.lolin.service;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.Map;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;
import org.springframework.stereotype.Service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.lolin.model.UserInfoFromDjangoDto;

@Service
public class DjangoServiceImpl implements DjangoService {

	@Override
	public double getTimeFromDjango(String nickName) {

		final String RequestUrl = "http://j4a104.p.ssafy.io:8080/server1/func1?";

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

		String BangJangJson = returnNode.path("BangJang").asText();
		System.out.println(returnNode);

		return 0;
	}

	@Override
	public UserInfoFromDjangoDto getUserInfoFromDjango(String nickName) {
		// TODO Auto-generated method stub

		// 여기에 티어, 레벨, 승률, liked 포지션도 같이 뽑아내줌

		final String RequestUrl = "http://j4a104.p.ssafy.io:8080/server1/func1?";

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

		String BangJangJson = returnNode.path("BangJang").asText();
		System.out.println(returnNode);

		return null;
	}

}

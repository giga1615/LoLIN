package com.lolin.service;

import java.io.IOException;
import java.net.MalformedURLException;
import java.sql.SQLException;
import java.util.List;

import com.lolin.model.RecommendedUserDto;

public interface RecommendationService {

	List<RecommendedUserDto> getRecommendedUser(String selectedPosition, String selectedGameStyle, String tier,
			String nickName, double time) throws Exception;

	List<RecommendedUserDto> getReadAllrecommend(String nickName) throws Exception;
	
	public RecommendedUserDto getMyInfo(String nickName, String id) throws Exception;

	void makeMemberForRecommendation(String nickName, Object obj) throws Exception;

	Object getMainUserInfoFromPython(String BangJang);

	void executePredictTimeAtPython(String BangJang) throws MalformedURLException, IOException;
}

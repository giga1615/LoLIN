package com.lolin.dao;

import java.util.List;

import org.springframework.stereotype.Repository;

import com.lolin.model.RecommendedUserDto;
import com.lolin.model.UserInfoFromDjangoDto;

@Repository
public interface RecommendDao {

	List<RecommendedUserDto> getRecommendedUser(String selectedPosition, String selectedGameStyle, String tier,
			String nickName, double time, int level) throws Exception;
	List<RecommendedUserDto> getReadAllrecommend(String nickName) throws Exception;
	
	
	public RecommendedUserDto getMyInfo(String nickName, String id) throws Exception;

	void makeRecommendationUserInfo(String tier, int user_level, int wins, int losses, String win_rate,
			String liked_position, String nickName) throws Exception;

}

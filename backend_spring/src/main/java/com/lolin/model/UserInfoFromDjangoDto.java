package com.lolin.model;

public class UserInfoFromDjangoDto {

	String tier;
	int user_level;
	String win_rate;
	String liked_position;

	public UserInfoFromDjangoDto() {
		super();
	}

	public UserInfoFromDjangoDto(String tier, int user_level, String win_rate, String liked_position) {
		super();
		this.tier = tier;
		this.user_level = user_level;
		this.win_rate = win_rate;
		this.liked_position = liked_position;
	}

	public String getTier() {
		return tier;
	}

	public void setTier(String tier) {
		this.tier = tier;
	}

	public int getUser_level() {
		return user_level;
	}

	public void setUser_level(int user_level) {
		this.user_level = user_level;
	}

	public String getWin_rate() {
		return win_rate;
	}

	public void setWin_rate(String win_rate) {
		this.win_rate = win_rate;
	}

	public String getLiked_position() {
		return liked_position;
	}

	public void setLiked_position(String liked_position) {
		this.liked_position = liked_position;
	}

	@Override
	public String toString() {
		return "UserInfoFromDjangoDto [tier=" + tier + ", user_level=" + user_level + ", win_rate=" + win_rate
				+ ", liked_position=" + liked_position + "]";
	}

}

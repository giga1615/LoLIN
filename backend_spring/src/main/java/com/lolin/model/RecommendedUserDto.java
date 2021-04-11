package com.lolin.model;

public class RecommendedUserDto {

	String nickname;
	double time_predict;
	String game_style;
	String liked_position;
	int wins;
	int losses;
	String tier;
	int liked;
	int user_level;
	String win_rate;
	int connection_check;

	public RecommendedUserDto() {
		super();

	}

	
	
	

	public RecommendedUserDto(String nickname, double time_predict, String game_style, String liked_position, int wins,
			int losses, String tier, int liked, int user_level, String win_rate, int connection_check) {
		super();
		this.nickname = nickname;
		this.time_predict = time_predict;
		this.game_style = game_style;
		this.liked_position = liked_position;
		this.wins = wins;
		this.losses = losses;
		this.tier = tier;
		this.liked = liked;
		this.user_level = user_level;
		this.win_rate = win_rate;
		this.connection_check = connection_check;
	}





	public int getLiked() {
		return liked;
	}



	public void setLiked(int liked) {
		this.liked = liked;
	}



	public String getNickname() {
		return nickname;
	}

	public void setNickname(String nickname) {
		this.nickname = nickname;
	}

	public double getTime_predict() {
		return time_predict;
	}

	public void setTime_predict(double time_predict) {
		this.time_predict = time_predict;
	}

	public String getGame_style() {
		return game_style;
	}

	public void setGame_style(String game_style) {
		this.game_style = game_style;
	}

	public String getLiked_position() {
		return liked_position;
	}

	public void setLiked_position(String liked_position) {
		this.liked_position = liked_position;
	}

	public int getWins() {
		return wins;
	}

	public void setWins(int wins) {
		this.wins = wins;
	}

	public int getLosses() {
		return losses;
	}

	public void setLosses(int losses) {
		this.losses = losses;
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

	public int getConnection_check() {
		return connection_check;
	}

	public void setConnection_check(int connection_check) {
		this.connection_check = connection_check;
	}





	@Override
	public String toString() {
		return "RecommendedUserDto [nickname=" + nickname + ", time_predict=" + time_predict + ", game_style="
				+ game_style + ", liked_position=" + liked_position + ", wins=" + wins + ", losses=" + losses
				+ ", tier=" + tier + ", liked=" + liked + ", user_level=" + user_level + ", win_rate=" + win_rate
				+ ", connection_check=" + connection_check + "]";
	}

	

}

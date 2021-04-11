package com.lolin.model;

public class LikeDto {

	String your_nickname;
	int connection_check;

	public LikeDto() {
		super();
	}

	public LikeDto(String your_nickname, int connection_check) {
		super();
		this.your_nickname = your_nickname;
		this.connection_check = connection_check;
	}

	public String getYour_nickname() {
		return your_nickname;
	}

	public void setYour_nickname(String your_nickname) {
		this.your_nickname = your_nickname;
	}

	public int getConnection_check() {
		return connection_check;
	}

	public void setConnection_check(int connection_check) {
		this.connection_check = connection_check;
	}

	@Override
	public String toString() {
		return "LikeDto [your_nickname=" + your_nickname + ", connection_check=" + connection_check + "]";
	}

}

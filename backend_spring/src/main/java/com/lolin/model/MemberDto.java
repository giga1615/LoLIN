package com.lolin.model;

public class MemberDto {

	String id;
	String nickName;
	String pw;

	public MemberDto() {

	}

	public MemberDto(String id, String pw) {
		super();
		this.id = id;
		this.pw = pw;

	}

	public MemberDto(String id, String nickName, String pw) {
		super();
		this.id = id;
		this.nickName = nickName;
		this.pw = pw;

	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPw() {
		return pw;
	}

	public void setPw(String pw) {
		this.pw = pw;
	}

	public String getNickName() {
		return nickName;
	}

	public void setNickName(String nickName) {
		this.nickName = nickName;
	}

	@Override
	public String toString() {
		return "MemberDto [id=" + id + ", nickName=" + nickName + "]";
	}

}

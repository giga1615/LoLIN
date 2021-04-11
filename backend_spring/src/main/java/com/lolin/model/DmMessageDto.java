package com.lolin.model;

public class DmMessageDto {
	private int dmNo;
	private String myId;
	private String yourId;
	private String myNickName;
	private String yourNickName;
	private String createTime;
	private String messageData;

	public DmMessageDto(String myId, String yourId, String messageData) {
		super();
		this.myId = myId;
		this.yourId = yourId;
		this.messageData = messageData;
	}

	public DmMessageDto(int dmNo, String myId, String yourId, String createTime, String myNickName, String yourNickName, 
			String messageData) {
		super();
		this.dmNo = dmNo;
		this.myId = myId;
		this.yourId = yourId;
		this.myNickName = myNickName;
		this.yourNickName = yourNickName;
		this.createTime = createTime;
		this.messageData = messageData;
	}

	public int getDmNo() {
		return dmNo;
	}

	public void setDmNo(int dmNo) {
		this.dmNo = dmNo;
	}

	public String getMyId() {
		return myId;
	}

	public void setMyId(String myId) {
		this.myId = myId;
	}

	public String getYourId() {
		return yourId;
	}

	public void setYourId(String yourId) {
		this.yourId = yourId;
	}

	public String getMyNickName() {
		return myNickName;
	}

	public void setMyNickName(String myNickName) {
		this.myNickName = myNickName;
	}

	public String getYourNickName() {
		return yourNickName;
	}

	public void setYourNickName(String yourNickName) {
		this.yourNickName = yourNickName;
	}

	public String getCreateTime() {
		return createTime;
	}

	public void setCreateTime(String createTime) {
		this.createTime = createTime;
	}

	public String getMessageData() {
		return messageData;
	}

	public void setMessageData(String messageData) {
		this.messageData = messageData;
	}

	@Override
	public String toString() {
		return "ChatMessageDto [dmNo=" + dmNo + ", myId=" + myId + ", yourId=" + yourId + ", myNickName=" + myNickName
				+ ", yourNickName=" + yourNickName + ", createTime=" + createTime + ", messageData=" + messageData
				+ "]";
	}

}

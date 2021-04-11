package com.lolin.model;

//채팅룸에 있는 메세지를 전달해준다.
public class MultiChatRoomMessageDto {

	int roomNo;
	String roomName;
	String id;
	String createTime;
	String nickName;
	String messageData;

	public MultiChatRoomMessageDto(int roomNo, String roomName, String id, String createTime, String nickName,
			String messageData) {
		super();
		this.roomNo = roomNo;
		this.roomName = roomName;
		this.id = id;
		this.createTime = createTime;
		this.nickName = nickName;
		this.messageData = messageData;
	}

	public MultiChatRoomMessageDto(int roomNo, String id, String messageData) {
		super();
		this.roomNo = roomNo;

		this.id = id;

		this.messageData = messageData;
	}

	public MultiChatRoomMessageDto(int roomNo, String roomName, String id, String nickName, String messageData) {
		super();
		this.roomNo = roomNo;
		this.roomName = roomName;
		this.id = id;
		this.nickName = nickName;
		this.messageData = messageData;
	}

	public int getRoomNo() {
		return roomNo;
	}

	public void setRoomNo(int roomNo) {
		this.roomNo = roomNo;
	}

	public String getRoomName() {
		return roomName;
	}

	public void setRoomName(String roomName) {
		this.roomName = roomName;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getCreateTime() {
		return createTime;
	}

	public void setCreateTime(String createTime) {
		this.createTime = createTime;
	}

	public String getNickName() {
		return nickName;
	}

	public void setNickName(String nickName) {
		this.nickName = nickName;
	}

	public String getMessageData() {
		return messageData;
	}

	public void setMessageData(String messageData) {
		this.messageData = messageData;
	}

	@Override
	public String toString() {
		return "ChatRoomAllMessageDto [roomNo=" + roomNo + ", roomName=" + roomName + ", id=" + id + ", createTime="
				+ createTime + ", nickName=" + nickName + ", messageData=" + messageData + "]";
	}

}
